import reserva
from reserva import Reserva
from datetime import date, datetime


data_atual=date.today()
class Restaurante:
    def __init__(self):
        self.mesas=[]
        self.clientes=[]
        self.reservas=[]

    def adicionar_mesa(self,numero,quantidade_de_cliente):


    def criar_reserva(self,cliente,mesa,data,horario,qtd_de_pessoas):
        data=datetime.strptime(data,"%d/%m/%Y").date()
        if not mesa.cabe_mesa(qtd_de_pessoas):
            print("A quantidade de pessoas excede a capacidade da mesa")
            return None
        if horario not in Reserva.horarios_disponiveis:
            print(f"O horario das {horario} indisponivel")
            return None
        if data < data_atual:
            print(f"Essa data já passou. Digite uma data valida!")
            return None
        for reserva_existente in self.reservas:
            if reserva_existente.mesa.numero == mesa.numero and reserva_existente.data == data and reserva_existente.horario == horario:
                print("Esse cadastro ja esta feito")
                return None
        nova_reserva=Reserva(cliente,mesa,data,horario, qtd_de_pessoas)
        self.reservas.append(nova_reserva)
        return nova_reserva