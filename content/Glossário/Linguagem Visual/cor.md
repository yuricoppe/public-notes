---
title: "Cor (Color)"
description: "A cor é um dos pilares da identidade visual e da experiência do usuário."
tags:
  - tema/ui
  - tema/design-system
  - tipo/glossario
---

## Cor (Color)

## Onde é usado

A cor é um dos pilares da identidade visual e da experiência do usuário. Ela é utilizada para:
- Estabelecer a identidade da marca.
- Criar hierarquia visual e direcionar a atenção do usuário.
- Fornecer feedback sobre interações (sucesso, erro, aviso).
- Melhorar a usabilidade e a acessibilidade.
- Evocar emoções e transmitir a personalidade do produto/sistema.

Define a paleta de cores primárias, secundárias, de feedback (sucesso, erro, aviso, informação), neutras e suas aplicações em todo o sistema para garantir consistência visual e acessibilidade.

## Detalhes Adicionais / Tópicos

### Paletas de Cores

![Estrutura de uma paleta: escalas de tom da cor primária e das neutras, de 100 a 900, e as quatro cores semânticas — sucesso, erro, aviso e informação — com o uso de cada uma](attachments/glossario-paleta-cores.svg)

- **Primária:** A cor principal da marca, usada em elementos de destaque e ações chave.
  - *Exemplo de Nomeação:* `cor-primaria-500` (tom principal), `cor-primaria-100` (tom mais claro), `cor-primaria-700` (tom mais escuro).
- **Secundária:** Cores de apoio que complementam a primária, usadas para variações, estados ou elementos menos proeminentes.
- **Neutras:** Tons de cinza, branco e preto usados para textos, fundos, bordas e superfícies da interface. Essenciais para legibilidade e estrutura.
  - *Exemplo de Nomeação:* `cor-neutra-900` (quase preto), `cor-neutra-500` (cinza médio), `cor-neutra-100` (cinza muito claro).
- **Feedback/Semânticas:** Cores com significado intrínseco para comunicar estados:
    - **Sucesso:** Verde (Ex: `cor-sucesso-500`) - para confirmações, validações positivas.
    - **Erro/Perigo:** Vermelho (Ex: `cor-erro-500`) - para alertas críticos, validações negativas.
    - **Aviso:** Amarelo/Laranja (Ex: `cor-aviso-500`) - para alertas não críticos, informações importantes.
    - **Informação:** Azul (Ex: `cor-info-500`) - para dicas, informações contextuais.

### Contraste e Acessibilidade

![Os três limites de contraste da WCAG — 3:1, 4,5:1 e 7:1 — e quatro amostras de texto sobre branco com a razão de cada uma e o resultado nos níveis AA e AAA](attachments/glossario-contraste-wcag.svg)

- Todas as combinações de cor de texto sobre fundo devem atender aos critérios de contraste WCAG AA (mínimo 4.5:1 para texto normal, 3:1 para texto grande) e, idealmente, AAA.
- Ferramentas de verificação de contraste devem ser usadas durante o design e desenvolvimento.
- Evitar depender exclusivamente da cor para transmitir informação; usar também [[Glossário/Linguagem Visual/iconografia|ícones]], texto ou outros indicadores visuais.

### Significado das Cores

- Considerar o impacto cultural e psicológico das cores.
- Documentar o uso intencional de cada cor para manter a consistência.

### Amostras (Swatches)

- Cada cor da paleta deve ser documentada com:
    - Nome da cor (ex: "Azul Primário Principal")
    - Variável CSS/SCSS (ex: `var(--cor-primaria-500)`, `$cor-primaria-500`)
    - Valor HEX (ex: `#3498DB`)
    - Valor RGB (ex: `rgb(52, 152, 219)`)
    - Valor HSL (ex: `hsl(207, 76%, 53%)`) - Opcional

## Variações de Aplicação

- **Cor Primária:**
  - Descrição: Usada para ações principais, [[Glossário/Elementos/botoes|botões]] de destaque e elementos que requerem maior atenção (ex: CTAs principais, [[Glossário/Elementos/links|links]] ativos).
  - Status: A definir
  - Link para o Figma: [Link para Cor Primária no Figma]
- **Cor Secundária:**
  - Descrição: Usada para elementos de menor hierarquia, botões secundários, ênfase moderada e para adicionar variedade visual sem competir com a cor primária.
  - Status: A definir
  - Link para o Figma: [Link para Cor Secundária no Figma]
- **Cores de Feedback (Ex: Erro):**
  - Descrição: Usada para indicar erros em [[Glossário/Padrões/form_structure|formulários]], [[Glossário/Componentes/messaging|mensagens]] de alerta críticas, status negativos. Deve ser acompanhada de texto ou ícone explicativo.
  - Status: A definir
  - Link para o Figma: [Link para Cores de Feedback no Figma]
- **Cores Neutras:**
  - Descrição: Usadas para textos de corpo, fundos de página, bordas de [[Glossário/Sistemas de Layout/containers_wrappers|containers]], divisores e elementos de interface que não necessitam de destaque cromático, garantindo legibilidade e uma base visual limpa.
  - Status: A definir
  - Link para o Figma: [Link para Cores Neutras no Figma]

## Status Geral

**Status:** A definir (Recomenda-se definir as [[Glossário/Linguagem Visual/paletas_por_categoria|paletas]] e testar a acessibilidade antes de avançar para outros componentes)

## Link para o Figma (Visão Geral de Cores)

[Link para a seção de Cores no Figma]
