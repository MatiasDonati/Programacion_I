import re
import pygame
import constantes
from configuraciones import *
import random

#enemigo Golpe
sonido_golpe = pygame.mixer.Sound('./audio/enemigo_hit.mp3')
sonido_golpe.set_volume(1)
#enemigo Muerte
sonido_muerte = pygame.mixer.Sound('./audio/enemigo_muerte.mp3')
sonido_muerte.set_volume(1.5)

class Enemigo:
    def __init__(self, x, y, ancho, alto, bloques, animaciones, que_hace) -> None:

        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, (ancho, alto))
        self.que_hace = que_hace
        self.animacion_actual = self.animaciones[self.que_hace]
        self.contador_pasos = 0

        self.rect_enemigo = pygame.Rect(x, y , ancho - 20, alto)
        # self.direccion_actual = random.choice(['derecha', 'izquierda'])
        self.direccion_actual = 'derecha'
        self.gravedad = False
        self.bloques = bloques
        self.vidas = 3
        self.cooldown_colision = 0
        self.muerto = False


    def update(self, ventana_ppal):

        # pygame.draw.rect(ventana_ppal, constantes.VERDE, self.rect_enemigo)

        for bloque_actual in self.bloques:
            if self.rect_enemigo.colliderect(bloque_actual.rect_bloque):
                if self.direccion_actual == 'derecha':
                    self.animacion_actual = self.animaciones['derecha']
                    self.rect_enemigo.x += 1
                    if self.rect_enemigo.x == bloque_actual.rect_bloque.x + (constantes.ANCHO_BLOQUE - constantes.ANCHO_ENEMIGO):
                        self.direccion_actual = 'izquierda'
                        self.animacion_actual = self.animaciones['izquierda']
                else:
                    self.rect_enemigo.x -= 1
                    if self.rect_enemigo.x == bloque_actual.rect_bloque.x:
                        self.direccion_actual = 'derecha'
                        self.animacion_actual = self.animaciones['derecha']

        self.animar(ventana_ppal)
                #para coli
        if self.cooldown_colision > 0:
            self.cooldown_colision -= 1

    def animar(self, ventana_ppal):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        ventana_ppal.blit(self.animacion_actual[self.contador_pasos], self.rect_enemigo)
        self.contador_pasos += 1

    def restar_vida(self):

        if self.cooldown_colision == 0:
            if type(self.vidas) == int and self.vidas > 1:
                self.vidas -= 1
                sonido_golpe.play()
                print(self.vidas)
            else:
                print("Murio Enemigoo!")
                sonido_muerte.play()
                self.muerto = True

            self.cooldown_colision = 50