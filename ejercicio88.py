import math
def cuadrado (lado):
    area = lado**2
    perimetro = lado * 4
    return f"el area es {round(area, 2)} y su perimetro es {round(perimetro,2)}"
def circulo(radio):
    area = math.pi*radio**2
    perimetro = 2*math.pi*radio
    return f"el area del circulo es {round(area,2)} y su perimetro es {round(perimetro,2)}"
def triangulo(base, altura, lado):
    area = (base * altura)/2
    perimetro = lado * 3
    return f"el area de un triangulo es {round(area,2)} y el perimetro {round(perimetro,2)}"
def rectangulo (la1, la2):
    area = la1 * la2
    perimetro = la1 + la2 + la1 + la2
    return f"el area de un rectangulo es {round(area,2)} y el perimetro es {round(perimetro,2)}"
while True:
    print("---MENU---")
    print("1.CUADRADO... ")
    print("2.CIRCULO... ")
    print("3.TRIANGULO... ")
    print("4.RECTANGULO... ")
    print("5.SALIR... ")
    opcion = input("Elija que figura que desea calcular su area y perimetro: ")
    if opcion == "1":
        print("---CUADRADO---")
        lado = float(input("introduzca el lado uno de los lados del cuadrado: "))
        if lado <= 0:
            print("el numero no puede ser menor o igual a 0")
        else:

            resultado = cuadrado(lado)
            print(f"resultado es: {resultado}")
    elif opcion == "2":
        print("---CIRCULO---")
        radio = float(input("ingrese el radio del circulo: "))
        if radio <=0:
            print("error el radio no puede ser menor o igual a 0")
        else:
            resultado= circulo(radio)
            print(f"el resultado es: {resultado}")

    elif opcion == "3":
        print("---TRIANGULO---")
        base = float(input("ingrese la base del triangulo: "))
        altura = float(input("ingresa la altura del triangulo: "))
        lado = float(input("ingrese el lado del triangulo: "))
        if base and altura and lado <= 0:
            print("error no puede ingresar valores menores o iguales a 0")
        else:
            resultado = triangulo(base,altura,lado)
            print(f"el resuultado es: {resultado}")

    elif opcion == "4":
        print("---RECTAMGULO---")
        la1 = float(input("ingrese el primer lado del rectangulo: "))
        la2 = float(input("ingrese el segundo lado del rectangulo: "))
        if la1 and la2 <= 0:
            print("error no puede ingresar valores menores o iguales a 0")
        else:
            resultado = rectangulo(la1, la2)
            print(f"el resultado es: {resultado}")
    elif opcion == "5":
        print("saliendo del programa")
        break
    else:
        print("error ingrese una opcion valida")