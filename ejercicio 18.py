for almacen in range (1,9):
    producto=input(f"este producto esta vencido? Si/No: ")
    if producto == "si":
        print("retirar el producto del ealmacen")
    elif producto == "no":
        print("el producto puede seguir en el almacen")