lista = []
lista.append(81)
lista.append(40)
lista.append(90)
lista.append(20)
lista.append(51)
for nota in lista:
    if nota >=0 and nota <=50:
        print(f"la nota del alumno es: {nota} esta reprobado")
    elif nota >= 51 and nota <=100:
        print(f"la nota del alumno es: {nota} esta aprobado")
    