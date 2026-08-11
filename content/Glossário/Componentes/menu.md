---
title: "Menu (Genérico)"
description: "O componente Menu é uma lista de opções ou ações apresentadas ao usuário."
tags:
  - tema/ui
  - tipo/glossario
---

## Menu (Genérico)

O componente Menu é uma [[Glossário/Elementos/listas|lista]] de opções ou ações apresentadas ao usuário. Pode ser usado para navegação, executar comandos ou selecionar [[Glossário/Padrões/settings|configurações]]. Esta documentação cobre o conceito genérico de menu, que pode se manifestar de várias formas (ex: [[Glossário/Elementos/form_controls|dropdown]] menu, context menu, navigation menu).

## Casos de Uso

-   **Menu de Navegação Principal (Navbar Menu):** Parte da navegação global do site.
-   **Menu Dropdown:** Uma lista de opções que aparece quando um [[Glossário/Elementos/botoes|botão]] ou item de menu é clicado/hover.
-   **Menu de Contexto (Context Menu / Right-Click Menu):** Uma lista de ações relevantes para um elemento específico da interface, geralmente acionada por um clique com o botão direito ou toque longo.
-   **Menu de Ações de Item (Item Action Menu):** Um menu (frequentemente um [[Glossário/Linguagem Visual/iconografia|ícone]] de "três pontos" ou "kebab") associado a um item em uma lista ou [[Glossário/Componentes/cards|card]], revelando ações para aquele item.
-   **Menu de Configurações de Conta/Perfil.**
-   **Menu de [[Glossário/Componentes/filters|Filtros]] ou Ordenação.**

## Elementos Comuns

![Menu suspenso anotado: gatilho com aria-expanded, itens com ícone, atalho e seta de submenu, separadores e item desabilitado, mais o mapa de navegação por teclado](attachments/glossario-anatomia-menu.svg)

-   **Gatilho (Trigger):** O elemento que abre o menu (pode ser um botão, [[Glossário/Elementos/links|link]], ícone, ou o próprio item de menu pai em um menu multinível).
-   **Contêiner do Menu:** O painel que contém a lista de itens de menu.
-   **Itens de Menu (Menu Items):**
    *   Rótulo textual da opção/ação.
    *   (Opcional) Ícone à esquerda do rótulo.
    *   (Opcional) Indicador de submenu (ex: seta para a direita) se o item abrir outro nível de menu.
    *   (Opcional) Tecla de atalho (ex: Ctrl+S).
    *   (Opcional) Estado (desabilitado, selecionado/ativo).
-   **Separadores (Opcional):** Linhas para agrupar itens de menu relacionados.
-   **Submenus (Opcional):** Menus aninhados que aparecem ao interagir com um item de menu pai.

## Melhores Práticas

-   **Clareza e Concisão:** Rótulos dos itens de menu devem ser curtos, claros e orientados para a ação (se aplicável).
-   **Organização Lógica:** Agrupar itens relacionados. Os itens mais frequentes ou importantes podem vir no topo.
-   **Feedback Visual:** Indicar claramente quando um item de menu está em foco (hover/teclado) ou selecionado.
-   **Navegação por Teclado:** Suporte completo para navegação com teclas de seta (para cima/baixo para mover entre itens, direita/esquerda ou Enter para abrir/fechar submenus ou selecionar), `Enter`/`Espaço` para ativar um item, `Escape` para fechar o menu.
-   **Acessibilidade (a11y):**
    *   Usar roles ARIA apropriados: `role="menubar"` (para menus horizontais persistentes), `role="menu"` (para menus popup), `role="menuitem"`, `role="menuitemcheckbox"`, `role="menuitemradio"`, `role="separator"`.
    *   Usar `aria-haspopup="true"` (ou `aria-haspopup="menu"`) no gatilho.
    *   Usar `aria-expanded` no gatilho para indicar se o menu está aberto ou fechado.
    *   Gerenciar o foco corretamente: ao abrir, o foco vai para o primeiro item; ao fechar, retorna ao gatilho.
-   **Consistência:** Manter um estilo e comportamento consistentes para menus em toda a aplicação.
-   **Evitar Níveis Múltiplos Excessivos:** Submenus muito profundos podem ser difíceis de navegar (especialmente em menus dropdown).
-   **Responsividade:** Menus devem se adaptar a diferentes tamanhos de tela. Menus de navegação podem se transformar em menus hambúrguer. Menus de contexto podem precisar de ajustes.

## Variações Comuns

-   **Menu Horizontal vs. Vertical.**
-   **Menu Popup (Dropdown, Contexto).**
-   **Menu Fixo (Navbar).**
-   **Menu com Ícones e Texto.**
-   **Menu Apenas com Ícones (com tooltips para acessibilidade).**

## O Que Evitar

-   Rótulos de menu ambíguos ou muito longos.
-   Menus desorganizados ou com muitos itens não agrupados.
-   Dificuldade em fechar um menu (ex: sem tecla Escape, ou área de clique pequena para fechar).
-   Submenus que desaparecem muito facilmente ao tentar mover o mouse para eles (problema comum em menus dropdown com submenus laterais).
-   Ignorar a navegação por teclado ou a acessibilidade ARIA.
