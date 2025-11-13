---
title: "action bar sheet"

---

## Barra de Ação / Planilha de Ação (Action Bar / Action Sheet)

## Onde é usado

**Barra de Ação (Action Bar):**
Uma barra persistente, geralmente no topo ([[Glossário/Componentes/header|header]]) ou no [[Glossário/Componentes/footer|rodapé]] ([[Glossário/Componentes/footer|footer]]) de uma tela ou seção, que contém ações contextuais primárias ou navegação.
- Ex: Barra de topo com título da página e [[Glossário/Elementos/botoes|botão]] de salvar/editar.
- Ex: Barra inferior em aplicativos móveis com ações comuns.

**Planilha de Ação (Action Sheet):**
Um tipo de diálogo [[Glossário/Componentes/dialog|modal]] que desliza da parte inferior (mais comum em mobile) ou aparece como um popover (desktop), apresentando um conjunto de duas ou mais opções relacionadas a uma tarefa iniciada pelo usuário.
- Ex: Ao compartilhar um item, uma planilha de ação pode mostrar opções como "Copiar [[Glossário/Elementos/links|link]]", "Enviar por email", "Compartilhar no Twitter".
- Ex: Ao clicar em um item de uma [[Glossário/Elementos/listas|lista]], pode oferecer "Editar", "Excluir", "Marcar como concluído".

## Detalhes Adicionais / Tópicos

### Barra de Ação (Action Bar)

- **Posicionamento:** Topo, [[Glossário/Componentes/footer|rodapé]], ou flutuante (contextual).
- **Conteúdo:** Títulos, [[Glossário/Elementos/botoes|botões]] de ação ([[Glossário/Linguagem Visual/iconografia|ícone]] ou texto), [[Glossário/Componentes/menu|menus]], campos de busca.
- **Comportamento:** Pode ser fixa, rolar com a página ou aparecer/desaparecer contextualmente.

### Planilha de Ação (Action Sheet)

- **Ativação:** Disparada por uma ação do usuário (clique em [[Glossário/Elementos/botoes|botão]], item de [[Glossário/Elementos/listas|lista]]).
- **Conteúdo:** [[Glossário/Elementos/listas|Lista]] de [[Glossário/Elementos/botoes|botões]] de ação, cada um representando uma escolha.
- **Ação Destrutiva:** Ações como "Excluir" devem ser visualmente distintas (ex: [[Glossário/Linguagem Visual/cor|cor]] vermelha) e, idealmente, posicionadas separadamente ou exigir confirmação adicional.
- **Cancelar:** Geralmente inclui uma opção de "Cancelar" proeminente para fechar a planilha sem fazer uma escolha.
- **Acessibilidade:** Deve ser navegável via teclado, gerenciar o foco corretamente, e ser anunciada por leitores de tela como um diálogo.

## Variações

- **Barra de Ação - [[Glossário/Elementos/cabecalhos|Cabeçalho]] Padrão:**
  - Descrição: Barra no topo da tela com título e ações primárias/navegação.
  - Elementos Típicos: [Título, [[Glossário/Elementos/botoes|Botão]] Voltar, [[Glossário/Elementos/botoes|Botão]] de [[Glossário/Componentes/menu|Menu]], Ações (Salvar, Editar)]
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Action Bar - [[Glossário/Componentes/header|Header]] no Figma]

- **Barra de Ação - [[Glossário/Componentes/footer|Rodapé]] Fixo (Mobile):**
  - Descrição: Barra na parte inferior da tela em dispositivos móveis com 2-5 ações principais.
  - Elementos Típicos: [[[Glossário/Linguagem Visual/iconografia|Ícones]] com ou sem texto para navegação principal]
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Action Bar - Mobile [[Glossário/Componentes/footer|Footer]] no Figma]

- **Planilha de Ação - Padrão Mobile:**
  - Descrição: [[Glossário/Elementos/listas|Lista]] de opções que desliza da parte inferior da tela.
  - Estrutura: [Título opcional, [[Glossário/Elementos/listas|lista]] de [[Glossário/Elementos/botoes|botões]] de ação, [[Glossário/Elementos/botoes|botão]] de cancelar separado]
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Action Sheet Mobile no Figma]

- **Planilha de Ação - Popover Desktop:**
  - Descrição: [[Glossário/Componentes/menu|Menu]] contextual que aparece próximo ao elemento que o disparou.
  - Estrutura: [[[Glossário/Elementos/listas|Lista]] de opções]
  - Status: A definir
  - [[Glossário/Elementos/links|Link]] para o Figma: [[[Glossário/Elementos/links|Link]] para Action Sheet Desktop Popover no Figma]

## Melhores Práticas

- **Barra de Ação:** Mantenha o número de ações limitado para evitar desordem. Priorize as ações mais importantes.
- **Planilha de Ação:** Use para ações contextuais relacionadas a um item ou tarefa específica. Não use para navegação principal. Mantenha a [[Glossário/Elementos/listas|lista]] de opções concisa.

## Status Geral

**Status:** A definir

## [[Glossário/Elementos/links|Link]] para o Figma (Visão Geral)

[[[Glossário/Elementos/links|Link]] para Action Bars no Figma]
[[[Glossário/Elementos/links|Link]] para Action Sheets no Figma]
