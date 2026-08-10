---
title: "Breakpoints Responsivos"
description: "Os breakpoints responsivos são os pontos específicos nos quais o layout do nosso portal se adapta para fornecer a melhor experiência de visualização em diferentes tamanhos de…"
tags:
  - tema/ui
  - tipo/glossario
---

## Breakpoints Responsivos

## Descrição Geral

Os breakpoints responsivos são os pontos específicos nos quais o layout do nosso portal se adapta para fornecer a melhor experiência de visualização em diferentes tamanhos de tela e dispositivos. Eles são cruciais para garantir que o conteúdo seja legível e a interface do usuário seja funcional, seja em um monitor desktop grande, um tablet ou um smartphone.

## Princípios Chave

- **Mobile-First (Conceitual):** Embora possamos definir breakpoints de desktop para mobile, a filosofia de design deve considerar a experiência móvel como fundamental, expandindo e adaptando para telas maiores.
- **Consistência:** As transições entre breakpoints devem ser suaves e manter a consistência da experiência do usuário.
- **Baseado em Conteúdo (Quando Possível):** Idealmente, os breakpoints devem ser determinados por onde o conteúdo começa a "quebrar" ou a experiência do usuário é degradada, e não apenas por tamanhos de dispositivo populares.

## Nossos Breakpoints

Definimos os seguintes breakpoints principais, comumente usados e que cobrem uma vasta gama de dispositivos:

| Nome      | Range de Largura da Tela (Viewport Width) | Dispositivos Típicos                                  |
|-----------|-------------------------------------------|-------------------------------------------------------|
| **XS**    | < 576px                                   | Smartphones (portrait e alguns landscape)             |
| **SM**    | ≥ 576px e < 768px                         | Smartphones maiores (landscape), tablets pequenos (portrait) |
| **MD**    | ≥ 768px e < 992px                         | Tablets (landscape), laptops pequenos                   |
| **LG**    | ≥ 992px e < 1200px                        | Laptops e desktops com resolução padrão             |
| **XL**    | ≥ 1200px e < 1400px                       | Desktops com resolução maior, laptops maiores        |
| **XXL**   | ≥ 1400px                                  | Monitores grandes, telas de alta resolução             |

**Nota:** Estes são os pontos onde o layout *pode* mudar. Nem todo componente ou seção precisará de estilos específicos para cada breakpoint.

## Como Implementar

Em CSS, os breakpoints são geralmente implementados usando Media Queries.

**Exemplo (Conceitual):**

```css
/* Estilos base (Mobile First - para XS e acima) */
.meu-componente {
  width: 100%;
  font-size: 16px;
}

/* SM - Small devices (tablets pequenos, smartphones landscape, 576px e acima) */
@media (min-width: 576px) {
  .meu-componente {
    /* Ajustes para SM */
  }
}

/* MD - Medium devices (tablets, 768px e acima) */
@media (min-width: 768px) {
  .meu-componente {
    width: 75%;
    font-size: 18px;
  }
  .coluna-lateral {
    display: block; /* Mostra a coluna lateral que estava escondida no mobile */
  }
}

/* LG - Large devices (desktops, 992px e acima) */
@media (min-width: 992px) {
  .meu-componente {
    width: 50%;
  }
}

/* XL - Extra large devices (large desktops, 1200px e acima) */
@media (min-width: 1200px) {
  .meu-componente {
    /* Ajustes para XL */
  }
}

/* XXL - Extra extra large devices (larger desktops, 1400px e acima) */
@media (min-width: 1400px) {
  .meu-componente {
    /* Ajustes para XXL */
  }
}
```

## Diretrizes de Uso

- **Adaptação do Grid:** O sistema de grid (`grid_system.md`) se adaptará com base nestes breakpoints (ex: número de colunas visíveis, empilhamento).
- **Visibilidade de Elementos:** Alguns elementos podem ser ocultados ou mostrados dependendo do breakpoint (ex: navegação mobile vs. desktop).
- **Tamanho de [[Glossário/Linguagem Visual/tipografia|Tipografia]] e [[Glossário/Linguagem Visual/espacamento|Espaçamento]]:** As escalas de tipografia e espaçamento (`spacing_system.md`) podem ser ajustadas para otimizar a legibilidade em diferentes telas.
- **Layout de Componentes:** Componentes individuais podem ter variações de layout para diferentes breakpoints.
- **Priorize a Experiência:** O objetivo não é apenas fazer o layout "caber", mas garantir que ele seja usável e agradável em cada breakpoint.

## Testes

É crucial testar a aparência e funcionalidade do portal em cada um desses breakpoints (e em larguras intermediárias) usando as ferramentas de desenvolvedor do navegador e, se possível, em dispositivos reais.

## Recursos Adicionais / Figma

- [Link para visualizações dos layouts em cada breakpoint no Figma]
- [Guias de como os componentes específicos se adaptam aos breakpoints]
