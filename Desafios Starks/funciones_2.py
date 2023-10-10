# A
def recorrer_lista_NB(lista):
    '''Printea los personajes con genero "NB"'''
    contador = 0
    for personaje in lista:
        if personaje["genero"] == "NB":
            print(f"{personaje['nombre']} es de genero 'NB'")
            contador += 1
    if contador == 0:
        print("\nNo hay personajes NB")

# B
def mostrar_femenino_mas_alto(lista_personajes):
    '''Devuelve el personaje femenino mas alo'''
    femenino_mas_alto = None
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            if femenino_mas_alto == None or float(personaje["altura"]) > femenino_mas_alto:
                femenino_mas_alto = float(personaje["altura"])
                nombre_femenino_mas_alto = personaje["nombre"]
    mensaje = f"El femenino mas alto es: {nombre_femenino_mas_alto}"

    return mensaje

# C
def mostrar_masculino_mas_alto(lista_personajes):
    '''Devuelve el personaje masculino mas alto'''
    masculino_mas_alto = None
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            if masculino_mas_alto == None or float(personaje["altura"]) > masculino_mas_alto:
                masculino_mas_alto = float(personaje["altura"])
                nombre_masculino_mas_alto = personaje["nombre"]
    mensaje = f"El masculino mas alto es: {nombre_masculino_mas_alto}"

    return mensaje

# D
def mostrar_masculino_mas_debil(lista_personajes):
    '''Devuelve el personaje masculino mas debil'''
    masculino_mas_debil =  None
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            if masculino_mas_debil == None or int(personaje["fuerza"]) < masculino_mas_debil:
                masculino_mas_debil = int(personaje["fuerza"])
                nombre_masculino_mas_debil = personaje["nombre"]
    mensaje = f"El masculino mas debil es: {nombre_masculino_mas_debil}"

    return mensaje

# E
def mostrar_debil_NB(lista_personajes):
    '''Devuelve el personaje NB mas debil'''
    nb_mas_debil = None
    for personaje in lista_personajes:
        if personaje["genero"] == "NB":
            if nb_mas_debil == None or int(personaje["fuerza"]) < nb_mas_debil:
                nb_mas_debil = int(personaje["fuerza"])
                nombre_nb_mas_debil = personaje["nombre"]

    if nb_mas_debil == None:
        mensaje = "No hay NB"
    else:
        mensaje = f"El masculino mas debil es: {nombre_nb_mas_debil}"

    return mensaje

# F
def mostrar_fuerza_promedio_NB(lista_personajes):
    '''Muestra la fuerza promedio de genero NB'''
    suma_fuerza_NB = 0
    cantidad_NB = 0
    for personaje in lista_personajes:
        # MASCULINO PARA CHEKEAR
        if personaje["genero"] == "NB":
            suma_fuerza_NB += int(personaje["fuerza"])
            cantidad_NB += 1
    if cantidad_NB != 0:
        promedio = suma_fuerza_NB / cantidad_NB
        mensaje = f"El promedio de fuerza NB es: {promedio}"
    else:
        mensaje = "No hay NB"

    return mensaje

# G
def mostrar_cuantos_hay_por_tipos_de_ojos(lista_personajes, flag=True):
    '''Printea cuantos hay de cada Color de Ojos'''

    lista_contador_colores_ojos = []

    tipos_de_ojos = set(personaje["color_ojos"] for personaje in lista_personajes)

    for color_ojo in tipos_de_ojos:
        contador = 0
        lista_nombres_mismo_color_ojos = []
        for personaje in lista_personajes:
            if personaje["color_ojos"] == color_ojo:
                contador += 1
                lista_nombres_mismo_color_ojos.append(personaje["nombre"])

        diccionario_colores = {}
        diccionario_colores[color_ojo] = contador
        diccionario_colores["nombres"] = lista_nombres_mismo_color_ojos

        lista_contador_colores_ojos.append(diccionario_colores)

    if flag == True:
        for color in lista_contador_colores_ojos:
            primera_clave = list(color.keys())[0]
            primer_valor = list(color.values())[0]
            print(f"Personajes con ojos de color '{primera_clave}': {primer_valor}")

        # USAR ESTE RETURN PARA EL INCISO I
    return lista_contador_colores_ojos

# H
def mostrar_cuantos_hay_por_tipos_de_color_pelo(lista_personajes):
    '''Printea cuantos hay de cada Color de Pelo'''
    diccionario_color_pelos = {}

    colores_de_pelos = set(personaje["color_pelo"] for personaje in lista_personajes)

    for color_pelo in colores_de_pelos:
        contador = 0
        for personaje in lista_personajes:
            if personaje["color_pelo"] == color_pelo:
                contador += 1
        diccionario_color_pelos[color_pelo] = contador

    for clave, valor in diccionario_color_pelos.items():
        print(f"Personajes con pelo de color '{clave}': {valor}")

# I
def listar_personajes_por_color_de_ojos(lista_personajes, flag=False):
    '''Printea los nombres de los personajes agrupados por Color de Ojos'''
    lista = mostrar_cuantos_hay_por_tipos_de_ojos(lista_personajes, flag)

    for elemento in lista:
        primera_clave = list(elemento.keys())[0]
        segundo_valor = list(elemento.values())[1]
        print(f"Ojos color: {primera_clave}: ")
        for nombre in segundo_valor:
            print(f"  {nombre}")

# J
def listar_personajes_por_tipo_inteligencia(lista_personajes):
    '''Printea los nombres de los personajes agrupados por el Tipo de Inteligencia'''
    lista_tipos_inteligencia = []

    for personaje in lista_personajes:
        tipos_de_inteligencia = set(personaje["inteligencia"] for personaje in lista_personajes)

    for inteligencia in tipos_de_inteligencia:
        contador = 0
        lista_nombres_inteligencia = []
        for personaje in lista_personajes:
            if personaje["inteligencia"] == inteligencia:
                contador += 1
                lista_nombres_inteligencia.append(personaje["nombre"])

        diccionario_inteligencias = {}
        diccionario_inteligencias[inteligencia] = contador
        diccionario_inteligencias["nombres"] = lista_nombres_inteligencia
        lista_tipos_inteligencia.append(diccionario_inteligencias)

    for inteligencia in lista_tipos_inteligencia:
        primera_clave = list(inteligencia.keys())[0]
        segundo_valor = list(inteligencia.values())[1]
        print(f"\nPersonajes con inteligencia '{primera_clave}':")
        for nombre in segundo_valor:
            print(nombre)
        print('')