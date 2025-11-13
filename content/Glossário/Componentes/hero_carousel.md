---
title: "hero carousel"

---

## Hero Carousel (Carrossel de Destaque)

O Hero Carousel (Carrossel de Destaque) é uma variação do componente Hero/Billboard que exibe múltiplos slides de destaque em rotação. Cada slide geralmente contém uma [[Glossário/Elementos/imagem|imagem]] ou vídeo, título, descrição e um Call to Action (CTA), similar a um Hero individual.

**Atenção:** Carrosséis, especialmente os automáticos, são frequentemente criticados por questões de usabilidade, acessibilidade e eficácia. Use com extrema moderação e considere alternativas. Se for utilizá-lo, siga rigorosamente as melhores práticas.

## Casos de Uso

-   Mostrar múltiplas promoções ou [[Glossário/Componentes/messaging|mensagens]] importantes no topo de uma página inicial, quando há mais de uma mensagem principal competindo por atenção.
-   Exibir um portfólio rotativo de produtos ou projetos em destaque.

## Elementos Comuns

Cada slide dentro do carrossel geralmente contém os elementos de um Hero padrão:
-   **[[Glossário/Elementos/imagem|Imagem]] de Fundo ou Vídeo.**
-   **Título Principal (Headline).**
-   **Subtítulo ou Descrição.**
-   **Call to Action (CTA) Principal.**

Elementos específicos do Carrossel:
-   **Controles de Navegação:**
    *   **Setas "Anterior"/"Próximo":** Para o usuário navegar manualmente entre os slides.
    *   **Indicadores de Slide (Dots/Pontos):** Pequenos pontos ou miniaturas que mostram quantos slides existem e qual está ativo. Podem ser clicáveis para navegar diretamente para um slide.
-   **(Opcional) [[Glossário/Elementos/botoes|Botão]] Play/Pause:** Se o carrossel tiver rotação automática.
-   **(Opcional) Animação de Transição:** Como os slides mudam (ex: fade, slide horizontal).

## Melhores Práticas

-   **Priorize Conteúdo Estático:** Um Hero estático bem projetado é geralmente mais eficaz. Use carrosséis apenas se houver uma forte justificativa de negócio e múltiplas [[Glossário/Componentes/messaging|mensagens]] de igual importância.
-   **Controle do Usuário é Essencial:**
    *   **Evite Rotação Automática:** Se usar, forneça controles claros de Pausa/Play. A rotação automática pode ser distrativa e os usuários podem perder conteúdo.
    *   A velocidade da rotação automática deve ser lenta o suficiente para leitura, mas não tão lenta que se torne tediosa.
    *   Pausar a rotação ao passar o mouse (hover) ou focar.
-   **Navegação Clara:** Setas e indicadores de slide devem ser visíveis e fáceis de usar.
-   **Primeiro Slide Mais Importante:** O primeiro slide é o mais visto. Coloque sua mensagem mais crucial nele.
-   **Número Limitado de Slides:** Evitar muitos slides (idealmente 3-5 no máximo). Poucos usuários passam de todos eles.
-   **Consistência Visual entre Slides:** Manter um design e layout consistentes, mudando apenas o conteúdo específico.
-   **Performance:** Otimizar [[Glossário/Elementos/imagem|imagens]]/vídeos para cada slide. Carregar apenas os assets do slide atual e talvez do próximo/anterior (lazy loading) para melhorar o tempo de carregamento inicial.
-   **Acessibilidade (a11y):**
    *   **Controles Acessíveis:** Todos os controles (setas, pontos, play/pause) devem ser operáveis por teclado e ter rótulos ARIA claros.
    *   **Anunciar Mudanças de Slide:** Para leitores de tela, as mudanças de slide (especialmente automáticas) devem ser anunciadas usando `aria-live` regions. O conteúdo do novo slide deve ser acessível.
    *   **Foco:** Gerenciar o foco do teclado de forma lógica ao interagir com os controles.
    *   **Pausar Rotação:** Garantir que usuários possam pausar, parar ou esconder o [[Glossário/Linguagem Visual/movimento|movimento]] se durar mais que 5 segundos (WCAG).
-   **Responsividade:** O carrossel deve funcionar bem e ser legível em todos os dispositivos.

## O Que Evitar

-   Rotação automática sem controle de pausa.
-   Muitos slides.
-   Controles de navegação pequenos, escondidos ou difíceis de usar.
-   Transições muito rápidas ou complexas que dificultam a leitura.
-   Conteúdo importante escondido em slides posteriores que a maioria dos usuários não verá.
-   Ignorar as implicações de performance de carregar múltiplas [[Glossário/Elementos/imagem|imagens]]/vídeos grandes.
-   Usar um carrossel quando um simples grid ou uma [[Glossário/Elementos/listas|lista]] de destaques seria mais eficaz.
