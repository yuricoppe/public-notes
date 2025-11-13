---
title: "slider"

---

## Controle Deslizante (Slider)

## Onde é usado

Controles deslizantes (sliders) são usados para permitir que o usuário selecione um valor ou um intervalo de valores dentro de um range definido, arrastando uma alça ao longo de uma trilha. São úteis para:
- Ajustar [[Glossário/Padrões/settings|configurações]] como volume, brilho, zoom.
- Selecionar valores numéricos em [[Glossário/Padrões/form_structure|formulários]] (ex: preço, idade, porcentagem) de forma visual.
- Definir um intervalo (range slider).

## Detalhes Adicionais / Tópicos

- **Trilha (Track):** A barra horizontal ou vertical ao longo da qual a alça se move.
- **Alça (Thumb/Handle):** O elemento que o usuário arrasta.
- **Valor Atual:** Exibição opcional do valor selecionado (numérico ou tooltip).
- **Marcadores de Passo (Steps/Ticks):** Opcionais, para indicar incrementos discretos na trilha.
- **Preenchimento da Trilha (Track Fill):** Opcional, para indicar a porção da trilha correspondente ao valor selecionado.
- **Acessibilidade:** Deve ser controlável via teclado (setas direcionais) e ter atributos ARIA adequados (`aria-valuenow`, `aria-valuemin`, `aria-valuemax`).

## Variações

- **Slider de Valor Único:**
  - Descrição: Permite selecionar um único valor no range.
  - Estilo da Trilha: [[[Glossário/Linguagem Visual/cor|Cor]], espessura, cantos arredondados]
  - Estilo da Alça: [Tamanho, [[Glossário/Linguagem Visual/cor|cor]], sombra, estado de hover/foco]
  - Exibição de Valor: [Ex: Tooltip ao arrastar, valor numérico fixo ao lado]
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Slider de Valor Único no Figma]

- **Slider de Intervalo (Range Slider):**
  - Descrição: Possui duas alças para selecionar um valor mínimo e máximo dentro de um range.
  - Estilo das Alças: Podem ser idênticas ou diferenciadas se necessário.
  - Preenchimento do Intervalo: A área entre as duas alças geralmente é destacada.
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Slider de Intervalo no Figma]

- **Slider com Passos Discretos:**
  - Descrição: O valor só pode ser selecionado em incrementos específicos, indicados por marcadores na trilha.
  - Estilo dos Marcadores: [Formato, [[Glossário/Linguagem Visual/cor|cor]]]
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Slider com Passos no Figma]

- **Slider Vertical:**
  - Descrição: Orientado verticalmente, comum para controles de volume.
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Slider Vertical no Figma]

## Melhores Práticas

- Use sliders quando a seleção de um valor aproximado é aceitável ou quando a faixa de valores é contínua.
- Para seleção de valores exatos e discretos, um campo de input numérico ou um [[Glossário/Elementos/form_controls|select]] podem ser mais apropriados, ou usados em conjunto com o slider.
- Forneça feedback claro sobre o valor selecionado.

## Status Geral

**Status:** A definir

## [[Glossário/Elementos/links|Link]] para o Figma (Visão Geral de Sliders)

[[[Glossário/Elementos/links|Link]] para a seção de Sliders no Figma]
