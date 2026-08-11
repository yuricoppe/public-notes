---
title: "Caption (Legenda)"
description: "Captions, ou legendas, são textos descritivos curtos associados a outros elementos da interface, como imagens, tabelas, gráficos, ou grupos de campos de formulário."
tags:
  - tema/ui
  - tipo/glossario
---

## Caption (Legenda)

Captions, ou legendas, são textos descritivos curtos associados a outros elementos da interface, como [[Glossário/Elementos/imagem|imagens]], tabelas, gráficos, ou grupos de campos de [[Glossário/Padrões/form_structure|formulário]]. Elas fornecem contexto adicional, atribuição ou uma breve explicação sobre o elemento ao qual se referem.

## Casos de Uso

-   **Imagens:** Descrever o conteúdo da imagem, fornecer crédito ao fotógrafo/ilustrador, ou adicionar informações relevantes que não estão no texto principal.
-   **Tabelas:** Fornecer um título ou um breve resumo do conteúdo da tabela.
-   **Gráficos e Diagramas:** Explicar o que os dados representam, a fonte dos dados, ou destacar pontos chave.
-   **Figuras (Ilustrações, Blocos de [[Glossário/Elementos/codigo|Código]]):** Similar a imagens e tabelas.
-   **Grupos de Campos de Formulário:** Usar `<legend>` dentro de um `<fieldset>` para descrever um grupo de controles relacionados.
-   **Citações (Blockquotes):** Atribuir a autoria da [[Glossário/Elementos/block_quote|citação]].

## Melhores Práticas

![Os três lugares onde uma legenda aparece: figcaption abaixo da figura, caption acima da tabela e legend como primeiro filho do fieldset](attachments/glossario-legenda-caption.svg)

-   **Concisão:** Legendas devem ser curtas e diretas ao ponto.
-   **Relevância:** Devem fornecer informações úteis e diretamente relacionadas ao elemento que acompanham.
-   **Posicionamento:**
    *   Para imagens e figuras, geralmente posicionadas abaixo do elemento.
    *   Para tabelas, podem ser acima ou abaixo, mas a consistência é chave.
    *   Para `<fieldset>`, a `<legend>` é o primeiro filho.
-   **Distinção Visual:** Legendas devem ser visualmente distintas do texto principal e do elemento que acompanham (ex: tamanho de fonte menor, [[Glossário/Linguagem Visual/cor|cor]] de texto diferente, itálico), mas ainda legíveis.
-   **Acessibilidade (a11y):**
    *   **Imagens:** Se a imagem já tem um `alt` text descritivo e a [[Glossário/Componentes/legend|legenda]] apenas repete essa informação ou adiciona detalhes menores, certifique-se de que não haja redundância excessiva. Se a legenda fornece a descrição primária, o `alt` text pode ser mais conciso ou referenciar a legenda.
    *   **Tabelas:** Usar o elemento `<caption>` para tabelas HTML. Leitores de tela anunciam o `<caption>` fornecendo contexto antes de ler os dados da tabela.
    *   **Figuras:** Utilizar os elementos `<figure>` e `<figcaption>` para associar semanticamente uma imagem, ilustração, diagrama, trecho de código, etc., com sua legenda.
        ```html
        <figure>
          <img src="imagem.jpg" alt="Descrição breve da imagem.">
          <figcaption>Esta é uma legenda mais detalhada para a imagem acima.</figcaption>
        </figure>
        ```
    *   **Formulários:** Utilizar `<fieldset>` e `<legend>` para agrupar e nomear grupos de [[Glossário/Elementos/form_controls|controles de formulário]] relacionados. Isso ajuda usuários de leitores de tela a entenderem o contexto dos campos.
        ```html
        <fieldset>
          <legend>Endereço de Entrega</legend>
          <label for="rua">Rua:</label>
          <input type="text" id="rua" name="rua">
          <!-- mais campos do endereço -->
        </fieldset>
        ```
-   **Consistência:** Aplicar um estilo e posicionamento consistentes para legendas em todo o sistema.

## Estilo

-   **[[Glossário/Linguagem Visual/tipografia|Tipografia]]:** Geralmente menor que o corpo do texto (ex: 80-90% do tamanho do corpo do texto).
-   **Cor:** Pode ser uma cor de texto secundária (ex: cinza escuro) para diferenciá-la.
-   **Alinhamento:** Geralmente alinhado com o elemento que descreve (esquerda, centro).

## O Que Evitar

-   Legendas longas que se assemelham a [[Glossário/Elementos/paragrafo|parágrafos]] de texto.
-   Informações redundantes que já estão claras pelo contexto ou pelo próprio elemento.
-   Estilo que dificulta a leitura ou que se confunde com outros elementos textuais.
-   Não usar os elementos HTML semânticos apropriados (`<caption>`, `<figcaption>`, `<legend>`).
