import pygame
import constantes
import personaje
import bloque
from personaje import *

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ALTO_BRUJA = constantes.ALTO_BRUJA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
COLOR_FONDO = constantes.GRIS
ancho_bloque = ANCHO_VENTANA /4
alto_bloque = ALTO_VENTANA / 15

pygame.init()

# TAMAO DE LA VENTANA
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
# TITULO DE LA VENTANA
pygame.display.set_caption("La Bruja Frida")
#Imagen Fondo
fondo = pygame.image.load('./imgs/nebulosa.jpg')

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)


#Creacion de Elementos
player = Personaje(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)

#Bloques
bloque_uno = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - alto_bloque, ancho_bloque, alto_bloque)
bloque_dos = bloque.Bloque(ANCHO_VENTANA - ancho_bloque - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - alto_bloque, ancho_bloque, alto_bloque)
bloque_tres = bloque.Bloque(ANCHO_VENTANA /2 - ancho_bloque /2  ,(ALTO_VENTANA - ALTO_BRUJA * 3) - alto_bloque, ancho_bloque, alto_bloque)
bloque_cuatro = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - alto_bloque, ancho_bloque, alto_bloque)
bloque_cinco = bloque.Bloque(ANCHO_VENTANA - ancho_bloque - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - alto_bloque, ancho_bloque, alto_bloque)

bloques = [bloque_uno, bloque_dos, bloque_tres, bloque_cuatro, bloque_cinco]


#Velocidades
velocidad_base = 2
velocidad_shift = 6

#Salto
isJump = False
jumpCount = 10

sobre_bloque = False

#LGICA DEL JUEGO
flag_run = True
while flag_run:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                #PASA EL TIEMPO
                pass

    lista_teclas = pygame.key.get_pressed()
    # personaje.presionar_tecla(lista_teclas)



    velocidad = velocidad_shift if lista_teclas[pygame.K_LSHIFT] else velocidad_base

    if lista_teclas[pygame.K_LEFT]:
        player.update(-velocidad, 0 , "izquierda")

    if lista_teclas[pygame.K_RIGHT]:
        player.update(velocidad , 0 , "derecha")

    if lista_teclas[pygame.K_DOWN]:
        player.update(0 , -velocidad , "abajo")

    #TRUCO VOLAR
    #TRUCO VOLAR
    if lista_teclas[pygame.K_w]:
        if lista_teclas[pygame.K_UP]:
            sobre_bloque = True
            player.update(0 , velocidad , "arriba")


    if not isJump:

        if not sobre_bloque:
            player.update(0 , -6 , "abajo")

        if lista_teclas[pygame.K_SPACE]:
            isJump = True
    else:

        if jumpCount >= -10:
            velocidad = -(jumpCount * abs(jumpCount)) * 0.4
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
        player.update(0, - velocidad, "arriba")

        #HACER QUE LA COLISION NO TENGA EFECTO SI TOCA LA CARA  DE LA BRUJA CON EL BLOQUE (si la bruja se choca con un objeto a la altura de su rectangulo)
        #Q EL PISO SEA UN RECTANGULO DONDE COLISIONA!!!!
        #Q EL PISO SEA UN RECTANGULO DONDE COLISIONA!!!!
        for bloque_actual in bloques:
            if player.rect_bruja.colliderect(bloque_actual.rect_bloque):
                velocidad -= 10
                jumpCount = 10
                isJump = False
                sobre_bloque = True
                player.rect_bruja.y = (bloque_actual.rect_bloque.y - ALTO_BRUJA ) + ALTO_BRUJA * 1/7
            else:
                sobre_bloque = False

    if player.rect_bruja.colliderect(bloque_uno.rect_bloque) == False and player.rect_bruja.colliderect(bloque_dos.rect_bloque) == False and player.rect_bruja.colliderect(bloque_tres.rect_bloque) == False and player.rect_bruja.colliderect(bloque_cuatro.rect_bloque) == False and player.rect_bruja.colliderect(bloque_cinco.rect_bloque) == False:
          sobre_bloque = False
    else:
        sobre_bloque = True


    #VOLCAR CAMBIOS
    ventana_ppal.fill(COLOR_FONDO)

    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo, (0, 0))

    player.actualizar_pantalla(ventana_ppal)

    bloque_uno.actualizar_pantalla(ventana_ppal)
    bloque_dos.actualizar_pantalla(ventana_ppal)
    bloque_tres.actualizar_pantalla(ventana_ppal)
    bloque_cuatro.actualizar_pantalla(ventana_ppal)
    bloque_cinco.actualizar_pantalla(ventana_ppal)

    pygame.display.flip()
pygame.quit()