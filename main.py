from cliente import Cliente
from mesa import Mesa
from restaurante import Restaurante

def main():
    restaurante=Restaurante()

    cliente1=Cliente("Carlos","21980878846")
    #mesa1=Mesa(1,5)
    mesa1=restaurante.adicionar_mesa(1,5)
    r1=restaurante.criar_reserva(cliente1,mesa2,"10/10/2026","20:00",2)

    r2=restaurante.criar_reserva(cliente1,mesa1,"10/11/2026","20:00",2)

    r3=restaurante.criar_reserva(cliente1,mesa1,"10/11/2026","21:00",2)

    print(r1)
    print(r2)
    print(r3)

    print()
if __name__ == "__main__":
    main()