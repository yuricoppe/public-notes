# Footer (Rodapé)

O Footer (Rodapé) é uma seção de conteúdo localizada na parte inferior de uma página web ou tela de aplicativo. Geralmente contém informações secundárias, links de navegação, direitos autorais e outros elementos que não são o foco principal do conteúdo da página, mas são importantes para a completude e usabilidade do site.

## Casos de Uso

-   Todas as páginas de um website.
-   Telas principais de uma aplicação web.

## Elementos Comuns de um Footer

-   **Informações de Copyright:** (ex: "© 2023 Nome da Empresa. Todos os direitos reservados.").
-   **Links de Navegação Secundária ou Utilitária:**
    *   Termos de Serviço
    *   Política de Privacidade
    *   Política de Cookies
    *   Mapa do Site
    *   Contato / Fale Conosco
    *   Sobre Nós / Quem Somos
    *   Carreiras / Trabalhe Conosco
    *   FAQ / Ajuda
-   **Links para Redes Sociais:** Ícones ou links textuais para os perfis da empresa em redes sociais.
-   **Logo da Empresa (Menor):** Reforço da marca.
-   **Informações de Contato:** Endereço, telefone, e-mail (menos comum para todos os sites, mais para empresas locais).
-   **Selo de Segurança ou Certificações (se aplicável).**
-   **Seletor de Idioma/Região (se aplicável).**
-   **Chamada para Ação (CTA) Secundária:** (ex: assinar newsletter).
-   **"Voltar ao Topo" (Back to Top Link - pode estar próximo ou integrado ao footer).**

## Melhores Práticas

-   **Consistência:** O footer deve ser consistente em todas as páginas do site em termos de design e conteúdo principal.
-   **Organização:** Agrupar links e informações de forma lógica (ex: colunas com títulos como "Empresa", "Recursos", "Legal").
-   **Legibilidade:** Usar tipografia clara e contraste suficiente, mesmo que o tamanho da fonte seja menor que o do corpo principal.
-   **Não Sobrecarregar:** Evitar encher o footer com excesso de links ou informações desnecessárias. Priorizar o que é mais útil para o usuário.
-   **Responsividade:** O layout do footer deve se adaptar bem a diferentes tamanhos de tela, empilhando colunas ou ajustando o layout conforme necessário.
-   **Acessibilidade (a11y):**
    *   Usar o elemento semântico `<header>` não, `<header>` é para o topo, usar `<footer>` para o rodapé.
    *   Garantir que todos os links sejam acessíveis por teclado e tenham texto descritivo.
    *   Manter uma estrutura de cabeçalhos lógica se houver títulos dentro do footer.
-   **Hierarquia Visual:** Mesmo sendo secundário, deve haver uma hierarquia clara dentro do próprio footer.

## Variações de Layout

-   **Footer Simples:** Apenas copyright e alguns links essenciais.
-   **Footer com Múltiplas Colunas:** Para organizar um número maior de links.
-   **"Fat Footer":** Um footer mais extenso com bastante conteúdo e links, comum em sites grandes.
-   **Footer Fixo/Flutuante (Sticky Footer - diferente do fixo no bottom da viewport):** Garante que o footer fique na parte inferior da viewport mesmo que o conteúdo da página seja curto, evitando que ele "suba" no meio da tela. (Isso é mais uma técnica de layout CSS do que um componente visual em si, mas afeta a percepção do footer).

## O Que Evitar

-   Footer desorganizado ou com excesso de links que o torna difícil de usar.
-   Links quebrados ou desatualizados.
-   Design que se destaca demais e compete com o conteúdo principal da página.
-   Texto muito pequeno ou com baixo contraste que dificulta a leitura.
-   Não usar o elemento `<footer>` apropriado. 