class Reserva:
    proximo_numero=1
    def __init__(self,cliente,mesa,data,horario,qtd_de_pessoas):
        self.numero=Reserva.proximo_numero
        Reserva.proximo_numero+=1
        self.cliente=cliente
        self.mesa=mesa
        self.data=data
        self.horario=horario
        self.qtd_de_pessoas=qtd_de_pessoas

    def mostrar_reserva(self):
        print(f"Reserva:{self.numero}\n"
              f"Nome:{self.cliente.nome}\n"
              f"Mesa:{self.mesa.numero}\n"
              f"Data:{self.data}\n"
              f"Horario:{self.horario}\n"
              f"Qtd de pessoas:{self.qtd_de_pessoas}")
