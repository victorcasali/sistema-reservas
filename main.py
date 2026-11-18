from cliente import Cliente
from mesa import Mesa
from restaurante import Restaurante

def main():
    restaurante = Restaurante()

    restaurante.listar_mesas()  # lista vazia: deve avisar

    restaurante.adicionar_mesa(1, 5)
    restaurante.adicionar_mesa(2, 4)
    restaurante.adicionar_mesa(3, 6)
    restaurante.adicionar_mesa(2, 8)  # número repetido: deve recusar

    print("-" * 30)
    restaurante.listar_mesas()  # deve mostrar as três mesas

if __name__ == "__main__":
    main()