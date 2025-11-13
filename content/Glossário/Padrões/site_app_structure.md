# Estrutura do Site / Aplicativo (Site / App Structure)

## Descrição Geral
O padrão de estrutura do site/aplicativo refere-se à organização geral e arquitetura da informação de um portal ou aplicação. Envolve como o conteúdo e as funcionalidades são agrupados, interligados e apresentados ao usuário através da navegação principal, [[Glossário/Componentes/menu|menus]], hierarquia de páginas e fluxos de usuário. Uma estrutura bem pensada é fundamental para a usabilidade, encontrabilidade (findability) e compreensão do sistema pelo usuário.

Este é um padrão de alto nível que influencia muitos outros padrões de UI (como navegação, [[Glossário/Componentes/menu|menus]], [[Glossário/Componentes/breadcrumbs|breadcrumbs]]) e está intrinsecamente ligado à Arquitetura da Informação (AI).

## Princípios Chave / Objetivos
- **Intuitividade:** A estrutura deve ser lógica e fácil para os usuários entenderem e preverem onde encontrar informações ou funcionalidades.
- **Encontrabilidade (Findability):** Os usuários devem conseguir localizar o que precisam de forma rápida e eficiente.
- **Eficiência:** Permitir que os usuários completem suas tarefas com o mínimo de esforço e cliques.
- **Escalabilidade:** A estrutura deve ser capaz de acomodar crescimento futuro (novo conteúdo, novas funcionalidades) sem se tornar confusa.
- **Consistência:** A organização e a navegação devem ser consistentes em todo o portal.
- **Orientação:** Ajudar os usuários a entenderem onde estão dentro do site/app e como chegar a outros lugares.

## Elementos Comuns / Estrutura Típica
- **Navegação Principal (Primary Navigation):** [[Glossário/Componentes/menu|Menu]] principal que dá acesso às seções de mais alto nível (ex: [[Glossário/Elementos/cabecalhos|cabeçalho]], [[Glossário/Componentes/menu|menu]] lateral).
- **Navegação Secundária/Local (Secondary/[[Glossário/Componentes/local_navigation|Local Navigation]]):** [[Glossário/Componentes/menu|Menus]] específicos para seções ou subseções.
- **[[Glossário/Componentes/maps|Mapas]] do Site (Sitemaps):** Representação visual ou textual da hierarquia do conteúdo.
- **[[Glossário/Componentes/breadcrumbs|Breadcrumbs]]:** Indicam a localização atual do usuário na hierarquia do site.
- **Página Inicial (Homepage/[[Glossário/Entregáveis/dashboard|Dashboard]]):** Ponto de partida principal, oferecendo acesso a seções chave e conteúdo em destaque.
- **[[Glossário/Componentes/footer|Rodapé]] ([[Glossário/Componentes/footer|Footer]] Navigation):** [[Glossário/Elementos/links|Links]] para informações secundárias, políticas, contato, etc.
- **Função de Busca Global (Global Search):** Permite ao usuário pesquisar em todo o conteúdo do site/app.
- **Hierarquia de Conteúdo:** Como as informações são organizadas em páginas, seções e subseções.
- **Fluxos de Usuário (User Flows):** Sequência de etapas que os usuários seguem para completar tarefas específicas.

## Comportamento e Interação
1. O usuário chega ao portal (geralmente na página inicial ou uma página de destino específica).
2. O usuário utiliza os elementos de navegação ([[Glossário/Componentes/menu|menus]], [[Glossário/Elementos/links|links]], busca) para explorar o conteúdo e acessar funcionalidades.
3. A estrutura guia o usuário através de diferentes seções e níveis de informação.
4. [[Glossário/Componentes/breadcrumbs|Breadcrumbs]] e outros sinais de orientação ajudam o usuário a manter o contexto.
5. Fluxos de usuário bem definidos conduzem a tarefas comuns de forma eficiente.

## Diretrizes de Uso e Boas Práticas

### Faça
- Baseie a estrutura nos modelos mentais e necessidades dos seus usuários (resultado de pesquisa com usuários, [[Glossário/Componentes/cards|card]] sorting, tree testing).
- Mantenha a navegação principal concisa e focada nas tarefas/seções mais importantes.
- Use linguagem clara e familiar nos rótulos de navegação.
- Garanta que a estrutura seja responsiva e funcione bem em diferentes tamanhos de tela.
- Teste a estrutura com usuários reais para identificar problemas de usabilidade.
- Crie uma hierarquia de informação clara e com profundidade razoável (evite muitos níveis aninhados).
- Mantenha a consistência na nomenclatura e posicionamento dos elementos de navegação.

### Não Faça
- Não organize a estrutura com base na organização interna da empresa, mas sim nas necessidades do usuário.
- Não sobrecarregue os [[Glossário/Componentes/menu|menus]] de navegação com muitas opções.
- Não use rótulos de navegação ambíguos ou jargões.
- Não crie becos sem saída onde o usuário não sabe como prosseguir ou voltar.
- Não altere drasticamente a estrutura principal com frequência, pois isso pode confundir usuários recorrentes.

## Considerações de Acessibilidade
- Garanta que toda a navegação seja operável via teclado e que a ordem do foco seja lógica.
- Use marcação semântica apropriada para elementos de navegação (ex: `<nav>`, listas `<ul>`/`<ol>` para menus).
- Forneça um [[Glossário/Elementos/links|link]] "Pular para o conteúdo principal" para usuários de teclado e leitores de tela.
- Certifique-se de que os [[Glossário/Elementos/links|links]] tenham texto descritivo que faça sentido fora de contexto.
- [[Glossário/Componentes/breadcrumbs|Breadcrumbs]] devem ser implementados de forma acessível.
- O [[Glossário/Entregáveis/site_map|mapa do site]], se fornecido, deve ser acessível.

## Exemplos / Cenários de Uso
- Estrutura de um portal de e-commerce (categorias de produtos, conta do usuário, carrinho, [[Glossário/Padrões/purchase_checkout|checkout]]).
- Estrutura de um portal de notícias (seções temáticas, artigos, busca, arquivos).
- Arquitetura de um aplicativo SaaS ([[Glossário/Entregáveis/dashboard|dashboard]], módulos de funcionalidades, [[Glossário/Padrões/settings|configurações]], ajuda).
- Organização de um site institucional (sobre nós, serviços, contato, blog).

## Variações Comuns (Modelos Organizacionais)
- **Hierárquica (Árvore):** Estrutura de cima para baixo, com categorias e subcategorias.
- **Sequencial:** Informação apresentada em uma ordem específica, passo a passo (ex: tutoriais, processos de [[Glossário/Padrões/purchase_checkout|checkout]]).
- **Matricial:** Permite que os usuários naveguem por múltiplos atributos ou facetas (comum em [[Glossário/Componentes/filters|filtros]] de busca).
- **Orgânica/Rede:** Conteúdo interligado de forma mais fluida, com muitos [[Glossário/Elementos/links|links]] cruzados (ex: wikis).
- **Baseada em Tarefas:** Estrutura organizada em torno das principais tarefas que os usuários precisam realizar.

## Status
A definir

## Recursos Adicionais / Figma
- [[[Glossário/Elementos/links|Link]] para o [[Glossário/Entregáveis/site_map|mapa do site]] ou diagramas da arquitetura da informação]
- [[[Glossário/Elementos/links|Link]] para [[Glossário/Entregáveis/wireframe|wireframes]] ou [[Glossário/Entregáveis/prototype|protótipos]] mostrando a navegação principal e fluxos de usuário]
- [Documentação de resultados de [[Glossário/Componentes/cards|card]] sorting ou tree testing] 