articulo= input("ingrese el articulo que se hara el proceso: ").upper()
print(f"----{articulo}-----")
juan = float(input("ingrese el valor del juan a dolar: "))
print(f"el yuan sera: {juan}")
precio_de_articulo = float(input("ingrese el valor en unidad del articulo: "))
print(f"el precio unitario del articulo sera: {precio_de_articulo}")
dolar =    precio_de_articulo / juan
print(f"el valor en dolara sera: {dolar} del juan en china")
dolar_a_boliviano = float(input("ingrese el valor al que se acomprado en dolar: ") )
boliviano = dolar * dolar_a_boliviano
print(f"el valor en unidad en bolivia sera: {boliviano}")
impuesto = boliviano * 1.24
print(f"el valor en unidad en boliviano con impuesto sera : {impuesto}")

ganancia = impuesto * 1000
print (f"la ganancia sera {ganancia}")
costo = ganancia * 2
print(f"la venta final sera: {costo}")









