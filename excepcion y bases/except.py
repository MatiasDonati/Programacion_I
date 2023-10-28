def divide(x, y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("No es posible dividir por cero!")
    else:
        print("El resultado es", resultado)

divide(2,2) #El resultado es 1.0
divide(2,0) #No es posible dividir por cero!

def leer_entero(intentos):
    retorno = None
    for i in range(intentos):
        valor = input("Ingrese un número entero: ")
        try:
            valor = int(valor)
            retorno = valor
            break
        except ValueError:
            print("Error se debe ingresar un número entero")
        finally:
            print('hola')
    return retorno

leer_entero(5)