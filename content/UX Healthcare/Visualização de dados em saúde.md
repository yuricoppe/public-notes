---
title: "Visualização de dados em saúde"
description: "O que muda quando o gráfico é de exame, prontuário ou rede de atendimento — com o caso do painel do SAMU e a pesquisa sobre resultados de exame para pacientes"
tags:
  - tema/dataviz
  - dominio/saude
  - tipo/artigo
---

As regras gerais de [[DataViz/index|visualização de dados]] valem aqui: a hierarquia perceptual, a paleta segura para daltonismo, o eixo que não mente. Este artigo é sobre o que **não** é transferível — e sobre por que os erros custam diferente.

A diferença de fundo é essa. Em produto comum, ler um gráfico errado significa uma decisão de negócio pior. Em saúde, significa alguém que não procurou atendimento quando devia, alguém que procurou sem precisar e ocupou uma vaga, ou uma ambulância parada onde não deveria estar.

## Quatro públicos, quatro problemas

![Os quatro públicos da visualização de dados em saúde: paciente, clínico, gestor e cidadão, com o que cada um precisa decidir, o tempo que tem e o erro típico](attachments/saude-dataviz-quatro-publicos.svg)

"Dataviz em saúde" não é uma disciplina só, e o que serve a um destes públicos costuma atrapalhar outro. Vale separar antes de qualquer decisão de desenho.

## O paciente: o número que não diz nada

O caso mais estudado é o resultado de exame em portal do paciente — e é onde a evidência é mais rica e mais contraditória.

![Três formas de apresentar um resultado de exame: só o número, barra com faixa de referência, e barra com âncora de dano e conclusão escrita](attachments/saude-dataviz-resultado-exame.svg)

A revisão sistemática de van der Mee e colegas, publicada no *JMIR* em 2024, reuniu 18 estudos sobre formatos de apresentação. O achado principal: **barras horizontais com blocos coloridos** venceram consistentemente — melhor compreensão de "estou dentro ou fora", maior satisfação e usabilidade. Número com faixa de referência, sozinho, não basta.

O resultado mais acionável dessa revisão é sobre as **âncoras de dano**: linhas de limiar rotuladas com o que fazer ("acima de 2,0, procure atendimento"). Formatos com essas âncoras reduziram substancialmente o contato desnecessário com o médico — ou seja, o desenho da tela mexeu na demanda do serviço.

Duas outras recomendações que saem dali: **faixas personalizadas** em vez da referência genérica, porque a faixa que importa para alguém com diabetes não é a da população geral; e **linguagem leiga** com um rótulo avaliativo, não só a cor.

### E a ressalva que precisa vir junto

Um estudo anterior, de Fraccaro e colegas, complica o quadro. Eles testaram três interfaces com 20 pacientes transplantados renais, usando rastreamento ocular, em cenários de risco baixo, médio e alto. O resultado: **nenhuma diferença significativa** de acerto entre as três — 55% para a versão contextualizada, 52% para a de base, 45% para a agrupada. Os pacientes subestimavam a necessidade de agir mesmo quando os valores anormais estavam destacados ou agrupados. E erravam mais no cenário de risco **médio**, confundindo-o com o baixo.

O rastreamento ocular trouxe o dado mais interessante: quem acertava tinha **menos fixações** (mediana de 11 contra 32) e menos tempo em cada área. Não era quem olhava mais — era quem sabia onde olhar.

A conclusão dos autores é que apresentação, isoladamente, pode não bastar; e que faz falta a pessoa saber **quais exames importam para a condição dela**.

Juntando as duas fontes, a leitura razoável é: formato resolve "estou dentro ou fora"; não resolve "isso é urgente para mim". A segunda pergunta precisa de conteúdo — a âncora de dano, a frase de conclusão, o próximo passo — e não de um gráfico melhor.

### Evaluability

Brian Zikmund-Fisher dá nome ao problema de fundo: **avaliabilidade**. Um número só é útil quando quem lê consegue julgar se ele é bom ou ruim. "Creatinina 1,4" não tem avaliabilidade nenhuma para a maior parte das pessoas; "pouco acima do normal, sem urgência" tem.

O projeto **Visualizing Health**, da Robert Wood Johnson Foundation com a Universidade de Michigan, é a materialização disso: uma galeria de gráficos de risco **testados com pessoas**, cobrindo 16 cenários comuns de comunicação de risco, sob licença Creative Commons, com um gerador de *icon array* junto. É o recurso mais diretamente reaproveitável de toda esta área.

### Risco e probabilidade

Quando o dado é uma probabilidade, o problema deixa de ser gráfico e vira numeracia. O trabalho de Gerd Gigerenzer sobre **frequências naturais** é a referência: "80 em cada 100 pessoas infectadas recebem resultado positivo" é compreendido onde "80% das pessoas infectadas" não é. E *icon arrays* — a grade de cem bonequinhos com uma parte destacada — funcionam porque representam a mesma frequência de forma concreta e contável.

Isso conversa direto com o que a fundamentação de pesquisa do GOV.UK registra sobre números: porcentagens e probabilidades são especialmente difíceis para quem tem baixa numeracia, e "7 em cada 10" comunica melhor que "70%". Em saúde, essa diferença muda decisão de tratamento.

## O clínico: o problema é o excesso

Do outro lado do balcão, o problema se inverte. O clínico não sofre de falta de dado — sofre de excesso, e tem segundos entre um paciente e o próximo.

Aqui a recomendação do Nielsen Norman Group sobre painéis vale ao pé da letra, e por um motivo específico: **comprimento e posição são processados pré-atentivamente**, área não. Num contexto em que a leitura acontece em segundos, essa diferença deixa de ser refinamento e vira requisito. Pizza, rosca, treemap e qualquer coisa em 3D estão fora.

Vale também saber o estado da arte, que é modesto. A análise de painéis de segurança do paciente publicada no *JAMIA Open* em 2021 encontrou variação enorme entre painéis hospitalares e — o ponto que importa — **ausência de evidência** sobre quais abordagens de desenho produzem melhores desfechos. Ou seja: nessa faixa, não há literatura para copiar. Há que testar.

Uma ponte com outro assunto destas anotações: o excesso de sinal em ambiente clínico já foi medido, e o resultado é a **fadiga de alarme** — entre 85% e 99% dos alarmes hospitalares não exigem intervenção. Painel clínico ruim é a versão visual do mesmo problema, e a saída é a mesma: menos coisas, priorizadas por consequência. Está em [[Notificações/A disciplina perdida do alarme|A disciplina perdida do alarme]].

## O gestor: o caso do SAMU

O melhor material em português sobre isto é um artigo dos anais do 10º CIDI, de 2021, sobre o painel de gestão federal do SAMU. Ele descreve um protótipo real, com método declarado e limitações admitidas — o que é raro.

![Os quatro níveis de organização da informação do painel do SAMU e as três decisões de design que sustentam a navegação](attachments/saude-dataviz-samu.svg)

O contexto: o projeto **Infovis para a Saúde Pública** rodou em 2020, financiado pela OPAS, executado pela FUSP em parceria com o Ministério da Saúde, com o objetivo de melhorar a Sala de Apoio à Gestão Estratégica. A equipe misturava designers de informação, cientistas de dados, pesquisadores de saúde pública e gestores.

O método vale registrar pela franqueza da escala: um *sprint* de três semanas, inteiramente remoto — uma semana de ideação com *brainsketching* em quadro digital e reuniões diárias com gestores do SAMU, uma semana de protótipo de alta fidelidade, uma semana de protótipo funcional em HTML, CSS e JS com integração de dados em JSON. Os requisitos vieram de "centenas de desejos" levantados em entrevistas semiestruturadas e convertidos em histórias de usuário.

Três decisões de desenho são transferíveis para fora da saúde:

**Pictograma como codificação de dado categórico.** O tipo de unidade móvel — suporte básico, suporte avançado, moto, lancha, aeronave — vem do CNES e é categórico puro. Virou um sistema de pictogramas usado no mapa, no tooltip, na tabela, no card e no modal, **sem mudar de sentido entre componentes**. É a mesma disciplina de um design system aplicada à camada de dado.

**Mapa de três camadas, com uma ausência assumida.** O mapa sobrepõe coroplético (município coberto ou não), símbolos (centrais e bases) e linhas ligando cada base à sua central. E aqui está a decisão mais honesta do artigo: como **não existe dado de tempo de deslocamento**, eles desenharam as linhas sobre a malha viária, para que o gestor que conhece o território faça a inferência. Em vez de inventar um número ou omitir a relação, expuseram a limitação de forma utilizável.

**Cor como estado, com regra de degradação.** O fundo do card indica risco de desabilitação da unidade — ativa, dois meses sem atendimento, quatro meses. E, acima de quatro unidades numa base, os cards **viram tabela**. É exatamente a distinção entre olhar um item e comparar vários, resolvida como regra de componente.

Os autores classificam o painel pelo vocabulário de Sarikaya e colegas: público **organizacional**, propósito **operacional**. A utilidade dessa classificação é negativa — ela diz o que o painel *não* precisa ser. Não é painel de imprensa, não é painel de cidadão, e as decisões refletem isso.

Duas limitações que eles próprios registram e que valem mais que muitos acertos: a série temporal de atendimentos é complicada pela **atualização trimestral** dos dados, e o painel se beneficiaria de georreferenciamento dos veículos, que não existia.

## O cidadão: a pandemia como aula

Os painéis de COVID-19 foram o maior experimento público de visualização de dados de saúde da história — o da Johns Hopkins sozinho passou de 3,6 bilhões de visualizações de página em trinta meses. E deixaram duas lições.

A primeira é sobre **incerteza**. Uma revisão de 2026 na *Frontiers in Digital Health* aponta que os painéis de pandemia praticamente não exibiram incerteza: nem intervalo de confiança, nem margem de erro, nem descrição textual da dúvida. Números de contagem foram apresentados como fatos exatos quando eram estimativas com atraso de notificação, subnotificação e revisão retroativa.

A segunda é sobre **acessibilidade**, e está em [[DataViz/Acessibilidade em dataviz|Acessibilidade em dataviz]]: as auditorias de painéis eleitorais de Sarah Fossheim encontraram os mesmos defeitos que os painéis de saúde pública repetem — dado só na cor, tooltip só no mouse, SVG sem descrição, cabeçalho fixo que come a tela no zoom.

Amanda Makulec escreveu em março de 2020 o texto que resume a responsabilidade envolvida, e o argumento central dele é que visualização em epidemia tem tanto potencial de gerar pânico quanto de informar. As recomendações práticas que sobrevivem: não publique contagem bruta sem denominador, não faça previsão sem competência epidemiológica, e diga de onde vêm os dados e quando foram atualizados.

## O que atravessa os quatro

**Diga a conclusão em texto.** Vale para exame, para painel clínico, para painel de gestão e para gráfico de imprensa. É a camada mais barata e a que mais gente alcança.

**Mostre a incerteza, ou diga que ela existe.** Dado de saúde quase nunca é exato: tem atraso, subnotificação e revisão. Apresentar como número cravado é uma afirmação falsa sobre o mundo.

**Classifique o público e o propósito antes de desenhar.** É a lição transferível do artigo do SAMU: saber que o painel é operacional e organizacional elimina metade das discussões.

**Trate acessibilidade como requisito clínico, não como conformidade.** Uma parte considerável das pessoas que mais precisam ler dado de saúde tem exatamente as condições que a acessibilidade endereça — baixa visão, baixa numeracia, idade avançada, cansaço, ansiedade.

---

**Ver também:** [[DataViz/index|DataViz]] · [[DataViz/Acessibilidade em dataviz|Acessibilidade em dataviz]] · [[UX Healthcare/index|UX Healthcare]] · [[Notificações/A disciplina perdida do alarme|A disciplina perdida do alarme]]

## Fontes

Verificadas em 11 ago 2026.

- **[Enhancing Patient Understanding of Laboratory Test Results: Systematic Review of Presentation Formats](https://pmc.ncbi.nlm.nih.gov/articles/PMC11347896/)** · van der Mee, Schaper, Jansen, Bons, Meex e Cals · *JMIR*, ago 2024 — 18 estudos; barras horizontais com blocos coloridos, faixas personalizadas e âncoras de dano.
- **[Presentation of laboratory test results in patient portals: influence of interface design on risk interpretation and visual search behaviour](https://pmc.ncbi.nlm.nih.gov/articles/PMC5809992/)** · Fraccaro et al. · *BMC Medical Informatics and Decision Making*, 2018 — rastreamento ocular, 20 pacientes; a ressalva indispensável à revisão acima.
- **[Patient Challenges and Needs in Comprehending Laboratory Test Results](https://www.jmir.org/2020/12/e18725/)** · *JMIR*, dez 2020 — separa necessidade genérica de contextual.
- **[Visualizing Health](http://www.vizhealth.org/)** · RWJF e Universidade de Michigan — galeria de gráficos de risco testados, 16 cenários, licença Creative Commons, gerador de icon array.
- **[Helping People Know Whether Measurements Have Good or Bad Implications](https://journals.sagepub.com/doi/10.1177/2372732218813377)** · Brian Zikmund-Fisher, 2019 — o conceito de avaliabilidade.
- **[What are natural frequencies?](http://library.mpib-berlin.mpg.de/ft/gg/gg_what_2011.pdf)** · Gerd Gigerenzer, *BMJ*, 2011 — por que "80 em 100" funciona onde "80%" falha.
- **Painel de visualização de dados para gestão federal do SAMU** · Velloso, Filgueiras, Carvalho e outros · [Anais do 10º CIDI](https://www.proceedings.blucher.com.br/article-details/painel-de-visualizao-de-dados-para-gesto-federal-do-servio-de-atendimento-mvel-de-urgncia-samu-36512), SBDI, Curitiba, 2021 — o caso brasileiro, com método e limitações declarados. O site bloqueia acesso automatizado; abre no navegador.
- **[Analysis of the structure and content of dashboards used to monitor patient safety in the inpatient setting](https://academic.oup.com/jamiaopen/article/4/4/ooab096/6429836)** · *JAMIA Open*, 2021 — a variação entre painéis hospitalares e a falta de evidência sobre desfechos.
- **[Uncertainty displays in pandemic dashboards: a review of COVID-19 use cases](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1869108/full)** · *Frontiers in Digital Health*, 2026.
- **[Ten Considerations Before You Create Another Chart About COVID-19](https://www.tableau.com/about/blog/2020/3/ten-considerations-you-create-another-chart-about-covid-19)** · Amanda Makulec, 2020.
- **What Do We Talk About When We Talk About Dashboards?** · Sarikaya, Correll, Bartram, Tory e Fisher · *IEEE TVCG*, 2019 — o vocabulário de público e propósito que o artigo do SAMU usa.

### Vídeo

- **[Designing Safe Visualization for Patient Data](https://youtu.be/I8dyNIZbis8)** · Jody Butts · UX Healthcare Frankfurt, 2020 · 39 min — o mais direto ao tema.
- **[Visualizing Health Data Responsibly](https://youtu.be/OFRmyk4Uong)** · Data Visualization Society, abr 2020 · 61 min — mesa com quatro especialistas, mediada por Amanda Makulec.
- **[Design That Speaks: using graphics to make health information clear](https://youtu.be/0QKAZ27cAG8)** · Utah Health Literacy Coalition, abr 2026 · 53 min — foco em letramento em saúde.
- **[Amanda Makulec on Visualizing COVID-19 Data Responsibly](https://youtu.be/Qsb69m-_D3A)** · Ann K. Emery, mai 2020 · 14 min.
- **[Webinar: Visualizing Health Care Data](https://youtu.be/EM2OQI3M8io)** · USC Center for Health Journalism · 59 min.
- **[Optimizing the Presentation and Visualization of Health Data for Patients and Providers](https://digital.ahrq.gov/national-webinars/optimizing-presentation-and-visualization-health-data-patients-and)** · AHRQ, 2017, com Zikmund-Fisher — ⚠️ só slides e Q&A em PDF; não há vídeo publicado.
