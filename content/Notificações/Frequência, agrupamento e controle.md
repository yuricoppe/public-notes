---
title: "Frequência, agrupamento e controle"
description: "Quantas mensagens são demais, por que agrupar de hora em hora não resolve, e o que medir quando a métrica óbvia mente"
tags:
  - tema/ux
  - dominio/notificacoes
  - tipo/artigo
---

Frequência é a reclamação número um sobre notificação — em teste de usabilidade, em avaliação de app, em conversa de corredor. E é também a variável que os times têm mais dificuldade de tratar, porque cada notificação, isolada, sempre parece justificada. O problema nunca está em uma mensagem. Está na soma, e ninguém é dono da soma.

## Agrupar funciona, mas o intervalo é o ingrediente ativo

O experimento mais claro sobre isso é de Nicholas Fitz, Kostadin Kushlev e colegas, publicado em 2019 na *Computers in Human Behavior*. Um experimento de campo randomizado, com 237 participantes, duas semanas, quatro condições: entrega normal, lotes de hora em hora, lotes três vezes ao dia (9h, 15h e 21h) e nenhuma notificação.

![Resultado do experimento de Fitz e colegas: só os lotes três vezes ao dia melhoraram atenção, humor e estresse; a entrega horária não se distinguiu do controle e o silêncio total aumentou a ansiedade](attachments/notificacoes-batching.svg)

Os resultados têm três partes, e as três importam:

**Lotes três vezes ao dia melhoraram tudo.** Mais atenção, mais concentração, melhor humor, menos estresse, mais sensação de controle sobre o próprio telefone, menos interrupções percebidas. Também menos desbloqueios de tela: cerca de 37 por dia contra 57 no grupo de controle.

**Lotes de hora em hora praticamente não se distinguiram do controle.** Essa é a parte que costuma ser esquecida quando o estudo é citado. Agrupar não é o mecanismo — agrupar em intervalos **largos e previsíveis** é. De hora em hora ainda é frequente o bastante para fragmentar a atenção do mesmo jeito.

**Desligar tudo foi pior que agrupar.** Quem não recebeu notificação nenhuma teve poucos dos benefícios e mais ansiedade e medo de estar perdendo algo. O silêncio total troca interrupção por incerteza, e incerteza também custa.

A leitura de design é específica: o valor não está em receber menos, e sim em **saber quando vai receber**. É a diferença entre um fluxo variável — que a própria pesquisa compara a uma máquina de apostas, pela imprevisibilidade da recompensa — e uma entrega agendada.

Nos termos de McFarlane, isso é a diferença entre interrupção **imediata** e **agendada**. Quase todo produto usa só a primeira.

## O que se perde no curto prazo volta no longo

A objeção previsível a reduzir frequência é que as métricas caem. Ela é verdadeira e incompleta.

O time de dados do Facebook publicou em 2022 o resultado de um experimento de um ano: um grupo recebia todas as notificações consideradas relevantes; o outro, apenas as de relevância máxima. No começo, o grupo que recebia menos visitava menos. Ao longo dos meses, a perda foi se recuperando — e, ao fim do período, havia virado ganho, tanto em satisfação quanto em uso.

A conclusão que eles tiram é metodológica antes de ser sobre notificação: **efeitos de longo prazo podem ser diferentes dos de curto prazo, ou até opostos.** Um teste A/B de duas semanas sobre frequência de notificação mede o custo da mudança e nenhum dos benefícios, porque as pessoas levam tempo para se ajustar — e o dano de longo prazo do excesso (desligar o canal, desinstalar) acontece devagar demais para aparecer na janela do teste.

É um argumento que serve para defender a decisão internamente: quem propõe reduzir frequência precisa negociar a **duração do experimento** antes de negociar o conteúdo dele.

## O orçamento

Da engenharia de alarmes vem a ideia de que existe uma taxa máxima e que ela é um número escrito em algum lugar — na indústria, um alarme a cada dez minutos por operador em regime normal.

Produto nenhum vai adotar esse número. Mas todo produto deveria ter o seu, e ele precisa ter três propriedades:

**Por pessoa, não em média.** Média esconde exatamente as pessoas que estão sendo bombardeadas. O que interessa é o percentil alto: quantas mensagens recebe quem mais recebe.

**Somando todos os canais.** Push, e-mail, SMS, in-app e o sino contam para o mesmo orçamento, porque quem recebe não separa por canal. Um produto que "reduziu o push" e migrou tudo para e-mail não reduziu nada.

**Com dono.** Se nenhuma pessoa é responsável pela soma, cada time otimiza o próprio pedaço e a soma explode. Esse é o mecanismo pelo qual sistemas de notificação apodrecem: ninguém tomou uma decisão ruim; todo mundo tomou uma decisão boa isoladamente.

Para calibrar a ordem de grandeza: uma pesquisa da Telefónica, citada pelo NN/g, encontrou uma média de **56 notificações por dia** por pessoa em 2016, considerando todos os aplicativos. O seu produto está disputando espaço dentro desse total, não dentro de um dia vazio.

## Modos, não interruptores

O padrão que o Vitaly Friedman recomenda, e que aparece em produtos que levam isso a sério, é oferecer **perfis prontos** em vez de uma lista de trinta chaves liga-desliga:

- **Modo calmo** — frequência baixa, só o essencial.
- **Modo regular** — o meio-termo.
- **Modo intenso** — para quem quer tudo.
- **Modo resumo** — tudo agrupado em uma mensagem por dia ou por semana.

A razão para preferir perfis é que uma tela com trinta chaves é, na prática, uma tela que ninguém configura. Ela transfere para a pessoa um trabalho de curadoria que exige entender a taxonomia interna do seu produto — e o resultado costuma ser desligar tudo, que é a única operação que dá para fazer sem entender nada.

Três mecanismos complementam os perfis:

**Começar devagar.** A frequência padrão inicial deve ser baixa e subir conforme o uso real, não o contrário. É muito mais fácil ganhar permissão para mandar mais do que recuperar alguém que já desligou.

**Perguntar no onboarding.** O Basecamp oferece, no cadastro, a escolha entre "Always On" e "Work Can Wait" — notificações a qualquer hora ou apenas em janelas definidas de horário e dia. Perguntar antes de a primeira notificação chegar é mais barato do que consertar depois.

**Adiar e pausar.** Poder silenciar por 24 horas parece contraintuitivo para engajamento, mas é o que evita que um momento ruim vire uma desativação permanente. Uma pausa é reversível; um bloqueio no nível do sistema não é.

Há ainda o movimento que o Slack faz e que quase ninguém copia: **sugerir a redução**. Quando um canal fica muito ativo, o próprio produto recomenda baixar o nível de notificação para só menções diretas. É o sistema admitindo que a configuração padrão parou de servir — em vez de esperar que a pessoa descubra sozinha, geralmente já irritada.

## Agrupar em vez de repetir

Quando o volume de eventos individuais cresce, a saída é consolidar: "47 pessoas reagiram ao seu post" em vez de 47 mensagens. Parece óbvio e quase nunca é implementado desde o começo, porque exige uma camada de agregação que o caminho mais curto — disparar no evento — não tem.

O agrupamento tem uma versão de conteúdo e uma de canal. A de conteúdo junta eventos semelhantes numa mensagem. A de canal sugere a troca: quando a frequência ultrapassa o tolerável em push, oferecer o resumo diário por e-mail. Canais têm urgência percebida diferente — push, in-app e SMS são lidos como intrusivos; e-mail, muito menos. Mover uma mensagem de canal é uma forma de reduzir custo de atenção sem perder a informação.

## Medir o que importa

A métrica óbvia mente. Taxa de abertura mede se a mensagem chamou atenção, não se ela ajudou — e otimizar por ela leva direto a títulos sensacionalistas e frequência crescente, porque é assim que se maximiza abertura no curto prazo. Lee Munroe é direto: taxa de abertura é métrica de vaidade; o que interessa é desfecho.

O conjunto que dá uma leitura honesta:

- **Desfecho**, não abertura: a pessoa fez o que a mensagem existia para provocar?
- **Tempo entre envio e ação.** Uma mensagem aberta três dias depois não precisava ter interrompido ninguém.
- **Taxa de desativação e de desinstalação por tipo de mensagem.** É o custo, e precisa ser atribuído ao gatilho específico que o causou — não ao produto em geral.
- **Bloqueio no nível do sistema.** É o pior desfecho possível e o mais difícil de reverter.
- **Volume por pessoa no percentil alto**, somando canais.

E, sobretudo, medir por tipo. Um sistema de notificação saudável tem tipos com desempenho muito diferente entre si; a média dos tipos não descreve nenhum deles. É a mesma lógica da racionalização de alarmes: a unidade de análise é o gatilho, um por um.

---

**Continua em:** [[Escrever a mensagem]] · [[Acessibilidade de mensagens]]

**Antes:** [[A disciplina perdida do alarme]] · [[Permissão e consentimento]]
