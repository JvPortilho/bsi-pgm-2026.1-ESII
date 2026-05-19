# main: iniciar funcionamento do sistema.

from services.servico_emprestimo import (
    ServicoEmprestimo
)

servico = ServicoEmprestimo()

servico.registrar_emprestimo(
    1,
    "joao",
    "jvportilho321@email.com",
    5
)

print(servico.verificar_atrasos())
