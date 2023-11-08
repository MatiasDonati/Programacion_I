import re
import pygame
import constantes
from configuraciones import *
import random

class Disparo:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("./imgs/bruja_color.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_disparo = pygame.Rect(x, y, ancho - 50, alto - 50)
        self.isJump = False
        self.jumpCount = 10
        self.vidas = 3


    def actualizar_pantalla(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_disparo)
        pygame.draw.rect(ventana_ppal, constantes.ROJO, self.rect_disparo)