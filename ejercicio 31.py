menu =["Pizza","Hamburguesa","Ensalada"]
print(menu)
opciones = input("ingrese opcion de paltillo ")

if opciones == "pizza":
        pizza = input("¿quiere familiar o individual?: ")
        if pizza == "familiar":
            print("preparando pedido")
        elif pizza == "individual":
            print("preparando pedido")
        else:
            print ("no se encuentra")
elif opciones == "hamburguesa":
        hamburguesa = input("¿quiere con queso o sin queso?")
        if hamburguesa == "con queso":
            print("preparando pedido")
        elif hamburguesa == "sin queso":
            print("preparando pedido")
        else:
            print("no se encuentra")
elif opciones == "ensalada":
        print("preparando ensalada fresca")

    