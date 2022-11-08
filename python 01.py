"""
#Ejercicio 01
print("hola")

#Ejercicio 02
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
j=int(input("Ingrese un numero: "))
if(j%2):
    print("el numero",j, "no es divisible por 2, IMPAR")
else:
    print("el numero",j, "es divisible por 2, PAR")

#Ejercicio 08
if ((not j%2) or (not j%3) or (not j%5) or (not j%7)):
    print("El numero ",j,"es divisible por 2, 3, 5 o 7") 
else:
    print("El numero",j,"no es divisible por 2, 3, 5 o 7")

#Ejercicio 09
if (j%2 and j%3 and j%5 and j%7):
    print("El numero",j,"no es divisible por 2, 3, 5 o 7")
    #print("El numero ",j," es divisible por 2, 3, 5 o 7") 
else:
    if(not j%2):
        if(not j%3):
            if(not j%5):
                if(not j%7):
                    print("El numero",j,"es divisible por 2, 3, 5 y 7")
                else:
                    print("El numero",j,"es divisible por 2, 3 y 5")
            elif(not j%7):
                print("El numero",j,"es divisible por 2, 3 y 7")
            else:
                print("El numero",j,"es divisible por 2 y 3")
        elif(not j%5):
            if(not j%7):
                print("El numero",j,"es divisible por 2, 5 y 7")
            else:
                print("El numero",j,"es divisible por 2 y 5")
        elif(not j%7):
            print("El numero",j,"es divisible por 2 y 7")
        else:
            print("El numero",j,"es divisible por 2")
    elif(not j%3):
        if(not j%5):
            if(not j%7):
                print("El numero",j,"es divisible por 3, 5 y 7")
            else:
                print("El numero",j,"es divisible por 3 y 5")
        elif(not j%7):
            print("El numero",j,"es divisible por 3 y 7")
        else:
            print("El numero",j,"es divisible por 3")
    elif(not j%5):
        if(not j%7):
            print("El numero",j,"es divisible por 5 y 7")
        else:
            print("El numero",j,"es divisible por 5")
    else:
        print("El numero",j,"es divisible por 7")

#Ejercicio 10
k=int(input("Ingrese un numero: "))
print(k,"es divisible por:")
for i in range(1,10,1):
    if(not k%i):
        print(i)
"""
#Ejercicio 11
"""for i in range (20,-1,-1):
    print (i)"""