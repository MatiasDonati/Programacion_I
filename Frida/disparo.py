import pygame
from configuraciones import *

class Disparo:
    def __init__(self, x, y, direccion):
        self.superficie = img_fueguito_derecha
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion

    def actualizar(self, ventana_ppal):
        if self.direccion == 'derecha':
            self.superficie = img_fueguito_derecha
            self.rectangulo.x += 10
        elif self.direccion == 'izquierda':
            self.superficie = img_fueguito_izquierda
            self.rectangulo.x -= 10
        ventana_ppal.blit(self.superficie, self.rectangulo)