x = int(input("Ingrese un número: "))

if x < 0:
    print("El número es negativo.")
else:
    ori = x
    invertido = 0
    while x > 0:
         digi = x % 10
         invertido = invertido * 10 + digi
         x = x // 10

    if invertido == ori:
        print("El número es un palíndromo.")
    else:
        print("El número no es un palíndromo.")

