<p align="center">
  <img src="assets/banner.png" alt="Pão Fofinho do Caique: fofinho, quentinho e feito com carinho" width="100%">
</p>

# Pão Fofinho do Caique 🍞

Peça o pão fofinho do Caique conversando com o Claude: ele mostra quantos pães tem hoje, pergunta só o que falta e entrega o pedido pronto no WhatsApp. Você só toca em enviar.

**🛒 Pedir pelo site (qualquer pessoa, sem instalar nada):** https://vhschuindt.github.io/pao-do-caique/

**📦 Baixar o plugin (Claude e ChatGPT):** https://github.com/VHSchuindt/pao-do-caique/raw/main/baixar/pao-do-caique.zip

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

**Pelo arquivo (Claude ou ChatGPT)**

1. Baixe o plugin: https://github.com/VHSchuindt/pao-do-caique/raw/main/baixar/pao-do-caique.zip
2. **No Claude:** Customize > Plugins > Adicionar > **Fazer upload de plugin** e escolha o `.zip`.
3. **No ChatGPT:** Plugins > Adicionar > **Enviar arquivo compactado do plugin** e escolha o `.zip`.

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

## O que o plugin acessa

- **Lê** o arquivo público `estoque.json` deste repositório (`https://raw.githubusercontent.com/VHSchuindt/pao-do-caique/main/estoque.json`) para saber preço, quantidade, entrega e formas de pagamento.
- **Roda**, quando o app permite executar código, um trecho de Python que está no próprio `SKILL.md` e só monta a mensagem do pedido e o link `https://wa.me/...`. Esse código não acessa a internet.
- **Não envia** dados para nenhum serviço. O pedido só vai para a loja se a pessoa abrir o link do WhatsApp e tocar em enviar.
- **Não guarda** dados. Veja a [política de privacidade](PRIVACIDADE.md).

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

---

[Política de privacidade](PRIVACIDADE.md)
