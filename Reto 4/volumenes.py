import math

def volumen_cilindro():
    print("")
    radio = int(input("Cual es el radio en cm del cilindro?: "))
    print("")
    altura = int(input("Cual es la altura en cm del cilindro?: "))
    print("")
    pi = math.pi
    volumen = pi*(radio**2)*altura
    volumen = round(volumen,4)
    print("El Volumen del cilindro es ",volumen, "cm3")
    print("")

def volumen_cubo():
    print("")
    lado_1 = int(input("Cual es el valor en cm del primer lado?: "))
    print("")
    lado_2 = int(input("Cual es el valor en cm del segundo lado?: "))
    print("")
    lado_3 = int(input("Cual es el valor en cm del tercer lado?: "))
    print("")
    volumen = lado_1 * lado_2 * lado_3
    volumen = round(volumen,4)
    print("El volumen de tu Cubo es de ",volumen, "cm3")
    print("")

def volumen_piramide():
    print("")
    altura = int(input("Cual es la altura en cm de tu piramide?: "))
    print("")
    lado_1 = int(input("Cual es la medida en cm del primer lado de la base de la piramide?: "))
    print("")
    lado_2 = int(input("Cual es la medida en cm del segundo lado de la base de la piramide?: "))
    print("")
    base= lado_1 * lado_2
    volumen = (1/3)*(base * altura)
    volumen = round(volumen,4)
    print("El volumen de tu piramide es: ",volumen, "cm3")
    print("")


menu = """
    Bienvenida a tu calculadora de volumenes

    1- Calcular el volumen de un cilindro
    2- Calcular el volumen de un cubo
    3- Calcular el volumen de una piramide.

    Escoge una opción: """

opcion=int(input(menu))

if opcion == 1:
    volumen_cilindro()
elif opcion ==2:
    volumen_cubo()
elif opcion ==3:
    volumen_piramide()
else:
    print("Selección Invalida. Vuelva a intentar")