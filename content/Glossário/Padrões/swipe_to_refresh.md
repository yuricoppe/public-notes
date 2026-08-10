---
title: "swipe to refresh"
description: "\"Deslizar para Atualizar\" (Swipe to Refresh) é um padrão de interação comum em aplicativos móveis e algumas aplicações web progressivas (PWAs), onde o usuário pode puxar uma…"
tags:
  - tema/ux
  - tipo/glossario
---

## Deslizar para Atualizar (Swipe to Refresh)

## Descrição Geral

"Deslizar para Atualizar" (Swipe to Refresh) é um padrão de interação comum em aplicativos móveis e algumas aplicações web progressivas (PWAs), onde o usuário pode puxar uma [[Glossário/Elementos/listas|lista]] ou tela para baixo com o dedo (ou mouse em alguns contextos desktop) para recarregar o conteúdo exibido. É uma forma intuitiva e gestual de solicitar dados mais recentes.

## Princípios Chave / Objetivos

- **Feedback Imediato:** Fornecer uma indicação visual clara de que a ação de atualização está em progresso.
- **Intuitividade:** Ser uma ação fácil de descobrir e executar em interfaces touch.
- **Performance Percebida:** Oferecer uma maneira rápida de obter conteúdo fresco sem navegação explícita para um [[Glossário/Elementos/botoes|botão]] de atualizar.
- **Não Intrusivo:** A ação não deve interferir com a rolagem normal do conteúdo, a menos que o gesto de "puxar para baixo" seja intencional e exceda um certo limite.

## Elementos Comuns / Estrutura Típica

- **Indicador Visual de "Puxar" (Pull Indicator):** Geralmente um [[Glossário/Linguagem Visual/iconografia|ícone]] (como uma seta para baixo ou um [[Glossário/Componentes/loading_spinner|spinner]] parcial) que aparece no topo da área de conteúdo quando o usuário começa a puxar para baixo.
- **Indicador de Carregamento (Loading Spinner/Indicator):** Um spinner ou animação que aparece quando o limite de "puxar" é atingido e a atualização de dados é iniciada. Substitui o indicador de "puxar".
- **Animação de Transição:** Transições suaves entre os estados de "puxar", "pronto para atualizar" e "atualizando".
- **Feedback Auditivo ou Tátil (Opcional):** Pode complementar o feedback visual.

## Comportamento e Interação

1. O usuário está visualizando uma lista ou tela com conteúdo que pode ser atualizado (ex: feed de notícias, caixa de entrada de emails).
2. O usuário toca na tela e desliza o dedo para baixo a partir do topo da área de conteúdo.
3.  - **Gesto Curto/Rolagem Normal:** Se o gesto de puxar for curto e não atingir um limite predefinido, a interface pode interpretar como rolagem para o topo ou nenhuma ação específica de atualização.
    - **Gesto de Puxar para Atualizar:** Se o usuário puxar para baixo além de um certo limite:
        - Um indicador visual (ex: seta para baixo) aparece e pode se animar (ex: rotacionar) à medida que o usuário puxa mais.
        - Ao soltar o dedo (ou ao atingir um estado "pronto para atualizar"), o indicador visual muda para um spinner de carregamento.
4. O sistema inicia a busca por novo conteúdo em segundo plano.
5.  - **Sucesso com Novo Conteúdo:** O novo conteúdo é carregado e exibido, geralmente no topo da lista, e o spinner desaparece.
    - **Sucesso sem Novo Conteúdo:** O spinner desaparece, e o conteúdo existente permanece (pode haver uma mensagem sutil como "Conteúdo atualizado").
    - **Falha:** O spinner desaparece, e uma mensagem de erro pode ser exibida (ex: "Não foi possível atualizar. Verifique sua conexão.").
6. A área de conteúdo retorna à sua posição normal.

## Diretrizes de Uso e Boas Práticas

### Faça

- Use em listas ou seções de conteúdo que são atualizadas com frequência e onde os usuários esperam ver os dados mais recentes (ex: feeds sociais, emails, resultados esportivos).
- Forneça feedback visual claro durante todo o processo (puxando, pronto para soltar, carregando).
- Mantenha a animação suave e performática.
- Certifique-se de que o limite para ativar a atualização não seja muito sensível (para evitar ativações acidentais) nem muito difícil de alcançar.
- Cancele a ação de atualização se o usuário puxar para baixo e depois deslizar para cima antes de soltar (e antes de atingir o estado "pronto para atualizar").

### Não Faça

- Não use para ações que não sejam de atualização de conteúdo (ex: navegação).
- Não o implemente em conteúdo estático que não muda.
- Não o torne a única forma de atualizar o conteúdo; considere também um botão de atualizar explícito para acessibilidade e descoberta, especialmente em contextos não-mobile.
- Não bloqueie a interface do usuário desnecessariamente durante a atualização; permita que o usuário continue interagindo com o conteúdo visível, se possível (embora o conteúdo possa estar desatualizado até a conclusão).

## Considerações de Acessibilidade

- **Alternativa:** Como este é um gesto primariamente touch, forneça sempre uma alternativa não gestual para atualizar o conteúdo, como um botão de "Atualizar" claramente rotulado e acessível via teclado. Isso é crucial para usuários que não podem realizar o gesto de deslizar ou que usam tecnologias assistivas.
- **Feedback para Leitores de Tela:** Anuncie o estado da atualização (ex: "Atualizando conteúdo...", "Conteúdo atualizado.") usando regiões `aria-live`.
- **Foco do Teclado:** Se um botão de atualização for a alternativa, ele deve ser focável e operável via teclado.

## Exemplos / Cenários de Uso

- Atualizar um feed de notícias em um aplicativo de rede social.
- Verificar novos emails em um aplicativo de email móvel.
- Recarregar resultados de jogos ao vivo em um aplicativo de esportes.
- Atualizar uma lista de tarefas compartilhadas.

## Variações Comuns

- **Indicadores Visuais Personalizados:** A aparência do indicador de puxar e do spinner pode variar de acordo com o [[Glossário/Entregáveis/design_system|design system]] da aplicação.
- **Integração com "Pull to Refresh, Push for More":** Algumas listas podem combinar "puxar para baixo para atualizar" com "empurrar para cima no final da lista para carregar mais itens (paginação)".

## Status

A definir

## Recursos Adicionais / Figma

- [Link para animações ou protótipos demonstrando o comportamento do Swipe to Refresh no Figma]
- [Especificações de timing e easing para as animações]
