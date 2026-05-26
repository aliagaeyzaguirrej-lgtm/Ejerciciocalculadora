#almacena un usuario unico 
class cliente:
    def __init__ (self, rut, nombre, apellido, monto_de_apertura):
            self.nombre = nombre
            self.apellido = apellido
            self.rut = rut
            self.monto_de_apertura= monto_de_apertura
            self.contraseña = None
    def __str__(self):
            return f"{self.nombre} {self.apellido} (RUD{self.rut}) {self.monto_de_apertura}"
    
    def establecer_password(self, nueva_password):
        
        self.contraseña = nueva_password
clien = {}
#deja ingresar al cliente sus datos   
def clientes ():
    print("nuevo registro")
    nombre = input("ingrese nombre: ")
    apellido = input("ingrese su apellido: ")
    rut = input("ingrese su rut: ")
    monto_de_apertura =float(input("ingrese un monto de apertura: "))
    if monto_de_apertura < 0:
         print("no se puede poner numeros menor a 0")
         return
    nuevo_usuario = cliente(rut, nombre, apellido, monto_de_apertura)
    while True:
        pw = input("ingrese una nueva contraseña: ")
        confirm = input("ingrese de nuevo su contraaseña")
        if pw == confirm:
             nuevo_usuario.establecer_password(pw)
             break
        else:
             print("no coinciden vuelva a intentarlo")
    clien[rut] = nuevo_usuario
    print("nuevo usuario creado")
    print(nuevo_usuario)
clientes()
    

