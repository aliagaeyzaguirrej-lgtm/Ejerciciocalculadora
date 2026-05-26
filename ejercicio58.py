billetes_disponibles = (10000,5000,2000,1000 )
monto = float(input("ingrese la cantidad a retirar: "))
if monto < 1000:
    print("el valor que ingreso es menor al minimo de billetes: $1000,")
else:
    for billetes in billetes_disponibles:
        entrega =  monto // billetes
        if entrega > 0:
            print(f"Seria {entrega} billetes de {billetes}")
        monto = monto % billetes

    if monto > 0:
        print(f"Precausion no se le puede entregar {monto} por falta de billetes mas chicos")
