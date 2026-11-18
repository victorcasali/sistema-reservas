import reserva
from cliente import Cliente
from mesa import Mesa
from reserva import Reserva
from datetime import date, datetime


data_atual=date.today()
class Restaurante:
    def __init__(self):
        self.mesas=[]
        self.clientes=[]
        self.reservas=[]

    def adicionar_mesa(self,numero,quantidade_de_cliente):  # Cria o méto-do. adicionar_mesa (impede mesas duplicadas pelo número, cadastra a mesa em self.mesas e a devolve).
        for mesa_existente in self.mesas:
            if mesa_existente.numero == numero:
                print("Essa mesa já existe")
                return None
        mesa=Mesa(numero,quantidade_de_cliente)
        self.mesas.append(mesa)
        return mesa

    def adicionar_cliente(self,nome,telefone):  # Crie o méto-do adicionar_cliente (recusa nome ou telefone vazios, guarda em self.clientes e devolve o cliente).
        if not nome.strip() or not telefone.strip():
            print("Entrada invalida.")
            return None
        cliente = Cliente(nome, telefone)
        self.clientes.append(cliente)
        return cliente

    def criar_reserva(self,cliente,mesa,data,horario,qtd_de_pessoas):  # Cria o méto-do criar_reserva (valida capacidade da mesa, horários, datas passadas, existência da mesa e duplicidade, salvando em self.reservas).
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
        if mesa not in self.mesas:
            print(f"Essa mesa não existe!")
            return None
        for reserva_existente in self.reservas:
            if reserva_existente.mesa.numero == mesa.numero and reserva_existente.data == data and reserva_existente.horario == horario:
                print("Esse cadastro ja esta feito")
                return None
        nova_reserva=Reserva(cliente,mesa,data,horario, qtd_de_pessoas)
        self.reservas.append(nova_reserva)
        return nova_reserva

    def listar_mesas(self):# Cria o méto-do listar_mesas (Criar uma lista visivel das mesas cadastradas).
        if not self.mesas:
            print("Nenhuma mesa cadastrada.")
            return
        for mesa in self.mesas:
            Mesa.mostrar_mesa(mesa)

    def buscar_reserva(self,numero):
        for reserva in self.reservas:
            if reserva.numero == numero:
                return reserva
        return None
