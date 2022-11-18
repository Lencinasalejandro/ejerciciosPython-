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
    print("el valor en la funcion es",numeros)
    

#devolver 2 variables con return
def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3

#funciones lambda
def cuadrado(num):
    return num**2

# definida como funcion lambda (funciones cortas que entren en un renglon)
# cuadrado = lambda num: num**2
""""
#map para usar con listas, aplica a cada valor de la lista y genera una nueva como resultado
def cuadrado(x):
return x ** 2
def cubo(x):
return x ** 3
enteros = [1, 2, 4, 7]
funciones = [cuadrado, cubo]
for e in enteros:
valores = list(map(lambda x : x(e), funciones))
print(valores)
"""

def suma(a, b):
    """Esta función devuelve la suma de los parámetros a y b.
    Imrpime solo este comentario, es el primero dentro de la funcion"""
    print("Hi")
    """"2do comentario"""
    return a + b

help(suma)

#-----------------------------------------------------------------------------
#Codigo principal
saludar()

saludar2("Ale")

imprimir(4,"Wenasss")

resultado=suma(7,2)
print("\nLa suma dio",resultado)

n=10
doblar_valor(n)
print("el valor luego de la funcion es",n,"\n")

num=[12,2,3]
print("el valor antes de la funcion es",num)  
doblar_valores(num)
print("el valor luego de la funcion es",num,"\n")

print("el valor antes de la funcion es",num)
doblar_valores (num[:])
print("el valor luego de la funcion es",num,"\n")



cuadrado, cubo = cuadrado_y_cubo(2)
print("\nCuadrado:", cuadrado)
print("Cubo:", cubo)

