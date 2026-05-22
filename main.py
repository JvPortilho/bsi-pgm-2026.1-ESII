# main: iniciar funcionamento do sistema.

from repositories.repositorio_emprestimo import (
    RepositorioEmprestimo
)

from services.notificador import (
    Notificador
)

from services.servico_emprestimo import (
    ServicoEmprestimo
)


def main():

    repositorio = (
        RepositorioEmprestimo()
    )

    notificador = (
        Notificador()
    )

    servico = ServicoEmprestimo(
        repositorio,
        notificador
    )

    while True:

        print(
            "\n1-Registrar  "
            "2-Devolver  "
            "3-Atrasos  "
            "0-Sair"
        )

        opcao = input("Opção: ")

        if opcao == "1":

            servico.registrar_emprestimo(
                int(
                    input(
                        "ID equipamento: "
                    )
                ),
                input("Nome: "),
                input("Email: "),
                int(input("Dias: "))
            )

        elif opcao == "2":

            servico.finalizar_emprestimo(
                int(
                    input(
                        "ID empréstimo: "
                    )
                )
            )

        elif opcao == "3":

            servico.verificar_atrasos()

        elif opcao == "0":
            break


if __name__ == "__main__":
    main()
