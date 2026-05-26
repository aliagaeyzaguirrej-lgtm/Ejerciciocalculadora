print("Bienvenido")
print("admin, cliente, retiro")
select = input("ingrese una opcion: ")
if select == "admin":
    print("---Administrador---")
    adm = "ADRIAN ALIAGA"
    ps = "admin123"
#pide al administrador que ingrese con su cuenta ya registrada
    ad = ""
    while not ad == adm:
        ad = input("ingrese el usuario: ").upper()
        if ad == adm:
            print(f"bienvennido {adm}")
            break
        else:
            print("usuario no encontrado, vuelva a intentarlo")
    cntrad = ""
    while not cntrad == adm:
        cntrad = input("ingrese su contraseña: ")
        if cntrad == ps:
            print("contraseña correcta")
            print("ingresando")
            break
        else:
            print("contraseña incorrecta, vuelva a intentarlo")
        
elif select == "cliente":
    print("---INGRESANDO A CLIENTES---")
    print ("crea tu usuario")
    class usuario:
        def __init__ (self, rut, nombre, apellido, monto_de_apertura ):
            self.nombre = nombre
            self.apellido = apellido
            self.rut = rut
            self.monto_de_apertura= monto_de_apertura
        def __str__(self):
            return f"{self.nombre} {self.apellido} (RUD{self.rut}) {self.monto_de_apertura}"
    clien = {}
    def clientes ():
        print("nuevo registro")
        nombre = input("ingrese nombre: ")
        apellido = input("ingrese su apellido: ")
        rut = input("ingrese su rut: ")
        montodeapertura =input("ingrese un monto de apertura: ")

    nuevo_usuario = usuario(nombre, apellido, rut)
    #ya esta creando su usuario del cliente
    nuevo_usuario[rut] = nuevo_usuario
    