class Cliente:
    def __init__(self,nome,telefone):
        self.nome=nome
        self.telefone=telefone
    def mostrar_cliente(self):
        print(f'Nome: {self.nome} - Telefone: (21){self.telefone}')