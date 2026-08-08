---
title: "Footnotes (Notas de Rodapé)"

---

## Footnotes (Notas de Rodapé)

Footnotes (Notas de [[Glossário/Componentes/footer|Rodapé]]) são referências ou informações adicionais colocadas na parte inferior de uma página (ou seção) para fornecer esclarecimentos, citações de fontes, ou [[Glossário/Componentes/comments|comentários]] sobre um ponto específico no corpo do texto principal. Elas são indicadas no texto por um número sobrescrito, símbolo ou letra.

## Casos de Uso

-   **Citações Acadêmicas:** Referenciar fontes em trabalhos de pesquisa, artigos.
-   **Esclarecimentos:** Fornecer definições, traduções ou informações contextuais que não se encaixam fluidamente no texto principal.
-   **Comentários do Autor:** Adicionar observações ou tangentes sem interromper o fluxo principal da leitura.
-   **Atribuições:** Dar crédito a fontes de dados específicos, citações curtas ou ideias.
-   **Textos Legais ou Técnicos:** Para explicar termos ou cláusulas específicas.

## Elementos Essenciais

1.  **Marcador de Referência no Texto:** Um número (geralmente sobrescrito: ¹, ², ³), asterisco (*, **, ***), ou outra convenção de símbolo no corpo do texto, indicando a presença de uma nota de rodapé.
    *   Este marcador é geralmente um [[Glossário/Elementos/links|link]] que leva o usuário diretamente para a nota de rodapé correspondente.

2.  **Seção de Notas de Rodapé:** Localizada na parte inferior da página (ou, em alguns contextos digitais, no final de um artigo ou seção).
    *   Geralmente separada do texto principal por uma linha horizontal.
    *   Cada nota é listada com seu marcador correspondente seguido pelo texto da nota.

3.  **Texto da Nota de Rodapé:** O conteúdo explicativo, [[Glossário/Elementos/block_quote|citação]] ou comentário.
    *   **(Opcional, mas bom para usabilidade) Link de Retorno:** A partir da nota de rodapé, um link (geralmente no marcador da nota) que leva de volta ao ponto de referência no texto principal.

## Melhores Práticas

-   **Discrição:** As notas de rodapé devem ser para informações suplementares. Se a informação é crucial para o entendimento do texto principal, ela deve estar no próprio texto.
-   **Consistência na Numeração/Marcação:** Usar um sistema consistente para os marcadores (numérico sequencial é o mais comum).
-   **Clareza:** O texto da nota de rodapé deve ser claro e conciso.
-   **Posicionamento:** Tradicionalmente no pé da página. Em conteúdo digital longo, pode ser ao final do artigo/seção para evitar que o usuário perca o contexto ao rolar até o final da página a todo momento.
-   **Acessibilidade (a11y) e Usabilidade Digital:**
    *   Os marcadores de referência no texto devem ser links clicáveis para a nota correspondente.
    *   Cada nota na seção de notas de rodapé deve ter um `id` para ser o alvo do link.
    *   O marcador na nota de rodapé também pode ser um link de volta para o ponto no texto (usando um `id` no marcador original ou em um `<span>` ao redor dele).
    *   Usar `aria-describedby` no elemento que contém o marcador de referência no texto, apontando para o ID da nota de rodapé, pode ajudar leitores de tela a anunciar que há uma nota associada.
    *   Outra abordagem para acessibilidade é usar `role="doc-footnote"` para o contêiner da nota e `role="doc-noteref"` para a referência no texto, embora o suporte possa variar. A abordagem de links internos (`<a>` com `href="#id"`) é mais robusta.
    *   Considerar tooltips ou popovers para notas curtas em interfaces digitais, como alternativa a rolar para o fim da página, mas isso já se afasta do conceito tradicional de footnote.
-   **Estilo Visual:** As notas de rodapé geralmente têm um tamanho de fonte menor que o texto principal e podem ter um recuo.

## Variações em Mídia Digital

-   **Notas de Fim (Endnotes):** Coletadas no final de um documento ou capítulo, em vez de no pé de cada página. Mais comum em livros.
-   **Tooltips/Popovers:** Para notas muito curtas, a informação pode aparecer em um tooltip ao passar o mouse/focar no marcador, ou em um popover ao clicar.
-   **Sidenotes (Notas Laterais):** Em layouts mais largos, as notas podem aparecer na margem lateral, próximas ao ponto de referência no texto.

## O Que Evitar

-   Usar notas de rodapé para informações essenciais que deveriam estar no corpo do texto.
-   Numeração inconsistente ou confusa.
-   Notas de rodapé excessivamente longas (se for muito longa, talvez mereça ser uma seção à parte ou um apêndice).
-   Dificultar a navegação entre o texto e a nota (ex: marcadores não clicáveis).
