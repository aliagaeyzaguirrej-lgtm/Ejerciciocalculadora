archivos=["a","b","c","x","e","f"]
print("iniciando escaneo de sistema")
for archivo in archivos:
    if archivo == "x":
        print ("peligro virus detectado (x). bloqueando sistema... ")
        break
    print(f"procesando archivo{archivo}...[ok]")
print("fin del reporte")
