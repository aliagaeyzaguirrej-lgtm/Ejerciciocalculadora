lista_de_tienda=("focos(fragil)" , "tazas(fragil)", "basos ( plastico)")
codigo_real= "123"
print("iniciando escaneo de sistema")
for almacen in lista_de_tienda:
    almacen = input("ingrese el producto que quiere saber su rompibilidad ")
    if almacen == "focos" or "tazas":
        
        print(f"el producto {almacen} es fragil")
    else:
        print("el producto no es fragil")
    password= ""
    while password != codigo_real:
        password=input("ingrese la contraseña")
        if password == codigo_real:
            print("ingreso con exito")
        else:
           print("no fue admitido")
        break


