from mesa import Mesa
def main():
    mesa1=Mesa(1,2)
    mesa2=Mesa(2,4)
    mesa3=Mesa(3,6)
    mesa4=Mesa(4,8)
    todas_mesas=[mesa1,mesa2,mesa3,mesa4]
   #mesa1.mostrar_mesa()
    for m in todas_mesas:
        m.mostrar_mesa()

if __name__ == "__main__":
    main()