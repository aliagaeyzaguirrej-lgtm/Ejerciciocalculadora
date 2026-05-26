nombre="esternocleidomastoideo"
busqueda ="z"
encontrado=False
for letra in nombre:
    if letra== busqueda:
        encontrado= True
        break
if encontrado:
    print(f"la letra'{busqueda}' si esta en la palabra.")
else:
    print(f"no se encontro la letra.")    