# A
def recorrer_lista_NB(lista:list):
    '''Printea los personajes con genero "NB"'''
    contador = 0
    for personaje in lista:
        if personaje["genero"] == "NB":
            print(f"{personaje['nombre']} es de genero 'NB'")
            contador += 1
    if contador == 0:
        print("\nNo hay personajes NB")

# B y C
def mostrar_mas_alto(lista_personajes:list, genero:str):
    '''Devuelve el personaje mas alto segun geneto pasado por parametro'''
    mas_alto = None
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            if mas_alto == None or float(personaje["altura"]) > mas_alto:
                mas_alto = float(personaje["altura"])
                nombre_mas_alto = personaje["nombre"]

    if genero == "M":
        tipo_genero = "Masculino"
    else:
        tipo_genero = "Femenino"
    mensaje = f"El {tipo_genero} mas alto es: {nombre_mas_alto}"

    return mensaje

# D y E
def mostrar_mas_debil(lista_personajes:list, genero):
    '''Devuelve el personaje masculino mas debil'''
    mas_debil =  None
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            if mas_debil == None or int(personaje["fuerza"]) < mas_debil:
                mas_debil = int(personaje["fuerza"])
                nombre_mas_debil = personaje["nombre"]

    if genero == "M":
        tipo_genero = "Masculino"
    else:
        tipo_genero = "NB"

    if mas_debil == None:
        mensaje = f"No hay personajes de {tipo_genero}"
    else:
        mensaje = f"El {tipo_genero} mas debil es: {nombre_mas_debil}"

    return mensaje

# F
def mostrar_fuerza_promedio_NB(lista_personajes:list):
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

# G Y H
def mostrar_cuantos_hay_por_tipos_clave(lista_personajes:list , ojos_o_pelo:str , flag=True):
    '''Printea cuantos hay de cada tipo de clave'''
    lista_contador = []


    valores = set(personaje[ojos_o_pelo] for personaje in lista_personajes)

    for color in valores:
        contador = 0
        lista_nombres_mismo_color = []
        for personaje in lista_personajes:
            if personaje[ojos_o_pelo] == color:
                contador += 1
                lista_nombres_mismo_color.append(personaje["nombre"])

        diccionario_colores = {}
        diccionario_colores[color] = contador
        diccionario_colores["nombres"] = lista_nombres_mismo_color

        lista_contador.append(diccionario_colores)

    if flag == True:
        for color in lista_contador:
            primera_clave = list(color.keys())[0]
            primer_valor = list(color.values())[0]
            if ojos_o_pelo == "color_ojos":
                tipo_valor = "Ojos"
            else:
                tipo_valor = "Pelo"
            print(f"Personajes con {tipo_valor} de color '{primera_clave}': {primer_valor}")

        # USAR ESTE RETURN PARA EL INCISO I
    return lista_contador

# I y J
def listar_personajes_por_clave(lista_personajes:list , tipo_valor:str , flag=False):
    '''Printea los nombres de los personajes agrupados por Clave pasada por parametro'''
    lista = mostrar_cuantos_hay_por_tipos_clave(lista_personajes, tipo_valor ,flag)

    for elemento in lista:
        primera_clave = list(elemento.keys())[0]
        segundo_valor = list(elemento.values())[1]
        if tipo_valor == "color_ojos":
            valor_clave = "Ojos"
        else:
            valor_clave = "Inteligencia"
        print(f"{valor_clave}: {primera_clave}: ")
        for nombre in segundo_valor:
            print(f"  {nombre}")