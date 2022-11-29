class Vehiculo(): #Clase padre o super clase
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
        
    def __str__(self) -> str:
        return f'Color: {self.color} Ruedas: {self.ruedas}'
    
    def avanzar(self):
        pass
    
    