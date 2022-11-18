#Objetos en Python
"""
class Persona:
    def inicilizar(self,nom,edad):
        self.nombre=nom
        self.edad=edad
    def imrpimir(self):
        print("Nombre: " + self.nombre + " Edad: " + str(self.edad))

persona1 = Persona() #instanciando la clase, ahora si es un objeto
persona1.inicilizar("Luciando",25)
persona1.imrpimir()

persona2=Persona()
persona2.inicilizar("Ramiro",46)
persona2.imrpimir()

print(type(persona2))

texto="Hola mundo"
print(type(texto))


class Animal:
    
    def __init__(self,nombre,edad,genero):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero

    def imprimir(self):
        print (f'{self.nombre} tiene {self.edad} años')
        #return f'{self.nombre} tiene {self.edad} años'

    def hablar(self,sonido):
        return f'{self.nombre} dice {sonido}'

perro1=Animal("Negro",2,"canino")
presentarse=perro1.imprimir
ladra=perro1.hablar("guauuuuuuu")
print(hablar)

gato1=Animal("michi",3,"gaturro")
maullido=gato1.hablar("miaauuuuu")
print(hablar)
"""

class Empleado:
    empresa="Google"
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su edad: "))
        self.sueldo=float(input("Igrese su sueldo: "))

    def __str__(self) -> str:
        return f'nombre: {self.nombre} tiene {self.edad} años, sueldo:{self.sueldo}'

    def paga_impuestos(self):
        if(self.sueldo>90000):
            return True
        return False

    def __del__(self):      #ver xq imprime 2 veces???
        print("Dado de baja")


emp1=Empleado()
print(emp1.sueldo)
print(emp1.empresa)
print(emp1.paga_impuestos())

Empleado.empresa="Apple"

emp2=Empleado()
print("el sueldo es",emp2.sueldo)
print("trabaja en ",emp2.empresa)
print("Paga impuestos", emp2.paga_impuestos())

