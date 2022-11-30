class Vehiculo():
    def __init__(self):
        self.color=input("Ingrese el color del vehiculo: ")
        self.ruedas=int(input("Ingrese la cantidad de ruedas: "))
    
    def __str__(self):
        return (f'\nEl vehiculo es {self.color} y tiene {self.ruedas} ruedas.\n')
        
class Coche(Vehiculo):
    def __init__(self):
        super().__init__()
        self.velocidad=int(input("Ingrese la velocidad del vehiculo: "))
        self.cilindrada=int(input("Ingrese la cilindrada del vehiculo: "))
    
    def __str__(self):
        return super().__str__() + (f'Su velocidad es {self.velocidad} y su cilindrada es {self.cilindrada}.\n')   

class Camioneta(Vehiculo):
    def __init__(self):
        super().__init__()
        self.carga=int(input("Ingrese la carga maxima del vehiculo: "))
    
    def __str__(self):
        return super().__str__() + (f'Su carga maxima es {self.carga}.\n')   

    
class Bicicleta(Vehiculo):
    def __init__(self):
        super().__init__()
        while True:
            self.tipo=input("Ingrese si es Urbana o Deportiva: ")
            if (self.tipo!="Urbana" and self.tipo !="Deportiva"):
                print("El tipo ingresado fue incorrecto.")
            else:
                break
    
    def __str__(self):
        return super().__str__() + (f'La bicicleta es {self.tipo}.\n')   


class Moto(Vehiculo):
    def __init__(self):
        super().__init__()
        self.velocidad=int(input("Ingrese la velocidad del vehiculo: "))
        self. cilindrada=int(input("Ingrese la cilindrada del vehiculo: "))
    
    def __str__(self):
        return super().__str__() + (f'La velocidad de la moto es {self.velocidad} y su cilindrada es {self.cilindrada}.\n')   


if __name__=='__main__':
    
    listado=[]

    listado.append(Coche())
    print (listado[0])
    listado.append(Camioneta())
    listado.append(Bicicleta())
    print(listado[2])
    listado.append(Moto())
    
    for elemento in listado:
        print(elemento)

