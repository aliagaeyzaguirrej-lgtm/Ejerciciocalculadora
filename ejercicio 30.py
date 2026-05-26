hora= float(input("Ingrese cuantas horas estuvo en el estacionamiento: "))
if hora <= 0:
    print("Error")
print("OPCIONES")
print("A. auto")
print("B. moto")
print("C. camion")
transporte = input("Ingrese el tipo de transporte de las opciones")
match transporte :
    case "A":
        print("El costo es de $2 por hora")
        print("Si estuvo mas de 8 horas tiene un 0.10 de descuento ")
        if hora >= 8:
              hora = hora * 2 - 0.10
              print(f"Su factura total con el 0,10 porciento es {hora}")
              
        
        hora = hora * 2
        print(f"Su factura total es de ${hora}")
    case "B":
        print("El costo es de $5 por hora")
        print("Si estuvo mas de 8 horas tiene un 0,10 porciento de descuento")
        if hora >=8:
            hora =hora*5-0.10
            print(f"Su factura total con descuento es de ${hora}")
        hora = hora * 5
        print(f"Su factura total es de ${hora}")
    case "C":
        print("El costo es de $10 por hora")
        print("Si estuvo mas de 8 horas tiene un 0,10 porciento de descuento")
        if hora >= 8:
            hora =hora * 10 - 0.10
            print(f"Su factura total con descuento es de ${hora}")
        hora = hora * 10
        print(f"Su factura es de ${hora}")
