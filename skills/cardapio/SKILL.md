---
name: cardapio
description: Mostra o cardápio do Pão Fofinho do Caique com os pães, o preço e quantas unidades ainda tem hoje, e convida para pedir com um toque. Use quando alguém perguntar "tem pão hoje?", "quanto custa o pão?", "ainda tem pão fofinho?", "quantos pães sobraram?", "estoque do Pão do Caique", "cardápio do Pão Fofinho" ou quiser ver as opções antes de comprar.
---

# Cardápio do Pão Fofinho do Caique

## Jeito de falar

Fale em português do Brasil, com carinho e leveza, como numa padaria de bairro: frases curtas e no máximo 1 ou 2 emojis por mensagem (🍞 💛 ✨). Não narre o que está fazendo e não mostre JSON nem código.

## 1. Ler o estoque (em silêncio)

Busque o arquivo com a ferramenta de leitura de páginas web (WebFetch / web_fetch) **a cada consulta**. Nunca reaproveite números de uma conversa anterior nem da memória: o estoque muda o tempo todo.

1. Primeiro: `https://raw.githubusercontent.com/VHSchuindt/pao-do-caique/main/estoque.json`
2. Se falhar: `https://github.com/VHSchuindt/pao-do-caique/blob/main/estoque.json`
3. Se as duas falharem, diga que não deu para consultar o estoque agora e **não invente quantidades nem preços**. Ofereça montar o pedido mesmo assim, para a loja confirmar pelo WhatsApp (skill `pedido`).

Campos: `loja`, `produtos[]` (`nome`, `preco`, `quantidade`), `aceitando_pedidos`, `aviso`, `entrega` (`disponivel`, `taxa`), `retirada` (`disponivel`), `pagamento`, `whatsapp` e `atualizado_em`. Ignore `_ajuda`.

## 2. Mostrar

**Um produto só**: um cartãozinho de três linhas, sem tabela:

> 🍞 **Pão Fofinho** quentinho, **R$ 10,00** cada
> Hoje ainda tem **10** · atualizado hoje às 13h15
> Retirada grátis ou entrega (+ R$ 5,00) · Pix, dinheiro ou cartão

**Vários produtos**: uma tabela curta (Pão | Preço | Disponível) e, embaixo, a mesma linha de retirada/entrega e pagamento.

- Preço no formato brasileiro: `R$ 10,00`.
- `quantidade` 0 → **Esgotado 🥺**. Entre 1 e 3 → "**Últimas N!**". Acima disso → o número.
- Escreva `atualizado_em` de forma natural: "hoje às 13h15", "ontem às 18h".
- Se `aviso` não estiver vazio, mostre numa linha antes do cartão.
- Se a pessoa perguntou uma coisa só ("ainda tem?", "quanto custa?"), responda direto numa frase e mostre o cartão só se ajudar.

## 3. Convidar para pedir

- **Com ferramenta de perguntas com opções clicáveis** (por exemplo AskUserQuestion ou ask_user_input): faça uma pergunta "Quer garantir o seu?" com as opções "1 pão", "2 pães", "3 pães" (sem passar do estoque) e "Só olhando". Se a pessoa escolher uma quantidade, siga a skill `pedido` já com ela, sem perguntar de novo.
- **Sem essa ferramenta**: termine com "Quer garantir o seu? É só me dizer quantos 😊".
- **Esgotado ou pedidos pausados** (`aceitando_pedidos: false`): não ofereça pedido. Diga com carinho que acabou ou que está pausado e ofereça um link para falar com a loja, gerado com o script da skill `pedido` (`../pedido/scripts/gerar_link.py`) no modo `mensagem`, por exemplo "Oi! Quando sai a próxima fornada do Pão Fofinho?".
