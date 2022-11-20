
#Ejercicio 01

def solo_mayor(num1,num2,num3):
    if(num1>0):
        if(num2>0):
            if(num3>0):
                if(num1>num2):
                    if(num1>num3):
                        return(num1)
                    elif(num1==num3):
                        return(-1)
                    else:
                        return(num3)
                elif(num1==num2):
                    if(num1>num3):
                        return(-1)
                    elif(num1==num3):
                        return(-1)
                    else:
                        return(num3)
                else:
                    if(num2>num3):
                        return(num2)
                    elif(num2==num3):
                        return(-1)
                    else:
                        return(num3)
            else:
                print("El tercer numero ingresado fue menor o igual a cero.")
                return(-1)
        else:
            print("El segundo numero ingresado fue menor o igual a cero.")
            return(-1)
    else:
        print("El primer numero ingresado fue menor o igual a cero.")
        return(-1)

print("Ingrese 3 numeros mayores a cero:")
primer_numero=int(input("Ingrese el primero: "))
segundo_numero=int(input("Ingrese el segundo: "))
tercer_numero=int(input("Ingrese el tercero: "))

resultado=solo_mayor(primer_numero,segundo_numero,tercer_numero)

if(resultado<0):
    print("No se hallo un maximo estricto entre los tres numeros ingresados.")
else:
    print(f'El maximo entre los tres valores ingresados fue {str(resultado)}.')

#Ejercicio 02

