import math

def run():

    lado_1 = int(input("Ingresa la medida del primer lado en cm: "))
    lado_2 = int(input("Ingresa la medida del segundo lado en cm: "))
    lado_3 = int(input("Ingresa la medida del tercer lado en cm: "))

    if lado_1 == lado_2 == lado_3:
        print("Tienes un triángulo equilatero")
        h = (math.sqrt(lado_1*3))/2
        print("la altura de tu triángulo es: ",h)
        area = ((math.sqrt(3))/4)*(lado_1 ** 2)
        print("El área de tu triángulo es ",area,"cm2")
    
    elif lado_1 == lado_2 != lado_3:
        print("Tienes un triángulo isósceles")
        area = (lado_3*(math.sqrt((lado_1**2)-(lado_3**2/4))))/2
        print("El área de tu triángulo es ",area,"cm2")
    
    elif lado_1 == lado_3 != lado_2:
        print("Tienes un triángulo isósceles")
        area = (lado_2*(math.sqrt((lado_1**2)-(lado_2**2/4))))/2
        print("El área de tu triángulo es ",area,"cm2")

    elif lado_2 == lado_3 != lado_1:
        print("Tienes un triángulo isósceles")
        area = (lado_1*(math.sqrt((lado_2**2)-(lado_1**2/4))))/2
        print("El área de tu triángulo es ",area,"cm2")

    else:
        print("Tienes un triángulo escaleno")
        smp=(lado_1 + lado_2 + lado_3)/2
        area = math.sqrt(smp*((smp-lado_1)*(smp-lado_2)*(smp-lado_3)))
        print("El área del triángulo es: ", area,"cm2")


if __name__ == "__main__":
    run()