#gestionar entregas, organizar los paquetes por sector y validar que los repartidores tengan permiso (clave unica)
logistica= {
    "Norte": [],
    "Centro" : [],
    "Sur" : [],
}
print("---REGISTRO DE PAQUETES---")

for sector in logistica:
    paquetes_ingresados = input(f"ingrese los paquetes dentro del sector{sector}: ")
    logistica[sector].append(paquetes_ingresados)
    


for sector, paquetes in logistica.items():
    print(f"Sector actual: {sector}")
    if sector == "Centro":
        print("Peligro zona restringida")
        clave_real = "admin123"
        intento = ""
        while intento != clave_real:
                intento = input("ingrese la clave unica: ")
                if intento != clave_real:
                    print("contraseña incorrecta vuelva a intentarlo")
        print("ingreso con exito")
    for p in paquetes:
        print (f"entregando paquete: {p}")
print(f"entrega completa {logistica}")
             
        


