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
## UC02 — Registrar Devolução

```mermaid
sequenceDiagram

actor Usuario

participant Main
participant ServicoEmprestimo
participant RepositorioEmprestimo

Usuario ->> Main: solicitar devolução

Main ->> ServicoEmprestimo: finalizar_emprestimo()

ServicoEmprestimo ->> RepositorioEmprestimo: listar_emprestimos()

loop procurar empréstimo

RepositorioEmprestimo -->> ServicoEmprestimo: empréstimo

end

ServicoEmprestimo ->> RepositorioEmprestimo: liberar_equipamento()

ServicoEmprestimo -->> Usuario: devolução concluída
```

---

## UC03 — Verificar Atrasos

```mermaid
sequenceDiagram

actor Sistema

participant ServicoEmprestimo
participant RepositorioEmprestimo
participant Notificador

Sistema ->> ServicoEmprestimo: verificar_atrasos()

ServicoEmprestimo ->> RepositorioEmprestimo: listar_emprestimos()

loop verificar empréstimos

RepositorioEmprestimo -->> ServicoEmprestimo: empréstimo

alt empréstimo atrasado

ServicoEmprestimo ->> ServicoEmprestimo: calcular_multa()

ServicoEmprestimo ->> Notificador: enviar_aviso_atraso()

Notificador -->> Sistema: aviso enviado

end

end
```
