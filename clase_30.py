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


    def depositar(self):
        
        pass #TO-DO
    
    def __str__(self):
        cadena="Nombre " + self.nombre + "saldo " str(self.saldo)
        return f{''}
        return(cadena)

    def extraer(self):
        pass


class Banco():
    def __init__(self) -> None:
        pass