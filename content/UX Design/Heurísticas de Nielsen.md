---
title: "Heurísticas de Nielsen"
description: "As dez heurísticas com perguntas de sinal de alerta e exemplos, para usar em avaliação heurística"
tags:
  - tema/ux
  - tipo/referencia
---

## 1. Visibilidade do status do sistema

O sistema deve manter a pessoa informada sobre o que está acontecendo, com feedback adequado e em tempo razoável.

**Perguntas de sinal de alerta:**

- Depois de uma ação (clique, envio, upload), há alguma confirmação visual de que algo aconteceu?
- Operações que demoram (carregamento, processamento) mostram um indicador de progresso, ou a tela só "congela"?
- O estado atual (logado, carrinho com itens, filtro ativo) está visível, ou a pessoa precisa adivinhar/lembrar?

**Exemplos comuns:** botão de "Salvar" sem nenhum feedback de sucesso/erro; loading infinito sem skeleton ou spinner; filtros aplicados que não aparecem destacados em nenhum lugar da tela.

---

## 2. Compatibilidade entre o sistema e o mundo real

A interface deve falar a língua do usuário, com palavras, frases e conceitos familiares — não jargão técnico ou interno do sistema.

**Perguntas de sinal de alerta:**

- Os textos usam termos técnicos/internos (códigos de erro, nomes de tabelas, siglas) que a pessoa comum não entenderia?
- Ícones e metáforas visuais correspondem ao que representam no mundo real, ou são ambíguos?
- A ordem das informações segue uma lógica natural para a tarefa (ex: do mais geral ao mais específico)?

**Exemplos comuns:** mensagem de erro como "Error 500: NullPointerException"; ícone de disquete para "salvar" sem rótulo, confundindo usuários mais novos; datas em formato técnico (`2026-06-21T00:00:00Z`) em vez de "21 de junho de 2026".

---

## 3. Controle e liberdade do usuário

A pessoa precisa de uma saída clara para ações indesejadas, sem precisar passar por um processo longo — "desfazer" e "refazer" devem ser suportados.

**Perguntas de sinal de alerta:**

- Existe um caminho claro de saída/cancelamento em fluxos modais, formulários longos ou processos de várias etapas?
- Ações destrutivas (excluir, cancelar assinatura) podem ser desfeitas, ou são irreversíveis sem aviso?
- É fácil voltar a um passo anterior em um fluxo de várias etapas, ou a pessoa precisa recomeçar do zero?

**Exemplos comuns:** modal sem botão de "X" ou "Cancelar" visível; exclusão de item sem confirmação nem opção de desfazer; wizard de cadastro que não permite voltar para revisar um campo.

---

## 4. Consistência e padrões

Elementos e ações similares devem ter a mesma aparência e comportamento em toda a interface; siga convenções da plataforma/indústria.

**Perguntas de sinal de alerta:**

- Botões com a mesma função (ex: ação primária) têm a mesma cor/posição em todas as telas, ou variam sem motivo?
- Os termos usados para o mesmo conceito são sempre os mesmos (ex: "Excluir" em uma tela e "Remover" em outra para a mesma ação)?
- A interface segue os padrões já estabelecidos da plataforma (web, iOS, Android) ou reinventa interações básicas sem necessidade?

**Exemplos comuns:** botão primário azul em uma tela e verde em outra; ícone de "voltar" que muda de posição entre telas do mesmo fluxo; um mesmo dado (ex: preço) formatado de forma diferente em telas distintas.

---

## 5. Prevenção de erros

Melhor que boas mensagens de erro é um design que previne o problema antes de ele acontecer.

**Perguntas de sinal de alerta:**

- Existem validações de formulário em tempo real, ou o erro só aparece depois do envio?
- Ações destrutivas/irreversíveis pedem confirmação?
- Campos com formato específico (telefone, CPF, data) dão alguma orientação de formato antes do erro?

**Exemplos comuns:** formulário que só mostra todos os erros de validação depois de clicar em "Enviar"; botão de "Excluir conta" sem nenhuma confirmação; campo de quantidade que aceita números negativos sem aviso.

---

## 6. Reconhecimento em vez de memorização

Minimize a carga de memória da pessoa: opções, elementos e instruções devem estar visíveis ou facilmente recuperáveis, não exigir que ela lembre informação de uma tela anterior.

**Perguntas de sinal de alerta:**

- A pessoa precisa lembrar de algo visto em uma tela anterior para completar a tarefa na tela atual (ex: um código, um valor)?
- Opções/histórico relevantes (buscas recentes, itens visitados) estão disponíveis, ou a pessoa precisa redigitar/lembrar?
- Rótulos e instruções estão visíveis no momento da ação, ou dependem de a pessoa ter lido algo em outro lugar?

**Exemplos comuns:** tela de pagamento que pede para confirmar um valor mostrado só na tela anterior; campo de busca sem sugestões nem histórico; instruções de preenchimento que só aparecem em um tooltip de difícil acesso.

---

## 7. Flexibilidade e eficiência de uso

Aceleradores (atalhos, automações) ajudam usuários experientes sem prejudicar usuários novos.

**Perguntas de sinal de alerta:**

- Existem atalhos, automações ou personalizações para quem usa o produto com frequência (favoritos, atalhos de teclado, valores padrão)?
- Tarefas repetitivas exigem os mesmos passos manuais toda vez, mesmo para usuários avançados?
- A interface tenta ser "única" para todo mundo, sem opção de adaptar à experiência da pessoa?

**Exemplos comuns:** nenhum atalho de teclado em uma ferramenta de uso intenso (ex: editor, dashboard); ausência de "favoritos" ou "valores padrão" em fluxos repetitivos; impossibilidade de pular etapas já preenchidas anteriormente.

---

## 8. Design estético e minimalista

Telas não devem conter informação irrelevante ou raramente necessária — cada elemento extra compete por atenção com o que importa.

**Perguntas de sinal de alerta:**

- Há elementos visuais (banners, textos, badges) que não ajudam na tarefa principal da tela?
- A hierarquia visual (tamanho, cor, posição) deixa claro o que é mais importante, ou tudo "grita" igual?
- Informação raramente usada está sempre visível, competindo com a informação principal?

**Exemplos comuns:** tela de checkout com banners promocionais distraindo do fluxo de pagamento; múltiplos elementos com a mesma cor de destaque, sem hierarquia clara; texto de ajuda extenso sempre visível em vez de sob demanda.

---

## 9. Ajudar os usuários a reconhecer, diagnosticar e se recuperar de erros

Mensagens de erro devem ser em linguagem simples (sem códigos), indicar precisamente o problema, e sugerir uma solução.

**Perguntas de sinal de alerta:**

- A mensagem de erro explica o que aconteceu em linguagem simples, ou só mostra um código/jargão?
- A mensagem indica exatamente qual campo/ação causou o problema?
- Há uma sugestão clara de como corrigir o erro, ou a pessoa precisa adivinhar?

**Exemplos comuns:** "Algo deu errado" sem nenhum detalhe; erro de senha que não diz qual requisito não foi atendido; campo com erro que não é destacado visualmente, deixando a pessoa procurar qual campo falhou.

---

## 10. Ajuda e documentação

Idealmente o sistema deve ser usável sem documentação, mas quando necessário, a ajuda deve ser fácil de buscar, focada na tarefa da pessoa, e com passos concretos.

**Perguntas de sinal de alerta:**

- Existe ajuda contextual (tooltip, FAQ, busca) acessível no momento em que a pessoa provavelmente precisaria dela?
- Se há documentação, ela é específica para a tarefa atual, ou genérica demais para ser útil?
- A ajuda está fácil de encontrar, ou escondida em um menu distante da ação?

**Exemplos comuns:** funcionalidade complexa sem nenhum tooltip ou link de ajuda; central de ajuda genérica sem busca; documentação que explica o "o quê" mas não o "como" passo a passo.