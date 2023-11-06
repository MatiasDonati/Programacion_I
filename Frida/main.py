import pygame
import constantes
import personaje
import bloque
from personaje import *
from enemigo import *
from configuraciones import *
import colision

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA

ALTO_BRUJA = constantes.ALTO_BRUJA
ANCHO_BRUJA = constantes.ANCHO_BRUJA

ALTO_ENEMIGO = constantes.ALTO_ENEMIGO
ANCHO_ENEMIGO = constantes.ANCHO_ENEMIGO

# COLOR_FONDO = constantes.GRIS

ancho_bloque = ANCHO_VENTANA / 4
alto_bloque = ALTO_VENTANA / 15

pygame.init()

#Personaje
diccionario_animaciones = {}
diccionario_animaciones['derecha'] = personaje_derecha
diccionario_animaciones['izquierda'] = personaje_izquierda
diccionario_animaciones['quieto'] = personaje_quieto
diccionario_animaciones['salta'] = personaje_salta

# TAMAO DE LA VENTANA
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
# TITULO DE LA VENTANA
pygame.display.set_caption("La Bruja Frida")
#Imagen Fondo
fondo = pygame.image.load('./imgs/nebulosa.jpg')

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)


#Bloques
bloque_uno = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - alto_bloque, ancho_bloque, alto_bloque)
bloque_dos = bloque.Bloque(ANCHO_VENTANA - ancho_bloque - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - alto_bloque, ancho_bloque, alto_bloque)
bloque_tres = bloque.Bloque(ANCHO_VENTANA /2 - ancho_bloque /2  ,(ALTO_VENTANA - ALTO_BRUJA * 3) - alto_bloque, ancho_bloque, alto_bloque)
bloque_cuatro = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - alto_bloque, ancho_bloque, alto_bloque)
bloque_cinco = bloque.Bloque(ANCHO_VENTANA - ancho_bloque - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - alto_bloque, ancho_bloque, alto_bloque)

bloques = [bloque_uno, bloque_dos, bloque_tres, bloque_cuatro, bloque_cinco]

#Creacion de Elementos
frida = Personaje(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)

enemigo = Enemigo(bloque_cinco.rect_bloque.x,bloque_cinco.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques)
enemigo_dos = Enemigo(bloque_cuatro.rect_bloque.x * 1.6,bloque_cuatro.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques)

enemigos = [enemigo, enemigo_dos]

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
    frida.presionar_tecla(lista_teclas, bloques)

    #VOLCAR CAMBIOS
    # ventana_ppal.fill(COLOR_FONDO)

    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo, (0, 0))

    frida.actualizar_pantalla(ventana_ppal)

    for enemigo_ in enemigos:
        enemigo_.actualizar_pantalla(ventana_ppal)

    colision.colisionar(frida, enemigos)

    for bloque_ in bloques:
        bloque_.actualizar_pantalla(ventana_ppal)

    pygame.display.flip()
pygame.quit()