---
title: "hero billboard"
description: "O componente Hero (Herói) ou Billboard (Painel) é uma área de destaque proeminente, geralmente posicionada no topo de uma página inicial ou página de destino (landing page)."
tags:
  - tema/ui
  - tipo/glossario
---

## Hero / Billboard (Componente de Destaque Principal)

O componente Hero (Herói) ou Billboard (Painel) é uma área de destaque proeminente, geralmente posicionada no topo de uma página inicial ou página de destino (landing page). Seu objetivo é capturar a atenção do usuário imediatamente, comunicar a proposta de valor principal e incentivar uma ação específica.

## Casos de Uso

-   Página inicial de um website.
-   Páginas de destino (landing pages) de campanhas de marketing.
-   Introdução de seções importantes ou lançamentos de produtos.

## Elementos Comuns

![Hero anotado: título dominante, subtítulo de apoio, um CTA principal e o overlay que garante contraste do texto sobre a foto](attachments/glossario-anatomia-hero.svg)

-   **Título Principal (Headline):** Mensagem central, concisa e impactante.
-   **Subtítulo ou Descrição:** Texto de apoio que elabora o título e fornece mais contexto ou benefícios.
-   **[[Glossário/Elementos/imagem|Imagem]] de Fundo ou Vídeo de Fundo:** Visualmente atraente e relevante para a mensagem.
    *   Pode ser uma [[Glossário/Linguagem Visual/fotografia|fotografia]], ilustração, gradiente ou vídeo.
-   **Call to Action (CTA) Principal:** Um ou mais [[Glossário/Elementos/botoes|botões]] claros que incentivam o usuário a realizar a próxima ação desejada (ex: "Saiba Mais", "Comece Agora", "Ver Produtos").
-   **(Opcional) Imagem ou Ilustração em Primeiro Plano:** Sobreposta ou ao lado do texto, complementando a mensagem.
-   **(Opcional) Logo ou Nome da Marca.**
-   **(Opcional) Indicadores de Scroll ou Setas:** Para sugerir que há mais conteúdo abaixo.

## Melhores Práticas

-   **Primeira Impressão Forte:** Deve ser visualmente atraente e comunicar a mensagem principal de forma rápida e clara.
-   **Proposta de Valor Clara:** O usuário deve entender o que o site/produto oferece em poucos segundos.
-   **CTA Proeminente:** O botão de Call to Action deve ser fácil de identificar e ter um texto que incentive o clique.
-   **Hierarquia Visual:** O título deve ser o elemento mais dominante, seguido pelo subtítulo e pelo CTA.
-   **Qualidade Visual:** Imagens e vídeos devem ser de alta qualidade e otimizados para a web.
-   **Legibilidade do Texto:** Garantir que o texto sobreposto a imagens ou vídeos tenha contraste suficiente para ser facilmente legível.
    *   Usar overlays, sombras de texto ou escolher imagens com áreas mais neutras para o texto.
-   **Responsividade:** O layout do Hero deve se adaptar perfeitamente a todos os tamanhos de tela, desde desktops grandes até dispositivos móveis. Isso pode envolver:
    *   Redimensionamento de fontes e imagens.
    *   Recorte de imagens de fundo de forma inteligente (`background-position`, `object-fit`).
    *   Empilhamento de elementos.
    *   Servir imagens de tamanhos diferentes para diferentes viewports.
-   **Performance:** Imagens e vídeos grandes podem impactar o tempo de carregamento da página (LCP - Largest Contentful Paint). Otimizar esses assets é crucial.
-   **Acessibilidade (a11y):**
    *   O título principal deve ser, idealmente, o `<h1>` da página.
    *   Todo o texto deve ter contraste adequado com o fundo.
    *   Imagens de fundo devem ter alternativas ou serem consideradas decorativas se o texto transmitir toda a informação essencial.
    *   CTAs (botões) devem ser acessíveis por teclado e ter rótulos claros.

## Variações

-   **Hero com Imagem de Tela Cheia.**
-   **Hero com Vídeo de Fundo.**
-   **Hero com Gradiente de Fundo.**
-   **Hero com Ilustrações.**
-   **Hero com [[Glossário/Padrões/form_structure|Formulário]] de Captura (ex: campo de e-mail para newsletter).**
-   **Carrossel de Heros (usar com moderação, pois carrosséis podem ter problemas de usabilidade e eficácia).**

## O Que Evitar

-   [[Glossário/Componentes/messaging|Mensagens]] confusas ou genéricas.
-   CTAs fracos ou escondidos.
-   Imagens de baixa qualidade ou irrelevantes.
-   Texto ilegível devido a baixo contraste com o fundo.
-   Performance ruim devido a assets não otimizados.
-   Ignorar a adaptação para dispositivos móveis.
-   Carrosséis automáticos que o usuário não controla.
