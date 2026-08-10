---
title: "containers wrappers"
description: "Containeres e wrappers são elementos de layout fundamentais usados para controlar a largura, o alinhamento e, às vezes, o espaçamento do conteúdo principal dentro de uma página…"
tags:
  - tema/ui
  - tipo/glossario
---

## Containeres e Wrappers

## Descrição Geral

Containeres e wrappers são elementos de layout fundamentais usados para controlar a largura, o alinhamento e, às vezes, o [[Glossário/Linguagem Visual/espacamento|espaçamento]] do conteúdo principal dentro de uma página ou seção. Eles ajudam a manter a consistência visual e a legibilidade, especialmente em telas largas.

## Princípios Chave

- **Controle de Largura:** Evitar que o conteúdo se estenda excessivamente em telas grandes, o que pode prejudicar a legibilidade (linhas de texto muito longas).
- **Centralização:** Facilitar a centralização do bloco principal de conteúdo na janela de visualização.
- **Consistência:** Aplicar uma largura máxima consistente para o conteúdo principal em todo o portal.
- **Simplicidade:** Devem ser elementos estruturais simples, focados no layout.

## Tipos Comuns

### 1. Container Principal (Main Page Container)

- **Propósito:** Envolver o conteúdo principal da página, aplicando uma largura máxima e centralizando-o na tela.
- **Especificações:**
    - **Largura Máxima:** Alinhada com a `Largura Máxima do Conteúdo` definida no `grid_system.md` (ex: 1200px).
    - **Centralização:** Usualmente `margin-left: auto; margin-right: auto;`.
    - **Padding Lateral:** Pode incluir o padding lateral da página (margens do grid), ou as margens do grid podem ser aplicadas externamente a este container.
    - **Uso:** Geralmente aplicado uma vez por página, envolvendo todo o conteúdo que deve respeitar a largura máxima.

**Exemplo (Conceitual HTML/CSS):**
```html
<body>
  <header>
    <div class="container">
      <!-- Conteúdo do Cabeçalho -->
    </div>
  </header>
  <main>
    <div class="container">
      <!-- Conteúdo Principal da Página -->
    </div>
  </main>
  <footer>
    <div class="container">
      <!-- Conteúdo do Rodapé -->
    </div>
  </footer>
</body>
```
```css
.container {
  width: 100%; /* Garante que ocupa a largura disponível */
  max-width: 1200px; /* Nossa largura máxima de conteúdo definida no grid */
  margin-left: auto;
  margin-right: auto;
  padding-left: 16px; /* Exemplo de padding, alinhado com margens do grid mobile */
  padding-right: 16px; /* Exemplo de padding, alinhado com margens do grid mobile */
}

/* Em breakpoints maiores, o padding pode aumentar */
@media (min-width: 768px) {
  .container {
    padding-left: 24px;
    padding-right: 24px;
  }
}

@media (min-width: 1200px) {
  .container {
    padding-left: 32px;
    padding-right: 32px;
  }
}
```

### 2. Wrapper de Seção (Section Wrapper)

- **Propósito:** Agrupar conteúdo dentro de uma seção específica, aplicando paddings internos ou um estilo de fundo, sem necessariamente impor a largura máxima total da página (útil para seções com fundo de [[Glossário/Linguagem Visual/cor|cor]] que se estendem por toda a largura da tela, mas com conteúdo centralizado).
- **Especificações:**
    - **Largura:** Geralmente `width: 100%;` para permitir fundos de largura total.
    - **Padding Interno:** Pode aplicar espaçamento vertical (`padding-top`, `padding-bottom`) usando o `spacing_system.md`.
    - **Conteúdo Centralizado:** Frequentemente contém um `.container` dentro dele para centralizar o texto e os elementos principais da seção.

**Exemplo (Conceitual HTML/CSS):**
```html
<section class="section-wrapper feature-section">
  <div class="container">
    <h2>Título da Seção de Destaque</h2>
    <p>Conteúdo desta seção...</p>
  </div>
</section>
```
```css
.section-wrapper {
  width: 100%;
  padding-top: var(--space-xl);
  padding-bottom: var(--space-xl);
}

.feature-section {
  background-color: #f0f0f0; /* Fundo de cor que se estende */
}
```

## Diretrizes de Uso

- **Hierarquia:** O `.container` principal é geralmente o mais externo para o conteúdo da página. Wrappers de seção podem existir dentro dele ou, mais comumente, o `.container` pode estar aninhado dentro de um `section-wrapper` de largura total.
- **Não Abuse:** Use apenas quando necessário para controle de layout e agrupamento.
- **Consistência:** Mantenha a implementação dos containers e wrappers consistente.
- **Relação com o Grid:** O `.container` é fundamental para o funcionamento do [[Glossário/Sistemas de Layout/grid_system|sistema de grid]], pois define os limites dentro dos quais as colunas do grid operam.

## Responsividade

- A `max-width` do `.container` garante que o conteúdo não fique excessivamente largo em desktops.
- Em telas menores, como `width: 100%` é aplicado, o container se ajustará à largura da tela, e os paddings laterais (se aplicados diretamente no container) fornecerão as margens necessárias.

## Recursos Adicionais / Figma

- [Link para exemplos de uso de Containeres e Wrappers no Figma]
- [Como o Grid System interage com os Containeres]
