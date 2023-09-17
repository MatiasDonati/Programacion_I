# A
def recorrer_lista_NB(lista_personajes):
    lista_personajes_NB = []
    for personaje in lista_personajes:
        if personaje["genero"] == "NB":
            lista_personajes_NB.append(personaje["nombre"])
    if len(lista_personajes_NB) == 0:
        mensaje = "\nNo hay personajes NB"
    else:
        mensaje = lista_personajes_NB

    return mensaje

# B
def mostrar_femenino_mas_alto(lista_personajes):
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
    masculino_mas_debil =  None
    for personaje in lista_personajes:
        if personaje["genero"] == "M":
            if masculino_mas_debil == None or int(personaje["fuerza"]) < masculino_mas_debil:
                masculino_mas_debil = int(personaje["fuerza"])
                nombre_masculino_mas_debil = personaje["nombre"]
    mensaje = f"El masculino mas debil es: {nombre_masculino_mas_debil}"

    return mensaje