# RepositorioEmprestimo: persistir empréstimos do sistema.

from models.equipamento import Camera, CaixaSom
from models.emprestimo import Emprestimo


class RepositorioEmprestimo:

    def __init__(self):

        self.equipamentos = [
            Camera(1, "Camera Canon", True),
            CaixaSom(2, "Caixa JBL", True)
        ]

        self.emprestimos = []

    def buscar_equipamento(self, equip_id):

        for equipamento in self.equipamentos:

            if equipamento.id == equip_id:
                return equipamento

        return None

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        return self.emprestimos

    def bloquear_equipamento(self, equip_id):

        equipamento = self.buscar_equipamento(equip_id)

        if equipamento:
            equipamento.disponivel = False

    def liberar_equipamento(self, equip_id):

        equipamento = self.buscar_equipamento(equip_id)

        if equipamento:
            equipamento.disponivel = True
