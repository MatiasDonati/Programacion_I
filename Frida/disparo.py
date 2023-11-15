import pygame
from configuraciones import *

class Disparo:
    def __init__(self, x, y, direccion, fueguito=False):
        # self.superficie = img_fueguito_derecha
        # self.superficie = img_hechizo_1_derecha
        self.superficie = img_hechizo_2_derecha
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion

        self.fueguito = fueguito
        if self.fueguito:
            self.superficie = img_fueguito_derecha

    def actualizar(self, ventana_ppal):
        if self.direccion == 'derecha':
            # self.superficie = img_fueguito_derecha
            # self.superficie = img_hechizo_1_derecha
            self.superficie = img_hechizo_2_derecha
            if self.fueguito:
                self.superficie = img_fueguito_derecha
            else:
                self.rectangulo.x += 10
        elif self.direccion == 'izquierda':
            # self.superficie = img_fueguito_izquierda
            # self.superficie = img_hechizo_1_izquierda
            if self.fueguito:
                self.superficie = img_fueguito_izquierda
            else:
                self.superficie = img_hechizo_2_izquierda
            self.rectangulo.x -= 10
        ventana_ppal.blit(self.superficie, self.rectangulo)