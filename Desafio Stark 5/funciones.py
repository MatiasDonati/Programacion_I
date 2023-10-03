import re
import json

# MATIAS EDUARDO DONATI
# DESAFIO STARK 5

def parse_json_stark(path:str)->list:
    """Recibe un Json y devuelve una Lista"""

    archivo = open(path, 'r')
    dic_json = json.load(archivo)
    archivo.close()
    return dic_json['heroes']

lista_heroes = parse_json_stark('Desafio Stark 5/data_stark.json')
# print(lista_heroes[0]["nombre"])

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

   while True:

    opcion_usuario = stark_menu_principal_desafio_5()

    match opcion_usuario:
        case 'A':
            pass
        case 'B':
            pass
        case 'C':
            pass
        case 'D':
            pass
        case 'E':
            pass
        case 'F':
            pass
        case 'G':
            pass
        case 'H':
            pass
        case 'I':
            pass
        case 'J':
            pass
        case 'K':
            pass
        case 'L':
            pass
        case 'M':
            pass
        case 'N':
            pass
        case 'O':
            pass
        case 'Z':
            print('Hasta luego!')
            break
        case -1:
            print(f"\nIngresó una opcion NO válida.\n")

stark_marvel_app_5(lista_heroes)