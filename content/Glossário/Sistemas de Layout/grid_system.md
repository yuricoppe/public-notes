# Sistema de Grid

## Descrição Geral
O sistema de grid é a espinha dorsal da organização espacial do nosso portal. Ele fornece uma estrutura consistente para alinhar e posicionar os elementos da interface, garantindo harmonia visual, previsibilidade e facilitando o design responsivo.

Nosso portal utiliza um **sistema de grid de 12 colunas flexíveis**.

## Princípios Chave
- **Consistência:** Todos os layouts de página e componentes devem se alinhar a este grid.
- **Flexibilidade:** O grid de 12 colunas permite uma ampla variedade de subdivisões para diferentes necessidades de layout.
- **Responsividade:** O grid é projetado para se adaptar fluidamente a diferentes [[Glossário/Sistemas de Layout/breakpoints|breakpoints]].

## Especificações

- **Número de Colunas:** 12
- **Gutter (Medianiz):**
    - **Desktop:** 24px (12px de cada lado da coluna)
    - **Tablet:** 16px (8px de cada lado da coluna)
    - **Mobile:** 16px (8px de cada lado da coluna)
- **Margens Laterais da Página (Page Margins):**
    - **Desktop (acima de 1200px):** 32px
    - **Tablet (entre 768px e 1199px):** 24px
    - **Mobile (abaixo de 767px):** 16px
- **Largura Máxima do Conteúdo (Max Content Width):** 1200px (dentro das margens da página).

## Como Usar

- Os elementos de layout principais (seções, contêineres de conteúdo) devem abranger um número de colunas do grid.
- O conteúdo dentro desses elementos também deve respeitar o alinhamento do grid.
- Os gutters são os espaços *entre* as colunas. O conteúdo não deve vazar para dentro dos gutters, a menos que seja uma decisão de design intencional e justificada (ex: [[Glossário/Elementos/imagem|imagens]] que sangram).

### Exemplo de Classes (Conceitual)

Em um sistema de classes CSS, isso poderia ser representado como:

```html
<div class="container">
  <div class="row">
    <div class="col-md-8">Conteúdo Principal (ocupa 8 de 12 colunas)</div>
    <div class="col-md-4">Barra Lateral (ocupa 4 de 12 colunas)</div>
  </div>
  <div class="row">
    <div class="col-md-12">Conteúdo de Largura Total (ocupa 12 de 12 colunas)</div>
  </div>
  <div class="row">
    <div class="col-md-6">Metade</div>
    <div class="col-md-6">Outra Metade</div>
  </div>
  <div class="row">
    <div class="col-md-3">Um Quarto</div>
    <div class="col-md-3">Um Quarto</div>
    <div class="col-md-3">Um Quarto</div>
    <div class="col-md-3">Um Quarto</div>
  </div>
</div>
```

## Responsividade

- Em telas menores (tablets e mobiles), as colunas podem precisar ser empilhadas (stack) verticalmente ou ter suas proporções ajustadas.
- A definição de como as colunas se comportam em diferentes [[Glossário/Sistemas de Layout/breakpoints|breakpoints]] será detalhada em `breakpoints.md` e nas especificações dos componentes.

## Boas Práticas
- **Planeje o Layout:** Antes de implementar, pense em como o conteúdo se encaixará no grid.
- **Evite Quebrar o Grid:** Não force elementos a desalinharem sem uma boa razão.
- **Use o Grid para [[Glossário/Linguagem Visual/espacamento|Espaçamento]] Horizontal:** O grid ajuda a manter o [[Glossário/Linguagem Visual/espacamento|espaçamento]] horizontal consistente.
- **Teste em Diferentes Telas:** Verifique sempre como o layout do grid se comporta em diversos dispositivos.

## Recursos Adicionais / Figma
- [[[Glossário/Elementos/links|Link]] para a especificação do Grid System no Figma]
- [Exemplos de layouts de página utilizando o grid] 