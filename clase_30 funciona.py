class Cliente:
    banco = "Nacion" #Atributos de clase
    def __init__(self,nom):
        self.nombre = nom 
        self.saldo = 0
    
    def depositar(self,importe):
        self.saldo += importe
        print("Deposito: " + str(importe))
        print("Tiene de saldo: " + str(self.obtener_saldo()))
        #To-Do Verificar que el saldo a depositar sea > 0
        pass  #TO-DO
    def __str__(self):
        cadena = "Nombre: " + self.nombre + " Saldo: " + str(self.saldo)
        return cadena

    def extraer(self,importe):
        self.saldo -= importe
        print("Importe a retirar: " + str(importe))
        print("Tiene de saldo: " + str(self.obtener_saldo()))
        #To-Do, verificar que se puede extraer saldo
#getter
    def obtener_saldo(self):
        return self.saldo

class Banco:
    def __init__(self):
        self.cli1 = Cliente("Ana")
        self.cli2 = Cliente("Juan")
        self.cli3 = Cliente("Maria")
        # clientes = [] #TO-DO
    
    def depositar(self):
        self.cli1.depositar(1000)
        self.cli2.depositar(500)
        self.cli3.depositar(2500)
    def extraccion(self):
        self.cli3.extraer(500)
        self.cli2.extraer(500)
        self.cli1.extraer(10500)

    def saldo(self):
        print(self.cli3.obtener_saldo())
    
    def __str__(self):
        cadena = str(self.cli1) + "\n" + str(self.cli2) + "\n" + str(self.cli3)
        return cadena
#Bloque Principal

banco1 = Banco()
banco1.depositar()
banco1.extraccion()
banco1.saldo()
print(banco1)