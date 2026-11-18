from cliente import Cliente
from mesa import Mesa
from restaurante import Restaurante

def main():
    restaurante = Restaurante()

    c1 = restaurante.adicionar_cliente("Carlos", "21980878846")  # deve ser aceito
    c2 = restaurante.adicionar_cliente("", "21980878846")  # nome vazio: recusa
    c3 = restaurante.adicionar_cliente("Ana", "")  # telefone vazio: recusa
    c4 = restaurante.adicionar_cliente("   ", "21980878846")  # só espaços: recusa
    c5 = restaurante.adicionar_cliente("Carlos", "21999990000")  # mesmo nome, outro telefone: aceito

    print(c2, c3, c4)

    print("Clientes cadastrados:")
    for c in restaurante.clientes:
        c.mostrar_cliente()
if __name__ == "__main__":
    main()