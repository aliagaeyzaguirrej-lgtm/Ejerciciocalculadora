acumulador_notas = 0.0
contador_alumnos = 0
continuar = "si"
print("---CONTADOR DE NOTAS---")
while continuar == "si":
    nota = float(input("Ingrese la nota del alumno: "))
    acumulador_notas =+ nota
    contador_alumnos += 1
    continuar = input("ingrese 'si' si desea contuar: ")
if contador_alumnos > 0:
    promedio = acumulador_notas / contador_alumnos
    print("/n---REPORTE DE EVALUACION---")
    print(f"Los examenes rendidos son: {contador_alumnos}")
    print(f"la suma total de todas las notas son: {acumulador_notas}")
    print(f"Promedio final de todas las notas son: {round(promedio, 1)}")
else:
    print("/n no se registraron las notas en el sistema ")

