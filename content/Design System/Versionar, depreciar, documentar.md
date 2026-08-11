---
title: "Versionar, depreciar, documentar"
description: "Como comunicar mudança sem quebrar quem usa: versionamento semântico aplicado a design, janelas de depreciação e o que uma boa página de componente contém"
tags:
  - tema/design-system
  - tipo/artigo
---

Um design system passa a maior parte da vida em manutenção. E manutenção, aqui, é quase inteiramente um problema de comunicação: a mudança em si costuma ser pequena; o caro é fazer com que dezenas de pessoas saibam dela, entendam se as afeta e consigam agir a tempo.

## Versionamento semântico, para quem desenha

O formato é `MAIOR.MENOR.CORREÇÃO`:

- **MAIOR** — mudança incompatível. Algo quebra.
- **MENOR** — recurso novo, compatível com o que existia.
- **CORREÇÃO** — conserto compatível.

Nathan Curtis defende que designers aprendam isso, e o motivo não é técnico: é que sem esse vocabulário compartilhado, as duas frustrações clássicas não têm como ser resolvidas. Do lado do designer, "adicionei um recurso novo do sistema ao meu design, e o desenvolvedor diz que não dá para usar". Do lado do desenvolvedor, "a designer espalhou estilos e upgrades de componente por uma feature nova, sem nenhuma noção do custo de atualização que isso dispara no app inteiro".

Um esclarecimento que evita mal-entendido: **versão maior não significa esforço grande.** Curtis dá o exemplo de uma quebra que sobe de `1.13.0` para `2.0.0` só por renomear uma classe de `system-btn--primary` para `system-button--primary`. O número não é campanha de marketing nem promessa de trabalho pesado — é um aviso de que há uma mudança estrutural a observar na atualização.

Três decisões que vale tomar cedo:

**Versionar a biblioteca inteira ou componente a componente.** Versionar por biblioteca é mais simples de comunicar e faz o número subir para todo mundo quando um único componente muda. Versionar por componente é mais preciso e muito mais trabalhoso de acompanhar.

**Desacoplar a versão da documentação da versão do código.** Assim dá para corrigir texto sem publicar release — e vale manter um arquivo das versões anteriores, porque sempre há times que atualizam com atraso.

**Separar os tokens como dependência própria.** Isso permite que o estilo evolua independentemente do código dos componentes, o que beneficia também quem consome só os tokens e não a biblioteca.

E uma que quase sempre é esquecida: **os arquivos de design também têm versão.** Curtis é direto — "use a última" não é bom o suficiente. A versão precisa estar comunicada em algum lugar visível: no nome da biblioteca vinculada, na hierarquia dos componentes, numa camada de anotação.

## Depreciar é um anúncio

![Ciclo de vida de um componente — proposto, experimental, estável, depreciado, removido — com o detalhe do que a fase de depreciação exige](attachments/design-system-ciclo-de-vida.svg)

Depreciação é a fase que mais falta. O padrão comum é o componente simplesmente sumir, ou pior, mudar de comportamento sem aviso. O efeito disso é previsível e difícil de reverter: os times param de atualizar. E um sistema que ninguém atualiza congela — a versão publicada e a versão em uso divergem até o sistema virar ficção.

Uma depreciação que funciona tem três partes:

**Um prazo dito em público.** A janela varia com a distância entre os times. Curtis cita os dois extremos: o Lightning, da Salesforce, dava 18 meses, por causa de times amplos e desconectados; o Origami, do Financial Times, comprimia para 3 a 6 meses, com uma comunidade de desenvolvimento mais próxima.

**O substituto apontado por nome.** "Descontinuado" sem alternativa é um problema transferido, não resolvido.

**Um guia de migração com antes e depois.** Trecho de código do jeito antigo, trecho do jeito novo. Quando a mudança é mecânica e ampla, um codemod economiza mais do que qualquer documento.

Durante a janela, o sistema sustenta os dois — o novo como padrão e o antigo numa página separada, marcado. E a regra de remoção mais simples que existe: o que foi depreciado numa versão maior sai na próxima. Depreciou na 10, remove na 11.

O contorno disso é a **etiqueta de estado**, e ela resolve mais do que parece. Proposto, experimental, estável, depreciado, removido — visível na documentação, no arquivo de design e, quando dá, no console. Lembrando que "não sei em que estado está esta peça" foi o segundo maior problema relatado por quem consome design systems na pesquisa da Sparkbox.

## O que uma página de componente precisa ter

Documentação ruim foi o problema número um relatado por quem usa (39%). Vale ser específico sobre o que falta.

**Quando usar — e quando não usar.** A segunda metade é a que quase sempre falta e a que mais evita erro. Um componente sem fronteira declarada vai ser usado fora dela.

**Estados e variantes**, com o nome exato que cada um tem no código e no arquivo de design. Nome divergente entre design e código é uma das fontes mais silenciosas de atrito.

**Comportamento em conteúdo real** — texto longo, texto em outro idioma, valor vazio, número grande. O componente demonstrado só com o conteúdo ideal é um componente não documentado.

**Acessibilidade**, com o que já vem resolvido e o que continua sendo responsabilidade de quem usa. Essa divisão precisa ser explícita, senão as duas partes assumem que a outra cuidou.

**Um exemplo que dá para copiar** e uma área para experimentar. Só 34% dos sistemas na pesquisa da Sparkbox tinham ambiente de teste na documentação.

**A versão em que entrou e o estado atual.**

E o mais escasso: **o registro de mudanças**. Não a lista de commits — a lista, em linguagem humana, do que mudou, o que quebra e o que fazer a respeito.

## Reduzir também é manutenção

Vale terminar com a parte que quase nunca entra em roadmap. No *deep dive* da Figma sobre o sistema da Uber, Ian Guisard trata explicitamente dos benefícios de **reduzir** a quantidade de componentes e do processo de depreciar os que sobram — junto com o registro de mudanças e as especificações que o sistema entrega para engenharia.

O instinto de qualquer time de design system é crescer, porque crescer é visível, é fácil de reportar e responde a pedidos reais. Mas cada componente publicado é uma dívida permanente: precisa de manutenção, de teste em navegador, de revisão de acessibilidade a cada mudança de fundação, e ocupa espaço na cabeça de quem procura. Um sistema com quarenta componentes bem cuidados serve melhor do que um com cento e vinte, dos quais trinta estão quebrados e ninguém sabe quais.

A pergunta que vale fazer uma vez por trimestre é a inversa da usual: **o que dá para tirar?** Componentes com um consumidor só; variantes que existem porque alguém pediu e ninguém mais usou; tokens que não são referenciados em lugar nenhum. Tirar é mais difícil politicamente do que acrescentar e rende mais.

---

**Antes:** [[Adoção e maturidade]] · [[Governança e contribuição]] · [[A anatomia em camadas]]
