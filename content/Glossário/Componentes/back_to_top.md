---
title: "back to top"
description: "O botão \"Voltar ao Topo\" é um controle de navegação que permite ao usuário retornar rapidamente ao início de uma página longa após rolar para baixo."
tags:
  - tema/ui
  - tipo/glossario
---

## Botão "Voltar ao Topo" (Back to Top)

## Onde é usado

O [[Glossário/Elementos/botoes|botão]] "Voltar ao Topo" é um controle de navegação que permite ao usuário retornar rapidamente ao início de uma página longa após rolar para baixo. Ele aparece contextualmente quando o usuário rola uma certa distância da página.

## Detalhes Adicionais / Tópicos

![Botão voltar ao topo: ausente na primeira tela e visível depois de uma tela de rolagem, fixo no canto inferior direito](attachments/glossario-back-to-top.svg)

- **Visibilidade Condicional:** Só aparece após o usuário rolar uma determinada quantidade da página (ex: uma altura de tela).
- **Posicionamento:** Geralmente fixo no canto inferior direito da tela, flutuando sobre o conteúdo.
- **[[Glossário/Linguagem Visual/iconografia|Ícone]]:** Comumente usa um ícone de seta para cima (`↑`).
- **Animação de Rolagem:** A rolagem para o topo deve ser suave para fornecer contexto ao usuário, em vez de um salto instantâneo.
- **Acessibilidade:** Deve ser focável e operável via teclado. O ícone deve ter um texto alternativo adequado (ex: `aria-label="Voltar ao topo da página"`).

## Variações

- **Botão "Voltar ao Topo" Padrão:**
  - Descrição: Botão flutuante que aparece no canto inferior direito após rolagem.
  - Estilo: [Formato (circular, quadrado com cantos arredondados), cor, sombra, ícone]
  - Comportamento da Aparição/Desaparição: [Fade-in/fade-out, slide-in/slide-out]
  - Distância de Rolagem para Ativação: [Ex: 500px ou 100vh]
  - Status: A definir
  - Link para o Figma: [Link para Botão Voltar ao Topo no Figma]

## Melhores Práticas

- Use apenas em páginas suficientemente longas onde a rolagem para o topo se torna uma tarefa.
- Não o torne muito intrusivo ou grande a ponto de obstruir o conteúdo importante.
- Garanta que a animação de rolagem seja suave e não desorientadora.

## Status Geral

**Status:** A definir

## Link para o Figma (Visão Geral)

[Link para o componente Botão Voltar ao Topo no Figma]
