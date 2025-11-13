# Hierarchical Task Analysis (HTA) Diagram (Diagrama de Análise Hierárquica de Tarefas)

Um **Hierarchical Task Analysis (HTA) Diagram (Diagrama de Análise Hierárquica de Tarefas)** é uma representação estruturada que decompõe uma tarefa complexa ou objetivo do usuário em uma hierarquia de sub-tarefas e operações menores e mais gerenciáveis. Ele mostra como as tarefas de alto nível são compostas por passos menores e a ordem em que esses passos precisam ser executados.

## Propósito Principal

Os principais objetivos de um Diagrama HTA são:

1.  **Compreender a Estrutura da Tarefa:** Detalhar e visualizar como os usuários realizam tarefas complexas, desde o objetivo principal até as ações individuais.
2.  **Analisar a Complexidade da Tarefa:** Identificar o quão complexa uma tarefa é, quantos passos são necessários e quais são as dependências entre eles.
3.  **Identificar Problemas e Ineficiências:** Revelar passos desnecessários, redundantes ou confusos em um fluxo de tarefa existente.
4.  **Informar o Design de Interfaces e Fluxos:** Ajudar a projetar interfaces e fluxos de usuário que suportem eficientemente a conclusão da tarefa.
5.  **Base para Documentação e Treinamento:** Servir como base para a criação de manuais de usuário, tutoriais ou materiais de treinamento.
6.  **Avaliar Carga de Trabalho Mental:** Pode ser usado como um input para entender a carga cognitiva associada a diferentes partes de uma tarefa.
7.  **Identificar Oportunidades de Automação:** Apontar para sub-tarefas que poderiam ser automatizadas.

## Estrutura e Componentes

Um diagrama HTA geralmente tem uma estrutura de árvore ou um formato de [[Elementos/listas|lista]] aninhada:

*   **Objetivo Principal (Goal):** A tarefa de mais alto nível que o usuário está tentando realizar (o topo da hierarquia).
    *   Ex: "Comprar um livro online"
*   **Sub-tarefas (Sub-tasks/Operations):** O objetivo principal é decomposto em várias sub-tarefas. Cada sub-tarefa pode, por sua vez, ser decomposta em sub-tarefas ainda menores.
    *   Ex: Para "Comprar um livro online":
        1.  Buscar pelo livro
        2.  Adicionar livro ao carrinho
        3.  Realizar o [[Padrões/purchase_checkout|checkout]]
        4.  Confirmar pedido
*   **Operações (Actions/Lowest-Level Tasks):** Os passos mais básicos e indivisíveis na hierarquia. São as ações físicas ou cognitivas que o usuário executa.
    *   Ex: Para "Buscar pelo livro":
        1.1. Navegar para a barra de busca
        1.2. Digitar o nome do livro
        1.3. Pressionar "Enter" ou clicar no [[Elementos/botoes|botão]] de busca
*   **Planos (Plans):** Descrevem a lógica ou as condições que determinam como e quando as sub-tarefas são executadas. Indicam a sequência (ex: "Faça 1, depois 2, depois 3"), condições (ex: "Se X, então faça A, senão faça B"), ou repetições.
    *   Ex: Plano para "Realizar o [[Padrões/purchase_checkout|checkout]]": "Primeiro, preencha informações de envio (3.1). Depois, preencha informações de pagamento (3.2). Se houver cupom, aplicar cupom (3.3). Finalmente, revisar pedido (3.4)."
*   **Numeração Hierárquica:** Usa-se um sistema de numeração (ex: 1, 1.1, 1.1.1, 2, 2.1) para indicar o nível na hierarquia e a relação entre as tarefas.

## Como Criar um Diagrama HTA

1.  **Identificar o Objetivo Principal:** Qual tarefa principal do usuário será analisada?
2.  **Coletar Dados da Tarefa:** Observar usuários realizando a tarefa, entrevistá-los, ou consultar especialistas no domínio.
3.  **Decompor a Tarefa:** Dividir o objetivo principal em 3-8 sub-tarefas principais.
4.  **Decompor Sub-tarefas:** Para cada sub-tarefa, repita o processo de decomposição até chegar ao nível de operações básicas (ações que não podem ser razoavelmente divididas mais).
5.  **Definir os Planos:** Para cada nível de decomposição, especificar o plano que governa a execução das sub-tarefas (sequência, condições).
6.  **Representar Graficamente ou Textualmente:** Desenhar o diagrama em formato de árvore ou usar uma [[Elementos/listas|lista]] aninhada com numeração.
7.  **Validar e Refinar:** Revisar o diagrama com usuários ou especialistas para garantir precisão e completude.

## Principais Benefícios

*   **Clareza Estrutural:** Fornece uma visão clara de como as tarefas são executadas.
*   **Foco na Eficiência:** Ajuda a otimizar os fluxos de tarefas.
*   **Design Centrado na Tarefa:** Garante que o design suporte as necessidades do usuário para completar suas tarefas.
*   **Comunicação Detalhada:** Permite comunicar os detalhes de uma tarefa de forma precisa.

## Quando Utilizar

*   Ao analisar tarefas complexas ou críticas para o sucesso do usuário.
*   Para entender os passos envolvidos em um processo de trabalho existente.
*   Ao projetar ou redesenhar interfaces para tarefas específicas.
*   Para identificar erros potenciais do usuário ou pontos de dificuldade.
*   Em contextos onde a segurança e a eficiência da tarefa são primordiais (ex: aviação, controle de processos industriais, sistemas médicos), mas também muito útil para produtos digitais em geral.

## Relação com Outros Entregáveis

*   **[User Flow](./user_flow.md):** Um [[Entregáveis/user_flow|User Flow]] mostra o caminho que um usuário percorre através de uma interface para completar uma tarefa, incluindo telas e decisões. Um HTA foca mais na decomposição hierárquica da tarefa em si, e pode informar a criação de um [[Entregáveis/user_flow|User Flow]].
*   **[Process Map](./process_map.md):** Semelhante, mas Process [[Componentes/maps|Maps]] podem ter um escopo mais amplo, incluindo múltiplos atores ou sistemas, enquanto HTA é mais focado na perspectiva da tarefa do usuário individual.

## Referências (NN/g)

*   (O HTA é uma técnica bem estabelecida em ergonomia e IHC - Interação Humano-Computador. A página do glossário do NN/g o inclui, indicando sua relevância.)
*   Veja também: [User Flow](./user_flow.md), [Process Map](./process_map.md).

---

*Este documento é parte do glossário de entregáveis de UX, baseado no conteúdo do Nielsen Norman Group e técnicas clássicas de análise de tarefas.* 