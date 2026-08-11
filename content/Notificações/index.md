---
title: "Notificações"
description: "Índice das anotações sobre sistemas de mensagens e notificação: os cinco artigos e as fontes que sustentam cada um"
tags:
  - tema/ux
  - dominio/notificacoes
  - tipo/indice
---

Esta pasta reúne o que estudei sobre **sistemas de mensagens** — o conjunto de decisões que determina o que um produto diz, quando diz, por qual canal e com quanto direito de interromper alguém.

O ponto de partida é uma constatação incômoda: o problema de decidir o que merece interromper uma pessoa já foi resolvido, com rigor e por escrito, em refinarias, salas de controle nuclear e hospitais. O software não herdou nada disso e vem redescobrindo tudo aos pedaços, geralmente depois de já ter perdido o canal.

## Comece por aqui

**[[A disciplina perdida do alarme]]** — o artigo de fundamento. 275 alarmes em 11 minutos antes da explosão de Milford Haven, os números da EEMUA 191, a fadiga de alarme em hospitais, a tecnologia calma de Weiser e os quatro métodos de interrupção de McFarlane. É de onde saem os critérios que os outros quatro artigos aplicam.

**[[Anatomia de um sistema de mensagens]]** — a taxonomia: indicador, validação e notificação; status contra tipo; a escada de interrupção do indicador ao modal; e o papel da central de notificações.

**[[Permissão e consentimento]]** — o duplo pedido, o que fazer quando a resposta é não, o que muda em iOS, Android e web, por que os números de opt-in discordam entre si, e por que o consentimento precisa ser granular.

**[[Frequência, agrupamento e controle]]** — o experimento de agrupamento de Fitz e colegas, o estudo de um ano do Facebook, o orçamento de atenção, os modos de perfil e o que medir quando taxa de abertura mente.

**[[Escrever a mensagem]]** — o que dizer quando só há um título, os limites reais de caracteres por plataforma, tom por gravidade e o que cortar.

**[[Acessibilidade de mensagens]]** — WCAG 4.1.3, a escolha entre `status`, `alert` e `alertdialog`, as três coisas que fazem um anúncio silenciosamente falhar, e por que o toast é o componente mais problemático dessa família.

## Fontes

Todas verificadas em 11 ago 2026.

### O argumento de fundo

- **[The Lost Discipline of the Alarm: What Notification Design Forgot](https://www.youtube.com/watch?v=Ira28fgSF7M)** · Saleh Kayyali, canal *Interface Studies*, jul 2026 · vídeo, 21 min
  A peça que organiza a tese: notificação é um problema de alarme, e existe uma disciplina inteira sobre isso que o celular nunca encontrou. A bibliografia da descrição do vídeo é o melhor mapa de leitura desse assunto que encontrei — a maior parte das fontes abaixo veio dali e foi lida na origem.

- **[Better Alarm Handling (CHIS6)](https://www.hse.gov.uk/pubns/chis6.pdf)** · Health and Safety Executive (Reino Unido), mar 2000 · PDF, 4 páginas
  A fonte primária de quase todos os números do primeiro artigo: os 275 alarmes em 11 minutos, as metas de taxa (1 a cada 10 minutos em regime normal, no máximo 10 nos 10 minutos após uma perturbação), os três níveis de prioridade com distribuição 5/15/80, e a regra de que indicadores de status não devem ser designados como alarmes. Quatro páginas que valem mais que a maioria dos artigos de UX sobre o tema.

- **[The explosion and fires at the Texaco Refinery, Milford Haven, 24 July 1994](https://www.jesip.org.uk/wp-content/uploads/2022/03/Texaco-Refinery-Explosion.pdf)** · HSE, 1997 · PDF
  O relatório de investigação completo. Denso e majoritariamente sobre engenharia de processo; o CHIS6 acima é o resumo utilizável da parte de fatores humanos.

- **[EEMUA Publication 191 — Alarm Systems: a guide to design, management and procurement](https://www.eemua.org/products/publications/print/eemua-publication-191)** · EEMUA, 1ª ed. 1999, 4ª ed. nov 2024
  O guia de referência da área, com contribuição da HSE. É pago; os números citados aqui vêm do CHIS6, que os reproduz com indicação de página.

- **[Sentinel Event Alert 50: Medical device alarm safety in hospitals](https://www.jointcommission.org/en-us/knowledge-library/newsletters/sentinel-event-alert/issue-50)** · The Joint Commission, abr 2013
  De onde vêm os 98 eventos relacionados a alarme entre 2009 e 2012, dos quais 80 fatais, e a estatística de que 85% a 99% dos sinais de alarme não exigem intervenção clínica. O site bloqueia acesso automatizado; há uma [cópia em PDF do alerta](https://www.kff.org/wp-content/uploads/sites/2/2013/04/sea_50_alarms_4_5_13_final1.pdf) hospedada pela KFF.

- **[FORUM: Why are people turning off our alarms?](https://doi.org/10.1121/1.397232)** · Robert D. Sorkin, *Journal of the Acoustical Society of America* 84, 1988
  Duas páginas cujo título é o argumento. Pago; a formulação do problema circula amplamente na literatura de fatores humanos.

- **[Designing Organizations for an Information-Rich World](https://gwern.net/doc/design/1971-simon.pdf)** · Herbert A. Simon, 1971 · PDF
  A origem da ideia de que uma riqueza de informação cria uma pobreza de atenção — formulada como problema de alocação, não como metáfora.

- **[Designing Calm Technology / The Coming Age of Calm Technology](https://calmtech.com/papers)** · Mark Weiser e John Seely Brown, Xerox PARC, 1995–96
  Centro e periferia da atenção, o *Dangling String* de Natalie Jeremijenko, a ideia de que informar não precisa exigir. É a resposta de design ao problema que Simon nomeou.

- **[Coordinating the Interruption of People in Human-Computer Interaction](https://www.interruptions.net/literature/McFarlane-Interact99-Coordinating.pdf)** · Daniel C. McFarlane, INTERACT '99 · PDF (digitalizado)
  Os quatro métodos: imediato, negociado, mediado e agendado. A versão com os resultados experimentais completos é [Comparison of Four Primary Methods…](https://www.interruptions.net/literature/McFarlane-HCI02_2.pdf), em *Human-Computer Interaction* 17, 2002.

- **[Principles of Mixed-Initiative User Interfaces](http://erichorvitz.com/chi99horvitz.pdf)** · Eric Horvitz, CHI '99 · PDF
  Doze princípios para sistemas que tomam iniciativa. O que interessa aqui: uma ação autônoma — inclusive interromper — só se justifica quando o valor esperado supera o de não fazer nada.

- **[The Cost of Interrupted Work: More Speed and Stress](https://ics.uci.edu/~gmark/chi08-mark.pdf)** · Gloria Mark, Daniela Gudith e Ulrich Klocke, CHI '08 · PDF
  Achado contraintuitivo: pessoas interrompidas terminaram as tarefas **mais rápido**, sem perda de qualidade — compensando com mais estresse, frustração, pressão de tempo e esforço. Nota de cautela: o número dos "23 minutos e 15 segundos para retomar", quase sempre atribuído a este artigo, **não está nele**; ele vem de uma entrevista da autora à Gallup em 2006 e nunca foi publicado como achado formal. Vale evitar.

### Design de notificação em produto

- **[Design Guidelines For Better Notifications UX](https://www.smashingmagazine.com/2025/07/design-guidelines-better-notifications-ux/)** · Vitaly Friedman, Smashing Magazine, jul 2025
  O guia prático mais atual: classificação por canal e por nível de atenção exigida, perfis de modo (calmo, regular, intenso, resumo), sugerir troca de canal, começar com frequência baixa. É de onde vêm os exemplos de Slack e Basecamp.

- **[Privacy UX: Better Notifications UX and Permission Requests](https://www.smashingmagazine.com/2019/04/privacy-better-notifications-ux-permission-requests/)** · Vitaly Friedman, Smashing Magazine, abr 2019
  O padrão do duplo pedido, os cinco tipos de gatilho de notificação, o agrupamento gradual e a lista de métricas a acompanhar. Anterior ao artigo de 2025 e mais detalhado na parte de permissão.

- **[Privacy UX: Privacy-Aware Design Framework](https://www.smashingmagazine.com/2019/04/privacy-ux-aware-design-framework/)** · Vitaly Friedman, Smashing Magazine, abr 2019
  Fecha a série de quatro partes. Os seis princípios de consentimento (ativo, granular, retirável, transparente, separado dos termos, com benefício explicado) e a coleta *just in time*. É o enquadramento que impede tratar o aceite de notificação como um sim genérico.

- **[Privacy UX: Better Cookie Consent Experiences](https://www.smashingmagazine.com/2019/04/privacy-ux-better-cookie-consent-experiences/)** · Vitaly Friedman, Smashing Magazine, abr 2019
  Sobre consentimento de cookies, não sobre notificação — mas é o mesmo problema de permissão pedida no pior momento possível, e os padrões escuros catalogados ali reaparecem inteiros nos pedidos de push.

- **[The Ultimate Guide to Push Notifications for Developers](https://www.smashingmagazine.com/2022/04/guide-push-notifications-developers/)** · Lee Munroe (OneSignal), Smashing Magazine, abr 2022
  O lado técnico: anatomia do push por plataforma com limites de caracteres e número de ações, matriz de suporte, o que medir. Escrito por alguém que trabalha em um fornecedor de push — ler os números de opt-in com essa ressalva. A parte de anatomia e limites é a mais útil e a menos sujeita a viés.

- **[Indicators, Validations, and Notifications: Pick the Correct Communication Option](https://www.nngroup.com/articles/indicators-validations-notifications/)** · Kim Flaherty, Nielsen Norman Group, atualizado jan 2024
  A separação entre os três mecanismos, com os critérios de escolha. É a distinção mais útil de todo este índice para o trabalho do dia a dia.

- **[Five Mistakes in Designing Mobile Push Notifications](https://www.nngroup.com/articles/push-notification/)** · Alita Kendrick, Nielsen Norman Group, nov 2018
  Pedir cedo demais, não dizer sobre o que é, mandar em rajadas, mandar irrelevante, dificultar o desligamento. Traz a estatística da Telefónica de 56 notificações por dia por pessoa em 2016.

- **[Notification pattern](https://carbondesignsystem.com/patterns/notification-pattern/)** · Carbon Design System (IBM)
  A referência de design system mais completa e específica: status contra tipo, os sete tipos com regra de duração e interação, boas práticas por componente, e uma seção de acessibilidade curta e correta. É de onde vem a regra de que toast com ação precisa persistir.

- **[Notifications: why less is more](https://medium.com/@AnalyticsAtMeta/notifications-why-less-is-more-how-facebook-has-been-increasing-both-user-satisfaction-and-app-9463f7325e7d)** · Time de análise do Facebook/Meta, dez 2022
  O experimento de um ano com notificações reduzidas: perda inicial de visitas que se recupera e vira ganho. O argumento central é metodológico — efeitos de longo prazo podem ser opostos aos de curto prazo.

- **[Batching smartphone notifications can improve well-being](https://static1.squarespace.com/static/57a40c19414fb54f51f8095f/t/614a55faa7b89e25f4e48ad1/1632261627146/2019+Fitz+Batching.pdf)** · Nicholas Fitz, Kostadin Kushlev e colegas, *Computers in Human Behavior*, 2019 · PDF
  Experimento randomizado de campo, n = 237, quatro condições. O achado que quase nunca é citado junto: agrupar de hora em hora **não** funcionou. Só o intervalo largo e previsível (três vezes ao dia) produziu efeito. Amostra recrutada via MTurk na Índia — vale considerar antes de generalizar.

- **[Push Notifications Statistics](https://www.businessofapps.com/marketplace/push-notifications/research/push-notifications-statistics/)** · Business of Apps
  Compilado de benchmarks de vários fornecedores. Útil para ordem de grandeza e nada além disso: as fontes discordam entre si para o mesmo ano e plataforma, porque cada uma mede a própria base com definições diferentes de opt-in.

### Plataforma e implementação

- **[Introducing quieter permission UI for notifications](https://blog.chromium.org/2020/01/introducing-quieter-permission-ui-for.html)** · Chromium Blog, jan 2020
  A intervenção do navegador no próprio mecanismo de pedido, e a lista dos padrões considerados abusivos: disfarçar o pedido, condicionar conteúdo ao aceite, contornar a prevenção.

- **[Adding notification permission data to the Chrome UX Report](https://developer.chrome.com/blog/notification-permission-data-in-crux)** · Chrome for Developers
  As quatro respostas possíveis a um pedido (aceitar, bloquear, dispensar, ignorar) e por que bloqueio e aceite são as únicas duas métricas que importam.

- **[Create and manage notification channels](https://developer.android.com/develop/ui/views/notifications/channels)** · Android Developers
  Canais, os cinco níveis de importância e o detalhe decisivo: depois de criado, o app não pode aumentar a importância de um canal — só a pessoa pode.

- **[Managing notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)** · Apple Human Interface Guidelines
  Autorização provisória, entrega discreta, níveis de interrupção e modos de foco.

### Acessibilidade

- **[Understanding SC 4.1.3: Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)** · W3C / WAI
  O critério, o que conta como mensagem de status, o que não conta, e a falha F103.

- **[ARIA Authoring Practices Guide — Alert Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alert/)** · W3C / WAI
  `role="alert"` não deve afetar o foco; se for preciso interromper o fluxo, o componente é `alertdialog`. E a recomendação explícita de evitar alertas que somem sozinhos.

- **[ARIA live regions](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)** · MDN
  `polite` contra `assertive`, `aria-atomic`, `aria-relevant`, a tabela de papéis com região viva implícita, e a regra que resolve a maior parte dos bugs: a região precisa existir no DOM antes de o conteúdo ser injetado.

## Relacionados

[[Glossário/Componentes/messaging|Messaging (Glossário)]] · [[Glossário/Componentes/toast|Toast]] · [[Acessibilidade/index|Acessibilidade]] · [[Conteúdo]]

---
