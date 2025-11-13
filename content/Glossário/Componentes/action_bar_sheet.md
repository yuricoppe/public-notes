# Barra de Ação / Planilha de Ação (Action Bar / Action Sheet)

## Onde é usado

**Barra de Ação (Action Bar):**
Uma barra persistente, geralmente no topo ([[Componentes/header|header]]) ou no [[Componentes/footer|rodapé]] ([[Componentes/footer|footer]]) de uma tela ou seção, que contém ações contextuais primárias ou navegação.
- Ex: Barra de topo com título da página e [[Elementos/botoes|botão]] de salvar/editar.
- Ex: Barra inferior em aplicativos móveis com ações comuns.

**Planilha de Ação (Action Sheet):**
Um tipo de diálogo [[Componentes/dialog|modal]] que desliza da parte inferior (mais comum em mobile) ou aparece como um popover (desktop), apresentando um conjunto de duas ou mais opções relacionadas a uma tarefa iniciada pelo usuário.
- Ex: Ao compartilhar um item, uma planilha de ação pode mostrar opções como "Copiar [[Elementos/links|link]]", "Enviar por email", "Compartilhar no Twitter".
- Ex: Ao clicar em um item de uma [[Elementos/listas|lista]], pode oferecer "Editar", "Excluir", "Marcar como concluído".

## Detalhes Adicionais / Tópicos

### Barra de Ação (Action Bar)
- **Posicionamento:** Topo, [[Componentes/footer|rodapé]], ou flutuante (contextual).
- **Conteúdo:** Títulos, [[Elementos/botoes|botões]] de ação ([[Linguagem Visual/iconografia|ícone]] ou texto), [[Componentes/menu|menus]], campos de busca.
- **Comportamento:** Pode ser fixa, rolar com a página ou aparecer/desaparecer contextualmente.

### Planilha de Ação (Action Sheet)
- **Ativação:** Disparada por uma ação do usuário (clique em [[Elementos/botoes|botão]], item de [[Elementos/listas|lista]]).
- **Conteúdo:** [[Elementos/listas|Lista]] de [[Elementos/botoes|botões]] de ação, cada um representando uma escolha.
- **Ação Destrutiva:** Ações como "Excluir" devem ser visualmente distintas (ex: [[Linguagem Visual/cor|cor]] vermelha) e, idealmente, posicionadas separadamente ou exigir confirmação adicional.
- **Cancelar:** Geralmente inclui uma opção de "Cancelar" proeminente para fechar a planilha sem fazer uma escolha.
- **Acessibilidade:** Deve ser navegável via teclado, gerenciar o foco corretamente, e ser anunciada por leitores de tela como um diálogo.

## Variações

- **Barra de Ação - [[Elementos/cabecalhos|Cabeçalho]] Padrão:**
  - Descrição: Barra no topo da tela com título e ações primárias/navegação.
  - Elementos Típicos: [Título, [[Elementos/botoes|Botão]] Voltar, [[Elementos/botoes|Botão]] de [[Componentes/menu|Menu]], Ações (Salvar, Editar)]
  - Status: A definir
  - [[Elementos/links|Link]] para o Figma: [[[Elementos/links|Link]] para Action Bar - [[Componentes/header|Header]] no Figma]

- **Barra de Ação - [[Componentes/footer|Rodapé]] Fixo (Mobile):**
  - Descrição: Barra na parte inferior da tela em dispositivos móveis com 2-5 ações principais.
  - Elementos Típicos: [[[Linguagem Visual/iconografia|Ícones]] com ou sem texto para navegação principal]
  - Status: A definir
  - [[Elementos/links|Link]] para o Figma: [[[Elementos/links|Link]] para Action Bar - Mobile [[Componentes/footer|Footer]] no Figma]

- **Planilha de Ação - Padrão Mobile:**
  - Descrição: [[Elementos/listas|Lista]] de opções que desliza da parte inferior da tela.
  - Estrutura: [Título opcional, [[Elementos/listas|lista]] de [[Elementos/botoes|botões]] de ação, [[Elementos/botoes|botão]] de cancelar separado]
  - Status: A definir
  - [[Elementos/links|Link]] para o Figma: [[[Elementos/links|Link]] para Action Sheet Mobile no Figma]

- **Planilha de Ação - Popover Desktop:**
  - Descrição: [[Componentes/menu|Menu]] contextual que aparece próximo ao elemento que o disparou.
  - Estrutura: [[[Elementos/listas|Lista]] de opções]
  - Status: A definir
  - [[Elementos/links|Link]] para o Figma: [[[Elementos/links|Link]] para Action Sheet Desktop Popover no Figma]

## Melhores Práticas

- **Barra de Ação:** Mantenha o número de ações limitado para evitar desordem. Priorize as ações mais importantes.
- **Planilha de Ação:** Use para ações contextuais relacionadas a um item ou tarefa específica. Não use para navegação principal. Mantenha a [[Elementos/listas|lista]] de opções concisa.

## Status Geral

**Status:** A definir

## [[Elementos/links|Link]] para o Figma (Visão Geral)

[[[Elementos/links|Link]] para Action Bars no Figma]
[[[Elementos/links|Link]] para Action Sheets no Figma] 