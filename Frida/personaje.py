# import re
import pygame
import constantes
import disparo
import colision

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
ALTO_BRUJA = constantes.ALTO_BRUJA

# Velocidades
velocidad_base = 4
velocidad_shift = 7

#ouch sound
pygame.mixer.init()
ruta_ouch = './audio/ouch.mp3'
sonido_vida_perdida = pygame.mixer.Sound(ruta_ouch)
sonido_vida_perdida.set_volume(0.8)

#Sonido Disparo
sonido_disparo = pygame.mixer.Sound('./audio/sonido_dispaso_hechizo.mp3')
sonido_disparo.set_volume(0.5)


#brujaMuerte
sonido_muerte_bruja = pygame.mixer.Sound('./audio/bruja_muerte.mp3')
sonido_muerte_bruja.set_volume(0.7)

class Personaje:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("./imgs/bruja_color.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_frida = pygame.Rect(x, y, ancho, alto)
        self.isJump = False
        self.jumpCount = 10
        self.vidas = 3
        self.muerta = False
        self.cooldown_colision = 0
        self.direccion = 'derecha'

        self.TIEMPO_ENTRE_DISPAROS = 500
        self.lista_proyectiles = []
        self.tiempo_ultimo_disparo = 0

        self.scoring = 0

    def actualizar_pantalla(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_frida)
        # pygame.draw.rect(ventana_ppal, constantes.ROJO, self.rect_frida)

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

        #para colision
        if self.cooldown_colision > 0:
            self.cooldown_colision -= 1

    def presionar_tecla(self, lista_eventos, bloques):

        velocidad = velocidad_shift if lista_eventos[pygame.K_LSHIFT] else velocidad_base
        sobre_bloque = False

        if lista_eventos[pygame.K_LEFT]:
            self.direccion = 'izquierda'
            self.update(-velocidad, 0, "izquierda")
        if lista_eventos[pygame.K_RIGHT]:
            self.update(velocidad, 0, "derecha")
            self.direccion = 'derecha'
        if lista_eventos[pygame.K_DOWN]:
            self.update(0, -velocidad, "abajo")


        if lista_eventos[pygame.K_w] and lista_eventos[pygame.K_UP]:
                sobre_bloque = True
                self.update(0, 4, "arriba")

        if not self.isJump:
            if not sobre_bloque:
                self.update(0, -6, "abajo")
            if lista_eventos[pygame.K_SPACE]:
                self.isJump = True
        else:

            if lista_eventos[pygame.K_LEFT]:
                self.update(-5, 0, "izquierda")
            if lista_eventos[pygame.K_RIGHT]:
                self.update(5, 0, "derecha")

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

    def restar_vida(self):

        if self.cooldown_colision == 0:
            if type(self.vidas) == int and self.vidas > 1:
                self.vidas -= 1
                print(self.vidas)
            else:
                print("¡Game Over!")
                self.vidas = ' =( No tenes mas vidas '
                self.muerta = True
                sonido_muerte_bruja.play()

            sonido_vida_perdida.play()
            self.cooldown_colision = 200

    def disparar(self, lista_teclas, enemigos, ventana_ppal):
        proyectil = None

        tiempo_actual = pygame.time.get_ticks()
        if lista_teclas[pygame.K_r] and tiempo_actual - self.tiempo_ultimo_disparo > self.TIEMPO_ENTRE_DISPAROS:
            if proyectil == None:
                proyectil = disparo.Disparo(self.rect_frida.x, self.rect_frida.centery, self.direccion)
                sonido_disparo.play()
                self.lista_proyectiles.append(proyectil)
            # else:
            #     proyectil_dos = disparo.Disparo(self.rect_frida.x, self.rect_frida.centery, self.direccion)
            #     self.lista_proyectiles.append(proyectil_dos)
            self.tiempo_ultimo_disparo = tiempo_actual

        if len(self.lista_proyectiles) != 0:
            proyectiles_a_eliminar = []

            for proyectil_actual in self.lista_proyectiles:
                proyectil_actual.actualizar(ventana_ppal)
                for enemigo_actual in enemigos:
                    hubo_colision = colision.matar_enemigo(proyectil_actual, enemigo_actual)
                    if hubo_colision:
                        enemigo_actual.restar_vida()
                        self.scoring += 10
                        if enemigo_actual.muerto:
                            self.scoring += 40
                            enemigos.remove(enemigo_actual)
                        proyectiles_a_eliminar.append(proyectil_actual)

            # Elimina los proyectiles marcados para eliminación
            for proyectil_a_eliminar in proyectiles_a_eliminar:
                self.lista_proyectiles.remove(proyectil_a_eliminar)