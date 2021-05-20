
def rangos(a,b,c):
    if a < c < b:
        print("Este es un buen número que está dentro de tu rango", c)
    else:
        print("Este numero no esta dentro de tu rango: ", c)
        c = int(input("Ingresa otro número: "))
        rangos(a,b,c)

if __name__ == "__main__":

    a = int(input("Ingresa un número que sea tu limite menor: "))
    b = int(input("Ingresa un número que sea tu limite superior: "))
    c = int(input("Ingresa un número aleatorio: "))
    rangos(a,b,c)