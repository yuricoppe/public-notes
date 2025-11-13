---
title: "Elementos de UI (UI Elements)"

---

## Elementos de UI (UI Elements)

Este diretório define os elementos fundamentais e atômicos que formam a base visual e estilística de toda a interface do usuário (UI) do portal. Elementos de UI são os "átomos" do nosso [[Glossário/Entregáveis/design_system|Design System]], a partir dos quais componentes mais complexos são construídos.

## O que são Elementos de UI?

Elementos de UI são as especificações básicas de estilo e identidade visual. Eles incluem:

- **[[Glossário/Linguagem Visual/cor|Cores]]:** A paleta de [[Glossário/Linguagem Visual/cor|cores]] primárias, secundárias, de destaque, de feedback (sucesso, erro, aviso), e tons de cinza. Inclui os valores hexadecimais e variáveis CSS/Sass, se aplicável.
- **[[Glossário/Linguagem Visual/tipografia|Tipografia]]:** Definições de famílias tipográficas (fontes) para títulos, corpo de texto, legendas, etc. Inclui tamanhos, pesos (bold, regular), alturas de linha e estilos (itálico).
- **[[Glossário/Linguagem Visual/iconografia|Ícones]]:** A biblioteca de [[Glossário/Linguagem Visual/iconografia|ícones]] utilizada no portal, suas especificações de tamanho, estilo (ex: outline, solid) e como utilizá-los (ex: SVG, font icon).
- **[[Glossário/Linguagem Visual/espacamento|Espaçamento]] (Base):** A unidade base de [[Glossário/Linguagem Visual/espacamento|espaçamento]] e como ela é aplicada para criar consistência (complementar ao `layout_systems/spacing.md` que define a escala).
- **Bordas e Sombras:** Estilos de bordas (espessura, [[Glossário/Linguagem Visual/cor|cor]], raio) e sombras (elevação, profundidade) usados para dar profundidade e definir contornos.
- **Estilos de Interação Básicos:** Definições padrão para estados como hover, focus, active em elementos interativos básicos (antes de serem aplicados a componentes específicos).

## Propósito

A documentação dos elementos de UI visa:

- **Consistência Visual:** Garantir que a aparência do portal seja uniforme e alinhada com a identidade da marca.
- **Fundação Sólida:** Fornecer a base para a criação de Componentes de UI (`ui_components/`) coesos.
- **Referência Rápida:** Servir como um guia rápido para designers e desenvolvedores sobre os estilos básicos a serem aplicados.

## Estrutura da Documentação

Cada elemento (ou grupo de elementos, como a paleta de [[Glossário/Linguagem Visual/cor|cores]]) será detalhado em arquivos `.md` específicos dentro deste diretório, incluindo:

- **Descrição e Propósito.**
- **Especificações Visuais e Técnicas (ex: valores de [[Glossário/Linguagem Visual/cor|cor]], nomes de fontes, tamanhos).**
- **Exemplos de Uso Correto e Incorreto.**
- **Considerações de Acessibilidade (ex: contraste de [[Glossário/Linguagem Visual/cor|cor]] para texto).**

## Relação com Outras Partes do [[Glossário/Entregáveis/design_system|Design System]]

- **Linguagem Visual (`visual_language/`):** Os elementos de UI são a concretização das diretrizes mais amplas da linguagem visual.
- **Componentes de UI (`ui_components/`):** Os elementos de UI são os blocos de construção estilísticos dos componentes de UI.

É essencial que todos os novos designs e implementações adiram estritamente aos elementos definidos aqui para manter a integridade visual do portal.
