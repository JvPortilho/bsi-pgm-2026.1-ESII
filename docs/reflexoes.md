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

## Aula 06 — Verificação de LSP

As subclasses Camera e CaixaSom foram analisadas para verificar se respeitam corretamente o contrato definido pela classe base Equipamento. Nos testes realizados, calcular_multa(0) retornou 0 em ambas as implementações, mantendo o comportamento esperado de multa não negativa.

Também foi verificado o comportamento para valores negativos, como calcular_multa(-5). Em todos os casos o retorno permaneceu 0, devido ao uso de max(0, valor), evitando multas negativas e mantendo consistência entre as subclasses.

Além disso, nenhuma das subclasses lança exceções inesperadas durante o cálculo. O método sempre retorna um valor numérico compatível com o contrato definido na superclasse abstrata.

Dessa forma, as subclasses podem substituir Equipamento sem causar falhas no funcionamento do ServicoEmprestimo, demonstrando conformidade com o princípio LSP.

A análise foi baseada na discussão sobre substituição comportamental apresentada por Valente no Capítulo 5, seção sobre LSP (Liskov Substitution Principle).

---

## Aula 06 — DIP

A aplicação do DIP alterou a forma como o ServicoEmprestimo se relaciona com os outros módulos do sistema. Antes da modificação, o próprio serviço criava internamente o repositório e o notificador, ficando diretamente dependente dessas implementações concretas.

Com a inversão de dependência, o serviço passou apenas a receber essas dependências externamente pelo construtor. Isso reduziu o acoplamento e tornou o sistema mais flexível para futuras alterações ou substituições.

A principal mudança não foi apenas técnica, mas também conceitual. O ServicoEmprestimo deixou de controlar a criação dos objetos e passou a depender somente dos comportamentos fornecidos pelas dependências já prontas. Isso facilita reutilização, manutenção e principalmente testes isolados.

Segundo Valente no Capítulo 5, seção sobre DIP (Dependency Inversion Principle), módulos de alto nível não devem depender diretamente de implementações concretas. Essa ideia ficou evidente ao perceber que agora seria possível utilizar versões falsas de repositório e notificador sem alterar o serviço principal.

A aplicação do DIP também prepara o sistema para os testes unitários das próximas aulas.
