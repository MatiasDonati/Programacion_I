import re
import pygame
import constantes
from disparo import *

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
ALTO_BRUJA = constantes.ALTO_BRUJA

# Velocidades
velocidad_base = 4
velocidad_shift = 7

class Personaje:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("./imgs/bruja_color.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_frida = pygame.Rect(x, y, ancho, alto)
        self.isJump = False
        self.jumpCount = 10
        self.vidas = 3


    def actualizar_pantalla(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_frida)
        pygame.draw.rect(ventana_ppal, constantes.ROJO, self.rect_frida)

    def update(self, incremento_x, incremento_y, direccion):
        nueva_x = self.rect_frida.x + incremento_x
        nueva_y = self.rect_frida.y - incremento_y

        if nueva_x > 0 and nueva_x < ANCHO_VENTANA - ANCHO_BRUJA:
            self.rect_frida.x = self.rect_frida.x + incremento_x

        if nueva_y > 0 and nueva_y < ALTO_VENTANA - ALTO_BRUJA:
            self.rect_frida.y = self.rect_frida.y - incremento_y

        if direccion == "izquierda":
            self.surface = pygame.image.load("./imgs/bruja_color_izq.png")
        elif direccion == "derecha":
            self.surface = pygame.image.load("./imgs/bruja_color.png")

        self.surface = pygame.transform.scale(self.surface, (ANCHO_BRUJA, ALTO_BRUJA))

    def presionar_tecla(self, lista_eventos, bloques):

        velocidad = velocidad_shift if lista_eventos[pygame.K_LSHIFT] else velocidad_base
        sobre_bloque = False

        if lista_eventos[pygame.K_LEFT]:
            self.update(-velocidad, 0, "izquierda")
        if lista_eventos[pygame.K_RIGHT]:
            self.update(velocidad, 0, "derecha")
        if lista_eventos[pygame.K_DOWN]:
            self.update(0, -velocidad, "abajo")
        if lista_eventos[pygame.K_r]:
            print('PUM!! PUM!! PUM!! PUM!! DISPARA FRIDA PUN PUN')

        if lista_eventos[pygame.K_w] and lista_eventos[pygame.K_UP]:
                sobre_bloque = True
                self.update(0, 4, "arriba")

        if not self.isJump:
            if not sobre_bloque:
                self.update(0, -6, "abajo")
            if lista_eventos[pygame.K_SPACE]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                velocidad = - (self.jumpCount * abs(self.jumpCount)) * 0.6
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False
            self.update(0, -velocidad, "arriba")

        for bloque_actual in bloques:
            if self.rect_frida.colliderect(bloque_actual.rect_bloque):
                self.rect_frida.y = bloque_actual.rect_bloque.y - (ALTO_BRUJA - ALTO_BRUJA * 1/7)
                self.isJump = False
                # sobre_bloque = False
                if lista_eventos[pygame.K_SPACE]:
                    self.isJump = True