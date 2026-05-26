nota = int(input("ingrese la nota del alumno"))
if nota >= 90 and nota <= 100:
    print("Excelente")
elif nota >= 70 and nota <= 80:
    print("Bueno")
elif nota >=51 and nota <= 60:
    print("Regular")
elif nota >= 8 and nota <= 51:
    print("Reprobado")
else:
    print("Tiene menos de 8")