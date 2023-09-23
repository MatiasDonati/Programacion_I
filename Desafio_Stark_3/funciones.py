# MATIAS EDUARDO DONATI
# DESAFIO STARK 3

from data_stark import lista_personajes
import re

def stark_normalizar_datos(lista_heroes:list):
    '''Recibe una lista, en caso de no estar vacia, cambia datos numericos que sean traidos de modo "str" a "int" o "float" segun corresponda. Devuelve un Boolean'''
    respuesta = False

    if len(lista_heroes) == 0:
        return respuesta

    for heroes in lista_heroes:
        for clave, valor in heroes.items():
            if type(valor) != int and type(valor) != float:
                if re.match(r'^[0-9]+\.[0-9]+$', valor):
                    heroes[clave] = float(valor)
                    respuesta = True
                elif re.match(r'^[0-9]+$', valor):
                    heroes[clave] = int(valor)
                    respuesta = True

    return respuesta

def obtener_dato(heroe:dict):
    '''Recibe en diccionario, de no estar vacio, busca si posee la clave "nombre". Devulve un Boolean'''
    respuesta = False

    if len(heroe) == 0:
        return respuesta

    for clave_recorrida in heroe:

        if re.search(r'\bnombre\b', clave_recorrida):
            respuesta = True

    return respuesta

def obtener_nombre(heroe:dict):
    '''Recibe un diccionario, de no estar vacio retorna mensaje con nombre. Caso contrario "False"'''

    if obtener_dato(heroe):
        respuesta = f"Nombre: {heroe['nombre']}"
    else:
        respuesta = False

    return respuesta

def obtener_nombre_y_dato(heroe:dict, clave:str):
    '''Recibe un diccionario y una clave"str", de no ser vacio, devuelve un mensaje con los datos. Caso contrario "False"'''
    respuesta = False
    nombre = obtener_nombre(heroe)
    if nombre:
        respuesta = f"{nombre} | {clave}: {heroe[clave]}"

    return respuesta

def obtener_maximo(lista:list, clave:str):
    '''Recibe una lista y una clave, y calculará la cantidad maxima de esa clave'''
    valor_max = None
    respuesta = False

    # Esto se puede omitir ya q de estar vacia la lista sigue devolviendo Flase, pero lo pide en consigna
    if len(lista) == 0:
        return respuesta

    for heroe in lista:
        if clave in heroe:
            if type(heroe[clave]) == int or type(heroe[clave]) == float:
                if valor_max == None or heroe[clave] > valor_max:
                    valor_max = heroe[clave]
                    nombre= heroe["nombre"]
                respuesta = valor_max
               #  respuesta = f"El mayor valor de {clave} es: {valor_max} del heroe {nombre}"
               # Esta asi para que no falle la funcion obtener_dato_cantidad()

    return respuesta
#Ejecutar siempre el nomrmalizador de datos previo a ejecutar cualquier funcion

def obtener_minimo(lista:list, clave:str):
    '''Recibe una lista y una clave, y calculará la cantidad minima de esa clave'''
    valor_minimo = None
    respuesta = False

    # Omiti validar la lista vacia ya que si se pasa una lista vacia devuelve False.

    for heroe in lista:
        if clave in heroe:
            if type(heroe[clave]) == int or type(heroe[clave]) == float:
                if valor_minimo == None or heroe[clave] < valor_minimo:
                    valor_minimo = heroe[clave]
                    nombre= heroe["nombre"]
                respuesta = valor_minimo
                # respuesta = f"El menor valor de {clave} es: {valor_minimo} del heroe {nombre}"

    return respuesta

def obtener_dato_cantidad(lista:list, valor_a_buscar:int or float, clave:str):
    '''Recibe una lista, un numero y una clave. El numero será utilizado para encontrar personajes que tengan ese valor en la clave indicada.'''
    lista_persaonjes_filtrados = []
    for heroe in lista:
        if heroe[clave] == valor_a_buscar:
            lista_persaonjes_filtrados.append(heroe)

    return lista_persaonjes_filtrados

# # Para probar
# stark_normalizar_datos(lista_personajes)
# mayor_valor = obtener_maximo(lista_personajes, "fuerza")
# minimo_valor = obtener_minimo(lista_personajes, "altura")
# print(obtener_dato_cantidad(lista_personajes, minimo_valor, "altura"))
# print(obtener_dato_cantidad(lista_personajes, mayor_valor, "fuerza"))

def stark_imprimir_heroes(lista:list):
    '''Recibe una lista de personajes y muestra cada personaje '''
    respuesta = False
    if len(lista) == 0:
        return respuesta
    for heroe in lista:
        print()
        for clave ,valor in heroe.items():
            print(f"{clave.capitalize()}: {valor}")

# # Para Probar
# stark_normalizar_datos(lista_personajes)
# mayor_valor = obtener_maximo(lista_personajes, "fuerza")
# lista_mayor_altura = obtener_dato_cantidad(lista_personajes, mayor_valor, "fuerza")
# stark_imprimir_heroes(lista_mayor_altura)

def sumar_dato_heroe(lista:list, clave:str):
    '''Recibe una lista de heroes y un clave(str). Se sumaran todos los valores de la clave pasada por parametro de toda la lista.'''
    respuesta = False
    suma_total = 0
    for heroe in lista:
        if len(heroe) == 0 or type(heroe) != dict:
            return respuesta
        suma_total += heroe[clave]

    return suma_total

# # Para Probar
# stark_normalizar_datos(lista_personajes)
# suma_fuerzas = sumar_dato_heroe(lista_personajes, "fuerza")
# print(suma_fuerzas)

def dividir(dividendo:int or float, divisor:int or float):
    '''Retorna la division de dos numeros recibidos por parametro'''
    respuesta = False
    if divisor == 0:
        return respuesta
    respuesta = dividendo / divisor

    return respuesta

def calcular_promedio(lista:list, clave:str):
    '''Retorna un promedio. Recibe una lista de heroes y la clave de los valores a promediar'''
    suma = sumar_dato_heroe(lista, clave)
    cantidad = len(lista)
    promedio = dividir(suma, cantidad)
    return promedio

# # Para Probar
# stark_normalizar_datos(lista_personajes)
# print(calcular_promedio(lista_personajes, "fuerza"))

def mostrar_promedio_dato(lista:list, clave:str):

    respuesta = False

    if len(lista) == 0:
        return respuesta

    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float:
            respuesta = True
        else:
            respuesta = False
            return respuesta

    return respuesta

# # PRUEBA
# stark_normalizar_datos(lista_personajes)
# print(mostrar_promedio_dato(lista_personajes, "fuerza"))

def imprimir_menu():
    print('Menu: ')

def validar_entero(numero:str):
    if re.match('^[0-9]+$', numero):
        return True
    else:
        return False
