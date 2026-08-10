---
title: "Fotografia"
description: "Esta seção orienta sobre o uso de fotografia em nosso produto, definindo o estilo, o propósito e as melhores práticas para garantir que as imagens contribuam positivamente para…"
tags:
  - tema/ui
  - tema/design-system
  - tipo/glossario
---

## Fotografia

Esta seção orienta sobre o uso de fotografia em nosso produto, definindo o estilo, o propósito e as melhores práticas para garantir que as [[Glossário/Elementos/imagem|imagens]] contribuam positivamente para a experiência do usuário e reforcem a identidade da marca.

## Introdução

A fotografia, quando utilizada de forma estratégica, pode:
-   Transmitir emoções e contar histórias de forma eficaz.
-   Aumentar o apelo visual e o engajamento do usuário.
-   Humanizar a marca e criar conexões com o público.
-   Ilustrar conceitos complexos ou abstratos de maneira clara.
-   Destacar produtos ou funcionalidades importantes.

## Estilo Fotográfico

Nosso estilo fotográfico deve ser:

1.  **Autêntico e Realista:**
    *   Preferir imagens que retratem pessoas, cenários e situações reais, evitando fotos excessivamente encenadas ou genéricas de banco de imagens.
    *   Mostrar diversidade e inclusão de forma natural.

2.  **Luminoso e Claro:**
    *   Optar por fotografias com boa iluminação, preferencialmente luz natural. Evitar imagens escuras, subexpostas ou com sombras muito duras, a menos que seja intencional para um contexto específico (ex: modo escuro).

3.  **Foco e Nitidez:**
    *   As imagens devem ser nítidas e com o sujeito principal em foco claro. Desfoques artísticos (bokeh) podem ser usados com moderação para destacar o objeto principal.

4.  **Composição Cuidada:**
    *   Aplicar princípios básicos de composição (regra dos terços, linhas guia, espaço negativo) para criar imagens visualmente equilibradas e agradáveis.

5.  **[[Glossário/Linguagem Visual/cor|Cores]] Consistentes com a Marca:**
    *   As cores predominantes nas fotografias devem, sempre que possível, harmonizar com a paleta de cores da marca ou serem neutras para não conflitarem.
    *   O tratamento de cor deve ser consistente em todas as imagens.

6.  **Contextual e Relevante:**
    *   As imagens devem ser diretamente relevantes ao conteúdo ou à mensagem que acompanham. Evitar o uso de fotos apenas para preencher espaço.

## Tipos de Imagens e Casos de Uso

-   **Fotografias de Pessoas:**
    *   **Uso:** Depoimentos, perfis de equipe, ilustrar interações humanas com o produto/serviço.
    *   **Diretrizes:** Pessoas devem parecer genuínas e expressar emoções apropriadas ao contexto. Evitar poses forçadas.

-   **Fotografias de Ambientes/Cenários:**
    *   **Uso:** Ilustrar locais de trabalho, contextos de uso do produto, ou para criar uma atmosfera específica.
    *   **Diretrizes:** Devem ser convidativos e bem iluminados.

-   **Fotografias de Objetos/Produtos:**
    *   **Uso:** Mostrar detalhes de produtos, funcionalidades em destaque.
    *   **Diretrizes:** Foco no produto, fundo limpo ou contextual que não distraia.

-   **Fotografias Conceituais/Abstratas:**
    *   **Uso:** Representar ideias, conceitos ou serviços que são difíceis de visualizar literalmente.
    *   **Diretrizes:** Usar com moderação. Devem ser de alta qualidade e alinhadas com a estética da marca. O significado deve ser relativamente claro ou complementado por texto.

## Otimização de Imagens para Web

-   **Formato:**
    *   **JPEG:** Para fotografias com muitas cores e gradientes. Priorizar JPEGs progressivos.
    *   **WebP:** Considerar o uso de WebP para melhor compressão e qualidade, com fallback para JPEG/PNG onde não suportado.
    *   **PNG:** Usar apenas se a transparência for necessária e não for uma fotografia ([[Glossário/Linguagem Visual/iconografia|ícones]], ilustrações).
-   **Compressão:**
    *   Comprimir as imagens para reduzir o tamanho do arquivo sem perda significativa de qualidade visual. O objetivo é balancear qualidade e performance de carregamento.
-   **Dimensionamento:**
    *   Redimensionar as imagens para as dimensões em que serão exibidas. Evitar carregar imagens muito grandes e redimensioná-las via CSS.
    *   Utilizar `srcset` e o elemento `<picture>` para fornecer imagens responsivas em diferentes tamanhos e resoluções de tela.
-   **Texto Alternativo (Alt Text):**
    *   Todas as imagens funcionais ou informativas DEVEM ter um texto alternativo descritivo e conciso para acessibilidade (leitores de tela) e SEO.
    *   Imagens puramente decorativas devem ter um `alt` vazio (`alt=""`).

## Considerações Éticas e Legais

-   **Direitos Autorais:** Utilizar apenas imagens para as quais temos os direitos de uso (produção própria, bancos de imagem com licença apropriada, Creative Commons com atribuição correta, etc.).
-   **Consentimento:** Obter consentimento das pessoas retratadas, especialmente se forem identificáveis.
-   **Representação:** Ser consciente da representação e evitar estereótipos.

## Ferramentas e Recursos

-   Bancos de imagens aprovados.
-   Guias de estilo para fotógrafos (se aplicável).
-   Ferramentas de otimização de imagem.

## O Que Evitar

-   Fotos de banco de imagens genéricas e impessoais.
-   Imagens de baixa resolução ou pixeladas.
-   Uso excessivo de [[Glossário/Componentes/filters|filtros]] ou edições que distorçam a realidade.
-   Imagens que não agregam valor ou distraem do conteúdo principal.
-   Ignorar as diretrizes de otimização e acessibilidade.
