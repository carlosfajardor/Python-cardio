import random

def juego(intentos):
    x = 0
    tu = 0
    pc = 0

    while str(x) != intentos:
        print("Piedra, Papel o Tijera?")
        opcion = input()
        opcion = opcion.lower()
        azar = random.choice(["piedra","papel","tijera"])
        if opcion == azar:
            print("La PC tambien escogio: ",azar)
            print("Es un empate")
            print("")
        elif azar == "piedra" and opcion == "tijera":
            x += 1
            pc +=1
            print("La PC escogio: ",azar)
            print("Tu escogiste: ",opcion)
            print("Gana la PC y pierdes tu")
            print("")
        elif azar == "piedra" and opcion == "papel":
            x += 1
            tu +=1
            print("La PC escogio: ",azar)
            print("Tu ecogiste: ",opcion)
            print("Ganaste Tú y la PC perdio")
            print("")
        elif azar == "papel" and opcion == "piedra":
            x += 1
            pc += 1
            print("La PC escogio: ",azar)
            print("Tu escogiste: ",opcion)
            print("Gana la PC y pierdes tu")
            print("")
        elif azar == "papel" and opcion == "tijera":
            x += 1
            tu +=1
            print("La PC escogio: ",azar)
            print("Tu ecogiste: ",opcion)
            print("Ganaste Tú y la PC perdio")
            print("")
        elif azar == "tijera" and opcion == "papel":
            x += 1
            pc += 1
            print("La PC escogio: ",azar)
            print("Tu escogiste: ",opcion)
            print("Gana la PC y pierdes tu")
            print("")
        elif azar == "tijera" and opcion == "piedra":
            x += 1
            tu +=1
            print("La PC escogio: ",azar)
            print("Tu ecogiste: ",opcion)
            print("Ganaste Tú y la PC perdio")
            print("")
        else:
            print("Opción Invalida, vuelve a intentarlo")
            print("")
    
    if pc > tu:
        print("Gano la PC",pc,"a", tu)
        print("")
    elif pc == tu:
        print("Empataron",tu,"a",pc)
        print("")
    else:
        print("Ganaste",tu,"a",pc)
        print("")

    print("Partida Terminada")
        

def run():
    print("Vamos a Jugar Piedra, Papel ó Tijera.")
    print("Gana el mejor de tres intentos")
    juego("3")
    restart = input("Quieres jugar de nuevo? (S/N): ")
    restart = restart.lower()

    if restart == "s":
        print("")
        run()
    else:
        print("")
        print("Gracias por jugar")
if __name__ == "__main__":
    run()
