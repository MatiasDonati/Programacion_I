import re
import pygame
import constantes

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
ALTO_BRUJA = constantes.ALTO_BRUJA


class Personaje:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("./imgs/bruja_color.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_bruja = pygame.Rect(x, y, ancho, alto)

    def actualizar_pantalla(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_bruja)

    def update(self, incremento_x, incremento_y, direccion):
        nueva_x = self.rect_bruja.x + incremento_x
        nueva_y = self.rect_bruja.y - incremento_y

        if nueva_x > 0 and nueva_x < ANCHO_VENTANA - ANCHO_BRUJA:
            self.rect_bruja.x = self.rect_bruja.x + incremento_x

        if nueva_y > 0 and nueva_y < ALTO_VENTANA - ALTO_BRUJA:
            self.rect_bruja.y = self.rect_bruja.y - incremento_y

        if direccion == "izquierda":
            self.surface = pygame.image.load("./imgs/bruja_color_izq.png")
        elif direccion == "derecha":
            self.surface = pygame.image.load("./imgs/bruja_color.png")

        self.surface = pygame.transform.scale(self.surface, (ANCHO_BRUJA, ALTO_BRUJA))


    #update se va a llamar en una funcion q sea presionar tecla aca...