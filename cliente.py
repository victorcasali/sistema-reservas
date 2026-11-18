class Cliente:
    def __init__(self,nome,telefone):  # Cria o méto-do construtor (inicializa o cliente armazenando seu nome e telefone).
        self.nome=nome
        self.telefone=telefone
    def mostrar_cliente(self):  # Cria o méto-do mostrar_cliente (exibe no terminal o nome do cliente e o telefone formatado com DDD 21).
        print(f'Nome: {self.nome} - Telefone: (21){self.telefone}')