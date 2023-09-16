from funciones import *

inciso_2 =  "Pedir un número entero."
inciso_3 = "Validar numero que el número esté entre -500 y 500"
inciso_4 =  "En una función cargar una lista de 20 números a partir de números aleatorios generados desde -1000 a 1000 pero agregar a la lista solamente números entre -500 y 500"
# Con la lista generada en el punto anterior realizar los siguientes puntos.
inciso_5 = "Crear una función que determina mediante un booleano si el número es par o impar"
inciso_6 = "Crear una función que determina mediante un booleano si el número es positivo o negativo"
inciso_7 =  "Crear una función que determine la sumatoria de los pares de la lista."
inciso_8 =  "Crear una función que encuentre el mayor de los impares."
inciso_9 =  "Crear una función que encuentre el menor de los pares"
inciso_10 =  "Crear una función que devuelva un diccionario con mayor de los impares, menor devlos pares y el promedio de los números en la lista."
inciso_11 =  "Crear una función que muestre cada uno de los puntos anteriormente definidos."

flag = True
while flag:
    opcion_elegida = input(f"""\n-2 - {inciso_2} \n-3 - {inciso_3}\n-4 - {inciso_4}\n-5 - {inciso_5}\n-6 - {inciso_6}\n-7 - {inciso_7}\n-8 - {inciso_8}\n-9 - {inciso_9}\n-10 - {inciso_10}\n-11 - {inciso_11}\n-0 - SALIR\nElija la opcion que quiera conocer: """)

    match opcion_elegida:
        case '2':
            pedir_numero()
        case '3':
            print(validar_numero(pedir_numero()))
        case '4':
           lista_numeros = generar_numeros_aleatorios()
           print(lista_numeros)
        case '5':
            for numero in lista_numeros:
                if determinar_par_o_impar(numero):
                    par_o_impar = "Par"
                else:
                    par_o_impar="Impar"
                print(f"El numero {numero} es {par_o_impar}")
        case '6':
            for numero in lista_numeros:
                if determinar_positivo_o_negativo(numero):
                    positivo_o_negativo = "Positivo"
                else:
                    positivo_o_negativo = "Negativo"
                print(f"El numero {numero} es {positivo_o_negativo}")
        case '7':
            print(f"La suma de los pares es: {sumar_pares(lista_numeros)}")
        case '8':
            print(f"El mayor de los impares es: {encontrar_al_mayor_impar(lista_numeros)}")
        case '9':
            print(f"El menor de los pares es: {encontrar_al_menor_par(lista_numeros)}")
        case '10':
           diccionario = crear_diccionario(lista_numeros)
           for clave, valor in diccionario.items():
               print(f"{clave}: {valor}")
        case '11':
           pass
        case '0':
            print('Hasta Pronto!!!')
            flag = False
        case _:
            print("\nOPCION INCORRECTA\nElija la opcion que quiera conocer: A-B-C-D-E o FIN para salir: ")