energia_total = 0
a_lograr = 100
while energia_total < a_lograr:
    print(f"la energia esta {energia_total} / {a_lograr} unidades.")
    carga = int(input("ingrese cantidad de combustible disponible"))
    energia_total += carga
    if carga < 0:
        print("no se permiten numeros negativos")
        continue
    if energia_total < a_lograr:
        print(f"aun no podemos despegar faltan {energia_total - a_lograr} unidades")
    else:
        print ("listos para despegar")
        print("despegando en 3, 2, 1...")
        break