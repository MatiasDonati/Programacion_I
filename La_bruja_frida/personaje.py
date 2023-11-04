import re
import pygame
import constantes


ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
ALTO_BRUJA = constantes.ALTO_BRUJA


"""
CONVERTIRLO A CLASE !!
ACOMODAR EL MAIN PARA TAL ACCION!
"""

def crear(x,y,ancho,alto):

    dict_personaje = {}

    # Hacer lista de imagenes para usar tipo animacion
    # Girar imagen programaticamente!

    dict_personaje["surface"] = pygame.image.load("./imgs/bruja_color.png")
    dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"],(ancho,alto))
    dict_personaje["rect_bruja"] = pygame.Rect(x,y,ancho,alto)
    # dict_personaje["animaciones"] = animaciones

    return dict_personaje

def actualizar_pantalla(personaje,ventana_ppal):

    ventana_ppal.blit(personaje["surface"],personaje["rect_bruja"])
    # pygame.draw.rect(ventana_ppal,constantes.ROJO,personaje["rect_bruja"])

def update(personaje,incremento_x,incremento_y, direccion):

    nueva_x = personaje["rect_bruja"].x + incremento_x
    nueva_y = personaje["rect_bruja"].y - incremento_y

    if nueva_x > 0 and nueva_x < ANCHO_VENTANA-ANCHO_BRUJA:
        personaje["rect_bruja"].x = personaje["rect_bruja"].x + incremento_x

    if nueva_y > 0 and nueva_y < ALTO_VENTANA-ALTO_BRUJA:
        personaje["rect_bruja"].y = personaje["rect_bruja"].y - incremento_y


    if direccion == "izquierda":
        personaje["surface"] = pygame.image.load("./imgs/bruja_color_izq.png")

    elif direccion == "derecha":
        personaje["surface"] = pygame.image.load("./imgs/bruja_color.png")

    personaje["surface"] = pygame.transform.scale(personaje["surface"],(ANCHO_BRUJA,ALTO_BRUJA))

    #update se va a llamar en una funcion q sea presionar tecla aca...