import pygame
import constantes
import bloque
from personaje import *
from enemigo import *
from configuraciones import *
import colision
from disparo import *

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ALTO_BRUJA = constantes.ALTO_BRUJA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
ALTO_ENEMIGO = constantes.ALTO_ENEMIGO
ANCHO_ENEMIGO = constantes.ANCHO_ENEMIGO
ANCHO_BLOQUE = constantes.ANCHO_BLOQUE
ALTO_BLOQUE = constantes.ALTO_BLOQUE

pygame.init()

#Personaje
diccionario_animaciones = {}
diccionario_animaciones['derecha'] = personaje_derecha
diccionario_animaciones['izquierda'] = personaje_izquierda
diccionario_animaciones['quieto'] = personaje_quieto
diccionario_animaciones['salta'] = personaje_salta

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Frida")

#Fuente del Texto
pygame.freetype.init()
fuente = pygame.freetype.Font(None, 36)

#Imagenes Fondo
fondo = pygame.image.load('./imgs/fondo3.jpg')
fondo_intro = pygame.image.load('./imgs/fondo_inicio.jpg')

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

#Bloques
bloque_uno = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_dos = bloque.Bloque(ANCHO_VENTANA - ANCHO_BLOQUE - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_tres = bloque.Bloque(ANCHO_VENTANA /2 - ANCHO_BLOQUE /2  ,(ALTO_VENTANA - ALTO_BRUJA * 3) - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_cuatro = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_cinco = bloque.Bloque(ANCHO_VENTANA - ANCHO_BLOQUE - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloques = [bloque_uno, bloque_dos, bloque_tres, bloque_cuatro, bloque_cinco]

#Creacion de Elementos
frida = Personaje(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)

bala = Disparo(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)

enemigo = Enemigo(bloque_cinco.rect_bloque.x,bloque_cinco.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_dos = Enemigo(bloque_cuatro.rect_bloque.x * 1.6,bloque_cuatro.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_tres = Enemigo(bloque_tres.rect_bloque.x,bloque_tres.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigos = [enemigo, enemigo_dos, enemigo_tres]

intro = True
while intro:
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_RETURN]:
        intro = False

    fondo_intro = pygame.transform.scale(fondo_intro, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo_intro, (0, 0))

    texto_superficie, texto_rect = fuente.render("¡Toca ENTER para Jugarrr", constantes.NEGRO)
    texto_superficie_2, texto_rect = fuente.render("ea ea ea ea", constantes.GRIS)

    x = ANCHO_VENTANA // 2 - texto_rect.width // 2
    y = ALTO_VENTANA // 2 - texto_rect.height // 2

    ventana_ppal.blit(texto_superficie, (x, y))
    ventana_ppal.blit(texto_superficie_2, (x, y+50))


    pygame.display.flip()


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

    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo, (0, 0))

    # frida.actualizar_pantalla(ventana_ppal)

    for enemigo_ in enemigos:
        enemigo_.update(ventana_ppal)

    colisionar = colision.colisionar(frida, enemigos)

    if not colisionar:
        frida.actualizar_pantalla(ventana_ppal)
    else:
        frida.restar_vida()

    # bala.actualizar_pantalla(ventana_ppal)

    for bloque_ in bloques:
        bloque_.actualizar_pantalla(ventana_ppal)

    pygame.display.flip()

    pygame.time.delay(7)

pygame.quit()