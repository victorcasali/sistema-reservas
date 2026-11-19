from cliente import Cliente
from mesa import Mesa
from restaurante import Restaurante

def main():
    restaurante = Restaurante()

    mesa1 = restaurante.adicionar_mesa(1, 5)
    mesa2 = restaurante.adicionar_mesa(2, 4)
    cliente1 = restaurante.adicionar_cliente("Carlos", "21980878846")

    restaurante.criar_reserva(cliente1, mesa1, "10/12/2026", "20:00", 2)
    restaurante.criar_reserva(cliente1, mesa2, "10/12/2026", "12:00", 3)
    restaurante.criar_reserva(cliente1, mesa1, "11/12/2026", "20:00", 2)

    do_dia = restaurante.reserva_do_dia("10/12/2026")
    print(len(do_dia))
    for r in do_dia:
        r.mostrar_reserva()
        print("-" * 30)

    print(len(restaurante.reserva_do_dia("15/12/2026")))

if __name__ == "__main__":
    main()