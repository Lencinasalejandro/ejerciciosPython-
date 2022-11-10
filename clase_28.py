#Funciones

#primero definirlas antes de llamarlas
#def funcion():
#   instrucciones
#   return()

def saludar():
    print("Hola comision 22535 \n")

def saludar2(nombre):
    saludar()
    print("Hola",nombre,"\n")

def imprimir(n,msj):
    for i in range(n):
        print(msj+ str(i))

def suma(a,b):
    return(a+b)

#por valor
def doblar_valor(numero):
    numero*=2
    print("el valor en la funcion es",numero)

#por referencia
def doblar_valores(numeros):
    for i in range(len(numeros)):
        numeros[i]*=2
    

#devolver 2 variables con return
def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3




#-----------------------------------------------------------------------------
#Codigo principal
saludar()

saludar2("Ale")

imprimir(4,"Wenasss")

resultado=suma(7,2)
print("La suma dio",resultado)

n=10
doblar_valor(n)
print("el valor luego de la funcion es",n)

num=[12,2,3]
print("el valor antes de la funcion es",num)  
doblar_valores(num)
print("el valor luego de la funcion es",num)

cuadrado, cubo = cuadrado_y_cubo(2)
print("Cuadrado:", cuadrado)
print("Cubo:", cubo)
