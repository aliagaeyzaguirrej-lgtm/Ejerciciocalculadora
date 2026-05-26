class Cliente:  # La clase de cliente
    def __init__(self, rut, nombre, apellido, monto_de_apertura):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.monto_de_apertura = monto_de_apertura
        self.contraseña = None  # La contraseña tiene un espacio vacio

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} | RUT: {self.rut} | Saldo: ${self.monto_de_apertura}"
    
    def establecer_password(self, nueva_password):
        self.contraseña = nueva_password

    def verificar_password(self, intento):
        # utilizamos la funcion def para el password
        return self.contraseña == intento

# El diccionario vacio para almacenar los nuevos usuarios
registro_clientes = {}

def registrar_cliente():
    print("\n--- NUEVO REGISTRO ---")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese su apellido: ")
    rut = input("Ingrese su rut: ")
    
    # Validamos que el monto sea un número
    try:
        monto = float(input("Ingrese monto de apertura: "))
    except ValueError:
        monto = 0.0
        print("Monto no válido, se registró como 0.0")

    # 1. Creamos la instancia del objeto
    nuevo_usuario = Cliente(rut, nombre, apellido, monto)
    
    # 2. Pedimos y establecemos la contraseña
    pw = input("Ingrese una contraseña: ")
    nuevo_usuario.establecer_password(pw)
    
    # 3. Guardamos el OBJETO en el diccionario usando el RUT como clave
    registro_clientes[rut] = nuevo_usuario
    print("Usuario registrado con éxito.")
if __name__ == "__main__":
    registrar_cliente()
    
    # Probamos si realmente se guardó
    print("\n--- DATOS DEL CLIENTE ---")
    for rut_clave in registro_clientes:
        print(registro_clientes[rut_clave])