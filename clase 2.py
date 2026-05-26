edad=int(input("ingresar edad: "))
if edad <= 12:
    print("es niño")
elif edad >= 13 and edad <= 17:
    print("es adolecente")
elif edad >= 18 and edad <= 64:
    print("es adulto")
elif edad >= 65:
    print("adulto mayor")

