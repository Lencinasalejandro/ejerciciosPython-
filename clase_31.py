# Define una clase Pelicula que gestione datos de películas
# La clase Película tiene los atributos título, duración y lanzamiento, e
#implementa __str__ para mostrar sus datos.
# Define la clase Catalogo, que administra una lista de películas. Estas
#películas son objetos de la clase Película. Debe implementar los métodos
#mostrar y agregar películas.

"""
class Pelicula():



class Catalogo():
"""

class Cliente():


    def __init__(self,nombre,saldo):
        self.__nombre=nombre
        self._saldo=saldo

    def __str__(self):
        cadena="Nombre: "+self.__nombre +"\nSaldo: "+str(self._saldo)
        return cadena

#1ero getter 2do setter

@property
def obtener_saldo(self):
    return self.__saldo

#@property sera un getter, no modifica el atributo
#@setter.xxxx si modifica el atributo y espera un argumento
#pueden tener igual nombre como "nombre"

@property
def nombre(self):      
    return self.__nombre

@nombre.setter #decoradoresssss
def nombre(self,nombre):
    self.__nombre=nombre
  
def depositar(self, importe):
    self._saldo += importe

def extraer(self, importe):
    self._saldo-=importe

cli=Cliente("ale",150)

print(cli)

print(cli.__nombre)
print(cli.saldo)


