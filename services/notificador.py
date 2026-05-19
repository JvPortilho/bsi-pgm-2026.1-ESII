# Notificador: emitir notificações do sistema.

class Notificador:

    def enviar_confirmacao(self, email, data_devolucao):

        mensagem = (
            f"Reserva registrada. "
            f"Entrega prevista: {data_devolucao}"
        )

        self.enviar_email(mensagem)

    def enviar_aviso_atraso(self, email):

        mensagem = "Existe um empréstimo pendente em atraso."

        self.enviar_email(mensagem)

    def enviar_email(self, mensagem):

        print(f"[EMAIL] {mensagem}")
