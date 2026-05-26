# 1. Tupla de billetes (de mayor a menor)
billetes_disponibles = (10000, 5000, 2000, 1000)

print("--- CAJERO AUTOMÁTICO ---")

# 2. Pedimos el monto directamente (asumiendo que el usuario ingresará un número)
monto = int(input("Ingrese el monto que desea retirar: $"))

# 3. Validación básica con IF
if monto < 1000:
    print("Error: El monto mínimo de retiro es $1000.")
else:
    print("\nEntregando el dinero:")
    
    # 4. Bucle FOR para desglosar el dinero
    for billete in billetes_disponibles:
        cantidad_billetes = monto // billete  # División entera
        
        if cantidad_billetes > 0:
            print(f"- {cantidad_billetes} billete(s) de ${billete}")
        
        monto = monto % billete  # El residuo para la siguiente vuelta

    # 5. Validación por si sobran monedas o montos impares
    if monto > 0:
        print(f"\n⚠️ No se pudieron entregar ${monto} por falta de billetes chicos.")