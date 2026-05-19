# Diagramas e Organização do Sistema

A estrutura implementada foi baseada na arquitetura definida anteriormente e nos princípios discutidos na resenha da Aula 3, principalmente separação de responsabilidades, redução de acoplamento e melhoria da organização do código.

---

# Organização dos módulos

## models/Equipamento

Responsável por representar os equipamentos disponíveis no sistema e suas regras específicas de multa.

## models/Emprestimo

Armazena os dados relacionados aos empréstimos realizados pelos usuários.

## services/ServicoEmprestimo

Centraliza as operações principais do sistema, como registro de empréstimos, devoluções e verificação de atrasos.

## services/Notificador

Responsável pelo envio de avisos e mensagens do sistema.

## repositories/RepositorioEmprestimo

Gerencia o armazenamento temporário dos dados de empréstimos e equipamentos.

## main.py

Responsável por iniciar a execução principal da aplicação.

---

# UC01 — Registrar Empréstimo

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

        Notificador -->> Usuario: confirmação enviada

    else equipamento indisponível

        ServicoEmprestimo -->> Usuario: empréstimo recusado

    end
```

---

# UC02 — Registrar Devolução

```mermaid
sequenceDiagram
    actor Usuario

    participant Main
    participant ServicoEmprestimo
    participant RepositorioEmprestimo

    Usuario ->> Main: solicitar devolução

    Main ->> ServicoEmprestimo: finalizar_emprestimo()

    ServicoEmprestimo ->> RepositorioEmprestimo: listar_emprestimos()

    loop localizar empréstimo
        RepositorioEmprestimo -->> ServicoEmprestimo: empréstimo
    end

    ServicoEmprestimo ->> RepositorioEmprestimo: liberar_equipamento()

    ServicoEmprestimo -->> Usuario: devolução concluída
```

---

# UC03 — Verificar Atrasos

```mermaid
sequenceDiagram
    actor Sistema

    participant ServicoEmprestimo
    participant RepositorioEmprestimo
    participant Notificador

    Sistema ->> ServicoEmprestimo: verificar_atrasos()

    ServicoEmprestimo ->> RepositorioEmprestimo: listar_emprestimos()

    loop analisar empréstimos

        RepositorioEmprestimo -->> ServicoEmprestimo: empréstimo

        alt empréstimo atrasado

            ServicoEmprestimo ->> ServicoEmprestimo: calcular_multa()

            ServicoEmprestimo ->> Notificador: enviar_aviso_atraso()

            Notificador -->> Sistema: aviso enviado

        end
    end
```
