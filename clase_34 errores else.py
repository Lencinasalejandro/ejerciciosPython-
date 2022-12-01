#capturas y manejo de excepciones

try:
    num1=int(input("ingrese un numero: "))      #ValueError
    num2=int(input("ingrese el numero 2: "))    #ValueError
    resultado=num1/num2         #ZeroDivisionError
    
except ZeroDivisionError:   #primero resuelvo los errores conocidos
    print("El divisor no puede ser cero (cero).")
except ValueError:          #excepciones conocidas
    print("Debe ingresar un valor numerico.")    

except:                     #Los errores desconocidos/genericos se resuelven ultimos
    print("Ocurrio un error!.")
    
else:                           #Si no ocurre ningun error 
    print("El resultado de la division es:",resultado)
    
finally:                    #opcional para loggear algun dato
    print("Se ejecuta siempre.")
    
print("Termino el programa!.")

    