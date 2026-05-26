monedas = (10000, 5000, 2000, 1000)

monto = int(input("ingrese un monto a retirar"))
if monto < 1000:
    print("lo sentimos no tenemos billetes menso de 1000")
else:
    for billete in monedas:
        cantidad_de_billtes = monto // billete
        if cantidad_de_billtes>0:
            print(f"{cantidad_de_billtes} Billetes de {billete}")
        monto = monto % billete
    if monto > 0 :
        print(f"lo sentimos no tenemos cambio de {monto} ")