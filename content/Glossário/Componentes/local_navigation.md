---
title: "local navigation"

---

## Local Navigation (Navegação Local)

Local Navigation (Navegação Local) refere-se a sistemas de navegação que permitem ao usuário mover-se entre seções ou visualizações relacionadas dentro de uma área específica de um site ou aplicativo. É distinta da navegação global (principal) do site.

## Casos de Uso

-   **Abas (Tabs):** Para alternar entre diferentes painéis de conteúdo dentro da mesma página ou seção (ex: abas em uma página de perfil de usuário: "Visão Geral", "Atividade", "[[Glossário/Padrões/settings|Configurações]]").
-   **[[Glossário/Componentes/menu|Menus]] Laterais de Seção (Section Side [[Glossário/Componentes/menu|Menus]]):** Em uma seção complexa de um site (ex: [[Glossário/Padrões/settings|configurações]] de conta, documentação de produto), um [[Glossário/Componentes/menu|menu]] lateral pode listar todas as subpáginas ou subseções.
-   **[[Glossário/Componentes/menu|Menus]] Horizontais Secundários:** Uma barra de [[Glossário/Elementos/links|links]] abaixo do [[Glossário/Elementos/cabecalhos|cabeçalho]] principal para navegar entre as principais áreas de uma seção específica.
-   **[[Glossário/Componentes/breadcrumbs|Breadcrumbs]]:** Embora também um auxílio de localização, podem funcionar como navegação local para níveis hierárquicos superiores.
-   **[[Glossário/Componentes/menu|Menu]] de Steps (Passos):** Para guiar o usuário através de um processo linear com múltiplas etapas (ex: [[Glossário/Padrões/purchase_checkout|checkout]], configuração).
-   **Índice (Table of Contents):** Em artigos longos ou páginas de documentação, um índice com [[Glossário/Elementos/links|links]] para as diferentes seções.

## Tipos Comuns e Seus Componentes

1.  **Abas (Tabs):**
    *   **[[Glossário/Elementos/listas|Lista]] de Abas:** Contêiner com os rótulos das abas clicáveis.
    *   **Painéis de Aba:** Conteúdo associado a cada aba, onde apenas um é visível por vez.
    *   Melhores Práticas: Indicar claramente a aba ativa. Usar para conteúdo que pode ser logicamente agrupado e visualizado independentemente.

2.  **[[Glossário/Componentes/menu|Menus]] Verticais/Laterais (para navegação local):**
    *   [[Glossário/Elementos/listas|Lista]] de [[Glossário/Elementos/links|links]] empilhados verticalmente.
    *   Pode ter múltiplos níveis (submenus que expandem).
    *   Melhores Práticas: Indicar a página/seção ativa. Usar para seções com muitas sub-opções.

3.  **[[Glossário/Componentes/menu|Menus]] Horizontais (para navegação local):**
    *   Linha de [[Glossário/Elementos/links|links]] de texto.
    *   Melhores Práticas: Para um número limitado de opções de navegação local. Indicar o item ativo.

4.  **Steppers (Indicadores de Etapa):**
    *   Visualização de etapas numeradas ou nomeadas, com indicação da etapa atual, concluídas e futuras.
    *   Pode ser clicável para navegar entre etapas (se permitido pelo fluxo).

## Melhores Práticas Gerais

-   **Contexto Claro:** O usuário deve entender que a navegação é local para a seção em que está, e não global.
-   **Indicação de Localização Ativa:** Sempre destacar visualmente o item de navegação ou aba atual.
-   **Consistência:** Usar padrões de navegação local consistentes dentro de seções semelhantes.
-   **Evitar Complexidade Excessiva:** Não aninhar muitos níveis de navegação local, o que pode confundir o usuário.
-   **Acessibilidade (a11y):**
    *   Para Abas: Usar `role="tablist"`, `role="tab"`, `role="tabpanel"` e atributos como `aria-selected`, `aria-controls`.
    *   Para [[Glossário/Componentes/menu|Menus]]: Usar [[Glossário/Elementos/listas|listas]] de links (`<ul><li><a>...</a></li></ul>`). O item ativo deve ter `aria-current="page"` (ou `aria-current="true"` para um item dentro de um conjunto).
    *   Para Steppers: Cada etapa pode ser um [[Glossário/Elementos/links|link]], e o estado atual/concluído deve ser comunicado visualmente e para leitores de tela.
    *   Garantir navegação por teclado completa.
-   **Responsividade:** A navegação local deve se adaptar a telas menores. [[Glossário/Componentes/menu|Menus]] horizontais podem se transformar em dropdowns ou [[Glossário/Componentes/menu|menus]] verticais. Abas podem se tornar roláveis horizontalmente ou acordeões.

## O Que Evitar

-   Usar navegação local que se parece muito com a navegação global, confundindo o usuário.
-   Esconder opções de navegação local importantes.
-   Falta de indicação clara do item ativo.
-   Navegação local inconsistente entre diferentes partes de uma seção.
-   Muitas opções em um [[Glossário/Componentes/menu|menu]] horizontal que quebra em múltiplas linhas de forma desajeitada.
