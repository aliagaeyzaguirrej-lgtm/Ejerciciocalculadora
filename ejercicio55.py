inventario = {
    "juguete": 20, 
    "autos": 30,
    "frutas" : 40,
    "casas" : 3,
}
print("JUGUETES")
print("AUTOS")
print("FRUTAS")
print("CASAS")
print("SALIR")
opcion = input("ingrese una de las siguientes opciones ").lower()
while opcion != "salir":
    match opcion:
        case "juguete":
            cantidad = int(input("ingrese la cantidad deseada"))
            inventario["juguete"] -= cantidad
            print(f"La cantidad en el inventario de juguete es {inventario["juguete"]}")
            if inventario["juguete"] >= 0 and inventario["juguete"] <= 5:
                print(f"Alerta el articulo solo queda: {inventario['juguete']}")
            elif inventario["juguete"] <= 0:
                print("ya no quedan mas unidades")
                continue

            
        case "autos":
            cantidad = int(input("ingrese la cantidad deseada"))
            inventario["autos"] -= cantidad
            print(f"La cantidad en el inventario de juguete es {inventario["autos"]}")
            if inventario["autos"] >= 0 and inventario["autos"] <= 5:
                print(f"Alerta el articulo solo queda: {inventario['autos']}")
           
        case "frutas":
            cantidad = int(input("ingrese la cantidad deseada"))
            inventario["autos"] -= cantidad
            print(f"La cantidad en el inventario de juguete es {inventario["autos"]}")
            if inventario["autos"] >= 0 and inventario["autos"] <= 5:
                print(f"Alerta el articulo solo queda: {inventario['autos']}")
            
        case "casas":
            cantidad = int(input("ingrese la cantidad deseada"))
            inventario["casas"] -= cantidad
            print(f"La cantidad en el inventario de juguete es {inventario["casas"]}")
            if inventario["autos"] <= 1:
                print(f"Alerta el articulo solo queda: {inventario['autos']}")
            
        case "salir":
            print("saliendo del sistema")
            break




                
            