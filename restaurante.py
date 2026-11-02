from reserva import Reserva


class Restaurante:
    def __init__(self):
        self.mesas=[]
        self.clientes=[]
        self.reservas=[]
    def criar_reserva(self,cliente,mesa,data,horario,qtd_de_pessoas):
        for reserva_existente in self.reservas:
            if reserva_existente.mesa.numero == mesa.numero and reserva_existente.data == data and reserva_existente.horario == horario:
                print("Esse cadastro ja esta feito")
                return None
        nova_reserva=Reserva(cliente,mesa,data,horario, qtd_de_pessoas)
        self.reservas.append(nova_reserva)
        return nova_reserva