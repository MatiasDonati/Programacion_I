from data_stark import lista_personajes
import re
# MATIAS EDUARDO DONATI
# DESAFIO STARK 4


def extraer_iniciales(nombre_heroe:str)->str:
    '''Recibe un nombre y devuelve sus iniciales en mayusculas separas por un ".", si el nombre contiene "the" lo omite.'''

    if len(nombre_heroe) == 0:
        return 'N/A'

    palabras = nombre_heroe.split()

    lista_iniciales = []

    for palabra in palabras:

        if palabra.lower() == 'the':
            continue

        palabra = palabra.replace('-', ' ')

        inicial = palabra[0].upper()

        lista_iniciales.append(inicial)

    salida = '.'.join(lista_iniciales)

    return salida

# print(extraer_iniciales("Howard the Duck"))

def definir_iniciales_nombre(heroe:dict):
    '''Recibe un diccionario evalua q no sea un diccionario y q contenga la clave "nombre". Luego agrega le agrega la clave "iniciales" ejecutando la funcion "extraer_iniciales"'''

    if type(heroe) != dict or 'nombre' not in heroe:
        retorno =  False

    heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
    retorno = True

    return retorno

# heroe = definir_iniciales_nombre(lista_personajes[20])
# print(heroe)

def agregar_iniciales_nombre(lista_heroes:list):
    '''Recibe una lista, valida que no esta vacia y que sea de tipo lista. Luego a cada diccionario le agrega el valor "iniciales" ejecutando la funcion "definir_iniciales_nombre". Devuelve un Boolean'''

    if len(lista_heroes) == 0 or type(lista_heroes) != list:
        retorno = False

    for heroe in lista_heroes:
        if definir_iniciales_nombre(heroe) == False:
            print('El origen de datos no contiene el formato correcto')
            retorno = False
        else:
            definir_iniciales_nombre(heroe)
            retorno = True
    return retorno

# print(agregar_iniciales_nombre(lista_personajes))
# for heroe in lista_personajes:
#     print(heroe['nombre'])
#     for clave, valor in heroe.items():
#         if clave == 'iniciales':
#             print(f'\n{clave}: {valor}\n')


def stark_imprimir_nombres_con_iniciales(lista_heroes:list):

    if len(lista_heroes) == 0 or type(lista_heroes) != list:
        retorno = False

    agregar_iniciales_nombre(lista_heroes)
    for heroe in lista_heroes:
        print(f"* {heroe['nombre']} ({heroe['iniciales']})")

# stark_imprimir_nombres_con_iniciales(lista_personajes)

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    retorno = False
    if type(id_heroe) == int and genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB":
        retorno = f"{genero_heroe}-{id_heroe:010}"
    return retorno

# print(generar_codigo_heroe(12, "M"))
# print(generar_codigo_heroe(1, "F"))
# print(generar_codigo_heroe(100, "NB"))