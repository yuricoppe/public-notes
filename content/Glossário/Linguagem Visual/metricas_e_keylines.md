# Métricas e Keylines

Esta documentação estabelece as métricas, grids e keylines utilizados para garantir consistência visual, alinhamento preciso e [[Linguagem Visual/espacamento|espaçamento]] harmonioso em todas as interfaces do nosso produto.

## Introdução

Métricas e keylines são fundamentais para:
- Criar uma base visual coesa e organizada.
- Facilitar o trabalho de design e desenvolvimento, fornecendo diretrizes claras.
- Assegurar que os elementos da interface estejam alinhados e espaçados de forma previsível em diferentes dispositivos e resoluções.
- Melhorar a legibilidade e a estética geral da interface.

## Unidade Base (Base Unit)

-   **Definição:** A unidade base é o menor valor de [[Linguagem Visual/espacamento|espaçamento]] e dimensionamento utilizado no sistema. Todos os outros valores de [[Linguagem Visual/espacamento|espaçamento]] e tamanho são múltiplos dessa unidade.
-   **Nosso Padrão:** `8px`.
    -   *Justificativa:* O valor de 8px (e seus múltiplos) é amplamente adotado por ser divisível por 2 e 4, o que facilita o dimensionamento para diversas densidades de tela e oferece uma boa granularidade para espaçamentos.

## Escala de [[Linguagem Visual/espacamento|Espaçamento]] ([[Linguagem Visual/espacamento|Spacing]] Scale)

Baseada na nossa unidade de `8px`:

-   `xx-small (0.25x)`: `2px` (para micro espaçamentos, como entre um [[Linguagem Visual/iconografia|ícone]] e seu texto adjacente, se muito próximos)
-   `x-small (0.5x)`: `4px` (para espaçamentos pequenos, como padding interno de pequenos [[Elementos/botoes|botões]] ou entre ícones)
-   `small (1x)`: `8px` (padding comum, margens entre elementos relacionados)
-   `medium (2x)`: `16px` (espaçamento entre seções de conteúdo, padding de cards)
-   `large (3x)`: `24px` (margens maiores, [[Linguagem Visual/espacamento|espaçamento]] entre grupos de elementos distintos)
-   `x-large (4x)`: `32px` (espaçamento significativo entre grandes blocos de layout)
-   `xx-large (6x)`: `48px` (usado para espaçamentos muito amplos, como entre o [[Componentes/header|header]] e o conteúdo principal da página)
-   `xxx-large (8x)`: `64px` (para áreas de respiro visual consideráveis)

**Como usar:** Aplicar consistentemente esta escala para margens, paddings e o espaço entre elementos.

## Grid de Layout Principal (Main Layout Grid)

-   **Tipo de Grid:** Grid de colunas responsivo.
-   **Número de Colunas:** `12 colunas` (para desktops e tablets).
    -   Em dispositivos móveis, o layout pode se adaptar para `4 ou 6 colunas` ou empilhar o conteúdo.
-   **Gutter (Calha):** `16px` (espaço entre as colunas).
-   **Margens Laterais (Page Margins):**
    -   Desktop: `32px` ou mais, dependendo da largura da viewport.
    -   Tablet: `24px`.
    -   Mobile: `16px`.

## Keylines (Linhas-Chave)

Keylines são linhas guias invisíveis que ajudam a alinhar elementos na interface de forma consistente. Elas são especialmente importantes para alinhar texto, [[Linguagem Visual/iconografia|ícones]] e outros elementos dentro de componentes e em relação à tela.

### Keylines Verticais Comuns:
-   Alinhamento de texto com [[Linguagem Visual/iconografia|ícones]].
-   Alinhamento de títulos com o corpo do texto.
-   Alinhamento de elementos dentro de [[Elementos/listas|listas]] ou tabelas.

### Keylines Horizontais Comuns:
-   Linha de base do texto.
-   Alinhamento superior e central de elementos em uma barra de navegação ou [[Elementos/cabecalhos|cabeçalho]].

## Densidade da Interface

-   **Padrão:** Interface com densidade equilibrada, priorizando a legibilidade e a facilidade de interação.
-   **Compacta (Opcional):** Para casos de uso específicos que exigem alta densidade de informação (ex: dashboards complexos), pode-se considerar uma variação com espaçamentos reduzidos (ex: múltiplos de `4px` como base secundária para componentes compactos), mas sempre mantendo a clareza.

## Exemplos Visuais

(Incluir aqui diagramas e exemplos visuais de aplicação do grid, da escala de [[Linguagem Visual/espacamento|espaçamento]] e das keylines em componentes e layouts de página. [[Entregáveis/mockup|Mockups]] com as guias visíveis são muito úteis.)

-   Exemplo de um [[Componentes/cards|card]] utilizando a escala de [[Linguagem Visual/espacamento|espaçamento]].
-   Exemplo de um layout de página com o grid de 12 colunas.
-   Exemplo de alinhamento de [[Linguagem Visual/iconografia|ícones]] e texto usando keylines.

## Ferramentas e Recursos

-   Especificações do grid para Figma/Sketch.
-   Variáveis de [[Linguagem Visual/espacamento|espaçamento]] (tokens) para desenvolvedores.

## Considerações de Responsividade

-   Como a escala de [[Linguagem Visual/espacamento|espaçamento]] e o grid se adaptam a diferentes tamanhos de tela.
-   [[Sistemas de Layout/breakpoints|Breakpoints]] principais e como o layout se ajusta. 