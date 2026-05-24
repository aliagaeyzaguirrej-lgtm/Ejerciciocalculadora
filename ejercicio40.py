total_galletas = 0
paquetes = 0
meta_paquetes = 3
print("---INICIO DE PRODUCCION---")

while paquetes < meta_paquetes:
    total_galletas += 1
    print(f"en el paquete hay {total_galletas} galletas")
    if total_galletas%4 == 0:
        paquetes += 1
        print(f"paquete {paquetes} completado")
print("n/" + "=" * 25)
print(f"PRODUCCION FINALIZADA")
print(f"total galletas: {total_galletas}")
print(f"total paquetes: {paquetes}")
print("="*25)



