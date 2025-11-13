# Caption ([[Componentes/legend|Legenda]])

Captions, ou legendas, são textos descritivos curtos associados a outros elementos da interface, como [[Elementos/imagem|imagens]], tabelas, gráficos, ou grupos de campos de [[Padrões/form_structure|formulário]]. Elas fornecem contexto adicional, atribuição ou uma breve explicação sobre o elemento ao qual se referem.

## Casos de Uso

-   **[[Elementos/imagem|Imagens]]:** Descrever o conteúdo da [[Elementos/imagem|imagem]], fornecer crédito ao fotógrafo/ilustrador, ou adicionar informações relevantes que não estão no texto principal.
-   **Tabelas:** Fornecer um título ou um breve resumo do conteúdo da tabela.
-   **Gráficos e Diagramas:** Explicar o que os dados representam, a fonte dos dados, ou destacar pontos chave.
-   **Figuras (Ilustrações, Blocos de [[Elementos/codigo|Código]]):** Similar a [[Elementos/imagem|imagens]] e tabelas.
-   **Grupos de Campos de Formulário:** Usar `<legend>` dentro de um `<fieldset>` para descrever um grupo de controles relacionados.
-   **Citações (Blockquotes):** Atribuir a autoria da [[Elementos/block_quote|citação]].

## Melhores Práticas

-   **Concisão:** Legendas devem ser curtas e diretas ao ponto.
-   **Relevância:** Devem fornecer informações úteis e diretamente relacionadas ao elemento que acompanham.
-   **Posicionamento:**
    *   Para [[Elementos/imagem|imagens]] e figuras, geralmente posicionadas abaixo do elemento.
    *   Para tabelas, podem ser acima ou abaixo, mas a consistência é chave.
    *   Para `<fieldset>`, a `<legend>` é o primeiro filho.
-   **Distinção Visual:** Legendas devem ser visualmente distintas do texto principal e do elemento que acompanham (ex: tamanho de fonte menor, [[Linguagem Visual/cor|cor]] de texto diferente, itálico), mas ainda legíveis.
-   **Acessibilidade (a11y):**
    *   **[[Elementos/imagem|Imagens]]:** Se a [[Elementos/imagem|imagem]] já tem um `alt` text descritivo e a [[Componentes/legend|legenda]] apenas repete essa informação ou adiciona detalhes menores, certifique-se de que não haja redundância excessiva. Se a [[Componentes/legend|legenda]] fornece a descrição primária, o `alt` text pode ser mais conciso ou referenciar a [[Componentes/legend|legenda]].
    *   **Tabelas:** Usar o elemento `<caption>` para tabelas HTML. Leitores de tela anunciam o `<caption>` fornecendo contexto antes de ler os dados da tabela.
    *   **Figuras:** Utilizar os elementos `<figure>` e `<figcaption>` para associar semanticamente uma [[Elementos/imagem|imagem]], ilustração, diagrama, trecho de [[Elementos/codigo|código]], etc., com sua [[Componentes/legend|legenda]].
        ```html
        <figure>
          <img src="[[Elementos/imagem|imagem]].jpg" alt="Descrição breve da [[Elementos/imagem|imagem]].">
          <figcaption>Esta é uma [[Componentes/legend|legenda]] mais detalhada para a [[Elementos/imagem|imagem]] acima.</figcaption>
        </figure>
        ```
    *   **[[Padrões/form_structure|Formulários]]:** Utilizar `<fieldset>` e `<legend>` para agrupar e nomear grupos de [[Elementos/form_controls|controles de formulário]] relacionados. Isso ajuda usuários de leitores de tela a entenderem o contexto dos campos.
        ```html
        <fieldset>
          <[[Componentes/legend|legend]]>Endereço de Entrega</[[Componentes/legend|legend]]>
          <label for="rua">Rua:</label>
          <input type="text" id="rua" name="rua">
          <!-- mais campos do endereço -->
        </fieldset>
        ```
-   **Consistência:** Aplicar um estilo e posicionamento consistentes para legendas em todo o sistema.

## Estilo

-   **[[Linguagem Visual/tipografia|Tipografia]]:** Geralmente menor que o corpo do texto (ex: 80-90% do tamanho do corpo do texto).
-   **[[Linguagem Visual/cor|Cor]]:** Pode ser uma [[Linguagem Visual/cor|cor]] de texto secundária (ex: cinza escuro) para diferenciá-la.
-   **Alinhamento:** Geralmente alinhado com o elemento que descreve (esquerda, centro).

## O Que Evitar

-   Legendas longas que se assemelham a [[Elementos/paragrafo|parágrafos]] de texto.
-   Informações redundantes que já estão claras pelo contexto ou pelo próprio elemento.
-   Estilo que dificulta a leitura ou que se confunde com outros elementos textuais.
-   Não usar os elementos HTML semânticos apropriados (`<caption>`, `<figcaption>`, `<legend>`). 