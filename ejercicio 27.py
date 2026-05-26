velocidad_carro= int(input("ingrese la velocidad del carro"))
if velocidad_carro <= 20:
    print("Es muy lento")
elif velocidad_carro >= 21 and velocidad_carro <= 60:
    print("velocidad moderada")
elif velocidad_carro >= 61 and velocidad_carro <= 120:
    print("velocidad alta")
else:
    print("multa por exceso de velocidad")

