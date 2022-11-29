from clase_32_superclase import Vehiculo

class Auto(Vehiculo):
    def __init__(self, color, ruedas,motor):
        super().__init__(color, ruedas)
        #Vehiculo.__init__(color,ruedas)
        self.motor=motor
        
    def __str__(self) -> str:
        return super().__str__() +"Tipo de motor" +str(self.motor)
    
    def avanzar(self):
        super().avanzar()
        print("El auto avanza.")
        
        
def __main__():
    print("Parte del programa principal")
    
if __name__=='__main__': #Indica el comienzo del codigo principal
    __main__()
    