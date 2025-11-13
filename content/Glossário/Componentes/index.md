# Componentes de UI (UI Components)

Este diretório é dedicado à documentação dos Componentes de UI (Interface do Usuário) reutilizáveis do portal. Componentes de UI são blocos de construção interativos e funcionais, geralmente mais complexos que os Elementos de UI básicos. Eles são montados a partir de elementos de UI e são usados para construir as seções e funcionalidades dentro dos Templates de Página.

## O que são Componentes de UI?

Componentes de UI são partes encapsuladas da interface com aparência e comportamento definidos. Exemplos comuns incluem:

- [[Elementos/botoes|Botões]] com estados específicos (ex: Primário, Secundário, com [[Linguagem Visual/iconografia|Ícone]])
- [[Componentes/cards|Cards]] (para exibir resumos de conteúdo, produtos, etc.)
- [[Componentes/dialog|Modais]] e Pop-ups
- Acordeões (Accordions) e Abas (Tabs)
- Barras de Navegação e [[Componentes/menu|Menus]] Suspensos (Dropdowns)
- [[Padrões/form_structure|Formulários]] completos e seus campos (Inputs, Selects, Textareas com validação e feedback)
- Carrosséis e [[Elementos/slider|Sliders]]
- Players de Vídeo/Áudio
- Componentes de Data (Date Pickers)
- Barras de Progresso e Indicadores de Carregamento

## Propósito

A documentação dos componentes de UI visa:

- **Reutilização:** Permitir que os mesmos componentes sejam usados em diferentes partes do portal, garantindo consistência e economizando esforço de design/desenvolvimento.
- **Consistência:** Assegurar que componentes com a mesma finalidade tenham a mesma aparência e comportamento.
- **Clareza:** Fornecer especificações claras sobre como cada componente deve ser usado, suas variações, estados e opções de configuração.
- **Acessibilidade:** Documentar as considerações de acessibilidade específicas para cada componente.

## Estrutura da Documentação de um Componente

Cada componente de UI documentado neste diretório (geralmente em seu próprio arquivo `.md`) deve incluir:

- **Descrição:** O que é o componente e qual seu propósito.
- **Visualização:** Exemplo visual (screenshot, [[Elementos/links|link]] para Figma).
- **Variações e Estados:** Diferentes aparências (ex: primário, secundário) e estados (ex: normal, hover, active, disabled, erro).
- **Especificações de Uso:** Quando e como usar o componente.
- **Opções/Propriedades Configuráveis:** Parâmetros que podem ser ajustados (ex: texto, [[Linguagem Visual/iconografia|ícone]], [[Linguagem Visual/cor|cor]]).
- **Boas Práticas (Faça e Não Faça).**
- **Diretrizes de Acessibilidade (ARIA, navegação por teclado, etc.).**
- **Trechos de [[Elementos/codigo|Código]] (Opcional):** Exemplos de implementação em HTML/CSS/JS, se aplicável.

## Relação com Outras Partes do [[Entregáveis/design_system|Design System]]

- **Elementos de UI (`ui_elements/`):** Componentes de UI são construídos utilizando os elementos de UI básicos ([[Linguagem Visual/cor|cores]], [[Linguagem Visual/tipografia|tipografia]], [[Linguagem Visual/iconografia|ícones]]).
- **Templates de Página (`page_templates/`):** Componentes de UI são os blocos de construção que preenchem as estruturas definidas nos templates de página.

Consulte os arquivos individuais neste diretório para as especificações de cada componente. 