"""
#Ejercicio 01
class persona():
    nombre=""
    edad=""
    
    def set_nombre(self):
        self.nombre=input("Ingrese el nombre de la persona: ")

    def set_edad(self):
        self.edad=int(input("Ingrese la edad de la persona: "))
        pass

    def get_nombre(self):
        pass

    def get_edad(self):
        pass

    def print_persona(self):
        print("La persona se llama",self.nombre,"y tiene",self.edad,"años.")


persona1=persona()
persona1.set_nombre()
persona1.set_edad()
persona1.print_persona()

persona2=persona()
persona2.set_nombre()
persona2.set_edad()
persona2.print_persona()



#Ejercicio 02 y 03
class persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def get_nombre(self):
        pass

    def get_edad(self):
        pass

    def print_persona(self):
        print("La persona se llama",self.nombre,"y tiene",self.edad,"años.")

    def es_mayor_de_edad(self):
        if(self.edad>=18):
            return True
        else:
            return False

persona1=persona("Ale",40)
persona1.print_persona()
if(persona1.es_mayor_de_edad()):
    print("La persona",persona1.nombre,"es mayor de edad")
else:
    print("La persona",persona1.nombre,"es menor de edad")

persona2=persona("Rose",15)
persona2.print_persona()
if(persona2.es_mayor_de_edad()):
    print("La persona",persona2.nombre,"es mayor de edad")
else:
    print("La persona",persona2.nombre,"es menor de edad")


#Ejercicio 04 y 05

class persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def get_nombre(self):
        pass

    def get_edad(self):
        pass

    def print_persona(self):
        print("La persona se llama",self.nombre,"y tiene",self.edad,"años.")

    def es_mayor_de_edad(self):
        if(self.edad>=18):
            return True
        else:
            return False

    def es_mayor_que(self,persona_x):
        if(self.edad>persona_x.edad):
            print(f'{self.nombre} es mayor que {persona_x.nombre}.')
        elif(self.edad==persona_x.edad):
            print(f'{self.nombre} y {persona_x.nombre} tienen la misma edad.')
        else:
            print(f'{self.nombre} es menor que {persona_x.nombre}.')
    
    @staticmethod
    def get_mayor(persona_x,persona_y):
        if (persona_x.edad>persona_y.edad):
            return persona_x
        else:
            return persona_y

persona1=persona("Ale",40)
persona1.print_persona()
if(persona1.es_mayor_de_edad()):
    print("La persona",persona1.nombre,"es mayor de edad")
else:
    print("La persona",persona1.nombre,"es menor de edad")

persona2=persona("Rose",24)
persona2.print_persona()
if(persona2.es_mayor_de_edad()):
    print(f'La persona {persona2.nombre} es mayor de edad.')
else:
    print(f'La persona {persona2.nombre} es menor de edad.')

persona1.es_mayor_que(persona2)
persona2.es_mayor_que(persona1)

persona3=persona.get_mayor(persona1,persona2)
print(f'La persona de mayor edad fue {persona3.nombre}.')



#Ejercicio 06

class alumno():
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=int(input("Ingrese la nota: "))
        print(f'El alumno {self.nombre} obtuvo la nota {self.nota}.')
    
    def aprueba(self):
        if(self.nota>=4 and self.nota<7):
            print(f'El alumno {self.nombre} esta aprobado.')
        elif(self.nota<4):
            print(f'El alumno {self.nombre} no esta aprobado.')
        else:
            print(f'El alumno {self.nombre} esta promocionado.')


alumno1=alumno()
alumno1.aprueba()

alumno2=alumno()
alumno2.aprueba()

#Ejercicio 7

class triangulo():

    def __init__(self):
        self.lado_a=int(input("Ingrese la longitud del lado A: "))
        self.lado_b=int(input("Ingrese la longitud del lado B: "))
        self.lado_c=int(input("Ingrese la longitud del lado C: "))
    
    def lado_y_tipo(self):
        if(self.lado_a==self.lado_b and self.lado_b==self.lado_c):
            print(f'Todos los lados son iguales y miden {self.lado_a}. \nEl triangulo es equiltero.')
        
        elif(self.lado_a==self.lado_b and self.lado_a>self.lado_c):
            print(f'El lado A y B miden {self.lado_a} y son los mayores. \nEl triangulo es isosceles.')

        elif(self.lado_a==self.lado_b and self.lado_a<self.lado_c):
            print(f'El lado C mide {self.lado_c} y es el mayor. \nEl triangulo es isosceles.')
        
        elif(self.lado_a==self.lado_c and self.lado_a>self.lado_b):
            print(f'El lado A y C miden {self.lado_a} y son los mayores. \nEl triangulo es isosceles.')

        elif(self.lado_a==self.lado_c and self.lado_a<self.lado_b):
            print(f'El lado B mide {self.lado_b} y es el mayor. \nEl triangulo es isosceles.')
        
        elif(self.lado_b==self.lado_c and self.lado_b>self.lado_a):
            print(f'El lado B y C miden {self.lado_b} y son los mayores. \nEl triangulo es isosceles.')

        elif(self.lado_c==self.lado_c and self.lado_b<self.lado_a):
            print(f'El lado C mide {self.lado_a} y es el mayor. \nEl triangulo es isosceles.')



        elif(self.lado_a>self.lado_b and self.lado_b>self.lado_c):
            print(f'El lado A mide {self.lado_a} y es el mayor. \nEl triangulo es escaleno.')
        
        elif(self.lado_a>self.lado_c and self.lado_b<self.lado_c):
            print(f'El lado A mide {self.lado_a} y es el mayor. \nEl triangulo es escaleno.')

        elif(self.lado_b>self.lado_a and self.lado_a>self.lado_c):
            print(f'El lado B mide {self.lado_b} y es el mayor. \nEl triangulo es escaleno.')
        
        elif(self.lado_b>self.lado_a and self.lado_a<self.lado_c):
            print(f'El lado B mide {self.lado_b} y es el mayor. \nEl triangulo es escaleno.')
        
        elif(self.lado_c>self.lado_a and self.lado_a>self.lado_b):
            print(f'El lado C mide {self.lado_c} y es el mayor. \nEl triangulo es escaleno.')
        
        elif(self.lado_c>self.lado_b and self.lado_a<self.lado_b):
            print(f'El lado C mide {self.lado_c} y es el mayor. \n El triangulo es escaleno.')
               
           
triangulo1=triangulo()

triangulo1.lado_y_tipo()

#Ejercicio 8

class Calculadora():
    def __init__(self):
        self.num1=int(input("Ingrese el primer numero: "))
        self.num2=int(input("Ingrese el segundo numero: "))

    def suma(self):
        print(f'La suma de los numeros ingresados es {self.num1+self.num2}')

    def resta(self):
        print(f'La resta de los numeros ingresados es {self.num1-self.num2}')

    def prod(self):
        print(f'El producto de los numeros ingresados es {self.num1*self.num2}')

    def division(self):
        print(f'La division de los numeros ingresados es {self.num1/self.num2}')  

calc=Calculadora()

calc.suma()
calc.resta()
calc.prod()
calc.division()



#Ejercicio 9
#Realizar una clase que administre una agenda. Se debe almacenar para cada
#contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
#con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,
#Editar contacto, Cerrar agenda.

listado=[]

class Contacto():
    def __init__(self):
        self.nombre=input("ingrese el nombre: ")
        self.cel=input("ingrese el telefono: ")
        self.mail=input("ingrese el mail: ")
        
        listado.append(self)

    
    def __str__(self):
        return (f'NOMBRE: {self.nombre} \nTELEFONO: {self.cel}\nEMAIL: {self.mail} \n')

class Agenda():
    
    def __init__(self):
        opcion=8
        
        while(opcion!=5):

            print("\nQue desea hacer?")
            print("Presione 1 para agragar un contacto")
            print("Presione 2 para eliminar un contacto")
            print("Presione 3 para listar los contactos")
            print("Presione 4 para buscar un contacto")
            print("Presione 5 para cerrar la agenda")
            opcion=int(input("\n"))
        
            if(opcion==1):
                con=Contacto()
                print("Contacto agregado.")
                print(con)
                
            elif(opcion==2):
                borrar_ok=False
                i=0
                borrar=input("ingrese el nombre del contacto a eliminar: ")
                for lista in listado:
                    if(lista.nombre==borrar):
                        print("Se encontro el contacto: \n",lista,"\ny sera eliminado")
                        listado.pop(i)
                        borrar_ok=True
                    i+=1
                
                if(not borrar_ok):
                    print("No se encontro contacto con el nombre ",borrar)

            elif(opcion==3):
                for lista in listado:
                    print(lista)
                print("La Agenda tiene ",len(listado)," contactos.")

            elif(opcion==4):
                busqueda_ok=False
                busqueda=input("ingrese el nombre del contacto: ")
                for lista in listado:
                    if(lista.nombre==busqueda):
                        print("Se encontró informacion para el contacto ",busqueda)
                        print(lista)
                        busqueda_ok=True
                if(not busqueda_ok):
                    print("No se encontro informacion para el contacto ",busqueda)

            elif(opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5):
                print("Ingresó una opcion incorrecta, intentelo de nuevo.")
        print("Gracias por usar la Agenda")


cont1=Contacto()
cont2=Contacto()

print(cont1)

print(listado[1])

agenda=Agenda()

"""

#Ejercicio 10

# En un banco tienen clientes que pueden hacer depósitos y extracciones de
# dinero. El banco requiere también al final del día calcular la cantidad de dinero
# que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase
# banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos
# __init__, depositar, extraer, mostrar_total. La clase banco tendrá como
# atributos 3 objetos de la clase cliente y los métodos __init__, operar y
# deposito_total. 

depositos=0

class Cliente():
    def __init__(self,nombre,dinero=0):
        self.nombre=nombre
        self.dinero=dinero

    def depositar(self,cantidad):
        if(cantidad>0):
            self.dinero+=cantidad
            depositos+=cantidad
            print(f'Se ha depositado {cantidad}.')
        else:
            print(f'Ingrese una cantidad mayor a cero.')
    
    def extraer(self,cantidad):
        if(cantidad>self.dinero):
            print(f'No se puede extraer mas dineo del disponible ({self.cantidad}).\nIngrese un monto valido.')
        else:
            self.dinero-=cantidad
            print(f'Se ha extraido {cantidad}.')

    def mostrar_total(self):
        print(f'El saldo es {self.dinero}.')

    def __str__(self):
        cadena="Nombre: "+self.nombre+"\nSaldo: "+str(self.dinero)
        return("")

class Banco():
    def __init__(self):
        self.cli1=Cliente("Juan",2000)
        self.cli2=Cliente("Ana",2500)
        self.cli3=Cliente("Pedro",1000)
        self.cli4=Cliente("Elsa",3000)

    def deposito_total(self):
        print(f'Se ha depositado {depositos}')

    def operar(self,Cliente):
        print(f'Presione D para depositar.')
        print(f'Presione E para extraer.')
        print(f'Presione M para mostar el saldo total.')
        opcion=input("\n")
        if (opcion=="D"):
            monto=int(input("Ingrese el monto a depositar: "))
            Cliente.depositar(monto)
        elif(opcion=="E"):
            monto=int(input("Ingrese el monto a extraer: "))
            Cliente.extraer(monto)
        elif(opcion=="M"):
            Cliente.mostrar_total()

        else:
            print("Opcion invalida.")



banco1=Banco()

banco1.deposito_total()

""".depositar(500)

banco1.operar(cli1)
banco1.operar(cli2)
banco1.operar(cli3)
"""
banco1.deposito_total()


