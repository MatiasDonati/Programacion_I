import re
import pygame
import colores

def crear(x,y,ancho,alto):

    dict_personaje = {}
    dict_personaje["surface"] = pygame.image.load("./imgs/bruja_color.png")
    dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"],(ancho,alto))
    dict_personaje["rect_bruja"] = pygame.Rect(x,y,ancho,alto)
    dict_personaje["score"] = 0

    return dict_personaje

def actualizar_pantalla(personaje,ventana_ppal):

    ventana_ppal.blit(personaje["surface"],personaje["rect_bruja"])
    # pygame.draw.rect(ventana_ppal,colores.ROJO,personaje["rect_bruja"])

def update(personaje,incremento_x, direccion):

    nueva_x = personaje["rect_bruja"].x + incremento_x

    if(nueva_x > 0 and nueva_x < 1050):
        personaje["rect_bruja"].x = personaje["rect_bruja"].x + incremento_x

    if direccion == "left":
        personaje["surface"] = pygame.image.load("./imgs/bruja_color_izq.png")
    else:
        personaje["surface"] = pygame.image.load("./imgs/bruja_color.png")
    personaje["surface"] = pygame.transform.scale(personaje["surface"],(150,150))
