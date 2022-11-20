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

"""

#Ejercicio 7