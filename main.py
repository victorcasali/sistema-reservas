from cliente import Cliente
from mesa import Mesa
from restaurante import Restaurante

def main():
    restaurante = Restaurante()

    mesa1 = restaurante.adicionar_mesa(1, 5)
    cliente1 = restaurante.adicionar_cliente("Carlos", "21980878846")

    restaurante.criar_reserva(cliente1, mesa1, "10/12/2026", "20:00", 2)
    restaurante.criar_reserva(cliente1, mesa1, "10/12/2026", "21:00", 3)

    print(restaurante.cancelar_reserva(1))     # existe: deve dar True
    print(restaurante.cancelar_reserva(99))    # não existe: mensagem + False
    print(restaurante.buscar_reserva(1))       # já cancelada: deve dar None
    print(len(restaurante.reservas))           # sobrou só a nº 2: deve dar 1

    nova = restaurante.criar_reserva(cliente1, mesa1, "11/12/2026", "20:00", 2)
    print(nova.numero)

if __name__ == "__main__":
    main()