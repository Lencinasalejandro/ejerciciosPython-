cadena = "hola comision 22535"
print ("cadena es del tipo",type(cadena))
print("cadena[2] tiene guardado un",cadena[2])
print('la longitud de cadena es',len(cadena))

for i in range (0,len(cadena)):
    print(cadena[i])

print ("22353 esta en la posicion",cadena.find("22535"))
print ("comi esta en la posicion",cadena.find("comi"))

for valor in cadena:
    if not valor.isnumeric():
        print(valor)

print(cadena)
cadena = cadena.replace("hola","bienvenido")
print("Reemplazo 'hola' por 'bienvenido'")
print(cadena)

print(cadena.capitalize())
print(cadena)
print(cadena.upper())

cadena = cadena.replace("bienvenido"," bienvenido")
print("cadena con espacio adelante",cadena)
print("cadena sin espacio adelante",cadena.strip()) #strip quita primer y ultimo espacio

cadena_vacia=""
print(type(cadena_vacia))
print(len(cadena_vacia))
cadena_vacia=125
print(cadena[1])
print(type(cadena_vacia))

repeat="ja"*10
print(repeat)

multilinea="""Muchas
lineas de
la misma
cadena
multilinea"""

print(multilinea)

print (3 +5)
print("3"+"5")
print("3","5")
print(str(3)+"5")

cadena1="Bola"
cadena2="Codo a codo"
if(cadena1<cadena2):
    print("cadena1 es alfabeticamente menor a cadena2")
if(cadena1>cadena2):
    print("cadena1 es alfabeticamente mayor a cadena2")
print("B" in cadena1)


print(cadena[3:11])

print(" -0- ".join(cadena1))

#listas/array

numeros=[1,2,3,4,5]
palabras=["hola","como","estas","amigo"]
lista_vacia=[]
print(type(numeros))
print(type(lista_vacia))

for value in palabras:
    print(len(value))


print(palabras[3].upper())


for i in range (len(numeros)):
    print(numeros[i]*i)

palabras.insert(1,"bolas")
print(palabras)

palabras.append("agrego")
print(palabras)

palabras.pop()
print(palabras)

palabras.remove("bolas")
print(palabras)

palabras.sort(reverse=True) #ver
print(palabras)

print(numeros.sort()) #ver

print(palabras.count("como"))

#matriz lista de listas

matriz=[[1,2],[8,9]]

print(matriz[1])
print(matriz[1][0])

dias=["Lunes","Martes","Miercoles","Jueves","Viernes"]
d1,d2,d3,d4,d5=dias
print(d1)
print(d2)
print(d3)

#Diccionario dic:{clave:valor, clave2:valor2}
dic0={} #vacio
dic={"Ramiro":39,"Luciano":32,"Ale":40}
dic2={"Ramiro":"Perez","Luciano":"Signorelli","Ale":"Lencinas"}
print (dic)
print(dic["Ale"])
for clave in dic:
    print(clave,dic[clave])
    print(dic[clave])
    
for clave in dic2:
    print(dic2[clave])

#for clave in dic2.values():
#    print(dic2[clave])

#TUPLAS
fecha=(10,22,2022)
print(fecha)
dia,mes,anio=fecha
print(dia)
print(mes)
print(anio)

tupla=(10,"Noviembre",2022,"Comision 22535")
print(tupla[1])

for elem in tupla:
    print(elem)

tupla2=("Palotes","Juan",(1982,11,7),29699486)
apellido,nombre,nac,dni=tupla2

conjunto={1,24,3,-5,7,16,9,-2,4,6}
print(conjunto) 
