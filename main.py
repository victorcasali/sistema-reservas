from cliente import Cliente
from mesa import Mesa
from restaurante import Restaurante

def main():
    restaurante = Restaurante()

    mesa1 = restaurante.adicionar_mesa(1, 5)
    cliente1 = restaurante.adicionar_cliente("Carlos", "21980878846")

    restaurante.criar_reserva(cliente1, mesa1, "10/12/2026", "20:00", 2)
    restaurante.criar_reserva(cliente1, mesa1, "10/12/2026", "21:00", 3)

    for numero in [1, 2, 99]:
        r = restaurante.buscar_reserva(numero)
        if r is not None:
            r.mostrar_reserva()
        else:
            print(f"Reserva {numero} não encontrada.")
        print("-" * 30)

if __name__ == "__main__":
    main()