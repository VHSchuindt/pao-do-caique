<p align="center">
  <img src="assets/banner.png" alt="Pão Fofinho do Caique: fofinho, quentinho e feito com carinho" width="100%">
</p>

# Pão Fofinho do Caique 🍞

Peça o pão fofinho do Caique conversando com o Claude: ele mostra quantos pães tem hoje, pergunta só o que falta e entrega o pedido pronto no WhatsApp. Você só toca em enviar.

## Como é pedir

> **Você:** quero 2 pães
>
> **Claude:** *(botões)* Retirar na loja · Entrega (+ R$ 5,00) — Pix · Dinheiro · Cartão
>
> **Claude:** Prontinho! 2x Pão Fofinho, total R$ 20,00 → **📲 Enviar pedido no WhatsApp**

| Skill | Como chamar | O que faz |
|---|---|---|
| `cardapio` | "tem pão hoje?" ou `/pao-do-caique:cardapio` | Mostra o preço e quantos pães ainda tem |
| `pedido` | "quero 2 pães" ou `/pao-do-caique:pedido` | Pergunta só o que falta, calcula o total e gera o link do WhatsApp |

O pedido só fica confirmado quando a loja responde no WhatsApp.

## Como instalar

**No Claude (site, app ou desktop)**

1. Abra **Customize > Plugins**.
2. Clique em **Add > Add marketplace**.
3. Digite `VHSchuindt/pao-do-caique` e confirme.
4. Adicione o plugin **Pão Fofinho do Caique**.

**No Claude Code**

```
/plugin marketplace add VHSchuindt/pao-do-caique
/plugin install pao-do-caique@pao-do-caique
```

## Para a loja: como atualizar o estoque

O cardápio inteiro fica no arquivo [`estoque.json`](estoque.json). O plugin lê esse arquivo a cada conversa, então basta editá-lo aqui no GitHub:

1. Abra o `estoque.json` e clique no lápis (✏️ **Edit**).
2. Mude o que precisar:
   - `quantidade`: quantos pães ainda tem (0 = esgotado);
   - `preco`: com ponto, ex.: `10.00`;
   - `aceitando_pedidos`: `false` para pausar os pedidos, com um recado em `aviso` (ex.: "fornada nova amanhã às 7h");
   - `atualizado_em`: data e hora da atualização.
3. Clique em **Commit changes**.

Para vender outro tipo de pão, copie a linha de `produtos` e troque `id`, `nome`, `preco` e `quantidade`.

> A baixa do estoque é manual: quando confirmar uma venda pelo WhatsApp, diminua a `quantidade`. O GitHub pode levar alguns minutos para mostrar a versão nova.
