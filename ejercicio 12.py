energia_total = 0
meta_de_energia= 100
while energia_total <= meta_de_energia:
    print (input(f"Energia actual: {energia_total}/{meta_de_energia} "))
    carga = int(input("ingrese cantidad de energia para cargar. "))
    if carga <= 0:
        print("no se puede colocar numeros negativos")
        continue
    energia_total += carga
    if energia_total < meta_de_energia :
        print(f"sigue cargando.. falta {meta_de_energia - energia_total} unidades")
    else:
       print("energia completa ")
       print("despegando en 3, 2, 1")
       break
    


    
        
    
    