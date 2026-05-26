class cliente:# La clase de cliente
    def __init__(self, nombre, apellido, rut, monto_de_apertura):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.monto_de_apertura = monto_de_apertura
        self.password = None
    def __str__ (self):
        return f"bienvenido {self.nombre} {self.apellido} RUT({self.rut}) su monto inicial es {self.monto_de_apertura})"
    def newpassword (self, clave_real):
        self.password = clave_real 
    # utilizamos la funcion def para el password
 # El diccionario vacio para almacenar los nuevos usuarios   
client = {}
def cliente_nuevo ():
    print("--Nuevo Cliente--")
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    rut = input("ingrese su rut: ")
    # Validamos que el monto sea un número si sale otro valor diferente evaluara como error y imprimira que no es valido

    try:
        monto_de_apertura = float(input("Ingrese un monto de apertura: "))
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return
    if monto_de_apertura <= 0:
         print("error no se aceptan numeros negativos")
 
         return
    # 1. Creamos la instancia del objeto
    nuevo_usuario = cliente(nombre, apellido, rut, monto_de_apertura)
    # 2. Pedimos y establecemos la contraseña
    while True:
        pw = input("ingrese una contraseña: ")
        clave_confirm = input("ingrese de nuevo su contraseña: ")
        if pw == clave_confirm:
            nuevo_usuario.newpassword(pw)
            print("las contraseñas coinciden")
            break
        else:
             print("vuelva a intentarlo")
    # 3. Guardamos el OBJETO en el diccionario usando el RUT como clave
    client[rut] = nuevo_usuario
    print("registro con exito")
    print(nuevo_usuario)
cliente_nuevo()

    



                
