# Definimos la estructura básica del cliente
class Cliente:
    def __init__(self, rut, nombre, apellido, saldo, password=None):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = float(saldo)
        self.password = password

# Diccionario global para guardar a los clientes (llave: RUT)
# Lo inicializamos vacío como pide el esquema
banco_datos = {}