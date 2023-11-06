import re
import pygame
import constantes

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
ALTO_BRUJA = constantes.ALTO_BRUJA

#Velocidades
velocidad_base = 2
velocidad_shift = 6


class Personaje:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("./imgs/bruja_color.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_bruja = pygame.Rect(x, y, ancho, alto)
        self.isJump = False  
        self.jumpCount = 10 


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

    
    def presionar_tecla(self,lista_eventos, bloques):

        #Salto
        sobre_bloque = False

        velocidad = velocidad_shift if lista_eventos[pygame.K_LSHIFT] else velocidad_base

        if lista_eventos[pygame.K_LEFT]:
            self.update(-velocidad, 0 , "izquierda")

        if lista_eventos[pygame.K_RIGHT]:
            self.update(velocidad , 0 , "derecha")

        if lista_eventos[pygame.K_DOWN]:
            self.update(0 , -velocidad , "abajo")

        #TRUCO VOLAR
        if lista_eventos[pygame.K_w]:
            if lista_eventos[pygame.K_UP]:
                sobre_bloque = True
                self.update(0 , velocidad , "arriba")
        """
         if not self.isJump:

            if not sobre_bloque:
                self.update(0 , -6 , "abajo")

            if lista_eventos[pygame.K_SPACE]:
                self.isJump = True

        else:
            if self.jumpCount >= -10:
                velocidad = -(self.jumpCount * abs(self.jumpCount)) * 0.4
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False
            self.update(0, - velocidad, "arriba")

            #HACER QUE LA COLISION NO TENGA EFECTO SI TOCA LA CARA  DE LA BRUJA CON EL BLOQUE (si la bruja se choca con un objeto a la altura de su rectangulo)
            #Q EL PISO SEA UN RECTANGULO DONDE COLISIONA!!!!
            #Q EL PISO SEA UN RECTANGULO DONDE COLISIONA!!!!

            for bloque_actual in bloques:
                if self.rect_bruja.colliderect(bloque_actual.rect_bloque):
                    print("colisionnnnnN")
                    self.rect_bruja.y = bloque_actual.rect_bloque.y + bloque_actual.rect_bloque.height
                    velocidad = 0  # Restablece la velocidad vertical
                    self.update(0, 0, "abajo")
                    sobre_bloque = True

                else:
                    sobre_bloque = False

        if self.rect_bruja.colliderect(bloques[0].rect_bloque) == False and self.rect_bruja.colliderect(bloques[1].rect_bloque) == False and self.rect_bruja.colliderect(bloques[2].rect_bloque) == False and self.rect_bruja.colliderect(bloques[3].rect_bloque) == False and self.rect_bruja.colliderect(bloques[4].rect_bloque) == False:
            sobre_bloque = False
        else:
            sobre_bloque = True
        """
       