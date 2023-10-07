import re
import json
from funciones_mejorado_2 import *
from funciones_3 import *
from funciones_4 import *

# MATIAS EDUARDO DONATI
# DESAFIO STARK 5

def imprimir_menu_desafio_5():
    '''Imprime menu'''
    print("Menú de opciones:\n")
    print(" A.  Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    print(" B.  Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print(" C.  Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print(" D.  Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print(" E.  Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    print(" F.  Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    print(" G.  Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    print(" H.  Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    print(" I.  Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
    print(" J.  Determinar cuántos superhéroes tienen cada tipo de color de ojos")
    print(" K.  Determinar cuántos superhéroes tienen cada tipo de color de pelo")
    print(" L.  Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    print(" M.  Listar todos los superhéroes agrupados por color de ojos")
    print(" N.  Listar todos los superhéroes agrupados por color de pelo")
    print(" O.  Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("'Z' Salir\n")

# imprimir_menu_desafio_5()

def stark_menu_principal_desafio_5():

    retorno = -1

    imprimir_menu_desafio_5()
    opcion_usuario = input(f"Ingrese una Opcion: ")
    if re.match(r'^[a-zA-Z]$', opcion_usuario) != None:
        retorno = opcion_usuario.upper()

    return retorno

# print(stark_menu_principal_desafio_5())

def stark_marvel_app_5(lista_heroes:list):

    # HACER DE DOS INCICOS UNA SOLA EJECUCION DE FUNCION CON IF

   stark_normalizar_datos(lista_heroes)

   while True:

    opcion_usuario = stark_menu_principal_desafio_5()

    match opcion_usuario:
        case 'A':

            # ACA TENGO Q PASAR LISTA HEROES ME PARECE
            # ACA TENGO Q PASAR LISTA HEROES ME PARECE
            # ACA TENGO Q PASAR LISTA HEROES ME PARECE
            # ACA TENGO Q PASAR LISTA HEROES ME PARECE

            lista_masculino = obtener_dato_cantidad(lista_personajes, "M", "genero")
            stark_imprimir_heroes(lista_masculino)
        case 'B':
            lista_femenino = obtener_dato_cantidad(lista_personajes, "F", "genero")
            stark_imprimir_heroes(lista_femenino)
        case 'C':
            mas_alto = obtener_maximo(lista_masculino, "altura")
            heroe_con_altura_maxima = obtener_dato_cantidad(lista_masculino, mas_alto, "altura")
            stark_imprimir_heroes(heroe_con_altura_maxima)
        case 'D':
            mas_alto = obtener_maximo(lista_femenino, "altura")
            heroe_con_altura_maxima = obtener_dato_cantidad(lista_femenino, mas_alto, "altura")
            stark_imprimir_heroes(heroe_con_altura_maxima)
        case 'E':
            mas_bajo = obtener_minimo(lista_masculino, "altura")
            heroe_con_altura_minima = obtener_dato_cantidad(lista_masculino, mas_bajo, "altura")
            stark_imprimir_heroes(heroe_con_altura_minima)
        case 'F':
            mas_bajo = obtener_minimo(lista_femenino, "altura")
            heroe_con_altura_minima = obtener_dato_cantidad(lista_femenino, mas_bajo, "altura")
            stark_imprimir_heroes(heroe_con_altura_minima)
        case 'G':
           lista_masculino = obtener_dato_cantidad(lista_personajes, "M", "genero")
           print(mostrar_promedio_dato(lista_masculino, "altura"))
        case 'H':
           lista_femenino = obtener_dato_cantidad(lista_personajes, "F", "genero")
           print(mostrar_promedio_dato(lista_femenino, "altura"))
        case 'I':
            mas_alto = obtener_maximo(lista_masculino, "altura")
            heroe_con_altura_maxima = obtener_dato_cantidad(lista_masculino, mas_alto, "altura")
            if len(heroe_con_altura_maxima) == 1:
                heroe = heroe_con_altura_maxima[0]
                print(obtener_nombre(heroe))
        case 'J' | 'K':
            lista_ojos_pelo = []
            clave = "color_ojos"
            if opcion_usuario == 'K':
                clave = "color_pelo"

            for heroe in lista_personajes:
                tipos_de_ojo_o_pelo = set(heroe[clave] for heroe in lista_personajes)

            for tipo_ojo_o_pelo in tipos_de_ojo_o_pelo:
                contador = 0
                for heroe in lista_personajes:
                    if tipo_ojo_o_pelo == heroe[clave]:
                        contador += 1

                diccionario_color_pelo_u_ojo = {}
                diccionario_color_pelo_u_ojo[tipo_ojo_o_pelo] = contador

                lista_ojos_pelo.append(diccionario_color_pelo_u_ojo)

            stark_imprimir_heroes(lista_ojos_pelo)
        case 'L':
            listado_por_inteligencia = []

            for heroe in lista_personajes:
                tipos_de_inteligencia = set(heroe["inteligencia"] for heroe in lista_personajes)

            for tipo_de_inteligencia in tipos_de_inteligencia:
                contador = 0
                for heroe in lista_personajes:
                    if tipo_de_inteligencia == heroe["inteligencia"]:
                        contador += 1

                diccionario_tipo_inteligencia = {}

                if tipo_de_inteligencia == "":
                    diccionario_tipo_inteligencia["No tiene"] = contador
                else:
                    diccionario_tipo_inteligencia[tipo_de_inteligencia] = contador

                listado_por_inteligencia.append(diccionario_tipo_inteligencia)

            stark_imprimir_heroes(listado_por_inteligencia)
        case 'M'| 'N'| 'O':

            clave = "color_ojos"
            if opcion_usuario == "N":
                clave = "color_pelo"
            else:
                clave = "inteligencia"

            for heroe in lista_personajes:
                tipo_ojo_o_inteligencia = set(heroe[clave] for heroe in lista_personajes)

            for ojo_o_inteligencia in tipo_ojo_o_inteligencia:
                print(f"# {ojo_o_inteligencia}")
                print('')
                for heroe in lista_personajes:
                    if heroe[clave] == ojo_o_inteligencia:
                        print(obtener_nombre_y_dato(heroe, clave))
                        print('')
        case 'Z':
            print('Hasta luego!')
            break
        case -1:
            print(f"\nIngresó una opcion NO válida.\n")

def leer_archivo(path:str)->list:
    """Recibe un Json y devuelve una Lista"""

    with open(path) as file:
        data = json.load(file)

    # archivo = open(path, 'r')
    # dic_json = json.load(archivo)
    # archivo.close()
    # return dic_json['heroes']

    return data['heroes']

# CASA
lista_heroes = leer_archivo('Desafios Starks/data_stark.json')

# LABURO
# lista_heroes = leer_archivo('Programacion_I-main\Desafios Starks\data_stark.json')
# print(lista_heroes)

# stark_marvel_app_5(lista_heroes)


def guardar_archivo(nombre_archivo:str, contenido:str):

    # Le puse modo "a" para poder realizar "stark_guardar_heroe_genero" y que no se haga una archivo por heroe.
   
    # CASA
    archivo = open(f"Desafios Starks/{nombre_archivo}", 'a')
   
    # LABURO
    # archivo = open(f"Programacion_I-main\Desafios Starks\{nombre_archivo}", 'a')
    archivo.writelines(contenido)

    if archivo:
        booleano = True
        # print(archivo.mode)
        # print(archivo.name)
        # print(archivo.closed)
        archivo.close()
        print(f"Se creó el archivo: {archivo.name}")
    else:
        booleano = False
        print(f"Error al crear el archivo: {nombre_archivo}")

    return booleano

# guardar_archivo("Sarasa_Prueba.csv", "Este es el contenido del Archivo")

def capitalizar_palabras(palabra_o_palabras:str):

    separadas = palabra_o_palabras.split()

    for indice in range(len(separadas)):
        separadas[indice] = separadas[indice].capitalize()

    unir_palabras_lista = ' '.join(separadas)

    return unir_palabras_lista

# print(capitalizar_palabras('hola vengo a probar si la letras se ponen en mayuscula, chau!'))

def obtener_nombre_capitalizado(heroe:dict):
    return capitalizar_palabras(heroe["nombre"])

# print(obtener_nombre_capitalizado(lista_heroes[0]))

def obtener_nombre_y_dato(heroe:dict, clave:str)->str or False:
    '''Recibe un diccionario y una clave"str", de no ser vacio, devuelve un mensaje con los datos. Caso contrario "False"'''
    respuesta = False
    nombre = obtener_nombre_capitalizado(heroe)
    if nombre:
        respuesta = f"{nombre} | {clave.capitalize()}: {heroe[clave]}"

    return respuesta

# print(obtener_nombre_y_dato(lista_heroes[0], "fuerza"))

def es_genero(heroe:dict, genero:str):
    retorno = False
    if heroe["genero"] == genero:
        retorno = True

    return retorno

# print(es_genero(lista_heroes[0], "F")) # False
# print(es_genero(lista_heroes[0], "M")) # True

def stark_guardar_heroe_genero(lista:list, genero:str):

    retorno = False

    for heroe in lista:
        if es_genero(heroe, genero):
            nombre = obtener_nombre_capitalizado(heroe)
            print(nombre)
            guardar_archivo(f"heroes_{genero}.csv", f"{nombre},")
            retorno = True

    return retorno

# stark_guardar_heroe_genero(lista_heroes, "M")

def calcular_min_genero(lista:list, clave:str, genero:str)->dict:

    stark_normalizar_datos(lista)

    valor_minimo = None
    respuesta = None

    for heroe in lista:
        if clave in heroe and heroe["genero"] == genero:
            if valor_minimo == None or heroe[clave] < valor_minimo:
                valor_minimo = heroe[clave]
                respuesta = heroe

    return respuesta

# print(calcular_min_genero(lista_heroes, "peso", "M"))

def calcular_max_genero(lista:list, clave:str, genero:str)->dict:

    stark_normalizar_datos(lista)

    valor_maximo = None
    respuesta = None

    for heroe in lista:
        if clave in heroe and heroe["genero"] == genero:
            if valor_maximo == None or heroe[clave] > valor_maximo:
                valor_maximo = heroe[clave]
                respuesta = heroe

    return respuesta

# print(calcular_max_genero(lista_heroes, "peso", "M"))

def calcular_max_min_dato_genero(lista:list, valor_a_buscar:str, clave:str, genero:str)->list:

    # Esta función retornará el héroe o heroína que cumpla con las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y 'minimo', retornará la heroína que tenga el mínimo (altura, peso u otro dato)
    # Ver si necesita dos parametros solamente ..

    stark_normalizar_datos(lista)

    if valor_a_buscar == "minimo":
        respuesta = calcular_min_genero(lista, clave, genero)
    elif valor_a_buscar == "maximo":
        respuesta = calcular_max_genero(lista, clave, genero)
    else:
        respuesta = "Denera ingresar minimo o maximo"

    return respuesta

# print(calcular_max_min_dato_genero(lista_heroes, "minimo", "peso", "M"))

def stark_imprimir_heroes(lista:list, valor_a_buscar:str, clave:str, genero:str)->print or False:

    """
    RETORNA TRUE O FALSE!
    RETORNA TRUE O FALSE!
    RETORNA TRUE O FALSE!
    RETORNA TRUE O FALSE!
   
    """

    heroe_buscado = calcular_max_min_dato_genero(lista, valor_a_buscar, clave, genero)
    if valor_a_buscar == "maximo":
        maximo_o_minimo = "Mayor"
    elif valor_a_buscar == "minimo":
        maximo_o_minimo = "Menor"
    else:
        print("Dato incorrecto")
        return False
    nombre = obtener_nombre_y_dato(heroe_buscado, clave)

    nombre_archivo = f"heroes_{valor_a_buscar}_{clave}_{genero}.csv"
    contenido = f"{maximo_o_minimo} {clave.capitalize()}: Nombre: {nombre}"
    guardar_archivo(nombre_archivo, contenido)

    print(contenido)

    return True

# stark_imprimir_heroes(lista_heroes, "maximo", "altura", "M")
# stark_imprimir_heroes(lista_heroes, "maximo", "peso", "M")

def sumar_dato_heroe_genero(lista:list, clave:str, genero:str)->int or float or False:
    '''Recibe una lista de heroes y un clave(str). Se sumaran todos los valores de la clave pasada por parametro de toda la lista.'''
    """
    Una vez que cumpla con las condiciones, podrá realizar la suma. La
    función deberá retornar la suma del valor de la key de los héroes o
    heroínas que cumplan las condiciones o -1 en caso de que no se
    cumplan las validaciones
    """
    stark_normalizar_datos(lista)

    suma_total = 0
    for heroe in lista:
        if len(heroe) == 0 or type(heroe) != dict:
            return -1
        if heroe["genero"] == genero:
            suma_total += heroe[clave]

    return suma_total

# print(sumar_dato_heroe_genero(lista_heroes, "altura", "M"))

def cantidad_heroes_genero(lista:list, genero:str):
   
    contador = 0
   
    for heroe in lista:
        if heroe["genero"] == genero:
            contador += 1

    return contador

# cantidad = cantidad_heroes_genero(lista_heroes, "M")
# print(cantidad)

def calcular_promedio_5(lista:list, clave:str, genero:str):
    '''Retorna un promedio. Recibe una lista de heroes y la clave de los valores a promediar'''
   
    suma = sumar_dato_heroe_genero(lista, clave, genero)
    cantidad = cantidad_heroes_genero(lista, genero)
    promedio = dividir(suma, cantidad)
    return promedio

# print(calcular_promedio_5(lista_heroes, "altura", "F"))

"""
VER DE IMPORTAR SOLO LAS FUNCIONES QUE UTILIZO PARA QUE NO HAYA REPETIDAS -- O VER DE CAMBIARLE EL NOMBRE !!!
VER DE IMPORTAR SOLO LAS FUNCIONES QUE UTILIZO PARA QUE NO HAYA REPETIDAS -- O VER DE CAMBIARLE EL NOMBRE !!!
VER DE IMPORTAR SOLO LAS FUNCIONES QUE UTILIZO PARA QUE NO HAYA REPETIDAS -- O VER DE CAMBIARLE EL NOMBRE !!!
VER DE IMPORTAR SOLO LAS FUNCIONES QUE UTILIZO PARA QUE NO HAYA REPETIDAS -- O VER DE CAMBIARLE EL NOMBRE !!!
VER DE IMPORTAR SOLO LAS FUNCIONES QUE UTILIZO PARA QUE NO HAYA REPETIDAS -- O VER DE CAMBIARLE EL NOMBRE !!!
"""

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista:list, genero:str):

    respuesta = False

    if len(lista) == 0:
        print("Error: Lista de héroes vacía")
        return respuesta

    altura_promedio = calcular_promedio_5(lista, "altura", genero)

    contenido = f"Altura promedio género {genero}: {altura_promedio}"
    print(contenido)

    nombre = f"PEDOheroes_promedio_altura_{genero}.csv"
    guardar_archivo(nombre, contenido)

    return True


def calcular_cantidad_tipo(lista:list, clave:str):
    if len(lista) == 0:
        return {"Error": "La lista se encuentra vacía"}

    diccionario_gral = {}

    for heroe in lista:
        tipo_clave = capitalizar_palabras(heroe[clave])
        if tipo_clave in diccionario_gral:
            diccionario_gral[tipo_clave] += 1
        else:
            diccionario_gral[tipo_clave] = 1

    return diccionario_gral

print(calcular_cantidad_tipo(lista_heroes, "inteligencia"))


