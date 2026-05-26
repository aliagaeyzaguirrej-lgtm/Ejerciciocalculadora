variable= input("ingrese una palabra")
contador= 0
for i in variable:
    if i == "a":
        contador += 1
    if contador == 3:
        print(" mecanica alcanzada")
    else :print("no se puede ejecutar")