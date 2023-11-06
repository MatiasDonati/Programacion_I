import re
import pygame
import constantes

class Enemigo:
    def __init__(self, x, y, ancho, alto, bloques) -> None:

        self.surface = pygame.image.load("./imgs2/bruja/idle/idle_1.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_enemigo = pygame.Rect(x, y, ancho, alto)
        self.direccion_actual = 'derecha'
        self.gravedad = False
        self.bloques = bloques

    def actualizar_pantalla(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_enemigo)
        # pygame.draw.rect(ventana_ppal, constantes.VERDE, self.rect_enemigo)
        self.update()
    def update(self):

        for bloque_actual in self.bloques:
            if self.rect_enemigo.colliderect(bloque_actual.rect_bloque):
                if self.direccion_actual == 'derecha':
                    self.rect_enemigo.x += 1
                    if self.rect_enemigo.x == bloque_actual.rect_bloque.x + (constantes.ANCHO_VENTANA / 4 - constantes.ANCHO_ENEMIGO):
                        self.direccion_actual = 'izquierda'
                else:
                    self.rect_enemigo.x -= 1
                    if self.rect_enemigo.x == bloque_actual.rect_bloque.x:
                        self.direccion_actual = 'derecha'