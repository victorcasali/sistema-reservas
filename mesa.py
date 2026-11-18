class Mesa:
    def __init__(self,numero,lugares):  # Cria o méto-do construtor (inicializa a mesa recebendo seu número e a quantidade de lugares).
        self.numero = numero
        self.lugares = lugares

    def mostrar_mesa(self):  # Cria o méto-do mostrar_mesa (exibe no terminal o número da mesa e quantos lugares ela possui).
        print(f'Mesa {self.numero} - {self.lugares} lugares')

    def cabe_mesa(self,valor):  # Cria o méto-do cabe_mesa (verifica se a quantidade de pessoas solicitada é menor ou igual à capacidade de lugares da mesa).
        if valor > self.lugares:
            return False
        else:
            return True