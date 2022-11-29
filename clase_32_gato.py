from clase_32_claseabstracta import Animal

class Gato(Animal):
    
    def mover(self): ##Tiene que llamarlas si o si
        print("El gato se mueve.")
    
    def emitir_sonido(self):  ##Tiene que llamarlas si o si
        super().emitir_sonido() 
        print("Miauuuu")
    

if __name__=="__main__":
    print("Valor de main de la clase gato")
    
