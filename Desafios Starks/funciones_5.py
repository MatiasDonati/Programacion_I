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

def stark_marvel_app_5(lista_personajes:list):

    # HACER DE DOS INCICOS UNA SOLA EJECUCION DE FUNCION CON IF

    stark_normalizar_datos(lista_personajes)

    while True:

        opcion_usuario = stark_menu_principal_desafio_5()
        lista_masculino = obtener_dato_cantidad(lista_personajes, "M", "genero")
        lista_femenino = obtener_dato_cantidad(lista_personajes, "F", "genero")

        # print(len(lista_personajes))
        # print(len(lista_masculino))
        # print(len(lista_femenino))

        match opcion_usuario:
            case 'A' | 'B':
                if opcion_usuario == "A":
                    lista = lista_masculino
                else:
                    lista = lista_femenino
                for heroe in lista:
                    print(heroe["nombre"])
            case 'C' | 'D':
                if opcion_usuario == 'C':
                    lista = lista_masculino
                else:
                    lista = lista_femenino
                mas_alto = obtener_maximo(lista, "altura")
                heroe_con_altura_maxima = obtener_dato_cantidad(lista, mas_alto, "altura")
                stark_imprimir_heroes(heroe_con_altura_maxima)
            case 'E' | 'F':
                if opcion_usuario == 'C':
                    lista = lista_masculino
                else:
                    lista = lista_femenino
                mas_bajo = obtener_minimo(lista, "altura")
                heroe_con_altura_minima = obtener_dato_cantidad(lista, mas_bajo, "altura")
                stark_imprimir_heroes(heroe_con_altura_minima)
            case 'G':
                print(mostrar_promedio_dato(lista_masculino, "altura"))
            case 'H':
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

# INICIAR MENU !

# stark_marvel_app_5(lista_heroes)


def guardar_archivo(nombre_archivo:str, contenido:str):

    # Le puse modo "a" para poder realizar "stark_guardar_heroe_genero" y que no se haga una archivo por heroe.

    # CASA
    # DEPENDE EL INCISO ME SRIVE "A", "W+"
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

# stark_guardar_heroe_genero(lista_heroes, "F")

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

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista:list, genero:str):

    respuesta = False

    if len(lista) == 0:
        print("Error: Lista de héroes vacía")
        return respuesta

    altura_promedio = calcular_promedio_5(lista, "altura", genero)

    contenido = f"Altura promedio género {genero}: {altura_promedio}"
    print(contenido)

    nombre = f"heroes_promedio_altura_{genero}.csv"
    guardar_archivo(nombre, contenido)

    return True

# stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, "F")

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

# print(calcular_cantidad_tipo(lista_heroes, "color_pelo"))

def guardar_cantidad_heroes_tipo(dicc_tipos_de_claves:dict, clave_a_buscar:str):

    retorno = False

    for clave, valor in dicc_tipos_de_claves.items():

        linea_a_guardar = (f"Caracteristica: {clave_a_buscar} {clave} - Cantidad de heroes: {valor}\n")
        guardar_archivo(f"heroes_cantidad_{clave_a_buscar}.csv", linea_a_guardar)

        retorno = True

    return retorno

# print(guardar_cantidad_heroes_tipo(calcular_cantidad_tipo(lista_heroes, "color_ojos"), "color_ojos"))

def stark_calcular_cantidad_por_tipo(lista:list, clave_ingresada:str):

    retorno = False

    diccionario_tipos_calve =  calcular_cantidad_tipo(lista, clave_ingresada)
    guardado = guardar_cantidad_heroes_tipo(diccionario_tipos_calve, clave_ingresada)
    if guardado:
        retorno = True

    return retorno

# print(stark_calcular_cantidad_por_tipo(lista_heroes, "color_ojos"))

def obtener_lista_de_tipos(lista:list, clave_a_buscar:str):

    claves = []

    for heroe in lista:
        if clave_a_buscar in heroe:
            if heroe[clave_a_buscar].strip():
                heroe[clave_a_buscar] = capitalizar_palabras(heroe[clave_a_buscar])
            else:
                 heroe[clave_a_buscar] = "N/A"

            claves.append(heroe[clave_a_buscar])

    lista_sin_duplicados = set(clave for clave in claves)

    return lista_sin_duplicados

# print(obtener_lista_de_tipos(lista_heroes, "color_ojos"))

def normalizar_dato(valor:str, valor_por_defecto:str="N/A"):
    if valor.strip():
        return valor
    else:
        return valor_por_defecto

# print(normalizar_dato(""))
# print(normalizar_dato("Green"))

def normalizar_heroe(heroe:dict,key:str):

    retorno = False

    if key in heroe:
        heroe[key] = normalizar_dato(heroe[key])
        if heroe[key] != "N/A":
            heroe[key] = capitalizar_palabras(heroe[key])
            retorno = heroe[key]

    return retorno

# print(normalizar_heroe(lista_heroes[0], "nombre"))


def obtener_heroes_por_tipo(lista, tipos_variedades, clave_a_evaluar):

    diccionario = {}

    for tipo in tipos_variedades:
        diccionario[tipo] = []

    for heroe in lista:
        if clave_a_evaluar in heroe:
            heroe[clave_a_evaluar] = normalizar_dato(heroe[clave_a_evaluar])
            if heroe[clave_a_evaluar] in tipos_variedades:
                nombre_heroe = normalizar_dato(heroe["nombre"])
                nombre_heroe = capitalizar_palabras(nombre_heroe)
                diccionario[heroe[clave_a_evaluar]].append(nombre_heroe)

    return diccionario

dic = (obtener_heroes_por_tipo(lista_heroes, obtener_lista_de_tipos(lista_heroes, "color_ojos"), "color_ojos"))
# for clave, valor in dic.items():
#     print(f"{clave}: {valor}\n")


def guardar_heroes_por_tipo(diccionario_valores:dict, tipo_dato:str):

    retorno = False

    for clave, valor in diccionario_valores.items():
        # Realice ese cambio porq no me permitia "N/A" en el archivo csv.
        if clave == "N/A" or clave == "N/a":
            clave = "Sin Tipo"
        valor = ' | '.join(valor)
        cadena_texto = f"{tipo_dato} {clave}: {valor}"
        nombre_archivo = f"heroes_segun_{clave}.csv"

        guardar_archivo(nombre_archivo, cadena_texto)
        retorno = True

    return retorno

# print(guardar_heroes_por_tipo(dic, "color_ojos"))

def stark_listar_heroes_por_dato(lista:list,clave:str):

    lista_tipos = obtener_lista_de_tipos(lista, clave)
    heroes_por_tipo =  obtener_heroes_por_tipo(lista,lista_tipos,clave)

    print(heroes_por_tipo)

    guardar_heroes_por_tipo(heroes_por_tipo, clave)

# stark_listar_heroes_por_dato(lista_heroes, "color_ojos")