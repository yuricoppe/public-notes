---
title: "imagem"

---

## Imagem (Image)

## Onde é usado

Imagens são elementos visuais cruciais para transmitir informações, ilustrar conceitos, adicionar apelo estético e melhorar o engajamento do usuário. São usadas em:
- Conteúdo de artigos e páginas (ilustrativas, fotografias).
- [[Glossário/Componentes/cards|Cards]] e [[Glossário/Elementos/listas|listas]] para representar itens.
- Galerias e carrosséis.
- Avatares de usuário.
- Banners e heros.

## Detalhes Adicionais / Tópicos

- **Formatos de Arquivo:**
  - `JPEG/JPG`: Para fotografias e imagens com muitas [[Glossário/Linguagem Visual/cor|cores]]/gradações. Oferece boa compressão com perda.
  - `PNG`: Para imagens com transparência, logotipos, [[Glossário/Linguagem Visual/iconografia|ícones]] complexos ou quando a fidelidade de [[Glossário/Linguagem Visual/cor|cor]] é crucial. Compressão sem perda.
  - `WEBP`: Formato moderno que oferece compressão superior com e sem perda, e suporta transparência e animação. Boa alternativa para JPEG e PNG, mas verificar compatibilidade com navegadores alvo.
  - `SVG`: Para logotipos, [[Glossário/Linguagem Visual/iconografia|ícones]] e ilustrações vetoriais. Escalável sem perda de qualidade.
  - `GIF`: Para animações simples (embora WebP ou vídeos curtos sejam alternativas mais modernas e eficientes).
- **Otimização:** Imagens devem ser otimizadas para a web para reduzir o tamanho do arquivo e melhorar o tempo de carregamento (compressão, remoção de metadados desnecessários).
- **Responsividade:** Usar técnicas como `<img>` com `srcset` e `sizes`, ou o elemento `<picture>`, para servir imagens de tamanhos apropriados para diferentes dispositivos e resoluções de tela.
- **Lazy Loading:** Carregar imagens apenas quando elas estão prestes a entrar na viewport do usuário, para melhorar o desempenho inicial da página.
- **Acessibilidade:** Fornecer texto alternativo (`alt` attribute) descritivo para todas as imagens que transmitem conteúdo. Para imagens puramente decorativas, usar `alt=""`.
- **Proporção (Aspect Ratio):** Manter a proporção original da imagem para evitar distorções, ou definir proporções específicas para layouts consistentes (ex: 16:9, 4:3, 1:1).
- **Legendas (Captions):** Texto opcional abaixo da imagem para fornecer contexto ou atribuição (ver componente `Caption` se existir).

## Variações

- **Imagem Padrão (Inline/Block):**
  - Descrição: Imagem padrão usada no fluxo do conteúdo.
  - Estilo: [Pode ter bordas, sombras, cantos arredondados conforme o estilo do sistema]
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para estilo de Imagem Padrão no Figma]

- **Imagem de Largura Total (Full Bleed):**
  - Descrição: Imagem que se estende por toda a largura do container ou da tela, comum em heros ou seções de destaque.
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Imagem Full Bleed no Figma]

- **Imagem com Posições (Inline with Positions - Float):**
  - Descrição: Imagem alinhada à esquerda ou direita do texto, com o texto fluindo ao redor. Usar com cautela devido a possíveis problemas de layout responsivo.
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Imagem com Float no Figma]

- **Avatar:**
  - Descrição: Imagem pequena, geralmente circular ou quadrada com cantos arredondados, usada para representar usuários ou perfis.
  - Tamanhos: [Definir tamanhos padrão para avatares, ex: 32px, 48px, 64px]
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para componente Avatar no Figma]

## Melhores Práticas

- Sempre otimizar imagens antes de usá-las na web.
- Escolher o formato de arquivo correto para o tipo de imagem.
- Fornecer texto alternativo significativo.
- Considerar o contexto e o impacto da imagem na experiência do usuário.

## Status Geral

**Status:** A definir

## [[Glossário/Elementos/links|Link]] para o Figma (Visão Geral de Imagens)

[[[Glossário/Elementos/links|Link]] para a seção de Imagens e diretrizes de mídia no Figma]
