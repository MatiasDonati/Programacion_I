import pygame
import colores

def cargar_imagen(ruta, ancho, alto):
    imagen = pygame.image.load(ruta)
    imagen = pygame.transform.scale(imagen, (ancho, alto))
    return imagen

def crear(x, y, ancho, alto):
    dict_personaje = {}
    dict_personaje["surface"] = cargar_imagen("personaje.png", ancho, alto)
    # dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"], ancho, alto)
    dict_personaje["rect_avatar"] = pygame.Rect(x - 100, y, ancho, alto)
    dict_personaje["rect_mano"] = pygame.Rect((x+ancho/2)-80, y+25, 30, 30)
    dict_personaje["score"] = 0
    return dict_personaje

def actualizar_pantalla(personaje, ventana_ppal):
    ventana_ppal.blit(personaje["surface"], personaje["rect_avatar"])
    # pygame.draw.rect(ventana_ppal, colores.ROJO, personaje["rect_avatar"])
    # pygame.draw.rect(ventana_ppal, colores.NEGRO, personaje["rect_mano"])

def update(personaje, incremento_x, incremento_y):
    nueva_x = personaje["rect_avatar"].x + incremento_x
    nueva_y = personaje["rect_avatar"].y + incremento_y

    if (nueva_x > 0 and nueva_x <600):
        personaje["rect_avatar"].x = personaje["rect_avatar"].x + incremento_x
        personaje["rect_mano"].x = personaje["rect_mano"].x + incremento_x

    if (nueva_y > 0 and nueva_y <600):
        personaje["rect_avatar"].y = personaje["rect_avatar"].y + incremento_y
        personaje["rect_mano"].y = personaje["rect_mano"].y + incremento_y