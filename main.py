from cliente import Cliente
from mesa import Mesa
from reserva import Reserva
from restaurante import Restaurante


def main():

    mesa1=Mesa(1,2)
    mesa2=Mesa(2,4)
    mesa3=Mesa(3,6)
    mesa4=Mesa(4,8)

    cliente1=Cliente("Mauricio",980878846)
    cliente2=Cliente("Mauricio",976543212)

    reserva1=Reserva(cliente1,mesa1,"23/10/1996","20:00",6)
    reserva1.mostrar_reserva()
    print("-"*50)
    reserva2=Reserva(cliente2,mesa2,"21/10/1996","16:00",4)
    reserva2.mostrar_reserva()

    todos_clientes=[cliente1,cliente2]

    todas_mesas=[mesa1,mesa2,mesa3,mesa4]
   #mesa1.mostrar_mesa()

    for c in todos_clientes:
        c.mostrar_cliente()

    #for m in todas_mesas:
        #m.mostrar_mesa()


    #pessoas=int(input('Quantas pessoas vão comer?'))
    #for m in todas_mesas:
        #if m.cabe_mesa(pessoas):
            #m.mostrar_mesa()

if __name__ == "__main__":
    main()