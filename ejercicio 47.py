class Cliente:
    def _init_(self, rut, nombre, saldo_inicial=0, password=None):
        self.rut = rut
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.password = password  

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        self.saldo -= monto

    
    def verificar_password(self, intento):
        return self.password == intento 