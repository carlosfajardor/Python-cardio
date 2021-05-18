def km_to_ml(km,ml): 
    millas = km / ml
    millas = round(millas, 2)
    print(km,"Kilometros equivalen a ",millas,"millas")
    print("")


def ml_to_km(km,ml):
    kilometros = km * ml
    kilometros = round(kilometros, 2)
    print(ml,"Millas equivales a ",kilometros,"kilometros")
    print("")

menu = """
Bienvenido a tu calculadora de distancias.

Tenemos 2 opciones de calculo:

1- Convertir Kilometros a millas
2- Convertir Millas a Kilometros

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    distancia = int(input("Cuantos kilometros quieres convertir en millas: "))
    print("")
    km_to_ml(distancia, 1.609344)
elif opcion ==2:
    distancia = int(input("Cuantas millas quieres convertir en kilometros: "))
    print("")
    ml_to_km(distancia, 1.609344)
else:
    print("Opción Invalida. por favor escoga una opción valida")
