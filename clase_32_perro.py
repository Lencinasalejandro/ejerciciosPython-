from clase_32_claseabstracta import Animal

class Perro(Animal):
    
    def mover(self): ##Tiene que llamarlas si o si
        print("El perro se mueve.")
    
    def emitir_sonido(self):  ##Tiene que llamarlas si o si
        super().emitir_sonido() 
        print("Guauuuu")
    

if __name__=="__main__":
    print("Valor de main de la clase perro")
    
