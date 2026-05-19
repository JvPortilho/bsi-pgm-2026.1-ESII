## Aula 04 — SRP

Durante a reorganização do sistema, a separação entre ServicoEmprestimo e Notificador foi uma das decisões mais difíceis. No início, parecia mais simples deixar as mensagens dentro do próprio serviço principal, já que elas acontecem logo após operações como empréstimos e atrasos.

Entretanto, isso faria o módulo possuir mais de uma responsabilidade. Caso a lógica de envio mudasse futuramente, o serviço de empréstimos também precisaria ser alterado. Isso aumentaria o acoplamento e dificultaria manutenção.

A decisão final foi separar o envio de notificações em um módulo próprio. O principal critério utilizado foi a ideia apresentada por Valente no Capítulo 5 sobre responsabilidade única e motivos de mudança. Assim, o serviço ficou responsável apenas pelas regras de negócio relacionadas aos empréstimos.

Outra decisão importante foi separar models de services. Os models ficaram responsáveis apenas pela representação dos dados, enquanto os services concentram comportamento e regras do sistema. Isso deixou a arquitetura mais organizada e fácil de entender.

---

## Aula 05 — OCP

Nesta atividade foi aplicado o princípio OCP utilizando polimorfismo para eliminar estruturas condicionais no cálculo de multas. Cada tipo de equipamento passou a possuir sua própria implementação do método calcular_multa(), evitando dependência de if/elif no serviço principal.

A solução tornou o sistema mais flexível para inclusão de novos equipamentos sem necessidade de alterar regras já existentes. Isso segue a ideia discutida por Valente no Capítulo 5 sobre sistemas abertos para extensão e fechados para modificação.

Apesar disso, a abordagem possui limites. Caso o sistema passe a possuir regras muito específicas de cobrança, a quantidade de subclasses pode crescer excessivamente e dificultar manutenção. Nesses casos, outras estratégias além de herança poderiam ser mais adequadas.
