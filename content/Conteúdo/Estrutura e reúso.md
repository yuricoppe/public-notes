---
title: "Estrutura e reúso"
description: "Por que conteúdo guardado como bloco de texto não pode ir a lugar nenhum — e as ferramentas que definem estrutura antes da escrita: modelo core, arquitetura de mensagem e gabaritos"
tags:
  - tema/conteudo
  - tipo/artigo
---

Existe uma decisão de conteúdo que é tomada antes de qualquer palavra ser escrita, quase sempre sem que ninguém perceba que está decidindo: **em que forma o conteúdo vai ser guardado.** Ela determina, anos depois, se aquele material pode aparecer num aplicativo, virar resumo numa lista, ser lido por voz ou alimentar outra coisa — ou se vai precisar ser reescrito à mão.

## Bloco ou pedaços

![Comparação entre conteúdo em bloco único e conteúdo em pedaços nomeados, com título, resumo, corpo, preço, data e imagem separados](attachments/conteudo-blob-chunk.svg)

Karen McGrane nomeou os dois estados com uma clareza que ficou: de um lado o **bloco**, um campo grande de texto formatado num editor rico, onde título, resumo, imagem, preço e data estão todos misturados dentro da mesma marcação. Do outro, os **pedaços**: cada parte com nome, tipo e regra própria.

A diferença não é técnica, é de consequência. Com o conteúdo em bloco, a aparência está grudada no significado. O negrito que alguém usou porque "ficava melhor" é indistinguível do negrito que marca um termo importante. O preço está dentro de uma frase e não pode ser comparado, atualizado em massa nem mandado numa notificação.

O teste é simples e vale fazer agora, mentalmente, com o produto que você tem: **peça o resumo de todos os itens para montar uma lista, ou só o preço para mandar num aviso.** Se a resposta é "dá, mas alguém vai ter que copiar à mão", o conteúdo está em bloco.

O princípio associado é o COPE — criar uma vez, publicar em todo lugar — que a NPR formulou construindo conteúdo agnóstico de apresentação. A ideia central é que quem escreve entrega **estrutura**, e quem exibe decide a apresentação. Sem isso, cada canal novo é um projeto de reescrita.

Um efeito colateral que ficou mais importante do que era: conteúdo estruturado é também o que máquinas conseguem consumir. Um resumo que existe como campo próprio pode ser reaproveitado por busca, por assistente e por qualquer sistema que precise da informação sem a diagramação em volta. Um resumo que está em negrito no meio de um bloco, não.

## O modelo de conteúdo

O nome do artefato que registra essa decisão é **modelo de conteúdo**: a lista dos tipos de conteúdo que o produto tem e, para cada um, os campos que o compõem, com tipo, obrigatoriedade, limite e a relação com outros tipos.

Escrever um modelo é uma sequência curta de perguntas, e ela força discussões úteis:

- Que **tipos** existem de verdade? Artigo, produto, evento, pessoa, ajuda. Quase sempre são menos do que o time imagina, e dois "tipos" diferentes viram um só com um campo a mais.
- Que **campos** cada tipo tem, e qual é obrigatório? A discussão sobre obrigatoriedade é onde se descobre o que o time realmente considera essencial.
- Que **limites** cada campo tem, e por quê? Um limite de resumo em 160 caracteres não é capricho: é o espaço que ele terá no lugar mais apertado onde vai aparecer.
- Como os tipos **se relacionam**? Um artigo tem autor; um autor tem vários artigos.

O sinal de que o modelo está errado costuma aparecer no uso: quando as pessoas começam a colocar informação no campo errado porque não existe campo certo, o modelo já não descreve o produto.

## Começar pela resposta: o modelo core

![O modelo core: caminhos de entrada levam a uma página núcleo, que cruza a tarefa da pessoa com o objetivo do negócio, e leva a caminhos de saída](attachments/conteudo-modelo-core.svg)

O **modelo core**, de Are Halland, ataca o problema por outro lado. Em vez de começar pela estrutura do site, começa pela página que precisa responder a alguma coisa.

Seis elementos, trabalhados página a página: o **público**, a **tarefa** que a pessoa veio fazer, o **objetivo do negócio**, os **caminhos de entrada** (como ela chega — busca, link externo, campanha), os **caminhos de saída** (para onde deve ir depois) e o **conteúdo núcleo**, que é a interseção de tudo isso.

O deslocamento que ele provoca é grande e simples: **quase ninguém entra pela página inicial.** Projetar a partir dela é projetar para a minoria dos acessos. A página núcleo — aquela em que a pessoa efetivamente aterrissa vinda de uma busca — é o objeto de trabalho.

O formato de oficina que Halland descreve tem um detalhe que vale copiar mesmo fora do método: trabalhar em **duplas de competências diferentes**, uma pessoa de conteúdo com uma de negócio ou de tecnologia. A revisão cruzada fica embutida no exercício, em vez de virar uma etapa de aprovação depois.

## O que dizer, antes de como dizer

Uma ferramenta anterior a todas as outras: a **arquitetura de mensagem**, de Margot Bloomstein. É a lista hierarquizada do que a organização quer comunicar — não o texto, e sim as ideias que o texto vai carregar.

O método é um card sort com adjetivos. O grupo separa termos em "somos", "não somos" e "gostaríamos de ser", e depois prioriza um número pequeno dentro do primeiro grupo. O valor não está no resultado bonito: está em **descobrir cedo onde as pessoas discordam**. Quando marketing acha que a marca é "ousada" e o jurídico acha que é "prudente", isso vai aparecer como conflito em cada revisão de texto pelos próximos dois anos — a menos que apareça numa sala, uma vez.

Kissane dá o conselho que evita o pior desfecho dessa atividade: não se enrole. Mensagens são ferramenta interna e devem ser desenvolvidas só até o ponto de utilidade. Uma semana a mais mexendo na redação das mensagens é uma semana perdida — elas não são o conteúdo, são o que dá forma a ele.

## Gabaritos de conteúdo

O artefato mais subestimado do repertório, também de Kissane: um **gabarito de conteúdo** é o acompanhante, em nível de parágrafo, do wireframe. Um documento por tipo de página, que diz a quem vai escrever exatamente o que se espera.

Quatro partes:

1. **Cada pedaço de informação** que precisa estar na página, e depois os opcionais.
2. **O que cada pedaço deve realizar.** Não o que ele é, e sim o que ele faz — "este resumo aparece nos resultados de busca externa, então precisa fazer sentido para quem não conhece o produto".
3. **As especificações**: contagem de palavras ideal, estilo de maiúscula, se é lista ou parágrafo, e observações do tipo "evite jargão aqui" ou "se der para trocar esta descrição por uma captura de tela com legenda, troque".
4. **Um exemplo preenchido** de cada pedaço — e, quando há mais de um formato possível, um exemplo de cada.

O ganho é duplo. Para quem escreve, resolve a página em branco. E para quem recebe o pedido — o especialista, o jurídico, a pessoa de produto que detém a informação — transforma "escreva sobre isso" numa tarefa com fronteiras, que é a diferença entre receber o texto na sexta e receber em três semanas.

Um gabarito bem-feito exige saber antes o que cada página deve fazer, o que vem da pesquisa, das mensagens e do wireframe. Se essa parte não existe, o gabarito não vai salvar nada — mas a tentativa de escrevê-lo revela a falta rápido, e é barata.

---

**Continua em:** [[Auditar, testar e medir]]

**Antes:** [[Voz, tom e microcópia]] · [[Conteúdo é decisão, não texto]]
