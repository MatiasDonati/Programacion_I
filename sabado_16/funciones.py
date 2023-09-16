import random

def pedir_numero():
    numero = int(input(f"Ingrese numero: "))
    return numero

def validar_numero(numero):
    respuesta = False
    if numero > -500 or numero < 500:
        respuesta = True
    return respuesta

def generar_numeros_aleatorios():
    lista_numeros = []
    flag = True

    while flag:

        numero_random = random.randint(-1000, 1000)
        if numero_random > -500 and numero_random < 500:
            lista_numeros.append(numero_random)
        if len(lista_numeros) == 20:
            flag = False

    return lista_numeros

def determinar_par_o_impar(numero):
    respuesta = False
    if numero % 2 == 0:
        respuesta = True

    return respuesta

def determinar_positivo_o_negativo(numero):
    respusta = False
    if numero > 0 :
        respusta = True

    return respusta

def sumar_pares(lista):
    suma_numeros_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            suma_numeros_pares += numero
    return suma_numeros_pares

def encontrar_al_mayor_impar(lista):
    numero_mayor_impar = None
    for numero in lista:
        if numero % 2 == 1:
            if numero_mayor_impar == None or numero > numero_mayor_impar:
                numero_mayor_impar = numero

    return numero_mayor_impar

def encontrar_al_menor_par(lista):
    numero_menor_par = None
    for numero in lista:
        if numero % 2 == 0:
            if numero_menor_par == None or numero < numero_menor_par:
                numero_menor_par = numero

    return numero_menor_par

def crear_diccionario(lista):
    suma_numeros = 0
    for numero in lista:
        suma_numeros += numero
    diccioario = {}
    diccioario["mayor_impar"] = encontrar_al_mayor_impar(lista)
    diccioario["menor_par"] = encontrar_al_menor_par(lista)
    promedio_total = suma_numeros / len(lista)
    diccioario["promedio_total_numeros"] = promedio_total

    return diccioario

def mostrar_puntos_anteriores():
    pass