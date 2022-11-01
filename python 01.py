#Ejercicio 01
print("hola")

"""Ejercicio
    02"""
a=3
b=5
print("La suma de a + b es ",(a + b))

#Ejercicio 03
c=input("Ingrese el nombre de usuario: ")
print("El nombre de usuario es:",c)

#Ejercicio 04
d=int(input("Ingrese un numero: "))
e=int(input("Ingrese otro numero: "))
print("La suma de los numero ingresados es:",d+e)

#Ejercicio 05
if(d>e):
    print("El primero es mayor que el segundo")
elif (d<e):
    print("El segundo es mayor que el primero")
else:
    print("Los numeros son iguales")

#Ejercicio 06
print("Ingrese tres numeros")
f=int(input("Primer numero: "))
g=int(input("Segundo numero: "))
h=int(input("Tercer numero: "))

if(f>g):
    if(f>h):
        print("El primer numero fue el mayor",f)
    elif(f==h):
        print("El primero y tercero son los mayores",f,h)
    else:
        print("El tercer numero fue el mayor",h)
else:
    if(f==g):
        print("El primero y el segundo son los mayores",f,g)
    elif(g>h):
        print("El segundo fue el mayor",g)
    else:
        print("El segundo y tercero son los mayores",g,h)

#Ejercicio 07

