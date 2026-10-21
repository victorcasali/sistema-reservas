class Mesa:
    def __init__(self,numero,lugares):
        self.numero=numero
        self.lugares=lugares
    def mostrar_mesa(self):
        print(f'Mesa {self.numero} - {self.lugares} lugares')
    def cabe_mesa(self,valor):
        if valor > self.lugares:
            return False
        else:
            return True
