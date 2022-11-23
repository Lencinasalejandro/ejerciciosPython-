"""Colaboración de clases
Para entender cómo se produce la colaboración entre clases vamos a
desarrollar algunos ejemplos, explicando paso a paso que estamos haciendo.
Enunciado 1:
● Un banco tiene 3 clientes que pueden hacer depósitos y extracciones.
● El banco necesita obtener, al final del día, un reporte de la cantidad de
dinero que sus clientes han depositado.
Del enunciado se deduce que necesitamos objetos de dos clases: clientes y
bancos. Para cada una de estas entidades necesitamos crear un"""

class Cliente():
    banco="Nacion"

    def __init__(self,nombre):
        self.nombre=nombre
        self.saldo=0


    def depositar(self,monto):
        #verificar si el monto es mayor que cero
        self.saldo=self.saldo+monto
        print(f'Deposito {monto}')
        print(f'Tiene  de saldo {self.obtener_saldo()}')
    
    def __str__(self):
        cadena = "Nombre: " + self.nombre + " Saldo: " + str(self.saldo)
        return cadena

    def extraer(self,monto):
        #verificar que se pueda extraer monto mayor a saldo
        self.saldo=self.saldo-monto

    
    def obtener_saldo(self):
        return self.saldo



class Banco():
    def __init__(self):
        self.cliente1=Cliente("Ana")
        self.cliente2=Cliente("Juan")
        self.cliente3=Cliente("Maria")

    def depositar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(500)
        self.cliente3.depositar(2500)

    def extraccion(self):
        self.cliente3.extraer(500)

    def saldo(self):
        print(self.cliente3.obtener_saldo())

    def depositos_totales(self):
        totales= self.cliente1.obtener_saldo() + self.cliente2.obtener_saldo() + self.cliente3.obtener_saldo()
        print (f'El banco tiene un saldo de {totales}')

    def __str__(self):
        cadena = str(self.cliente1) + "\n" + str(self.cliente2)+ "\n" + str(self.cliente3)
        return cadena
        



banco1=Banco()

banco1.depositar()

banco1.extraccion()

banco1.saldo()

banco1.depositos_totales()

print(banco1)