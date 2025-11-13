---
title: "form structure"

---

## Estrutura de Formulário (Form Structure)

## Descrição Geral

O padrão de estrutura de formulário define as melhores práticas para organizar e apresentar campos de entrada de dados, rótulos, [[Glossário/Componentes/messaging|mensagens]] de ajuda e ações (como [[Glossário/Elementos/botoes|botões]] de submissão) de forma clara, eficiente e acessível. Formulários são um dos principais meios de interação do usuário com um portal, seja para entrada de dados, pesquisa, configuração ou qualquer outra tarefa que requeira input do usuário.

## Princípios Chave / Objetivos

- **Clareza:** O usuário deve entender facilmente o que cada campo significa e qual informação é esperada.
- **Eficiência:** Minimizar o esforço cognitivo e o tempo necessário para preencher o formulário.
- **Prevenção de Erros:** Ajudar o usuário a evitar erros antes que eles aconteçam e facilitar a correção quando ocorrerem.
- **Acessibilidade:** Garantir que os formulários sejam utilizáveis por todas as pessoas, incluindo aquelas com deficiências.
- **Consistência:** Manter uma apresentação e comportamento consistentes para formulários em todo o portal.

## Elementos Comuns / Estrutura Típica

- **Rótulos (Labels):** Descrição concisa do propósito de cada campo de entrada. Devem estar sempre visíveis e claramente associados ao seu respectivo controle.
- **Campos de Entrada (Input Fields):** Elementos onde o usuário insere dados (ex: caixas de texto, áreas de texto, [[Glossário/Componentes/menu|menus]] suspensos, seletores de data, [[Glossário/Elementos/form_controls|caixas de seleção]], [[Glossário/Elementos/botoes|botões]] de rádio).
- **Texto de Ajuda/Dicas (Helper Text/Hints):** Informações adicionais ou instruções para um campo específico, posicionadas perto do campo.
- **Agrupamento de Campos (Fieldsets e Legends):** Para agrupar campos relacionados logicamente, especialmente em formulários longos (ex: "Endereço de Entrega", "Informações de Pagamento").
- **Validação e [[Glossário/Componentes/messaging|Mensagens]] de Erro:** Feedback imediato sobre a validade dos dados inseridos. [[Glossário/Componentes/messaging|Mensagens]] de erro devem ser claras, específicas e posicionadas perto do campo problemático.
- **Indicação de Obrigatoriedade:** Marcar claramente os campos que são obrigatórios (ex: com um asterisco *).
- **[[Glossário/Elementos/botoes|Botões]] de Ação:** [[Glossário/Elementos/botoes|Botões]] primários (ex: "Salvar", "Enviar") e secundários (ex: "Cancelar", "Limpar").
- **Progressão (para formulários multi-etapas):** Indicadores de progresso para formulários longos divididos em várias etapas.

## Comportamento e Interação

1. O formulário é apresentado ao usuário.
2. O usuário interage com os campos, inserindo dados.
3.  - **Validação em Tempo Real (Inline Validation):** Idealmente, o sistema fornece feedback sobre a validade dos dados à medida que o usuário preenche ou ao sair de um campo.
    - **Validação na Submissão:** No mínimo, a validação ocorre quando o usuário tenta submeter o formulário.
4. [[Glossário/Componentes/messaging|Mensagens]] de erro são exibidas para campos inválidos, e o foco pode ser direcionado para o primeiro erro.
5. O usuário corrige os erros e tenta submeter novamente.
6. Após a submissão bem-sucedida, o usuário recebe uma mensagem de confirmação ou é redirecionado.

## Diretrizes de Uso e Boas Práticas

### Faça

- Organize os campos em uma única coluna sempre que possível, para facilitar a leitura e o escaneamento.
- Posicione os rótulos acima dos campos de entrada (top-aligned) para melhor associação e leitura rápida.
- Use linguagem clara e concisa para rótulos e textos de ajuda.
- Agrupe campos relacionados usando `fieldset` e `legend`.
- Forneça feedback claro e imediato para validação e erros.
- Torne óbvio qual é o [[Glossário/Elementos/botoes|botão]] de ação primário.
- Garanta que o formulário seja totalmente navegável e operável via teclado.
- Dimensões dos campos de entrada devem, idealmente, sugerir o tamanho da entrada esperada.

### Não Faça

- Não use placeholders como substitutos de rótulos (labels); placeholders desaparecem e não são acessíveis.
- Não esconda rótulos ou instruções importantes.
- Não crie formulários excessivamente longos em uma única página; divida-os em etapas lógicas se necessário.
- Não desabilite o [[Glossário/Elementos/botoes|botão]] de submissão até que todos os campos estejam válidos, a menos que haja uma razão muito forte; em vez disso, permita a submissão e mostre os erros.
- Não use CAPTCHAs a menos que seja absolutamente necessário e, se usar, escolha opções acessíveis.
- Não limpe automaticamente os campos após um erro de submissão, a menos que seja um campo de senha.

## Considerações de Acessibilidade

- Associe explicitamente cada rótulo (`<label>`) ao seu controle de formulário (campo de entrada, [[Glossário/Elementos/form_controls|caixa de seleção]], etc.) usando o atributo `for` (que corresponde ao `id` do controle).
- Use `fieldset` e `legend` para agrupar [[Glossário/Elementos/form_controls|controles de formulário]] relacionados (ex: um grupo de [[Glossário/Elementos/botoes|botões]] de rádio ou [[Glossário/Elementos/form_controls|caixas de seleção]]).
- Forneça [[Glossário/Componentes/messaging|mensagens]] de erro textuais e associe-as programaticamente aos campos correspondentes (ex: via `aria-describedby` ou `aria-errormessage`).
- Garanta que a indicação de campos obrigatórios seja feita de forma acessível (não apenas por [[Glossário/Linguagem Visual/cor|cor]] ou um asterisco visual sem alternativa textual).
- Os formulários devem seguir uma ordem lógica de tabulação.
- Garanta bom contraste de [[Glossário/Linguagem Visual/cor|cores]] para todos os elementos do formulário.

## Exemplos / Cenários de Uso

- Formulário de contato.
- Formulário de [[Glossário/Padrões/purchase_checkout|checkout]] em e-commerce.
- Formulário de [[Glossário/Padrões/create_account|registro]] de usuário.
- Formulário de [[Glossário/Padrões/settings|configurações]] de perfil.
- Formulário de pesquisa com [[Glossário/Componentes/filters|filtros]] avançados.

## Variações Comuns

- **Formulário de Etapa Única (Single-Step Form):** Todos os campos em uma única visualização.
- **Formulário Multi-Etapas (Multi-Step Form / Wizard):** Campos divididos em várias seções ou páginas para reduzir a carga cognitiva.
- **Formulário Inline:** Campos de formulário integrados diretamente em uma linha de texto ou outro conteúdo (ex: campo de busca no [[Glossário/Elementos/cabecalhos|cabeçalho]]).
- **Formulário [[Glossário/Componentes/dialog|Modal]]:** Apresentado dentro de uma janela [[Glossário/Componentes/dialog|modal]].

## Status

A definir

## Recursos Adicionais / Figma

- [[[Glossário/Elementos/links|Link]] para os componentes de formulário (campos, [[Glossário/Elementos/botoes|botões]], etc.) no Figma]
- [[[Glossário/Elementos/links|Link]] para exemplos de layouts de formulários no Figma]
