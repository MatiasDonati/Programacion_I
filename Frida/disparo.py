import pygame
from configuraciones import *

class Disparo:
    def __init__(self, x, y, direccion, fueguito):
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
            if self.fueguito == 'enemigos':
                self.superficie = img_fueguito_derecha
                self.rectangulo.x += 5
            elif self.fueguito == 'enemigo_final':
                self.superficie = img_disparo_enemigo_final_derecha
                self.rectangulo.x += 5
            else:
                self.superficie = img_hechizo_2_derecha
                self.rectangulo.x += 10

        elif self.direccion == 'izquierda':
            if self.fueguito == 'enemigos':
                self.superficie = img_fueguito_izquierda
                self.rectangulo.x -= 5
            elif self.fueguito == 'enemigo_final':
                self.superficie = img_disparo_enemigo_final_izquierda
                self.rectangulo.x -= 5
            else:
                self.superficie = img_hechizo_2_izquierda
                self.rectangulo.x -= 10

        ventana_ppal.blit(self.superficie, self.rectangulo)