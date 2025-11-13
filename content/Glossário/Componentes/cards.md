# Cards (Cartões)

Cards são contêineres de interface que agrupam informações e ações relacionadas sobre um único tópico ou item. Eles são uma forma popular de apresentar conteúdo de maneira organizada e escaneável, especialmente em layouts de grade ou [[Elementos/listas|listas]].

## Casos de Uso

-   Exibição de produtos em um e-commerce.
-   Artigos de blog ou notícias.
-   Perfis de usuário.
-   Listagem de eventos, cursos, ou qualquer item individual.
-   Tarefas em um painel Kanban.
-   Resumos de dados ou widgets em dashboards.

## Elementos Comuns de um Card

Um card pode conter uma combinação dos seguintes elementos:

-   **Mídia (Opcional):** [[Elementos/imagem|Imagem]], vídeo, ilustração no topo ou lateral do card.
-   **[[Elementos/cabecalhos|Cabeçalho]]/Título (Opcional):** Título principal do card.
-   **Subtítulo/Descrição Curta (Opcional):** Informação secundária ou um breve resumo.
-   **Conteúdo Principal (Opcional):** Texto mais detalhado, [[Elementos/listas|listas]], metadados.
-   **Ações (Opcional):** [[Elementos/botoes|Botões]], [[Elementos/links|links]] ou [[Linguagem Visual/iconografia|ícones]] que permitem ao usuário interagir com o conteúdo do card (ex: "Saiba Mais", "Adicionar ao Carrinho", "Editar").
-   **[[Linguagem Visual/iconografia|Ícones]] (Opcional):** Para metadados ou ações.
-   **Avatar/Thumbnail (Opcional):** Pequena [[Elementos/imagem|imagem]] representando um usuário ou item.
-   **Tags/[[Componentes/badges|Badges]] (Opcional):** Para categorizar ou destacar status.

## Melhores Práticas

-   **Consistência de Conteúdo:** Cards em um mesmo grupo devem ter uma estrutura e tipos de conteúdo semelhantes para facilitar a comparação e a escaneabilidade.
-   **Hierarquia Visual Clara:** Usar [[Linguagem Visual/tipografia|tipografia]], [[Linguagem Visual/espacamento|espaçamento]] e ênfase para guiar o olho do usuário através das informações do card.
-   **Área Clicável:** Se o card inteiro for clicável e levar a uma página de detalhes, isso deve ser claro. Se houver múltiplas ações dentro do card, elas devem ser os alvos clicáveis primários.
-   **[[Linguagem Visual/espacamento|Espaçamento]]:** Usar padding adequado dentro do card e margens entre os cards para evitar um layout congestionado.
-   **Responsividade:** Cards devem se adaptar bem a diferentes tamanhos de tela, ajustando seu tamanho, layout interno (ex: mídia no topo em mobile, lateral em desktop) ou o número de colunas em um grid.
-   **Limitar Conteúdo:** Não sobrecarregar os cards com muita informação. Eles são melhores para resumos que levam a mais detalhes.
-   **Acessibilidade (a11y):**
    *   Garantir que o conteúdo do card siga uma ordem lógica no DOM.
    *   Se o card inteiro for um [[Elementos/links|link]], envolva seu conteúdo em uma tag `<a>` ou use JavaScript para adicionar o comportamento de clique e role `button` com `aria-label` adequado.
    *   Todos os elementos interativos dentro do card ([[Elementos/botoes|botões]], [[Elementos/links|links]]) devem ser acessíveis por teclado e ter rótulos claros.
    *   [[Elementos/imagem|Imagens]] devem ter `alt` text.

## Variações de Estilo e Layout

-   **Card Padrão:** Mídia no topo, seguida de título, descrição e ações.
-   **Card com Mídia Lateral:** [[Elementos/imagem|Imagem]] à esquerda ou direita, com conteúdo ao lado.
-   **Card Horizontal:** Mais largo do que alto, frequentemente usado em [[Elementos/listas|listas]].
-   **Card Compacto:** Menor, com menos informação, para [[Elementos/listas|listas]] densas.
-   **Card de Destaque (Featured Card):** Pode ser maior ou ter um estilo visual diferente para chamar mais atenção.
-   **Card com Overlay:** Texto ou ações sobrepostas à mídia (usar com cuidado para garantir legibilidade).

## Interações Comuns

-   **Hover State:** Feedback visual ao passar o mouse (ex: sombra sutil, leve elevação).
-   **Click/Tap:** Navegar para uma visão detalhada ou executar uma ação primária.

## O Que Evitar

-   Cards com alturas muito variáveis em um mesmo grid, o que pode criar um layout desordenado (a menos que seja um layout estilo Masonry intencional).
-   Excesso de informações ou ações, tornando o card confuso.
-   Falta de clareza sobre o que é clicável.
-   Contraste insuficiente entre o texto e o fundo do card, especialmente se usar [[Elementos/imagem|imagens]] de fundo. 