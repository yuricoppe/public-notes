---
title: "A disciplina perdida do alarme"
description: "Refinarias, salas de controle nuclear e UTIs resolveram o problema de decidir o que merece interromper alguém. O celular não herdou nada disso."
tags:
  - tema/ux
  - dominio/notificacoes
  - tipo/artigo
---

Em 24 de julho de 1994, a refinaria da Texaco em Milford Haven, no País de Gales, explodiu. Vinte e seis pessoas ficaram feridas e o prejuízo material passou de £48 milhões. A investigação da Health and Safety Executive britânica apontou três fatores, e o primeiro deles não foi uma válvula, um sensor ou um erro de cálculo:

![Comparação entre os 275 alarmes recebidos por dois operadores nos 11 minutos antes da explosão de Milford Haven e o teto de 10 alarmes recomendado pela EEMUA para os primeiros 10 minutos depois de uma perturbação](attachments/notificacoes-milford-haven.svg)

Nos onze minutos anteriores à explosão, dois operadores tiveram que reconhecer, confirmar e agir sobre **275 alarmes**. Cerca de vinte e cinco por minuto. O sistema não escondeu nada: entregou tudo, ao mesmo tempo, com a mesma insistência, sem dizer o que importava.

O relatório da HSE resume o diagnóstico numa frase que qualquer pessoa que já desenhou um sistema de notificação deveria conseguir repetir de cor: *havia alarmes demais e eles estavam mal priorizados*. Os outros dois fatores foram displays que não ajudavam os operadores a entender o que estava acontecendo, e treinamento insuficiente para lidar com uma perturbação prolongada.

## A disciplina que veio depois

O acidente não foi o primeiro sinal, mas foi o que consolidou uma área inteira de engenharia. Cinco anos depois, a EEMUA publicou a primeira edição do guia 191, *Alarm Systems*, com contribuição da própria HSE. Ele virou a referência de fato, e mais tarde ganhou equivalentes formais em ISA-18.2 e IEC 62682.

O que esses documentos contêm não é teoria. São números, e números incômodos:

- Em operação normal, a taxa média de alarmes não deve passar de **um a cada dez minutos por operador**.
- Depois de uma perturbação grave, **no máximo dez alarmes** nos primeiros dez minutos.
- Use cerca de **três níveis de prioridade** — nem mais, nem menos.
- Distribua as prioridades de forma desigual e deliberada: mais ou menos **5% alta, 15% média e 80% baixa**.

![Pirâmide de prioridade recomendada pela EEMUA: 5% alta, 15% média, 80% baixa, com a definição de cada nível pela consequência de não haver resposta](attachments/notificacoes-piramide-prioridade.svg)

Essa última é a que mais dói de traduzir para produto. Ela diz que a prioridade é um **orçamento fixo**, não um adjetivo que cada time atribui à própria feature. Se tudo é alto, a categoria "alto" deixou de existir. E o critério para alocar esse orçamento é explícito no guia: a prioridade deriva **da consequência de o operador não responder** — não da importância que quem construiu o alarme atribui a ele.

Há também uma regra de fronteira, escrita em uma linha, que resolveria metade das discussões de design de notificação se fosse levada a sério: *indicadores de status do processo não devem ser designados como alarmes*. Uma coisa mostra estado. Outra pede resposta. São objetos diferentes.

E há a definição do que um alarme serve para fazer. Segundo a EEMUA, um sistema de alarme deve "direcionar a atenção do operador para condições da planta que exigem avaliação ou ação em tempo hábil". Ou seja: se não há avaliação nem ação a fazer, não é alarme. É informação, e informação tem outros lugares para morar.

## O vocabulário do fracasso

A parte mais útil de emprestar dessa disciplina talvez não sejam os números, e sim os nomes. Quando um problema tem nome, ele pode ser medido, discutido em reunião e colocado em um relatório. A maior parte dos times de produto discute notificação sem vocabulário nenhum, e por isso a conversa termina sempre no mesmo lugar — "está muito, né?" — sem que ninguém consiga dizer o quanto é muito.

**Enxurrada de alarmes** (*alarm flood*) é a chegada de mais alarmes do que uma pessoa consegue processar num intervalo — na convenção da área, mais de dez em dez minutos. Milford Haven foi uma enxurrada.

**Alarme permanente** (*standing alarm*) é o que está ativo há horas ou dias e ninguém mais enxerga. Vira parte da paisagem. O equivalente em produto é o badge vermelho que nunca zera.

**Alarme incômodo** (*nuisance alarm*) é o que dispara sem que haja nada a fazer: ruído de sensor, limiar mal ajustado, evento repetido. Detecta-se pelo comportamento das pessoas — muitos alarmes reconhecidos em sequência rápida, ou o som desligado com frequência.

**Racionalização** é o processo de revisar cada alarme existente, um por um, e decidir se ele fica, muda de prioridade ou morre. A HSE dá o dado de custo com uma franqueza rara: uma primeira passada rápida cobre talvez 50 alarmes por turno, mas uma revisão séria pode levar **mais de um turno por alarme**. Ninguém faz isso por acidente. É projeto, com dono e cronograma.

## Não foi um caso isolado

Quinze anos antes de Milford Haven, em 1979, a sala de controle de Three Mile Island viveu a mesma coisa. Centenas de luzes acenderam ao mesmo tempo, acompanhadas de sirenes. Um operador descreveu o painel como uma árvore de Natal. Outro disse à Comissão Kemeny que os alarmes estavam disparando, mas não davam nenhuma informação útil. O painel agrupava alarmes demais e tinha um botão de reconhecimento que silenciava todos de uma vez — o que resolve o barulho e destrói a informação.

E o problema não ficou na indústria pesada. Ele reapareceu, com outro nome, no lugar mais sensível possível.

Em abril de 2013, a Joint Commission emitiu o Sentinel Event Alert nº 50 sobre segurança de alarmes de dispositivos médicos em hospitais. O documento reporta 98 eventos relacionados a alarme no banco de dados da organização entre janeiro de 2009 e junho de 2012. Desses, **80 resultaram em morte**, 13 em perda permanente de função e 5 em cuidado adicional ou internação prolongada. O fator contribuinte mais comum era a **fadiga de alarme**.

O número que sustenta essa fadiga é o mais eloquente de toda esta página: entre **85% e 99%** dos sinais de alarme em ambiente hospitalar **não exigem intervenção clínica**. Não é que os profissionais sejam desatentos. É que a taxa de acerto do sistema é tão baixa que ignorar virou a estratégia racional. Quando quase todo alarme é falso, prestar atenção em todos é que seria o comportamento errado.

Robert Sorkin publicou em 1988, no *Journal of the Acoustical Society of America*, um texto curto cujo título já é o argumento inteiro: *Why are people turning off our alarms?* A resposta, resumida, é que as pessoas desligam alarmes quando desligá-los passa a ser mais adaptativo do que atendê-los.

Isto é o ponto que atravessa todos os casos: **a desativação não é indisciplina do usuário, é uma resposta correta a um sistema que perdeu credibilidade**. Quando alguém desliga as notificações do seu produto, o dado que você tem em mãos não é sobre a pessoa. É sobre a taxa de acerto do que você mandou.

## O computador sabia disso também

A parte estranha da história é que a computação chegou a conclusões parecidas, mais ou menos na mesma época, e também não usou.

Em 1971, Herbert Simon escreveu a frase que virou o resumo de tudo: uma riqueza de informação cria uma pobreza de atenção. Não como metáfora — como problema de alocação. Informação consome atenção; portanto, projetar sistemas de informação é, necessariamente, projetar como a atenção será gasta.

Nos anos 1990, o Xerox PARC formulou a resposta de design. Mark Weiser e John Seely Brown propuseram a **tecnologia calma**: uma tecnologia que se move entre o *centro* e a *periferia* da atenção, em vez de morar sempre no centro. A periferia, na definição deles, é aquilo a que estamos sintonizados sem prestar atenção explícita — o ruído do motor enquanto se dirige, que só vem para o centro quando muda. O exemplo canônico é o *Dangling String* de Natalie Jeremijenko: um cordão preso a um motor, ligado à rede do prédio, que se agita conforme o tráfego. Ninguém precisa lê-lo. Ele informa sem exigir nada.

O contraste com o que temos é direto: quase todo componente de notificação de produto é projetado para ir ao centro. Não há periferia no celular. O que existe é uma fila única, e tudo nela grita no mesmo tom.

Em 1999, Daniel McFarlane comparou empiricamente quatro maneiras de coordenar a interrupção de alguém.

![Os quatro métodos de coordenar interrupções de McFarlane: imediato, negociado, mediado e agendado, com quem decide a hora em cada um](attachments/notificacoes-quatro-metodos.svg)

Nenhum dos quatro venceu em todas as medidas — esse é o achado honesto. Mas o **negociado**, em que a pessoa é avisada de que há algo e escolhe quando atender, teve o melhor desempenho geral, com uma ressalva importante: as pessoas adiam. Às vezes indefinidamente.

No mesmo ano, Eric Horvitz publicou os princípios de interfaces de iniciativa mista, cujo núcleo é uma conta que quase nenhum produto faz: uma ação autônoma — inclusive interromper — só se justifica quando seu valor esperado supera o de não fazer nada. Interromper tem custo. O custo entra na conta antes, não depois de alguém reclamar.

## O que o celular fez com tudo isso

Nada.

O telefone construiu **um canal**, chamou tudo o que passa por ele de alarme e deixou a pessoa resolver o ruído por conta própria. Uma mensagem da mãe e uma promoção de cupom chegam pelo mesmo caminho, com o mesmo peso visual, o mesmo som, a mesma vibração. A hierarquia que a engenharia de alarmes levou décadas para formalizar foi substituída por um interruptor binário por aplicativo: tudo ou nada.

O que o sistema operacional oferece de controle é real mas insuficiente. Os canais de notificação do Android, obrigatórios desde a versão 8, foram um avanço genuíno: cada tipo de notificação é declarado separadamente e a pessoa ajusta som, vibração e visibilidade por tipo — e, uma vez criado, o app não pode aumentar a importância de um canal, só a pessoa pode. Do lado do iOS existem autorização provisória, entrega discreta e os modos de foco. Mas tudo isso é infraestrutura de contenção construída depois do fato, para conter uma decisão de arquitetura que já estava tomada.

O resultado é o previsível, e a pesquisa de fadiga de alarme prevê exatamente: as pessoas desligam. Não por tipo, porque o produto raramente separa por tipo. Desligam o app inteiro.

## Como isso vira trabalho de design

A tradução não é literal. Nenhum produto tem 275 gatilhos disparando em onze minutos, e a consequência de errar não é uma explosão. Mas quatro coisas passam inteiras:

**Prioridade é orçamento.** Se o seu produto tem três níveis de urgência e o nível mais alto contém mais de 5% dos gatilhos, você não tem três níveis. Tem um, com decoração.

**A prioridade vem da consequência de ninguém responder.** Não do quanto o time quer que a mensagem seja vista, não da meta trimestral da feature, não de quem foi mais insistente na reunião de planejamento.

**Existe uma taxa máxima, e ela é mais baixa do que parece.** A engenharia de alarmes fala em um a cada dez minutos por pessoa. Um produto pode discutir qual é o seu número, mas precisa ter um — e precisa medi-lo por pessoa, não em média, porque a média esconde exatamente as pessoas que estão sendo bombardeadas.

**Se não há resposta definida, não é notificação.** É indicador. A regra da HSE sobre não designar indicadores de status como alarmes é a mesma coisa que a separação entre indicador, validação e notificação que o Nielsen Norman Group descreve — só que escrita quinze anos antes, e com consequência legal.

![As quatro perguntas do inventário de racionalização: existe resposta definida, quem é a pessoa certa, qual a consequência de ignorar, e em quanto tempo precisa chegar](attachments/notificacoes-racionalizacao.svg)

O exercício prático que sai de tudo isso é o inventário. Listar todos os gatilhos que o produto já tem — todos, incluindo os que ninguém lembra de ter criado — e passar cada um pelas quatro perguntas. Não é uma sessão de design. É uma planilha, e a primeira rodada costuma cortar mais do que ajustar.

## Quem é o operador

Vale uma diferença que não dá para ignorar. Na refinaria, o operador é treinado, pago para estar ali e tem um procedimento escrito para cada alarme. Nada disso vale para quem usa um aplicativo. A pessoa não foi treinada, não tem procedimento e não deve nada ao seu produto.

Isso torna o problema mais difícil, não mais fácil. O operador da sala de controle não pode desligar o painel. Sua usuária pode — e, se você errar a taxa, ela vai.

Há ainda uma assimetria que a analogia esconde e que convém dizer com todas as letras: na planta industrial, quem projeta o alarme e quem sofre com o excesso trabalham para o mesmo objetivo. Em produto, muitas vezes não. A pessoa que decide mandar a notificação é remunerada pelo engajamento que ela gera; quem recebe paga o custo de atenção. A engenharia de alarmes nunca precisou resolver esse conflito de incentivo, porque ele não existia lá. É o pedaço do problema para o qual não há norma técnica — e o único que depende inteiramente de quem está desenhando.

---

**Continua em:** [[Anatomia de um sistema de mensagens]] · [[Frequência, agrupamento e controle]]

**Fontes** — todas verificadas em 11 ago 2026, listadas com detalhe em [[Notificações/index|Notificações]].
