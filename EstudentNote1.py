estudiantes = {}

while True:
    print("\n =======Menu=====")
    print("1. ver todos los estudiantes")
    print("2. Anadir nuevo Estudiante")
    print("3. Anadir/Actulizar nota de estudiante")
    print("4. Calcular promedio de notas de un estudiante ")
    print("5. Salir ")
    
    opcion = input("Elegir una opcion:")
    
    if opcion == "1":
        if len(estudiantes) == 0:
            print("no hay estudiantes")
        else:
            for nombre, notas in estudiantes.items():
                print("\n Estudiante: ", nombre)
                
                if len(notas) == 0:
                    print("No tiene notas registradas")
                else:
                    for asignatura, nota in notas.items():
                        print(asignatura,":", nota)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")
        
        if nombre in estudiantes:
            print("el estudiante ya existe")
        else:
            estudiantes[nombre] = {}
            print("Estudinate anadido correctamento")
            
    elif opcion == "3":
        nombre = input("Ingrese estudiante registrado: ")
        
        if nombre not in estudiantes:
            print("El estudiante no esta registrado")
        else:
            asignatura = input("ingrese su asignatura ")
            
            nota = float(input("Ingrese la nota: "))
            if nota < 0:
                print("la nota no tiene que ser negativa")
            else:
                estudiantes[nombre][asignatura] = nota
                print("Nota anadida o actulizada correctamente.")
    elif opcion == "4":
        nombre = input("Ingrese Nombre del estudiante:")
        if nombre not in estudiantes:
            print("El estudiante no esta registrado")
        else:
            notas = estudiantes[nombre]
            if len(notas) == 0:
                print("el estudiante no tiene notas registradas")
            else:
                suma = 0
                
                for nota in notas.values():
                    suma = suma + nota
                    
                promedio = suma / len(notas)
                print("el promedio es ", nombre, "es: ", promedio)
                
    elif opcion == "5":
        print("Saliendo del progrma")
        break
    else:
        print("Opcion invalida")
        