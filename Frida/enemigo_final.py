# import pygame
# from configuraciones import *

# class EnemigoFinal:
#     def __init__(self, x, y, ancho, alto, animaciones, que_hace):
#         self.animaciones = animaciones
#         reescalar_imagenes(self.animaciones, (ancho, alto))
#         self.que_hace = que_hace
#         self.animacion_actual = self.animaciones[self.que_hace]
#         self.contador_pasos = 0
#         self.rect_enemigo = pygame.Rect(x, y , alto, alto)
#         self.direccion_actual = 'quieto'
#         self.vidas = 7
#         self.dispara = False
#         self.lista_proyectiles = []
#         self.tiempo_ultimo_disparo = 0
#         self.TIEMPO_ENTRE_DISPAROS = 2000

#     def update(self, ventana_ppal):
#         pass

import re
import pygame
import constantes
from configuraciones import *
import random
import disparo
import colision

class EnemigoFinal:
    def __init__(self, x, y, ancho, alto, animaciones, que_hace) -> None:

        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, (ancho, alto))
        self.que_hace = que_hace
        self.animacion_actual = self.animaciones[self.que_hace]
        self.contador_pasos = 0

        self.rect_enemigo_final = pygame.Rect(x, y , ancho - 20, alto)
        self.direccion = 'derecha'
        self.gravedad = False
        self.vidas = 3
        self.cooldown_colision = 0
        self.muerto = False

        self.velocidad = 1
        self.tiempo_inicial = pygame.time.get_ticks()
        self.sube = True

        #Segundo Nivel
        self.dispara = False
        self.lista_proyectiles = []
        self.tiempo_ultimo_disparo = 0
        self.TIEMPO_ENTRE_DISPAROS = 2000

    def update(self, ventana_ppal):

        # pygame.draw.rect(ventana_ppal, constantes.VERDE, self.rect_enemigo)

        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial

        if tiempo_transcurrido > 10000:
            self.velocidad = 2

        # if tiempo_transcurrido > 20000:
        #     self.velocidad = 3

        if self.rect_enemigo_final.y >= 0 and self.sube:
            self.rect_enemigo_final.y -= self.velocidad
            if self.rect_enemigo_final.y <= 0:
                self.sube = False
        else:
            self.rect_enemigo_final.y += self.velocidad
            if self.rect_enemigo_final.y >= 600:
                self.sube = True

        if self.rect_enemigo_final.x <= 1000 and self.animacion_actual == self.animaciones['derecha']:
            self.rect_enemigo_final.x += self.velocidad
            if self.rect_enemigo_final.x >= 1000:
                self.animacion_actual = self.animaciones['izquierda']
                self.direccion = 'izquierda'

        else:
            self.rect_enemigo_final.x -= self.velocidad
            if self.rect_enemigo_final.x <= 0:
                self.animacion_actual = self.animaciones['derecha']
                self.direccion = 'derecha'

        self.animar(ventana_ppal)
                #para colision
        if self.cooldown_colision > 0:
            self.cooldown_colision -= 1

    def animar(self, ventana_ppal):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        ventana_ppal.blit(self.animacion_actual[self.contador_pasos], self.rect_enemigo_final)
        self.contador_pasos += 1

    # def restar_vida(self):

    #     if self.cooldown_colision == 0:
    #         if type(self.vidas) == int and self.vidas > 1:
    #             # self.animacion_actual = self.animaciones['explosion']
    #             self.vidas -= 1
    #             # print(self.vidas)

    #         else:
    #             # print("Murio Enemigoo!")
    #             self.muerto = True

    #         self.cooldown_colision = 50

    def disparar(self, ventana_ppal, frida):
        proyectil = None
        proyectiles_a_eliminar = []

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_disparo > self.TIEMPO_ENTRE_DISPAROS:
            if proyectil == None:
                proyectil = disparo.Disparo(self.rect_enemigo_final.x, self.rect_enemigo_final.centery, self.direccion, True)
                self.lista_proyectiles.append(proyectil)
            self.tiempo_ultimo_disparo = tiempo_actual

        for proyectil_actual in self.lista_proyectiles:
            proyectil_actual.actualizar(ventana_ppal)
            # ACA CAPTAR LA COLISION
            choque = colision.atacar_a_frida(proyectil_actual, frida)
            proyectiles_a_eliminar.append(proyectil_actual)
            if choque:
                frida.restar_vida()
                for proyectil_a_eliminar in proyectiles_a_eliminar:
                    self.lista_proyectiles.remove(proyectil_a_eliminar)
                #HACER ANIMACION FRIDA COLISIONADA !!