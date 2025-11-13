---
title: "iconografia"

---

## Iconografia (Iconography)

## Onde é usado

Ícones são representações gráficas compactas usadas para:
- Comunicar conceitos, ações ou status de forma rápida e intuitiva.
- Melhorar a usabilidade e a experiência do usuário, especialmente em interfaces com muito texto ou em espaços limitados.
- Reforçar a identidade visual do sistema.
- Ajudar na navegação e na identificação de funcionalidades.

Descreve a biblioteca de ícones do sistema, incluindo seu estilo visual, tamanhos, princípios de design e uso adequado para comunicar ações, status ou conceitos de forma rápida e intuitiva.

## Detalhes Adicionais / Tópicos

### Estilo Visual Consistente

- Definir um estilo visual único para todos os ícones (ex: contornado, preenchido, duas [[Glossário/Linguagem Visual/cor|cores]], etc.).
- Manter a mesma espessura de linha, cantos arredondados (se houver) e nível de detalhe.

### Tamanhos Padrão

- Definir uma grade de tamanhos para os ícones (ex: 16x16, 24x24, 32x32 pixels) para garantir nitidez e alinhamento.
- Especificar como os ícones devem escalar e se comportar em diferentes densidades de tela.

### Semântica e Clareza

- Cada ícone deve ter um significado claro e universalmente compreensível dentro do contexto do sistema.
- Evitar ícones abstratos ou ambíguos.
- Testar a compreensão dos ícones com usuários, se possível.

### Acessibilidade

- Para ícones que transmitem informação ou representam ações (não puramente decorativos), fornecer alternativas textuais (ex: `aria-label`, texto dentro de um `<span>` visualmente escondido).
- Garantir contraste suficiente entre o ícone e seu fundo.

### Formatos de Arquivo

- **SVG (Scalable Vector Graphics):** Preferível para ícones, pois são vetoriais, escaláveis sem perda de qualidade e podem ser manipulados via CSS/JS.
- **Fontes de Ícones (Icon Fonts):** Alternativa que agrupa ícones em um arquivo de fonte. Pode ser eficiente, mas SVG oferece mais flexibilidade.
- **PNG/WEBP:** Para ícones rasterizados ou ilustrações mais complexas, se vetores não forem adequados. Fornecer em múltiplas resoluções.

### Categorias de Ícones

- **Navegação:** Usados em [[Glossário/Componentes/menu|menus]], barras de navegação (ex: Home, Perfil, [[Glossário/Padrões/settings|Configurações]]).
- **Ação:** Indicam funcionalidades interativas (ex: Salvar, Editar, Excluir, Adicionar, Pesquisar).
- **Informativo/Status:** Comunicam estados ou fornecem informação (ex: Erro, Sucesso, Aviso, Ajuda, Informação).
- **Decorativo:** Usados primariamente para apelo visual, sem funcionalidade intrínseca.

### Pictogramas

- Representações visuais simplificadas de objetos ou conceitos.
- Devem seguir o estilo geral da iconografia.

### Ilustrações

- Gráficos mais detalhados usados para enriquecer a experiência, em telas de [[Glossário/Padrões/launch|onboarding]], estados vazios, ou para comunicar conceitos complexos de forma visual.
- Definir o estilo das ilustrações para manter a consistência com o restante do [[Glossário/Entregáveis/design_system|Design System]].

### Alinhamento

- Definir diretrizes para o alinhamento de ícones com texto (verticalmente) e com outros elementos da interface.

## Variações (Exemplos por Tipo de Ícone)

- **Ícone de Ação (Ex: Salvar `💾`):**
  - Descrição: Representa uma ação que o usuário pode realizar, como salvar dados.
  - Tamanhos Comuns: [Ex: 24x24px para [[Glossário/Elementos/botoes|botões]], 16x16px para [[Glossário/Elementos/links|links]] de ação]
  - Estilo: [Ex: Contornado, espessura de 2px]
  - Alternativa Textual: "Salvar"
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Ícone de Salvar no Figma]

- **Ícone Informativo (Ex: Ajuda `?`):**
  - Descrição: Fornece acesso a informações de ajuda ou contexto adicional.
  - Tamanhos Comuns: [Ex: 16x16px, 20x20px]
  - Estilo: [Ex: Preenchido]
  - Alternativa Textual: "Ajuda"
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Ícone de Ajuda no Figma]

## Status Geral

**Status:** A definir (É importante ter uma biblioteca base de ícones antes de construir muitos componentes)

## [[Glossário/Elementos/links|Link]] para o Figma (Visão Geral da Iconografia)

[[[Glossário/Elementos/links|Link]] para a biblioteca de Ícones no Figma]
