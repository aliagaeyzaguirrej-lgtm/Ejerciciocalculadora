print("bienvanidos a la calculadora")
print("para salir escriba salir")
print("las operaciones son suma, resta, multi, div")
resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingrese operación: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese operación: ")
    if n2.lower() == "salir":
        n2 == int(n2)
        break
    n2 = int(n2)
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("operación no valida")
        break
    print(f"El resultado es {resultado}")
    