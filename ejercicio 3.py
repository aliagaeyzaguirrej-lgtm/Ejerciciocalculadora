producto= input("ingrese nombre del producto ")
cantidad= int(input("ingrese cantidad deseada "))
precio = float(input("ingrese precio unitario"))
valor_del_iva=float(input("ingrese valor del iva"))
precio_total=cantidad * precio + valor_del_iva
print(valor_del_iva)
print(producto,precio_total)

