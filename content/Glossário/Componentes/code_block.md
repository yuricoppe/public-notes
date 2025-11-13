# Code Block (Bloco de Código)

O componente Code Block é usado para exibir trechos de código de programação de forma legível e estruturada, geralmente com destaque de sintaxe (syntax highlighting) e funcionalidades adicionais como copiar o código.

## Casos de Uso

-   Documentação técnica e tutoriais.
-   Artigos de blog sobre programação.
-   Exemplos de código em APIs e bibliotecas.
-   Qualquer interface que precise apresentar código de forma clara.

## Funcionalidades Essenciais

-   **Exibição de Código:** Apresentar o código de forma monoespaçada e preservando a formatação (espaços, quebras de linha).
-   **Destaque de Sintaxe (Syntax Highlighting):** Colorir diferentes partes do código (palavras-chave, comentários, strings, etc.) de acordo com a linguagem de programação para melhorar a legibilidade.
-   **Identificação da Linguagem (Opcional, mas Recomendado):** Indicar a linguagem do bloco de código (ex: JavaScript, Python, HTML).
-   **Botão "Copiar Código":** Permitir que o usuário copie facilmente todo o conteúdo do bloco de código para a área de transferência.
-   **Rolagem (Scroll):** Se o código for extenso, permitir rolagem horizontal e/ou vertical dentro do bloco.

## Melhores Práticas

-   **Legibilidade:** Usar fontes monoespaçadas claras. Garantir bom contraste entre o texto do código e o fundo do bloco, e entre as diferentes cores do syntax highlighting.
-   **Performance:** O syntax highlighting, especialmente do lado do cliente, não deve impactar significativamente o desempenho da página, principalmente para blocos de código muito grandes.
-   **Consistência no Estilo:** Manter um estilo visual consistente para blocos de código em toda a aplicação/site.
-   **Acessibilidade (a11y):**
    *   Garantir que o texto do código seja selecionável e copiável, mesmo que haja um botão "Copiar".
    *   As cores do syntax highlighting devem ter contraste suficiente.
    *   O botão "Copiar" deve ser acessível por teclado e ter um rótulo claro (ex: `aria-label="Copiar código"`).
    *   Fornecer um feedback audível ou visual (ex: tooltip "Copiado!") após a ação de copiar.
    *   Para o bloco de código em si, semanticamente, pode-se usar `<pre><code>...</code></pre>`. A tag `<pre>` preserva espaços e quebras de linha, e `<code>` indica que o conteúdo é um trecho de código.
-   **Não usar imagens para código:** O código deve ser texto real para ser acessível, selecionável e indexável.
-   **Numeração de Linhas (Opcional):** Pode ser útil para blocos de código mais longos ou quando se referenciando linhas específicas no texto.

## Variações e Funcionalidades Adicionais

-   **Tema Claro/Escuro:** Oferecer variações de tema para o bloco de código.
-   **Título/Nome do Arquivo:** Exibir um título ou nome de arquivo associado ao bloco de código.
-   **Opção de Download:** Permitir o download do trecho de código como um arquivo.
-   **Edição Simples (Raro):** Em alguns contextos (playgrounds de código), permitir edição leve.

## Estrutura Comum

-   Contêiner principal do bloco.
-   (Opcional) Cabeçalho com nome da linguagem, nome do arquivo, botão de copiar.
-   Área de código (dentro de `<pre><code>`).
-   (Opcional) Numeração de linhas.

## Exemplo de Marcação (Simplificado)

```html
<div class="code-block">
  <div class="code-block-header">
    <span class="language">JavaScript</span>
    <button aria-label="Copiar código">Copiar</button>
  </div>
  <pre><code class="language-javascript">
function greet(name) {
  console.log('Hello, ' + name + '!');
}
  </code></pre>
</div>
```

## O Que Evitar

-   Destaque de sintaxe com baixo contraste ou cores confusas.
-   Fontes não monoespaçadas para o código.
-   Bloquear a seleção de texto manual.
-   Processamento de syntax highlighting muito pesado que cause lentidão. 