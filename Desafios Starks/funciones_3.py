import re

# MATIAS EDUARDO DONATI
# DESAFIO STARK 3

def stark_normalizar_datos(lista_heroes:list)->bool:
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

def obtener_dato(heroe:dict, clave="nombre")->dict or False:
    '''Recibe un diccionario, de no estar vacio, busca si posee la clave "nombre". Devuelve el diccionario caso contrario False'''
    respuesta = False

    if len(heroe) == 0:
        return respuesta

    for clave_recorrida in heroe:

        if re.search(rf'\b{clave}\b', clave_recorrida):
            respuesta = heroe

    return respuesta

def obtener_nombre(heroe:dict)->str or False:
    '''Recibe un diccionario, de no estar vacio retorna mensaje con nombre. Caso contrario "False"'''

    if obtener_dato(heroe):
        respuesta = f"Nombre: {heroe['nombre']}"
    else:
        respuesta = False

    return respuesta

def obtener_nombre_y_dato(heroe:dict, clave:str)->str or False:
    '''Recibe un diccionario y una clave"str", de no ser vacio, devuelve un mensaje con los datos. Caso contrario "False"'''
    respuesta = False
    nombre = obtener_nombre(heroe)
    if nombre:
        respuesta = f"{nombre} | {clave}: {heroe[clave]}"

    return respuesta

def obtener_maximo(lista:list, clave:str)-> int or float or False:
    '''Recibe una lista y una clave, y calculará la cantidad maxima de esa clave'''
    valor_max = None
    respuesta = False

    if len(lista) == 0:
        return respuesta

    for heroe in lista:
        if clave in heroe:
            if type(heroe[clave]) == int or type(heroe[clave]) == float:
                if valor_max == None or heroe[clave] > valor_max:
                    valor_max = heroe[clave]
                    nombre= heroe["nombre"]
                respuesta = valor_max

    return respuesta

def obtener_minimo(lista:list, clave:str)-> int or float or False:
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

    return respuesta

def obtener_dato_cantidad(lista:list, valor_a_buscar:int or float or str, clave:str)->list:
    '''Recibe una lista, un valor(int, float o str) y una clave. El numero será utilizado para encontrar personajes que tengan ese valor en la clave indicada.'''
    lista_persaonjes_filtrados = []
    for heroe in lista:
        if heroe[clave] == valor_a_buscar:
            lista_persaonjes_filtrados.append(heroe)

    return lista_persaonjes_filtrados

def stark_imprimir_heroes(lista:list)->print or False:
    '''Recibe una lista de personajes y muestra cada personaje '''
    respuesta = False
    if len(lista) == 0:
        return respuesta
    for heroe in lista:
        print()
        for clave ,valor in heroe.items():
            print(f"{clave.capitalize()}: {valor}")

def sumar_dato_heroe(lista:list, clave:str)->int or float or False:
    '''Recibe una lista de heroes y un clave(str). Se sumaran todos los valores de la clave pasada por parametro de toda la lista.'''
    respuesta = False
    suma_total = 0
    for heroe in lista:
        if len(heroe) == 0 or type(heroe) != dict:
            return respuesta
        suma_total += heroe[clave]

    return suma_total

def dividir(dividendo:int or float, divisor:int or float)-> int or float or False:
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

def mostrar_promedio_dato(lista:list, clave:str):
    respuesta = False

    if len(lista) == 0:
        return respuesta

    for heroe in lista:
        if type(heroe[clave]) == int or type(heroe[clave]) == float:
            respuesta = calcular_promedio(lista, clave)
        else:
            respuesta = False
            return respuesta

    return respuesta

def imprimir_menu():
    '''Imprime Menu.'''
    print("Menú de opciones:")
    print("1.  Normalizar datos")
    print("2.  Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
    print("3.  Recorrer la lista y determinar cuál es el super héroe más ALTO de género F")
    print("4.  Recorrer la lista y determinar cuál es el super héroe más ALTO de género M")
    print("5.  Recorrer la lista y determinar cuál es el superhéroe más DEBIL de género M")
    print("6.  Recorrer la lista y determinar cuál es el superhéroe más DEBIL de género NB")
    print("7.  Recorrer la lista y determinar la FUERZA PROMEDIO de los superhéroes de género NB")
    print("8.  Determinar CUANTOS superhéroes tienen cada TIPO DE COLOR DE OJOS.")
    print("9.  Determinar CUANTOS superhéroes tienen cada TIPO DE COLOR DE PELO.")
    print("10. Listar todos los superhéroes AGRUPADOS por TIPO DE OJOS")
    print("11. Listar todos los superhéroes AGRUPADOS por TIPO DE INTELIGENCIA")
    print("0.  Salir")

def validar_entero(numero:str)->int or float:
    '''Verifica el parametro este formado únicamente por dígitos.'''
    if re.match('^[0-9]+$', numero):
        return True
    else:
        return False

def stark_menu_principal():
    '''Ejecutaa la funcion "imprimir_menu", pide un numero y hace las respectivas validaciones para saber si es un numero que coincida con las opciones del menú. Devuelve un numero.'''
    respuesta = False

    imprimir_menu()

    opcion_usuario = input('Ingrese una de las opciones: ')
    while opcion_usuario.isalpha():
        opcion_usuario = input('Ingrese un numero entero\nIngrese una de las opciones: ')

    if validar_entero(opcion_usuario):
        opcion_usuario = int(opcion_usuario)
        respuesta = opcion_usuario
    while respuesta <0 or respuesta > 11:
        opcion_usuario = input('Debera ingresar numero del 1 al 11 o 0 para salir: ')
        if validar_entero(opcion_usuario):
            opcion_usuario = int(opcion_usuario)
            respuesta = opcion_usuario

    return respuesta

def stark_marvel_app():

    opcion_menu = stark_menu_principal()

    return opcion_menu