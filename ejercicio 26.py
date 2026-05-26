longitud1 = int(input("ingrese la primera longitud"))
longitud2 = int(input("ingrese la segunda longitud"))
longitud3 = int(input("ingrese la tercera longitud"))
if longitud1 == longitud2 == longitud3:
    print("Es un equilatero")
    
elif longitud1 == longitud2 :
    print("Es un Isosceles")
elif longitud1 == longitud3:
        print("Es un isosceles")
elif longitud2 == longitud3:
        print("es isosceles")
elif longitud1 != longitud2 != longitud3:
    print("Es un Escaleno")
    
else:
    print("no es un triangulo")