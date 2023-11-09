import pygame
import constantes
import bloque
from personaje import *
from enemigo import *
from configuraciones import *
import colision
from disparo import *
from tiempo import *


vida_frida = False

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
fondo_fin = pygame.image.load('./imgs/fin.jpg')


# TIMER
segundos = "30"
fin_tiempo = False
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,1000)

#definir musica
pygame.mixer.init()
ruta_audio = './audio/DiagramadeVen.mp3'
sonido_fondo = pygame.mixer.Sound(ruta_audio)
volumen = 0.5
sonido_fondo.set_volume(volumen)
flag_sonido = False

#carcajada sound
ruta_risa = './audio/carcajada.mp3'
sonido_risa = pygame.mixer.Sound(ruta_risa)
sonido_risa.set_volume(0.05)
risa_reproducida = False

#carcajada sound
ruta_musica_fin = './audio/besau.mp3'
musica_fin = pygame.mixer.Sound(ruta_musica_fin)
sonido_risa.set_volume(1)

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

sonido_risa.play()
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

    texto_superficie, texto_rect = fuente.render("¡FRIDA!", constantes.GRIS)
    texto_superficie_2, texto_rect = fuente.render("Presina Enter para Jugar...", constantes.NEGRO)

    x = ANCHO_VENTANA // 2 - texto_rect.width // 2
    y = ALTO_VENTANA // 2 - texto_rect.height // 2

    ventana_ppal.blit(texto_superficie, (x, y))
    ventana_ppal.blit(texto_superficie_2, (x, y+50))

    pygame.display.flip()

sonido_risa.stop()

flag_run = True
while flag_run:

    if flag_sonido == False:
        sonido_fondo.play()
        flag_sonido = True

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    if int(segundos) <= 5:
                        volumen = volumen - 0.1
                        sonido_fondo.set_volume(volumen)
                    if int(segundos) == 0:
                        fin_tiempo = True
                        segundos = 'Tiempo Terminado...'
                        sonido_fondo.stop()

    lista_teclas = pygame.key.get_pressed()
    frida.presionar_tecla(lista_teclas, bloques)

    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo, (0, 0))

    segundos_texto, segundos_rect = fuente.render(str(segundos), constantes.GRIS)
    ventana_ppal.blit(segundos_texto, (10, 10))

    texto_vidas, texto_rect = fuente.render(f'Vidas: {str(frida.vidas)}', constantes.GRIS)
    ventana_ppal.blit(texto_vidas, (ANCHO_VENTANA - texto_rect.width - texto_rect.width * 0.5 , 10))

    for enemigo_ in enemigos:
        enemigo_.update(ventana_ppal)

    # frida.actualizar_pantalla(ventana_ppal)
    colisionar = colision.colisionar(frida, enemigos)
    if not colisionar:
        frida.actualizar_pantalla(ventana_ppal)
    else:
        muerta = frida.restar_vida()
        if muerta:
           flag_run = False 

    # bala.actualizar_pantalla(ventana_ppal)

    for bloque_ in bloques:
        bloque_.actualizar_pantalla(ventana_ppal)

    pygame.display.flip()

    pygame.time.delay(7)

sonido_fondo.stop()

pygame.display.set_caption("Fin")
musica_fin.play()

# pygame.time.delay(100)

flag_final = True
while flag_final:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_final = False

    fondo_fin = pygame.transform.scale(fondo_fin, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo_fin, (0, 0))

    texto_superficie, texto_rect = fuente.render("ADIOS!", constantes.NEGRO)

    ventana_ppal.blit(texto_superficie, (500, 300))

    pygame.display.flip()

pygame.quit()