class Mesa:
    def __init__(self,numero,quantidade):
        self.numero=numero
        self.quantidade=quantidade
    def mostrar_mesa(self):
        print(f'Mesa {self.numero} - {self.quantidade} lugares')
