num1 = float(input("ingrese un numero"))
num2 = float(input("ingrese el siguiente numero"))
operacion= input("ingrese la operacion que quiera realizar +, -, *, /")

if operacion == "+":
    resultado = num1+ num2
    print(f"el resultado es {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"el resuultado es {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"el resultado es {resultado}")
elif operacion == "/":
    if num2 == 0:
        print("Error no se puede dividir entre 0")
    else:
        resultado = num1 / num2
        print(f"el resuktado es {resultado}")
else:
    print("error introdusca un valor valido")
