---
title: "espacamento"

---

## Espaçamento (Space)

## Onde é usado

O espaçamento (ou espaço em branco) é um elemento de design fundamental que define as relações entre os elementos na interface. É usado para:
- Criar agrupamentos lógicos de conteúdo e funcionalidades.
- Melhorar a legibilidade e a escaneabilidade, reduzindo a desordem visual.
- Estabelecer hierarquia e guiar o olhar do usuário.
- Criar um ritmo visual e uma sensação de equilíbrio e profissionalismo.
- Definir áreas de toque adequadas para elementos interativos.

Estabelece as diretrizes para margens (espaço externo), preenchimentos (paddings - espaço interno) e o espaço em branco geral no layout, utilizando uma escala consistente para garantir harmonia visual, legibilidade e agrupamento lógico de elementos.

## Detalhes Adicionais / Tópicos

### Escala de Espaçamento Consistente

- Definir uma escala de espaçamento modular (ex: baseada em múltiplos de 4px ou 8px) para todos os valores de margem e padding.
- Isso garante consistência, previsibilidade e facilita a tomada de decisões de design e desenvolvimento.
- *Exemplo de Tokens/Variáveis:* `espaco-xs: 4px`, `espaco-s: 8px`, `espaco-m: 16px`, `espaco-l: 24px`, `espaco-xl: 32px`, `espaco-xxl: 48px`.

### Margens (Margins)

- Espaço fora das bordas de um elemento. Usado para separar um elemento de outros.

### Preenchimentos (Paddings)

- Espaço dentro das bordas de um elemento, entre a borda e o conteúdo.

### Espaço em Branco (Whitespace / Negative Space)

- O espaço vazio ao redor e entre os elementos. Não precisa ser literalmente branco.
- Crucial para não sobrecarregar o usuário com informação e para destacar o conteúdo importante.

### Unidades/Medidas

- **Pixels (px):** Unidade absoluta, boa para consistência fina (ex: bordas, [[Glossário/Linguagem Visual/iconografia|ícones]] pequenos).
- **Rems/Ems:** Unidades relativas ao tamanho da fonte do elemento raiz (rem) ou do elemento pai (em). Boas para escalabilidade e acessibilidade, pois se ajustam às preferências de tamanho de fonte do usuário.
- Recomenda-se o uso de `rem` para espaçamentos que devem escalar com o texto e `px` para detalhes finos que não devem.

### [[Glossário/Linguagem Visual/metricas_e_keylines|Métricas]] e Linhas-Chave ([[Glossário/Linguagem Visual/metricas_e_keylines|Keylines]])

- Linhas guia imaginárias que ajudam a alinhar elementos de forma consistente em toda a interface, especialmente em layouts complexos e grids.

### Estrutura e Layout

- Como o espaçamento contribui para a estrutura de componentes individuais (ex: [[Glossário/Componentes/cards|cards]], [[Glossário/Elementos/botoes|botões]]) e para o layout geral da página (ex: espaçamento entre seções, colunas de um grid).

### [[Glossário/Linguagem Visual/fotografia|Fotografia]] e Mídia

- Considerar o espaço ao redor de [[Glossário/Elementos/imagem|imagens]], vídeos e outros elementos de mídia para que "respirem" e não pareçam apertados no layout.

## Escala de Espaçamento (Exemplo Prático com Nomes Semânticos)

- **`espaco-squish-xs` (Espaçamento Interno Mínimo):**
  - Valor: [Ex: 4px]
  - Uso: Padding interno muito pequeno para componentes compactos, como tags ou [[Glossário/Componentes/badges|badges]] pequenas.
  - Status: A definir

- **`espaco-inset-s` (Espaçamento Interno Pequeno):**
  - Valor: [Ex: 8px]
  - Uso: Padding interno para [[Glossário/Elementos/botoes|botões]] pequenos, itens de [[Glossário/Elementos/listas|lista]], inputs.
  - Status: A definir

- **`espaco-stack-m` (Empilhamento Médio):**
  - Valor: [Ex: 16px]
  - Uso: Margem vertical entre [[Glossário/Elementos/paragrafo|parágrafos]], itens de uma [[Glossário/Elementos/listas|lista]] vertical, ou entre um rótulo e seu campo.
  - Status: A definir

- **`espaco-inline-m` (Espaçamento em Linha Médio):**
  - Valor: [Ex: 16px]
  - Uso: Margem horizontal entre elementos lado a lado, como [[Glossário/Elementos/botoes|botões]] em um grupo.
  - Status: A definir

- **`espaco-section-l` (Espaçamento de Seção Grande):**
  - Valor: [Ex: 32px ou 48px]
  - Uso: Margem vertical entre grandes seções de uma página, ou padding de [[Glossário/Sistemas de Layout/containers_wrappers|containers]] principais.
  - Status: A definir

*(Nota: Os nomes e valores são exemplos e devem ser adaptados à necessidade do projeto. O uso de nomes semânticos para os tokens de espaçamento pode melhorar a comunicação e a intenção do design.)*

## Status Geral

**Status:** A definir (Fundamental para a consistência visual de todos os componentes e layouts)

## [[Glossário/Elementos/links|Link]] para o Figma (Visão Geral de Espaçamento)

[[[Glossário/Elementos/links|Link]] para as diretrizes de Espaçamento e a escala de tokens no Figma]
