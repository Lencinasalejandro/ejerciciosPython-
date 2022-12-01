def dividir():
    num1=ingresar()
    num2=ingresar()
    
    div=num1/num2
    return div

def ingresar():
    return int(input("Ingrese un numero: "))

#programa ppal

# num1=int(input("Ingrese un numero: "))
# num2=int(input("Ingrese el numero 2: "))
#dividir(num1,num2)

try:
    dividir()
   
except ZeroDivisionError:   #primero resuelvo los errores conocidos
    print("El divisor no puede ser cero (cero).")
except ValueError:          #excepciones conocidas
    print("Debe ingresar un valor numerico.")    

except:                     #Los errores desconocidos/genericos se resuelven ultimos
    print("Ocurrio un error!.")
