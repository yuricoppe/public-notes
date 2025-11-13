# Content Inventory (Inventário de Conteúdo)

Um **Content Inventory (Inventário de Conteúdo)** é uma [[Elementos/listas|lista]] abrangente e quantitativa de todo o conteúdo digital existente em uma plataforma, como um website, aplicativo ou intranet. Ele cataloga cada peça de conteúdo, geralmente em nível de página ou de ativo individual (como PDFs, [[Elementos/imagem|imagens]], vídeos), e registra características específicas sobre cada item.

O inventário de conteúdo é frequentemente o primeiro passo para uma [Content Audit (Auditoria de Conteúdo)](./content_audit.md), que envolve a avaliação qualitativa desse conteúdo.

## Propósito Principal

Os principais objetivos de um inventário de conteúdo são:

1.  **Compreender o Escopo do Conteúdo:** Ter uma visão clara de todo o conteúdo existente, sua quantidade e onde está localizado.
2.  **Base para Auditoria e Análise:** Fornecer a [[Elementos/listas|lista]] completa de itens que serão posteriormente avaliados em uma [[Entregáveis/content_audit|auditoria de conteúdo]].
3.  **Planejamento de Migração:** Essencial ao planejar a migração de conteúdo para uma nova plataforma ou sistema de gerenciamento de conteúdo (CMS).
4.  **Identificação de Propriedade e Responsabilidade:** Registrar quem é o proprietário ou responsável pela manutenção de cada peça de conteúdo.
5.  **Organização e Gerenciamento:** Ajudar a organizar e gerenciar grandes volumes de conteúdo digital.
6.  **Identificação de Redundâncias Preliminares:** Embora a análise profunda seja da auditoria, o inventário já pode começar a sinalizar duplicidades óbvias.

## Como Criar um Inventário de Conteúdo

1.  **Definir o Escopo:** Decidir quais partes do seu ecossistema digital serão incluídas (ex: todo o site, apenas o blog, todas as landing pages de marketing).
2.  **Escolher uma Ferramenta:** Geralmente, uma planilha (Google Sheets, Excel) é a ferramenta mais comum e eficaz. Ferramentas de crawling de sites também podem automatizar parte do processo.
3.  **Identificar os Atributos a Serem Coletados:** Decidir quais informações serão registradas para cada item de conteúdo. Alguns atributos comuns incluem:
    *   ID Único
    *   URL / Localização do Arquivo
    *   Título da Página / Nome do Ativo
    *   Tipo de Conteúdo (ex: página HTML, PDF, [[Elementos/imagem|imagem]], vídeo, post de blog)
    *   Autor / Proprietário do Conteúdo
    *   Data da Última Modificação / Publicação
    *   Contagem de Palavras (para texto)
    *   Meta Descrição
    *   Palavras-chave
    *   Formato do Arquivo (para ativos)
    *   Tamanho do Arquivo
    *   Idioma
    *   Seções/Categorias do Site
    *   [[Linguagem Visual/metricas_e_keylines|Métricas]] básicas de analytics (ex: visualizações de página nos últimos X meses) - opcional, mas útil para a auditoria.
4.  **Coletar os Dados:**
    *   **Manualmente:** Navegando pelo site e registrando cada página/ativo.
    *   **Automaticamente:** Usando ferramentas de crawling (ex: Screaming Frog SEO Spider, Sitebulb) para extrair URLs e alguns metadados. A entrada manual ainda será necessária para outros atributos.
    *   **Via CMS/Banco de Dados:** Exportando dados diretamente do sistema de gerenciamento de conteúdo, se possível.
5.  **Organizar e Limpar os Dados:** Garantir que a planilha esteja bem organizada, consistente e livre de erros óbvios.

## Conteúdo Típico de uma Planilha de Inventário

Cada linha representa uma peça de conteúdo (página ou ativo), e cada coluna representa um atributo, por exemplo:

| ID  | URL                                | Título da Página            | Tipo        | Proprietário | Data Modif. | Cont. Palavras |
| --- | ---------------------------------- | --------------------------- | ----------- | ------------ | ----------- | -------------- |
| 1   | `/sobre-nos`                       | Sobre Nossa Empresa         | Página HTML | Marketing    | 2023-10-26  | 750            |
| 2   | `/blog/como-fazer-x`               | Como Fazer X Facilmente     | Post de Blog| Redação      | 2024-01-15  | 1200           |
| 3   | `/recursos/guia-completo-y.pdf`    | Guia Completo de Y          | PDF         | Produto      | 2023-05-10  | N/A            |

## Principais Benefícios

*   **Visão Completa:** Fornece um panorama de todo o patrimônio de conteúdo.
*   **Fundamental para a Auditoria:** Sem inventário, uma auditoria completa é impossível.
*   **Planejamento Eficaz:** Essencial para projetos de redesenho, migração ou reestruturação.
*   **Melhora a Governança de Conteúdo:** Ajuda a atribuir responsabilidades e a entender o ciclo de vida do conteúdo.

## Quando Utilizar

*   **Sempre antes de uma [Content Audit (Auditoria de Conteúdo)](./content_audit.md).**
*   Antes de iniciar um projeto de redesenho de site.
*   Ao planejar uma migração de conteúdo para uma nova plataforma.
*   Para obter controle sobre um grande volume de conteúdo não gerenciado.
*   Como parte de uma iniciativa de governança de conteúdo.

## Ferramentas Úteis

*   **Planilhas:** Google Sheets, Microsoft Excel (essenciais).
*   **Crawlers de Website:** Screaming Frog SEO Spider, Sitebulb, Xenu's [[Elementos/links|Link]] Sleuth (para automatizar a coleta de URLs e alguns metadados).
*   **Sistemas de Gerenciamento de Conteúdo (CMS):** Muitos CMSs oferecem funcionalidades de exportação de [[Elementos/listas|listas]] de conteúdo.

## Referências (NN/g)

*   Artigo Relacionado: [Content Inventory and Auditing 101](https://www.nngroup.com/articles/content-inventory-auditing/)
*   Vídeo Relacionado: [How To: Content Inventory and Audit](https://www.nngroup.com/videos/content-inventory-audit/)
*   Template: [NN/g Content Inventory and Auditing Excel Template (XLSX)](https://media.nngroup.com/media/editor/2020/03/19/NNg_Content%20Inventory%20and%20Auditing_Excel%20Template.xlsx) (Este template serve tanto para inventário quanto para auditoria)
*   Veja também: [Content Audit](./content_audit.md)

---

*Este documento é parte do glossário de entregáveis de UX, baseado no conteúdo do Nielsen Norman Group.* 