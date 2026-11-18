"""Monta a mensagem do pedido do Pão Fofinho do Caique e o link do WhatsApp.

Uso:
    python3 gerar_link.py '<json do pedido>'
    echo '<json do pedido>' | python3 gerar_link.py

JSON de entrada:
{
  "loja": "Pão Fofinho do Caique",       # campo "loja" do estoque.json
  "whatsapp": "5565999999999",
  "itens": [{"nome": "Pão Fofinho", "preco": 10.0, "quantidade": 2}],
  "nome": "Ana",
  "tipo": "entrega",            # "entrega" ou "retirada"
  "endereco": "Rua X, 123 - Bairro Y",   # so para entrega
  "taxa_entrega": 5.0,          # 0 para retirada
  "pagamento": "Pix",
  "observacoes": ""
}

Saida: JSON com "mensagem", "subtotal", "taxa_entrega", "total" e "link".

Modo contato (so falar com a loja, sem pedido):
    {"whatsapp": "5565999999999", "mensagem": "Oi! Quando sai a proxima fornada?"}
Saida: JSON com "mensagem" e "link".
"""
import json
import re
import sys
import urllib.parse

LOJA_PADRAO = "Pão Fofinho do Caique"


def brl(valor: float) -> str:
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


def link_whatsapp(numero: str, mensagem: str) -> str:
    return f"https://wa.me/{numero}?text={urllib.parse.quote(mensagem, safe='')}"


def main() -> None:
    bruto = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    pedido = json.loads(bruto)

    numero = re.sub(r"\D", "", str(pedido.get("whatsapp", "")))
    if not numero or set(numero[2:]) <= {"0"}:
        sys.exit("ERRO: numero de WhatsApp da loja nao configurado no estoque.json")

    if str(pedido.get("mensagem", "")).strip() and not pedido.get("itens"):
        mensagem = str(pedido["mensagem"]).strip()
        print(json.dumps({"mensagem": mensagem, "link": link_whatsapp(numero, mensagem)},
                         ensure_ascii=False, indent=2))
        return

    itens = [i for i in pedido.get("itens", []) if int(i.get("quantidade", 0)) > 0]
    if not itens:
        sys.exit("ERRO: o pedido nao tem itens")

    loja = str(pedido.get("loja") or LOJA_PADRAO).strip()
    linhas = [f"Olá, {loja}! Quero fazer um pedido:", ""]
    subtotal = 0.0
    for item in itens:
        qtd = int(item["quantidade"])
        valor = round(float(item["preco"]) * qtd, 2)
        subtotal += valor
        linhas.append(f"• {qtd}x {item['nome']} — {brl(valor)}")
    subtotal = round(subtotal, 2)

    tipo = str(pedido.get("tipo", "retirada")).lower()
    taxa = round(float(pedido.get("taxa_entrega", 0) or 0), 2) if tipo == "entrega" else 0.0
    total = round(subtotal + taxa, 2)

    linhas.append("")
    linhas.append(f"Subtotal: {brl(subtotal)}")
    if taxa:
        linhas.append(f"Taxa de entrega: {brl(taxa)}")
    linhas.append(f"*Total: {brl(total)}*")
    linhas.append("")
    linhas.append(f"Nome: {pedido.get('nome', '').strip()}")
    if tipo == "entrega":
        linhas.append(f"Entrega: {pedido.get('endereco', '').strip()}")
    else:
        linhas.append("Retirada no local")
    if pedido.get("pagamento"):
        linhas.append(f"Pagamento: {pedido['pagamento']}")
    if str(pedido.get("observacoes", "")).strip():
        linhas.append(f"Obs.: {pedido['observacoes'].strip()}")

    mensagem = "\n".join(linhas)
    link = link_whatsapp(numero, mensagem)

    print(json.dumps({
        "mensagem": mensagem,
        "subtotal": brl(subtotal),
        "taxa_entrega": brl(taxa),
        "total": brl(total),
        "link": link,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
