---
title: "Voz, tom e microcópia"
description: "A voz não muda e o tom muda sempre; como documentar isso de forma utilizável; e as regras de rótulo, erro e estado vazio que decidem se alguém consegue seguir"
tags:
  - tema/conteudo
  - tipo/artigo
---

Quase toda empresa tem um documento de tom de voz, e quase nenhum é usado. O padrão é conhecido: três a cinco adjetivos ("acessível", "confiável", "humano"), uma página de exemplos genéricos, e nenhuma consequência prática na hora de escrever a mensagem de erro de um formulário às cinco da tarde.

O problema não é o documento. É que ele responde à pergunta errada.

## Voz é uma; tom é muitos

![Diagrama mostrando a voz constante e o tom variando conforme o estado de quem lê: deu certo, esperando, erro comum, perdeu algo](attachments/conteudo-voz-e-tom.svg)

A distinção que o guia de estilo da Mailchimp popularizou é a mais útil que existe: **você tem sempre a mesma voz; o que muda é o tom.**

Voz é o que não muda — o vocabulário, o nível de formalidade, se há humor e de que tipo, se você explica ou pressupõe. Tom é o ajuste conforme o estado emocional de quem está lendo naquele momento.

O que torna isso operacional é que os estados são poucos e previsíveis num produto. Alguém comemorando, alguém esperando, alguém que errou algo banal, alguém que perdeu dinheiro ou tempo. Documentar tom por **estado** — em vez de por adjetivo — transforma o guia em ferramenta, porque quem escreve chega nele com um caso concreto na mão.

A regra que resolve os casos difíceis também vem da Mailchimp: **é sempre mais importante ser claro do que ser divertido.** Humor em mensagem de erro envelhece na segunda exibição, e a pessoa vai vê-la muitas vezes.

## Um formato que funciona

Torrey Podmajersky propõe uma **tabela de voz** que resolve o problema do documento inútil. Em vez de adjetivos soltos, cada princípio do produto é desdobrado em decisões verificáveis: que vocabulário usar e evitar, que estruturas gramaticais, que pontuação, que uso de maiúscula, que tipo de humor cabe.

A diferença prática é que "acessível" não decide nada, enquanto "usamos 'você', nunca 'o usuário'; nunca exclamação em erro; verbos no imperativo nos botões; nada de gerúndio em rótulo" decide muita coisa e pode ser revisado por outra pessoa.

Um par de regras que vale copiar de qualquer guia sério, porque são as que mais aparecem em revisão:

- **O rótulo do botão diz o que vai acontecer.** "Salvar rascunho" em vez de "OK"; "Excluir conta" em vez de "Confirmar". Quem lê só o botão precisa saber onde está pisando — e muita gente lê só o botão.
- **A pergunta e a resposta combinam.** Se o diálogo pergunta "Descartar as alterações?", os botões são "Descartar" e "Continuar editando", não "Sim" e "Não".

## Mensagens de erro

É onde a microcópia mais importa, porque é onde a pessoa está travada.

![Anatomia de uma mensagem de erro anotada: perto do campo, nomeia o problema, diz o que fazer, preserva o que foi digitado e não culpa](attachments/conteudo-anatomia-erro.svg)

As diretrizes do Nielsen Norman Group organizam isso em três frentes.

**Visibilidade.** A mensagem fica junto do que falhou, não no topo da página. É perceptível sem depender só de cor — texto, ícone e destaque juntos, lembrando que há cerca de 350 milhões de pessoas no mundo com alguma deficiência de visão de cores. E o grau de interrupção acompanha a gravidade: aviso leve não merece modal.

Há também o erro de **mostrar cedo demais** — acusar o campo enquanto a pessoa ainda está digitando, ou no instante em que ela sai dele para consultar outra coisa.

**Comunicação.** Linguagem humana, sem código nem jargão. Descrição precisa do problema, porque "ocorreu um erro" não é diagnóstico. Conselho construtivo: a saída, não só o obstáculo. E tom que não culpa — a recomendação explícita é evitar palavras como *inválido*, *ilegal*, *incorreto*, que descrevem a pessoa em vez do problema.

**Eficiência.** Preservar o que foi digitado, em vez de limpar o campo e cobrar o retrabalho no pior momento possível. Reduzir o esforço de correção, oferecendo o palpite quando dá para adivinhar. E, quando cabe, explicar em uma linha por que a regra existe.

Acima de tudo isso está a frente que nem aparece na tela: **o erro que não acontece.** Aceitar CPF com e sem pontuação, telefone com e sem parênteses, data em mais de um formato; mostrar a regra de senha antes da digitação e não depois. Quase todo erro de formulário é uma decisão de tolerância que foi tomada por omissão.

## Estados vazios e espera

Dois lugares que quase sempre recebem o texto padrão da biblioteca e mereciam atenção.

**Estado vazio** é a primeira coisa que alguém vê quando chega, e a única tela do produto em que se pode explicar o que aquilo faz sem interromper ninguém. "Nenhum item encontrado" desperdiça isso. Diga o que aparece ali quando houver algo, e ofereça a primeira ação.

Vale separar dois casos que costumam usar a mesma frase e são opostos: **vazio porque é novo** — a pessoa ainda não fez nada, e o texto deve ensinar — e **vazio porque filtrou** — existe conteúdo, um filtro o está escondendo, e o texto deve oferecer a saída.

**Espera** precisa dizer o que está acontecendo, não que "está carregando". Quando a operação é longa, dizer o que já foi feito e o que falta é a diferença entre esperar e desistir.

## Escrever para ser traduzido

Se existe qualquer chance de tradução, três decisões precisam ser tomadas antes:

**Espaço.** Texto traduzido cresce, e cresce mais quanto mais curto for o original. Rótulos muito curtos podem dobrar ou triplicar de tamanho; parágrafos crescem algo em torno de 30%. Um botão que cabe justo em português vai quebrar em alemão.

**Frases inteiras.** Concatenar pedaços — `"Você tem "+ n + " item(ns)"` — quebra em qualquer idioma com gênero, plural ou ordem de palavras diferentes. Cada frase precisa existir inteira, com as variações de plural declaradas.

**Contexto para quem traduz.** Uma palavra solta numa planilha é ambígua: "Fechar" pode ser encerrar, pode ser um negócio fechado, pode ser um botão de dispensar. Sem uma nota dizendo onde a palavra aparece e o que ela faz, a tradução é um chute.

## O guia que se usa

Fechando onde começou: um guia de conteúdo só é usado se responder às perguntas que aparecem no trabalho. O que faz diferença, na ordem:

1. **Uma lista de decisões já tomadas** — os termos do produto e o que **não** usar como sinônimo. Essa é a parte mais consultada de qualquer guia e a que menos gente escreve.
2. **Padrões por componente** — como se escreve um erro, um botão destrutivo, um estado vazio, uma confirmação. Junto do componente no design system, não num documento separado.
3. **Tom por estado**, com exemplos reais do produto.
4. **A voz**, por último. É a parte que os guias colocam primeiro e a que menos decide.

---

**Antes:** [[Escrever claro]] · **Continua em:** [[Estrutura e reúso]]

**Ver também:** [[Notificações/Escrever a mensagem|Escrever a mensagem]] · [[Notificações/Acessibilidade de mensagens|Acessibilidade de mensagens]]
