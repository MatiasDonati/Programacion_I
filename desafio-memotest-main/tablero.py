from constantes import *
import tarjeta
import random
import pygame

def crear_tablero():
    '''
    Crea un diccionario con toda la informacion necesaria para el tablero, creando la lista de tarjetas y todos sus parametros.
    Retorna un diccionario con el tablero
    '''
    tablero = {}
    tablero['tarjetas'] = generar_lista_tarjetas(CANTIDAD_TARJETAS_H, CANTIDAD_TARJETAS_V, ANCHO_TARJETA, ALTO_TARJETA)
    tablero['tiempo_ultimo_destape'] = pygame.time.get_ticks()
    tablero['primer_tarjeta_seleccionada'] = None
    tablero['segunda_tarjeta_seleccionada'] = None

    return tablero
    #Creo el diccionario del tablero

def generar_lista_tarjetas(tarjetas_horizontal:int, tarjetas_vertical:int, ancho_tarjeta:int, alto_tarjeta:int)->list:
    '''
    Función que se encarga de generar una lista de tarjetas.
    Va a generar la cantidad de tarjetas que le especifique anteriormente con las constantes teniendo en cuenta el eje X y el eje Y correspondiente de las superficies de cada una de las tarjetas.
    Retorna la lista de las tarjetas generadas
    '''
    lista_tarjetas = []
    indice = 0
    lista_id = generar_lista_ids_tarjetas(CANTIDAD_TARJETAS_UNICAS)

    pos_x = 0
    pos_y = 0

    for x in range(CANTIDAD_TARJETAS_H):
        pos_x = ANCHO_TARJETA * x
        for y in range(CANTIDAD_TARJETAS_V):
            pos_y = ALTO_TARJETA * y
            # print(pos_x, pos_y)
            path = f"./recursos/0{lista_id[indice]}.png"
            img = tarjeta.crear_tarjeta("./recursos/00.png", lista_id[indice],path, pos_x, pos_y, ANCHO_TARJETA, ALTO_TARJETA)
            indice += 1
            lista_tarjetas.append(img)

    return lista_tarjetas


def generar_lista_ids_tarjetas(cantidad_de_tarjetas_unicas:int):
    '''
    Funcion que se encarga de ordenar de forma aleatoria los id de las tarjetas para que las mismas tengan un orden aleatorio en cada partida.
    '''
    lista_ids = []
    for tarjeta in range(1, cantidad_de_tarjetas_unicas + 1):
        lista_ids.append(tarjeta)
        lista_ids.append(tarjeta)

    random.shuffle(lista_ids)

    return lista_ids


def detectar_colision(tablero, pos_xy):

    # if tablero["primer_tarjeta_seleccionada"] and tablero["segunda_tarjeta_seleccionada"]:
    #     return

    for tarjeta in tablero["tarjetas"]:

        if tarjeta["rectangulo"].collidepoint(pos_xy) and tarjeta["visible"] == False:
            tarjeta["visible"] = True

            print(tablero["primer_tarjeta_seleccionada"])

            if tablero["primer_tarjeta_seleccionada"] == None:
                tablero["primer_tarjeta_seleccionada"] = tarjeta
            else:
                print(tablero["primer_tarjeta_seleccionada"])

                tablero["segunda_tarjeta_seleccionada"] = tarjeta
                tablero["tiempo_ultimo_destape"] = pygame.time.get_ticks()


def actualizar_tablero(tablero):

    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tablero['tiempo_ultimo_destape']

    if tiempo_transcurrido >= TIEMPO_MOVIMIENTO:
        # Se ha superado el tiempo de espera, ocultar las tarjetas
        tablero['tiempo_ultimo_destape'] = 0

        for card in tablero['tarjetas']:
            if not card['descubierto']:
                card['visible'] = False

        if tablero['primer_tarjeta_seleccionada'] and tablero['segunda_tarjeta_seleccionada']:
            tarjeta1 = tablero['primer_tarjeta_seleccionada']
            tarjeta2 = tablero['segunda_tarjeta_seleccionada']

            if tarjeta1['identificador'] == tarjeta2['identificador']:
                # Si coinciden, marcarlas como descubiertas
                tarjeta1['descubierto'] = True
                tarjeta2['descubierto'] = True
                print("MATCHEOOOOOOO")
            else:
                print(" NO NO NO NO NO MATCHEOOOOOOO")
                '''ACA HAY UN PROBLEMA'''
                # for tarjeta in tablero['tarjetas']:
                #     if tarjeta['identificador'] == tablero['primer_tarjeta_seleccionada']['identificador']:
                #         tarjeta['visible'] = False

            tablero['primer_tarjeta_seleccionada'] = None
            tablero['segunda_tarjeta_seleccionada'] = None


def descubrir_tarjetas(lista_tarjetas, identificador):
    '''
        Función que se encarga de cambiarle la bandera a las tarjetas a las que el usuario haya acertado en el memotest y por ende mostrarlas.
        Recorre las tarjetas de la lista y si tiene el mismo identificador que el pasado por parametro y tambien la misma no ha sido descubierta anteriormente cambia la bandera de la clave descubierto a True
        Recibe la lista de tarjetas y el identificador a la que le va a reemplazar la bandera descubierto
    '''
    #Cambio la bandera de desubierto a True si la misma no se descubrio anteriormente.
    pass

def comparar_tarjetas(tablero):
    '''
    Funcion que se encarga de encontrar un match en la selección de las tarjetas del usuario.
    Si el usuario selecciono dos tarjetas está función se encargara de verificar si el identificador
    de las mismas corresponde si es así retorna True, sino False.
    En caso de que no hayan dos tarjetas seleccionadas retorna None
    '''
    retorno = False

    if tablero["primer_tarjeta_seleccionada"]['identificador'] == tablero["segunda_tarjeta_seleccionada"]['indiidentificadorcador']:
        retorno = True

    if tablero["primer_tarjeta_seleccionada"]['identificador'] == None or tablero["primer_tarjeta_seleccionada"]['identificador'] == None:
        retorno = None

    return retorno

def dibujar_tablero(tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    pantalla_juego.fill(COLOR_BLANCO)

    for card in tablero['tarjetas']:
        if card['visible'] == True:
            pantalla_juego.blit(card['imagen'], card['rectangulo'])
        else:
            pantalla_juego.blit(card['imagen_escondida'], card['rectangulo'])


        # if event.type == pygame.MOUSEBUTTONDOWN:

        #     print(event)
        #     if card['rectangulo'].collidepoint(event.pos):

        #         card['visible'] = True

    #Dibuja el tablero con todas las cartas en la pantalla de mi juego