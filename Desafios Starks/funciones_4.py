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

# print(extraer_iniciales("Howard the Duck asdeee"))

def definir_iniciales_nombre(heroe:dict):
    '''Recibe un diccionario evalua q no sea un diccionario y q contenga la clave "nombre". Luego agrega le agrega la clave "iniciales" ejecutando la funcion "extraer_iniciales"'''

    if type(heroe) != dict or 'nombre' not in heroe:
        return False

    heroe["iniciales"] = extraer_iniciales(heroe["nombre"])

    return True

# heroe = definir_iniciales_nombre(lista_personajes[6])
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


def stark_imprimir_nombres_con_iniciales(lista_heroes:list)->str or False:
    '''Recibe una lista, agrega iniciales e imprime una cadena de string con las inciales. Si la lista esta vacia o en parametro no es una lista deuelve "False"'''

    if len(lista_heroes) == 0 or type(lista_heroes) != list:
        retorno = False

    agregar_iniciales_nombre(lista_heroes)
    for heroe in lista_heroes:
        print(f"* {heroe['nombre']} ({heroe['iniciales']})")

# stark_imprimir_nombres_con_iniciales(lista_personajes)

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    '''Recibe un id y un genero por parametro'''
    retorno = False
    if type(id_heroe) == int and genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB":
        retorno = f"{genero_heroe}-{id_heroe:010}"
    return retorno

# print(generar_codigo_heroe(12, "M"))
# print(generar_codigo_heroe(1, "F"))
# print(generar_codigo_heroe(223, "NB"))

def agregar_codigo_heroe(heroe:dict, id_heroe:int)->bool:
    '''Recine un diccionario y un id, utilizando la funcion "generar_codigo_heroe" se agrega el codigo como valor de la clave "codigo_heroe".Previamente valida que la cantidad de numeros del codigo sean 10.'''

    retorno = False

    if len(heroe) != 0:

        codigo = generar_codigo_heroe(id_heroe, heroe["genero"])

        # chequear minusculas, estan al pedo
        # chequear minusculas, estan al pedo

        codigo_a_validar =  re.sub(r'[a-zA-Z-]','', codigo)

        if len(codigo_a_validar) == 10:
            heroe['codigo_heroe'] = codigo
            retorno = True

    return retorno

# print(agregar_codigo_heroe(lista_personajes[23], 8))

def stark_generar_codigos_heroes(lista_heroes:list):
    '''Ejecuta "agregar_codigo_heroe". Printea cuandos codigos se asignaron, e imprime detalle de heroes con sus codigos. Tambien informa en caso de que algun diccionario no posea clave "codigo_heroe"'''

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
    '''Recibe un numero en formato STR y lo devuelve entero. De no ser entero retonar "-3"'''
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
    '''Recibe un numero en formato STR y lo devuelve flotante. De no ser flotante retonar "-3"'''

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

# print(sanitizar_flotante('54.545454'))

# 3.3
def sanitizar_string(valor_str:str, valor_por_defecto:str='-'):
    '''Recibe una cadena de texto y un valor por defecto. Si no es un numero retira los espacios vacios a principio y final de la cadena. Reemplaza "/" por espacio. Transforma todo a minuscula. Si es un numero retonra "N/A"'''

    if len(valor_str) == 0 and valor_por_defecto != '-':
        return valor_por_defecto.lower()

    if not re.search(r'[0-9]', valor_str):
        valor_str = valor_str.replace('/', ' ').strip()
        valor_por_defecto = valor_por_defecto.strip()
        retorno = valor_str.lower()
    else:
        retorno = 'N/A'

    return retorno

# 3.4
def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str) -> bool:
    '''Recine un diccionario, una clave y un tipo de dato, si es un dato int, float o string, realiza la sanitizacion correspondiente. De lo contrario retorna "False"'''
    if tipo_dato.lower() not in ('entero', 'flotante', 'string'):
        print('Tipo de dato no reconocido.')
        return False

    if clave not in heroe:
        print('La clave especificada no existe en el heroe')
        return False

    match tipo_dato:
        case 'entero':
            heroe[clave] = sanitizar_entero(heroe[clave])
        case 'flotante':
            heroe[clave] = sanitizar_flotante(heroe[clave])
        case _:
            heroe[clave] = sanitizar_string(heroe[clave])

    return True

# 3.5
def stark_normalizar_datos_4(lista_heroes:list):
    '''Recibe una lista, de no estar vacia, normaliza sus datos ejecutando las funciones de sanitizacion'''

    if len(lista_heroes) == 0:
        print("Error: Lista de héroes vacía")

    for heroe in lista_personajes:
        # for clave in heroe:
        for clave in ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']:
            if clave in heroe:
                if clave in ['fuerza']:
                    tipo_dato = 'entero'
                elif clave in ['altura', 'peso']:
                    tipo_dato = 'flotante'
                else:
                    tipo_dato = 'string'
                sanitizar_dato(heroe, clave, tipo_dato)

    print('\nDatos Normalizados\n')

# stark_normalizar_datos_4(lista_personajes)

# 4.1
def generar_indice_nombres(lista_heroes:list):
    '''Recibe una lista, la recorre y hace un split en los nombres de cada heroe'''

    mensaje = "El origen de datos no contiene el formato correcto"

    if len(lista_heroes) != 0:

        lista_nueva = []

        for heroe in lista_heroes:
            if type(heroe) == dict and 'nombre' in heroe:
                    nombre = heroe["nombre"]
                    nombre_separado = nombre.split()
                    for palabra in nombre_separado:
                        lista_nueva.append(palabra)
            else:
                return "El origen de datos no contiene el formato correcto"

        mensaje = lista_nueva
    return mensaje

# print(generar_indice_nombres(lista_personajes))

# 4.2
def stark_imprimir_indice_nombre(lista_heroes:list):
    '''Separa lis indices generados por un "-". '''
    nombres_separados_por_guion = '-'.join(generar_indice_nombres(lista_heroes))
    print(nombres_separados_por_guion)

# stark_imprimir_indice_nombre(lista_personajes)

# 5.1
def convertir_cm_a_mtrs(valor_cm:int or float):

    # if re.match(r'^[0-9]+(\.[0-9]+)?$', valor_cm) and float(valor_cm) > 0:
    #     valor_m = float(valor_cm) / 100

    if type(valor_cm) == float and valor_cm > 0:
        valor_m = float(valor_cm) / 100
        retorno = valor_m
    else:
        retorno = -1

    return retorno

# print(convertir_cm_a_mtrs(345.03))

# 5.2
def generar_separador(patron:str, largo:int, imprimir:bool=True):

    respuesta = "N/A"

    if re.match(r'^.{1,2}$', patron) and int(largo) >=1 and int(largo) <= 235:

        if imprimir:
            respuesta = ''.join(patron * largo)
            print(respuesta)
        else:
            respuesta = patron

    return respuesta

# print(generar_separador('?%', 5))
# print(generar_separador('HOA', 10, False))

# 5.3
def generar_encabezado(titulo:str):

    print('*' * 120)
    print(titulo.upper())
    print('*' * 120)

# generar_encabezado('principal')

# 5.4
def imprimir_ficha_heroe(heroe:dict):

    heroe['altura'] = convertir_cm_a_mtrs(heroe['altura'])

    generar_encabezado('principal')
    print(f"             NOMBRE DEL HÉROE:                          {heroe['nombre']} ({heroe['iniciales']})")
    print(f"             IDENTIDAD SECRETA:                         {heroe['identidad']}")
    print(f"             CONSULTORA:                                {heroe['empresa']}")
    print(f"             CÓDIGO DEL HÉROE:                          {heroe['codigo_heroe']}")

    generar_encabezado('fisico')
    print(f"             ALTURA:                                    {heroe['altura']} Mtrs.")
    print(f"             PESO:                                      {heroe['peso']} Kg.")
    print(f"             FUERZA:                                    {heroe['fuerza']} N")

    generar_encabezado('señas particulares')
    print(f"             COLOR DE OJOS:                                    {heroe['color_ojos']}")
    print(f"             COLOR DE PELO:                                    {heroe['color_pelo']}")


# imprimir_ficha_heroe(lista_personajes[0])

def stark_navegar_fichas(lista_heroes:list):

    indice_heroe = 0
    heroe = lista_heroes[indice_heroe]
    imprimir_ficha_heroe(heroe)

    while True:

        opcion = input('[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir\n')
        while opcion != '1' and opcion != '2' and opcion != 'S' and opcion != 's':
            opcion = input(f' "{opcion}" no es una opcion correcta...\n\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir\n')
        opcion = opcion.upper()

        match opcion:
            case '1':
                indice_heroe = indice_heroe + 1
                if indice_heroe == 24:
                    indice_heroe = 0
                imprimir_ficha_heroe(lista_heroes[indice_heroe])
            case '2':
                indice_heroe = indice_heroe - 1
                if indice_heroe == -1:
                    indice_heroe = 23
                imprimir_ficha_heroe(lista_heroes[indice_heroe])
            case _:
                print('Hasta pronto!')
                break

# stark_navegar_fichas(lista_personajes)

def imprimir_menu():
    '''Imprime Menu.'''
    print("Menú de opciones:\n")
    print(" 1.  Imprimir la lista de nombres junto con sus iniciales")
    print(" 2.  Generar códigos de héroes")
    print(" 3.  Normalizar datos")
    print(" 4.  Imprimir índice de nombres")
    print(" 5.  Navegar fichas")
    print("'S' Salir\n")

# imprimir_menu()

def stark_menu_principal():
    imprimir_menu()
    opcion_usuario = input('Ingrese una de las opciones: ')

    return opcion_usuario

# print(stark_menu_principal())

def stark_marvel_app_3():
    opcion_usuario = stark_menu_principal()
    return opcion_usuario

# print(stark_marvel_app_3())