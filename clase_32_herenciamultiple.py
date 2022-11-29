class A:
    def a(self): #init
        print("ESte met lo heredo de A")
        
    def b(self): #init
        print("ESte met lo heredo de A")
        
class B:
    def b(self): #init
        print("ESte met lo heredo de B")
        
class C(B,A):
    def __init__(self):
        print("Soy clase C")
        
    def c(self):
        print("ESte met lo heredo de C")
    
#programa ppal

if __name__=="__main__":
    print("objeto A: ")
    a1=A()
    a1.a()
    a1.b()
    
    print("objeto B: ")
    b1=B()
    b1.b()
    
    print("objeto C: ")
    c1=C()
    c1.c()
    c1.a()
    c1.b()  #el metodo "b" lo hereda de la clase B xq esta mas a la izq cuando lo instancio (orden de herencia)
    