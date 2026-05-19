# Diagramas de Sequência

A decomposição abaixo segue os princípios discutidos na resenha, aplicando separação de responsabilidades, redução de acoplamento e maior coesão entre os módulos.

---

## UC01 — Registrar Empréstimo

```mermaid
sequenceDiagram

actor Usuario

participant Main
participant ServicoEmprestimo
participant RepositorioEmprestimo
participant Notificador

Usuario ->> Main: solicitar empréstimo

Main ->> ServicoEmprestimo: registrar_emprestimo()

ServicoEmprestimo ->> RepositorioEmprestimo: buscar_equipamento()

RepositorioEmprestimo -->> ServicoEmprestimo: equipamento

alt equipamento disponível

ServicoEmprestimo ->> RepositorioEmprestimo: salvar_emprestimo()

ServicoEmprestimo ->> RepositorioEmprestimo: bloquear_equipamento()

ServicoEmprestimo ->> Notificador: enviar_confirmacao()

Notificador -->> Usuario: mensagem enviada

else equipamento indisponível

ServicoEmprestimo -->> Usuario: empréstimo negado

end
