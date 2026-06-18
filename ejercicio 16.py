nombre="esternocleidomastoideo"
busqueda ="e"
encontrado=False
for letra in nombre:
    if letra== busqueda:
        
        encontrado= True
        break
if encontrado:
    print(f"la letra'{busqueda}' si esta en la palabra. y ")
else:
    print(f"no se encontro la letra.")    