opcion=""
while opcion != "D":
    print("Menu de opciones:")
    print("A. Convertir a dolar")
    print("B. convertir a Euros")
    print("C. convertir a pesos")
    print("D. salir")
    opcion = input("Elige una opcion: ")
    for monto in opcion:
        monto = float(input("Ingrese un monto: "))
        match opcion:
            case "A":
                monto = monto * 9.57
                print(f"En dolares es: {monto} ")
            
            case "B":
                monto = monto * 8.8
                print(f"En euros es: {monto}")
                
            case "C":
                monto = monto * 129.80
                print(f"En peso chileno es: {monto}")
            case "D":
                print("saliendo...")
                break
            case _:
                print("opcion invalida, intenta de nuevo")
                break