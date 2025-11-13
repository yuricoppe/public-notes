# Code Block (Bloco de [[Glossário/Elementos/codigo|Código]])

O componente Code Block é usado para exibir trechos de [[Glossário/Elementos/codigo|código]] de programação de forma legível e estruturada, geralmente com destaque de sintaxe (syntax highlighting) e funcionalidades adicionais como copiar o [[Glossário/Elementos/codigo|código]].

## Casos de Uso

-   Documentação técnica e tutoriais.
-   Artigos de blog sobre programação.
-   Exemplos de [[Glossário/Elementos/codigo|código]] em APIs e bibliotecas.
-   Qualquer interface que precise apresentar [[Glossário/Elementos/codigo|código]] de forma clara.

## Funcionalidades Essenciais

-   **Exibição de [[Glossário/Elementos/codigo|Código]]:** Apresentar o [[Glossário/Elementos/codigo|código]] de forma monoespaçada e preservando a formatação (espaços, quebras de linha).
-   **Destaque de Sintaxe (Syntax Highlighting):** Colorir diferentes partes do [[Glossário/Elementos/codigo|código]] (palavras-chave, [[Glossário/Componentes/comments|comentários]], strings, etc.) de acordo com a linguagem de programação para melhorar a legibilidade.
-   **Identificação da Linguagem (Opcional, mas Recomendado):** Indicar a linguagem do bloco de [[Glossário/Elementos/codigo|código]] (ex: JavaScript, Python, HTML).
-   **[[Glossário/Elementos/botoes|Botão]] "Copiar [[Glossário/Elementos/codigo|Código]]":** Permitir que o usuário copie facilmente todo o conteúdo do bloco de [[Glossário/Elementos/codigo|código]] para a área de transferência.
-   **Rolagem (Scroll):** Se o [[Glossário/Elementos/codigo|código]] for extenso, permitir rolagem horizontal e/ou vertical dentro do bloco.

## Melhores Práticas

-   **Legibilidade:** Usar fontes monoespaçadas claras. Garantir bom contraste entre o texto do [[Glossário/Elementos/codigo|código]] e o fundo do bloco, e entre as diferentes [[Glossário/Linguagem Visual/cor|cores]] do syntax highlighting.
-   **Performance:** O syntax highlighting, especialmente do lado do cliente, não deve impactar significativamente o desempenho da página, principalmente para blocos de [[Glossário/Elementos/codigo|código]] muito grandes.
-   **Consistência no Estilo:** Manter um estilo visual consistente para blocos de [[Glossário/Elementos/codigo|código]] em toda a aplicação/site.
-   **Acessibilidade (a11y):**
    *   Garantir que o texto do [[Glossário/Elementos/codigo|código]] seja selecionável e copiável, mesmo que haja um [[Glossário/Elementos/botoes|botão]] "Copiar".
    *   As [[Glossário/Linguagem Visual/cor|cores]] do syntax highlighting devem ter contraste suficiente.
    *   O [[Glossário/Elementos/botoes|botão]] "Copiar" deve ser acessível por teclado e ter um rótulo claro (ex: `aria-label="Copiar código"`).
    *   Fornecer um feedback audível ou visual (ex: tooltip "Copiado!") após a ação de copiar.
    *   Para o bloco de [[Glossário/Elementos/codigo|código]] em si, semanticamente, pode-se usar `<pre><code>...</code></pre>`. A tag `<pre>` preserva espaços e quebras de linha, e `<code>` indica que o conteúdo é um trecho de [[Glossário/Elementos/codigo|código]].
-   **Não usar [[Glossário/Elementos/imagem|imagens]] para [[Glossário/Elementos/codigo|código]]:** O [[Glossário/Elementos/codigo|código]] deve ser texto real para ser acessível, selecionável e indexável.
-   **Numeração de Linhas (Opcional):** Pode ser útil para blocos de [[Glossário/Elementos/codigo|código]] mais longos ou quando se referenciando linhas específicas no texto.

## Variações e Funcionalidades Adicionais

-   **Tema Claro/Escuro:** Oferecer variações de tema para o bloco de [[Glossário/Elementos/codigo|código]].
-   **Título/Nome do Arquivo:** Exibir um título ou nome de arquivo associado ao bloco de [[Glossário/Elementos/codigo|código]].
-   **Opção de Download:** Permitir o download do trecho de [[Glossário/Elementos/codigo|código]] como um arquivo.
-   **Edição Simples (Raro):** Em alguns contextos (playgrounds de [[Glossário/Elementos/codigo|código]]), permitir edição leve.

## Estrutura Comum

-   Contêiner principal do bloco.
-   (Opcional) [[Glossário/Elementos/cabecalhos|Cabeçalho]] com nome da linguagem, nome do arquivo, [[Glossário/Elementos/botoes|botão]] de copiar.
-   Área de [[Glossário/Elementos/codigo|código]] (dentro de `<pre><code>`).
-   (Opcional) Numeração de linhas.

## Exemplo de Marcação (Simplificado)

```html
<div class="code-block">
  <div class="code-block-[[Glossário/Componentes/header|header]]">
    <span class="language">JavaScript</span>
    <[[Glossário/Elementos/botoes|button]] aria-label="Copiar [[Glossário/Elementos/codigo|código]]">Copiar</[[Glossário/Elementos/botoes|button]]>
  </div>
  <pre><code class="language-javascript">
function greet(name) {
  console.log('Hello, ' + name + '!');
}
  </code></pre>
</div>
```

## O Que Evitar

-   Destaque de sintaxe com baixo contraste ou [[Glossário/Linguagem Visual/cor|cores]] confusas.
-   Fontes não monoespaçadas para o [[Glossário/Elementos/codigo|código]].
-   Bloquear a seleção de texto manual.
-   Processamento de syntax highlighting muito pesado que cause lentidão. 