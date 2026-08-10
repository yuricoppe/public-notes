---
title: "principios movimento"
description: "Esta seção aborda os princípios fundamentais que guiam o uso de movimento e animações na interface, com o objetivo de criar experiências de usuário mais intuitivas, responsivas…"
tags:
  - tema/ui
  - tema/design-system
  - tipo/glossario
---

## Princípios do Movimento

Esta seção aborda os princípios fundamentais que guiam o uso de [[Glossário/Linguagem Visual/movimento|movimento]] e animações na interface, com o objetivo de criar experiências de usuário mais intuitivas, responsivas e agradáveis.

## Introdução

O movimento, quando bem aplicado, pode:
- Melhorar a usabilidade, fornecendo feedback e orientação.
- Aumentar o engajamento do usuário.
- Reforçar a hierarquia visual e o fluxo de informações.
- Adicionar personalidade e sofisticação à interface.

## Nossos Princípios Fundamentais

1.  **Funcional e Proposital:**
    *   O movimento deve ter um propósito claro, como guiar o usuário, fornecer feedback ou explicar transições. Evitar animações puramente decorativas que possam distrair ou confundir.

2.  **Responsivo e Performático:**
    *   As animações devem ser suaves e rápidas, sem causar lentidão na interface. O desempenho é crucial para uma boa experiência.
    *   O movimento deve responder às interações do usuário de forma imediata e natural.

3.  **Consistente e Previsível:**
    *   Utilizar padrões de movimento consistentes em todo o sistema. Isso ajuda os usuários a aprenderem como a interface se comporta e a anteciparem resultados.

4.  **Sutil e Discreto:**
    *   Na maioria dos casos, o movimento deve ser sutil para não sobrecarregar o usuário. Animações exageradas podem ser cansativas e prejudicar a usabilidade.

5.  **Contextual e Hierárquico:**
    *   O movimento pode ajudar a estabelecer relações espaciais e hierárquicas entre os elementos da interface.
    *   Animações de entrada e saída podem indicar a origem e o destino de novos elementos ou visualizações.

6.  **Acessível:**
    *   Considerar usuários com sensibilidade a movimento. Oferecer opções para reduzir ou desabilitar animações complexas, se necessário.
    *   Garantir que o movimento não seja o único meio de transmitir informações importantes.

## Timing e Curvas de Animação (Easing)

-   **Duração:**
    *   **Rápida (100-200ms):** Para feedback sutil e pequenas transições (ex: hover de [[Glossário/Elementos/botoes|botão]]).
    *   **Média (200-400ms):** Para transições de painéis, [[Glossário/Componentes/dialog|modais]], expansão de elementos.
    *   **Lenta (>400ms):** Usar com moderação, geralmente para animações mais complexas ou que envolvem elementos maiores. Evitar durações excessivamente longas.

-   **Curvas de Animação (Easing Functions):**
    *   **`ease-out` (desaceleração):** Elementos entram na tela rapidamente e desaceleram. Bom para elementos que aparecem.
    *   **`ease-in` (aceleração):** Elementos começam devagar e aceleram ao sair. Bom para elementos que desaparecem.
    *   **`ease-in-out` (aceleração e desaceleração):** Suave no início e no fim. Bom para transições onde o elemento está sempre visível e muda de estado ou posição.
    *   **`linear`:** Movimento constante. Raramente usado para UI, pois pode parecer artificial.

## Exemplos de Aplicação

-   **Feedback de Interação:** Animação sutil em botões ao passar o mouse ou clicar.
-   **Transições de Estado:** Mudança suave de [[Glossário/Linguagem Visual/cor|cor]] ou [[Glossário/Linguagem Visual/iconografia|ícone]] para indicar uma alteração de estado.
-   **Transições de Página/View:** Animações que indicam a direção da navegação (ex: slide).
-   **Revelação de Conteúdo:** Expansão de acordeões ou [[Glossário/Componentes/menu|menus]] [[Glossário/Elementos/form_controls|dropdown]].
-   **Notificações e Alertas:** Movimento sutil para chamar a atenção para novas [[Glossário/Componentes/messaging|mensagens]].

## Ferramentas

-   Referência a bibliotecas de animação utilizadas (se houver).
-   Links para exemplos no Figma ou [[Glossário/Entregáveis/prototype|protótipos]].

## O Que Evitar

-   Animações longas e desnecessárias.
-   Movimento que obstrui o conteúdo ou a tarefa do usuário.
-   Excesso de animações diferentes na mesma tela.
-   Animações que causam problemas de performance.
