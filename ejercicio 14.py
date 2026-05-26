frase = input("escribe una frase:").lower()
contador_a=0
for letra in frase:
    if letra == "a":
        contador_a+=1
    print(f'la letra a aparece {contador_a} veces.')    