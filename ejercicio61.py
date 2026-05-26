clp = int(input("ingrese el monto para la conversion"))
cambio = (
    ("USD", 0.0090),
    ("BOB", 0.0040),
    ("EURO", 0.40),
    ("ARG", 0.90)
)
for moneda, tipo_cambio in cambio:
    monto_convertido = clp * tipo_cambio
    print(f"{clp} en {moneda} es {monto_convertido}")