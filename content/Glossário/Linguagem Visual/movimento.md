---
title: "Movimento (Motion)"
description: "O movimento, quando bem aplicado, torna a interface mais intuitiva, responsiva e agradável."
tags:
  - tema/ui
  - tema/design-system
  - tipo/glossario
---

## Movimento (Motion)

## Onde é usado

O movimento, quando bem aplicado, torna a interface mais intuitiva, responsiva e agradável. Ele é usado para:
- Fornecer feedback sobre interações do usuário (ex: um [[Glossário/Elementos/botoes|botão]] que reage ao clique).
- Guiar o foco do usuário entre visualizações ou estados diferentes.
- Indicar relações espaciais ou hierárquicas entre elementos.
- Melhorar a percepção de performance, mascarando pequenos atrasos de carregamento.
- Adicionar personalidade e encantar o usuário, sem ser distrativo.

Define os princípios de animação e transições na interface, como timing, easing (curvas de aceleração) e os tipos de transições, para criar uma experiência de usuário fluida, responsiva e engajadora.

## Detalhes Adicionais / Tópicos

### Princípios de Movimento

- **Funcional:** O movimento deve ter um propósito claro, ajudando o usuário a entender o que está acontecendo.
- **Responsivo:** As animações devem iniciar rapidamente em resposta à interação do usuário.
- **Consistente:** Usar padrões de movimento semelhantes para ações ou transições equivalentes.
- **Sutil e Discreto:** Evitar animações longas, complexas ou que distraiam o usuário da tarefa principal.
- **Performático:** As animações devem ser fluidas (idealmente 60fps) e não devem degradar a performance da aplicação.

### Timing

- Definir durações padrão para diferentes tipos de animação (ex: curta para feedback rápido, média para transições de painel).
- *Exemplo de Escala:* Rápido (100-200ms), Médio (200-400ms), Lento (400-600ms).

### Easing (Curvas de Aceleração)

- Controla como a velocidade de uma animação muda ao longo do tempo.
- `ease-in`: Começa devagar, acelera no final (bom para elementos entrando na tela).
- `ease-out`: Começa rápido, desacelera no final (bom para elementos saindo da tela ou feedback rápido).
- `ease-in-out`: Começa devagar, acelera no meio, desacelera no final (para transições suaves entre estados).
- `linear`: Velocidade constante (raramente usado para UI, pode parecer mecânico).

### Tipos de Transições e Animações

- **Fade (Esmaecer):** Alterar a opacidade para mostrar/esconder elementos.
- **Slide (Deslizar):** Mover elementos para dentro/fora da tela ou para novas posições.
- **Scale (Escalar):** Aumentar/diminuir o tamanho de elementos (ex: para [[Glossário/Componentes/dialog|modais]], pop-ups).
- **Expand/Collapse (Expandir/Recolher):** Para acordeões, [[Glossário/Componentes/menu|menus]], etc.
- **Mudança de [[Glossário/Linguagem Visual/cor|Cor]]/Estilo:** Transições suaves entre estados visuais (ex: hover em botões).

### Performance

- Priorizar animações de propriedades CSS que são mais performáticas (ex: `transform`, `opacity`).
- Evitar animar propriedades que causam reflow/repaint excessivo (ex: `width`, `height`, `top`, `left` em elementos complexos).
- Testar o desempenho das animações em dispositivos menos potentes.

## Exemplos de Aplicação

- **Transição de Hover em Botões:**
  - Descrição: Feedback visual sutil ao passar o mouse sobre um botão, indicando interatividade.
  - Duração: [Ex: 150ms]
  - Easing: [Ex: ease-out]
  - Propriedades Animadas: [Ex: `background-color`, `box-shadow`, `transform: scale(1.05)`]
  - Status: A definir
  - Link para o Figma/Exemplo: [Link para exemplo de animação no Figma ou protótipo]

- **Abertura de Modal:**
  - Descrição: Animação ao exibir um modal, geralmente combinando fade e scale para uma entrada suave.
  - Duração: [Ex: 300ms]
  - Easing: [Ex: ease-in-out]
  - Tipo: [Ex: Scale-in com Fade-in do overlay]
  - Status: A definir
  - Link para o Figma/Exemplo: [Link para exemplo de animação no Figma ou protótipo]

- **Carregamento ([[Glossário/Componentes/loading_spinner|Loading Spinner]]/Indicator):**
  - Descrição: Animação contínua para indicar que o sistema está processando algo.
  - Tipo: [Ex: Rotação, Pulsar]
  - Easing: [Ex: linear para rotação contínua]
  - Status: A definir
  - Link para o Figma/Exemplo: [Link para animação de carregamento]

## Status Geral

**Status:** A definir (Definir após os componentes básicos, pois muitas animações são aplicadas a eles)

## Link para o Figma (Visão Geral de Movimento)

[Link para as diretrizes de Movimento no Figma ou documentação de animação]
