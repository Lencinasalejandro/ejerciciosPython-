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

#Ejercicio 11
resp="s"
while(resp=="s"):
    l=int(input("ingrese un numero: "))
    if(l==2 or l==3 or l==5 or l==7):
        print ("El numero",l,"es primo. \n")
    else:
        if(not l%2 or not l%3 or not l%5 or not l%7):
            print ("El numero",l,"no es primo. \n")
        else:
            print("El numero",l,"es primo. \n")
    resp=input("presione s para seguir o cualquier tecla para salir: \n")

#Ejercicio 12

nota=int(input("\nIngrese una nota entre cero y diez (0-10): "))
if (nota>=0 and nota <=3):
    print("\nUsted ingresó",nota)
    print("La nota fue muy deficiente.")
elif(nota>3 and nota <=6):
    print("\nUsted ingresó",nota)
    print("La nota fue suficiente.")
elif(nota>6 and nota <=8):
    print("\nUsted ingresó",nota)
    print("La nota fue notable.")
elif(nota>8 and nota <=10):
    print("\nUsted ingresó",nota)
    print("La nota fue notable.")
else:
    print("\nUsted ingresó",nota)
    print("La nota esta fuera del rango.")

#Ejercicio 13
for i in range(1,31):
    print('\n')
    for k in range(i):
        if (i<10):
            print('0'+str(i)+' ',end='')
        else:
            print(str(i)+' ',end='')



#Ejercicio 14
for i in range(31,0,-1):
    print('\n')
    for k in range(i):
        if (i<10):
            print('0'+str(i)+' ',end='') #end() por defecto es '\n', al llamar end('') se imprime un espacio al final del print
        else:
            print(str(i)+' ',end='')

"""

#Ejercicio 15
linea=0
for i in range(1,501):
    if(linea==5):
        print('-------------------------')
        linea=0
    else:
        if(not i%4):
            print(str(i)+" Multiplo de 4")
            linea += 1
        elif(not i%5):
            print(str(i)+" Multiplo de 5")
            linea += 1
        elif(not i%9):
            print(str(i)+" Multiplo de 9")
            linea += 1
        else:
            print(str(i))
            linea += 1