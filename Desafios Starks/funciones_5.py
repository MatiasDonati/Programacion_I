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


lista_heroes = leer_archivo('Desafios Starks/data_stark.json')
# stark_marvel_app_5(lista_heroes)


# INSTARLAR RAINBOW VSC

def guardar_archivo(nombre_archivo:str, contenido:str):

    archivo = open(nombre_archivo, 'w+')
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

guardar_archivo("Sarasa_Prueba.csv", "ESTE ES EL CONTENIDO DEL ARasdasdasdasdasdCHIVO")