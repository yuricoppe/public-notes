---
title: "create account"

---

## Criação de Conta (Create Account)

## Descrição Geral

O padrão de criação de conta (também conhecido como registro ou sign-up) permite que novos usuários estabeleçam uma identidade e acesso a um sistema ou portal. Envolve a coleta de informações essenciais do usuário, a definição de credenciais de acesso e, frequentemente, a aceitação de termos de serviço e políticas de privacidade.

## Princípios Chave / Objetivos

- **Facilidade de Uso:** Tornar o processo de registro o mais simples e rápido possível.
- **Clareza:** Informar claramente quais dados são necessários e por quê.
- **Segurança:** Garantir a segurança das informações fornecidas e das credenciais criadas.
- **Confirmação:** Fornecer feedback claro de que a conta foi criada com sucesso.
- **Conformidade:** Assegurar a conformidade com regulamentações de privacidade (ex: LGPD, GDPR).

## Elementos Comuns / Estrutura Típica

- Campos de entrada para informações pessoais (ex: nome, email, data de nascimento).
- Campos para definição de credenciais (ex: nome de usuário, senha, confirmação de senha).
- [[Glossário/Elementos/form_controls|Checkbox]] para aceitação de Termos de Serviço e Política de Privacidade.
- [[Glossário/Elementos/botoes|Botão]] de ação primário para submeter (ex: "Criar Conta", "Registrar").
- [[Glossário/Elementos/links|Links]] para [[Glossário/Padrões/authentication|login]] (caso o usuário já tenha uma conta) ou para políticas.
- Feedback visual para validação de campos e requisitos de senha.
- Opcional: Verificação de email ou número de telefone como parte do processo.
- Opcional: Campos para informações de perfil adicionais (podem ser coletados após o registro inicial).

## Comportamento e Interação

1. O usuário seleciona a opção para criar uma nova conta.
2. O sistema apresenta o [[Glossário/Padrões/form_structure|formulário]] de registro.
3. O usuário preenche os campos obrigatórios e opcionais.
4. O usuário define e confirma sua senha, seguindo os critérios de complexidade.
5. O usuário aceita os termos e políticas.
6. O usuário submete o [[Glossário/Padrões/form_structure|formulário]].
7. O sistema valida os dados e a disponibilidade do nome de usuário/email.
8.  - **Sucesso:**
        - O sistema cria a nova conta.
        - O usuário é notificado do sucesso (ex: mensagem na tela, email de boas-vindas).
        - Opcionalmente, o usuário pode ser logado automaticamente e/ou redirecionado para um tour de [[Glossário/Padrões/launch|onboarding]] ou para o [[Glossário/Entregáveis/dashboard|dashboard]].
        - Opcionalmente, pode ser necessária uma etapa de verificação de email/telefone.
    - **Falha:** O sistema exibe [[Glossário/Componentes/messaging|mensagens]] de erro claras, indicando quais campos precisam ser corrigidos (ex: email já em uso, senha não atende aos critérios).

## Diretrizes de Uso e Boas Práticas

### Faça

- Solicite apenas as informações estritamente necessárias para a criação da conta na etapa inicial. Informações adicionais podem ser coletadas posteriormente.
- Indique claramente quais campos são obrigatórios e quais são opcionais.
- Forneça feedback em tempo real sobre a validade dos dados inseridos e a força da senha.
- Permita que os usuários vejam a senha que estão digitando (opção "mostrar senha").
- Envie um email de boas-vindas e/ou confirmação.
- Informe sobre o uso dos dados coletados ([[Glossário/Elementos/links|link]] para Política de Privacidade).
- Otimize o processo para dispositivos móveis.

### Não Faça

- Não crie [[Glossário/Padrões/form_structure|formulários]] de registro excessivamente longos e complexos.
- Não peça informações sensíveis desnecessariamente.
- Não use CAPTCHAs que sejam difíceis de resolver ou inacessíveis.
- Não esconda os [[Glossário/Elementos/links|links]] para Termos de Serviço e Política de Privacidade.
- Não defina senhas fracas como padrão ou permita senhas óbvias sem aviso.

## Considerações de Acessibilidade

- Todos os campos de [[Glossário/Padrões/form_structure|formulário]] devem ter rótulos (`<label for>`) claros e associados.
- As [[Glossário/Componentes/messaging|mensagens]] de erro e sucesso devem ser acessíveis a leitores de tela e visualmente distintas.
- Requisitos de senha devem ser comunicados de forma acessível antes que o usuário comece a digitar.
- Garanta navegação e operação por teclado para todos os elementos.
- Mantenha contraste de [[Glossário/Linguagem Visual/cor|cores]] adequado.
- Evite depender apenas de indicações visuais ([[Glossário/Linguagem Visual/cor|cor]]) para feedback; use também texto ou [[Glossário/Linguagem Visual/iconografia|ícones]].

## Exemplos / Cenários de Uso

- Registro em uma nova rede social.
- Criação de conta em uma loja virtual para realizar compras.
- Inscrição em um serviço de streaming.
- Cadastro para acesso a um fórum ou comunidade online.

## Variações Comuns

- **Registro Rápido:** Apenas email e senha, com coleta de mais dados posteriormente.
- **Registro com Verificação:** Requer verificação de email ou SMS para ativar a conta.
- **Registro Social:** Usar contas existentes (Google, Facebook) para criar a conta no novo sistema.
- **Registro por Convite:** Acesso ao [[Glossário/Padrões/form_structure|formulário]] de registro apenas através de um [[Glossário/Elementos/links|link]] de convite.

## Status

A definir

## Recursos Adicionais / Figma

- [[[Glossário/Elementos/links|Link]] para o design de telas de Criação de Conta no Figma]
- [[[Glossário/Elementos/links|Link]] para os Termos de Serviço e Política de Privacidade padrão]
