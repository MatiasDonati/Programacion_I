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
# print(generar_codigo_heroe(223, "NB"))

def agregar_codigo_heroe(heroe:dict, id_heroe:int):

    retorno = False

    if len(heroe) != 0:

        codigo = generar_codigo_heroe(id_heroe, heroe["genero"])

        codigo_a_validar =  re.sub(r'[a-zA-Z-]','', codigo)

        if len(codigo_a_validar) == 10:
            heroe['codigo_heroe'] = codigo
            retorno = True

    return retorno

# print(agregar_codigo_heroe(lista_personajes[23], 8))

def stark_generar_codigos_heroes(lista_heroes:list):

    if len(lista_heroes) != 0:

        contador = 0

        for indice in range(len(lista_heroes)):
            if type(lista_heroes[indice]) == dict and 'genero' in lista_heroes[indice]:
                bool_agrega_codigo = agregar_codigo_heroe(lista_heroes[indice], indice+1)
                if bool_agrega_codigo:
                    contador += 1

        print(f"Se asignaron {contador} codigos")
        for heroe in lista_heroes:
            if 'codigo_heroe' in heroe:
                print(f"* El código del héroe {heroe['nombre']} es: {heroe['codigo_heroe']}")
            else:
                print(f"* El heroe {heroe['nombre']} no posee clave 'codigo_heroe'")

# stark_generar_codigos_heroes(lista_personajes)

# 3.1
def sanitizar_entero(numero_str:str):
    retorno = -3
    

    if type(numero_str) == str:
        numero_str = numero_str.strip()

        if re.search(r'[^0-9-]', numero_str) or numero_str == '':
            retorno = -1
        elif int(numero_str) < 0:
            retorno = -2
        else:
            retorno = int(numero_str)

    return retorno

# print(sanitizar_entero('gfg@F234'))

# 3.2
def sanitizar_flotante(numero_str:str):
    retorno = -3

    if type(numero_str) == str:
        numero_str = numero_str.strip()

        if re.search(r'[^0-9-.]', numero_str):
            retorno = -1
        elif float(numero_str) < 0:
            retorno = -2
        else:
            retorno = float(numero_str)

    return retorno

# print(sanitizar_flotante('-9.7'))

# 3.3
def sanitizar_string(valor_str:str, valor_por_defecto:str='-'):

    if len(valor_str) == 0 and valor_por_defecto != '-':
        return valor_por_defecto.lower()

    if not re.search(r'[0-9]', valor_str):
        valor_str = valor_str.replace('/', ' ').strip()
        valor_por_defecto = valor_por_defecto.strip()
        retorno = valor_str.lower()
    else:
        retorno = 'N/A'

    return retorno

# print(sanitizar_string('', 'FolkasASDASDASDASDd'))
# print(sanitizar_string('    Esta/TODO/BiEn    '))
# print(sanitizar_string('4'))

# 3.4
def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str) -> bool:

    # if not re.match(r'^(string|entero|flotante)$',tipo_dato, re.I ):
    if tipo_dato.lower() not in ('entero', 'flotante', 'string'):
        print('Tipo de dato no reconocido.')
        return False

    if clave not in heroe:
        print('La clave especificada no existe en el heroe')
        return False

    match tipo_dato:
        case 'entero':
            heroe[clave] = sanitizar_entero(heroe[clave])
            print(heroe[clave])
        case 'flotante':
            heroe[clave] = sanitizar_flotante(heroe[clave])
            print(heroe[clave])
        case _:
            # string
            heroe[clave] = sanitizar_string(heroe[clave])
            print(heroe[clave])

    return True

# print(sanitizar_dato(lista_personajes[9],'fuerza', 'entero'))

# 3.5
def stark_normalizar_datos(lista_heroes:list):
    if len(lista_heroes) == 0:
        print("Error: Lista de héroes vacía")

    for heroe in lista_personajes:
        for clave in ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']:
            if clave in heroe:
                if clave in ['fuerza']:
                    tipo_dato = 'entero'
                elif clave in ['altura', 'peso']:
                    tipo_dato = 'flotante'
                else:
                    tipo_dato = 'string'
                sanitizar_dato(heroe, clave, tipo_dato)

    print('Datos Normalizados')

stark_normalizar_datos(lista_personajes)

# SANITIZAR ENTERO ME DEVUELVE -1 SIEMPRE VER  ONDA !
# SANITIZAR ENTERO ME DEVUELVE -1 SIEMPRE VER  ONDA !