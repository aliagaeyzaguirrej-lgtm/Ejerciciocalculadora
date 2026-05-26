opcion=""

while opcion !="3":
    print("\n---MENÚ DE OPCIONES---")
    print("1. Saludar")
    print("2. Ver hora")
    print("3. Salir")
    
    opcion = input("Elige una opcion: ")
    
    match opcion:
        case"1":
            print("Hola, programador")
        case "2":
            print("son las 10:00 AM (ejemplo)")
        case "3":
            print("saliendo del programa...")
        case _:
            print("opcion invalida, intenta de nuevo")
            