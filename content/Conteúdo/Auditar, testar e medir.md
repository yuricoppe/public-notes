---
title: "Auditar, testar e medir"
description: "O inventário e a auditoria qualitativa, os testes de conteúdo que cabem numa tarde, e por que não se deve perguntar de qual versão a pessoa gosta mais"
tags:
  - tema/conteudo
  - tipo/artigo
---

Conteúdo é a parte do produto que mais escapa de avaliação. Componente tem revisão de código, layout tem revisão de design, e texto costuma ser aprovado por quem tem o cargo mais alto na reunião. Este artigo é sobre as três formas de tirar a decisão do gosto: saber o que se tem, testar se funciona, e acompanhar se continua funcionando.

## Saber o que se tem

Antes de qualquer coisa, o **inventário**: um mapa exaustivo de tudo que existe. Erin Kissane descreve o formato mínimo — para cada peça, o título, o formato (texto, vídeo, PDF), a URL ou localização, o tipo (página de destino, artigo, página de suporte, contato) e o **dono**, a pessoa responsável pela manutenção.

A última coluna é a que costuma faltar e a que mais revela. Um inventário em que metade das linhas tem o campo "dono" vazio já entregou o diagnóstico antes de qualquer análise.

Kissane não romantiza o trabalho: inventariar um site grande leva bastante tempo, e é o único jeito de realmente entender o que se tem. Vale ser honesto sobre isso no planejamento, em vez de descobrir na segunda semana.

Depois vem a **auditoria qualitativa**, que é avaliar a qualidade do que está no inventário. Aqui há uma armadilha de sequência que ela aponta com precisão: **não dá para avaliar conteúdo sem saber o que se está procurando.** Dá para reconhecer texto mal escrito, mas não dá para saber se o conteúdo está funcionando sem antes conhecer as necessidades de quem lê. Por isso a ordem correta é pesquisa primeiro, personas ou proxies em mãos, e só então a auditoria.

Com isso pronto, os sete princípios de [[Conteúdo é decisão, não texto]] viram uma régua utilizável: é apropriado? é útil? está centrado em quem usa? é claro, consistente, conciso? foi mantido, ou está desatualizado?

E há um uso da auditoria que é político, não editorial: é ela que permite dizer a quem decide **quanto trabalho** custa implementar as recomendações. Sem esse número, a proposta é uma opinião.

## Testar

![Tabela ligando a pergunta ao método: compreensão pelo teste cloze, clareza pelo marca-texto, rótulos pelo teste da banana, vocabulário por card sorting](attachments/conteudo-testes.svg)

Os testes de conteúdo têm uma vantagem que os torna difíceis de recusar: quase todos são baratos, rápidos e não exigem ferramenta.

**Teste cloze** mede compreensão frase a frase. Pegue um trecho de 125 a 250 palavras, apague uma palavra a cada cinco ou seis, e peça para a pessoa preencher as lacunas. A convenção é que **60% de acerto ou mais** indica um texto compreensível o bastante. É rápido o suficiente para rodar com colegas antes de levar a usuários.

**Teste do marca-texto** mostra *onde* trava. Duas cores: uma para o que ajuda, outra para o que confunde. Sobrepondo as marcações de várias pessoas você tem um mapa de calor do texto — e os pontos que todo mundo marcou da mesma cor não precisam de mais discussão.

**Teste da banana**, descrito por Vitaly Friedman, é para rótulos e ícones: troque todas as ações por "banana" e pergunte o que cada uma faria. O que a pessoa consegue deduzir vem do contexto e do ícone; o que ela não consegue dependia inteiramente da palavra — e vale conferir se a palavra estava dando conta.

**Card sorting e teste de árvore** resolvem vocabulário e agrupamento: como as pessoas nomeiam e organizam as coisas, e se conseguem achar algo na estrutura que você propôs.

**Teste de cinco segundos** mede primeira impressão: o que ficou, o que a pessoa acha que a página faz.

A regra que atravessa todos, e a mais importante: **não pergunte de qual versão a pessoa gosta mais.** Preferência declarada não prevê compreensão, e pedir opinião sobre texto convida qualquer um a virar editor. Peça para a pessoa explicar, com as próprias palavras, o que acabou de ler — ou, melhor ainda, peça para ela fazer a coisa que o texto pedia.

Vale também não falar durante a sessão. O impulso de explicar o que se quis dizer destrói exatamente o dado que se foi buscar.

## Medir

Métrica de conteúdo é a parte mais frágil, porque quase tudo que é fácil de medir é fácil de enganar.

**Tempo na página** é ambíguo por natureza: pode significar interesse ou dificuldade, e você não consegue distinguir os dois sem outra fonte. Numa página de ajuda, tempo alto é geralmente sintoma ruim.

**Rolagem** diz até onde foi, não o que foi lido — e o padrão de varredura em "bolo de camadas" produz rolagem completa com leitura mínima.

O que costuma valer mais:

**Sucesso na tarefa.** A pessoa conseguiu fazer o que o conteúdo existia para permitir? É a única medida que fecha o raciocínio.

**Contatos de suporte por assunto.** É o indicador de conteúdo mais honesto que a maioria das empresas já tem e não usa. Cada dúvida repetida no suporte é uma página que não respondeu — e, ao contrário de teste, é um fluxo contínuo e de graça.

**Busca interna sem resultado**, que aponta o vocabulário que as pessoas usam e o seu produto não reconhece.

**Taxa de erro por campo**, num formulário, que localiza exatamente qual rótulo ou instrução está falhando.

**Frescor.** Que proporção do conteúdo foi revisada nos últimos doze meses, e quanta coisa não tem dono. Não mede qualidade, mas prevê deterioração — e é a métrica que dá substância ao princípio de que nada se publica sem plano de manutenção.

## Uma rotina que cabe

Nada disso funciona como projeto único. O que sustenta é um ciclo modesto e repetido:

**A cada trimestre**, olhar os assuntos mais frequentes no suporte e as buscas sem resultado. Duas listas curtas que dizem onde o conteúdo falhou desde a última vez.

**A cada semestre**, uma auditoria de uma fatia — não do site inteiro. Um caminho, uma seção, um tipo de página. Auditoria total é a que nunca acontece.

**A cada peça nova**, um teste cloze de dez minutos antes de publicar. É o menor investimento com o maior retorno de todo este conjunto de anotações.

**A cada revisão**, atualizar a data e o dono. Conteúdo sem dono declarado é conteúdo que já começou a envelhecer.

---

**Antes:** [[Estrutura e reúso]] · [[Como as pessoas leem]]

**Ver também:** [[Notificações/Frequência, agrupamento e controle|Medir notificações]]
