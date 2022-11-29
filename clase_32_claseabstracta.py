from abc import ABC, abstractmethod #se define asi las clases abstractas

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def emitir_sonido(self):
        print("Animal emite sonido")
        
