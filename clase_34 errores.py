#capturas y manejo de excepciones

try:
    num1=int(input("ingrese un numero: "))      #ValueError
    num2=int(input("ingrese el numero 2: "))    #ValueError
    resultado=num1/num2         #ZeroDivisionError
    print(resultado)             #NameError
    
except ZeroDivisionError:   #primero resuelvo los errores conocidos
    print("El divisor no puede ser cero (cero).")
except ValueError:          #excepciones conocidas
    print("Debe ingresar un valor numerico.")    

except:                     #Los errores desconocidos/genericos se resuelven ultimos
    print("Ocurrio un error!.")
    
print("Termino el programa!.")

    