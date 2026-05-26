numero = int(input("ingrese el numero que quiere la tabla"))
print (f"tabla del {numero}")
for i in range (1,11):
    resultado = i * numero
    print(f"{numero} x {i} = {resultado}")