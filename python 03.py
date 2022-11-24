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

"""

#Ejercicio 9
"""Realizar una clase que administre una agenda. Se debe almacenar para cada
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,
Editar contacto, Cerrar agenda."""

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
    opcion=8
    def __init__(self):
        while(opcion!=5):
            print("\n Que desea hacer?")
            print("Presione 1 para agragar un contacto")
            print("Presione 2 para eliminar un contacto")
            print("Presione 3 para listar los contactos")
            print("Presione 4 para buscar un contacto")
            print("Presione 5 para cerrar la agenda")
            opcion=input("\n")
        
            if(opcion==1):
                print(len(listado))


cont1=Contacto()
cont2=Contacto()


print(cont1)

print(listado[1])

agenda=Agenda()
