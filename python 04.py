class Vehiculo():
    color=input("Ingrese el color del vehiculo: ")
    ruedas=int(input("Ingrese la cantidad de ruedas: "))
    
class Coche(Vehiculo):
    velocidad=int(input("Ingrese la velocidad del vehiculo: "))
    cilindrada=int(input("Ingrese la cilindrada del vehiculo: "))
    
class Camioneta(Coche):
    carga=int(input("Ingrese la carga maxima del vehiculo: "))
    
class Bicicleta(Vehiculo):
    while True:
        tipo=input("Ingrese si es Urbana o Deportiva: ")
        if (tipo!="Urbana" and tipo !="Deportiva"):
            print("El tipo ingresado fue incorrecto.")
        else:
            break

class Moto(Bicicleta):
    velocidad=int(input("Ingrese la velocidad del vehiculo: "))
    cilinddrada=int(input("Ingrese la cilindrada del vehiculo: "))
    
listado=[]

listado.append(Coche())
listado.append(Camioneta())
listado.append(Bicicleta())
listado.append(Moto())

print(vehiculos)

