import pygame
import constantes
import bloque
from personaje import *
from enemigo import *
from configuraciones import *
import colision
from disparo import *
from eventos import *
from textos import *
import obtener_nombre
import re

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ALTO_BRUJA = constantes.ALTO_BRUJA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
ALTO_ENEMIGO = constantes.ALTO_ENEMIGO
ANCHO_ENEMIGO = constantes.ANCHO_ENEMIGO
ANCHO_BLOQUE = constantes.ANCHO_BLOQUE
ALTO_BLOQUE = constantes.ALTO_BLOQUE

pygame.init()

#Usuario ingreso nombre
ingreso_nombre = False
# patron_usuario = re.compile(r'^[a-zA-Z0-9]{4,}$')
patron_usuario = re.compile(r'^(?=.*[a-zA-Z])[a-zA-Z0-9 ]{4,}$')

#Enemigo animaciones
diccionario_animaciones = {}
diccionario_animaciones['derecha'] = personaje_derecha
diccionario_animaciones['izquierda'] = personaje_izquierda
diccionario_animaciones['quieto'] = personaje_quieto
diccionario_animaciones['salta'] = personaje_salta
diccionario_animaciones['explosion'] = explosion

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Frida")

#Fuente del Texto
pygame.freetype.init()
# ruta_fuente = './fuente/Granesta.ttf'
# fuente = pygame.font.Font(ruta_fuente, 36)
fuente = pygame.freetype.Font(None, 36)

#Imagenes Fondo
fondo = pygame.image.load('./imgs/fondo3.jpg')
fondo_nivel_dos = pygame.image.load('./imgs/fondo_nivel_3.jpg')
fondo_intro = pygame.image.load('./imgs/fondo_inicio.jpg')
fondo_fin = pygame.image.load('./imgs/fin.jpg')

# Timer
segundos = "30"
fin_tiempo = False
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,1000)

#Musica Juego Nivel 1
pygame.mixer.init()
ruta_audio = './audio/DiagramadeVen.mp3'
sonido_fondo = pygame.mixer.Sound(ruta_audio)
volumen = 0.5
sonido_fondo.set_volume(volumen)
flag_sonido = False

sonido_nivel_dos = pygame.mixer.Sound('./audio/nivel_2.mp3')
sonido_nivel_dos.set_volume(0.5)



#Carcajada Introduccion
ruta_risa = './audio/carcajada.mp3'
sonido_risa = pygame.mixer.Sound(ruta_risa)
sonido_risa.set_volume(0.7)


#Carcajada Introduccion
sonido_una_risa = pygame.mixer.Sound('./audio/una_carcajada.mp3')
sonido_una_risa.set_volume(0.7)
sonido_risa_fin_nivel_reproducido = False


#Musica Final
ruta_musica_fin = './audio/besau.mp3'
musica_fin = pygame.mixer.Sound(ruta_musica_fin)
musica_fin.set_volume(1)

#Bloques
bloque_uno = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_dos = bloque.Bloque(ANCHO_VENTANA - ANCHO_BLOQUE - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_tres = bloque.Bloque(ANCHO_VENTANA /2 - ANCHO_BLOQUE /2  ,(ALTO_VENTANA - ALTO_BRUJA * 3) - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_cuatro = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_cinco = bloque.Bloque(ANCHO_VENTANA - ANCHO_BLOQUE - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloques = [bloque_uno, bloque_dos, bloque_tres, bloque_cuatro, bloque_cinco]

#Creacion de Elementos
frida = Personaje(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)

#enemigos nivel 1
enemigo = Enemigo(bloque_cinco.rect_bloque.x,bloque_cinco.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_dos = Enemigo(bloque_cuatro.rect_bloque.x * 1.6,bloque_cuatro.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_tres = Enemigo(bloque_tres.rect_bloque.x,bloque_tres.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigos = [enemigo, enemigo_dos, enemigo_tres]

pantalla_final_perdido = False

sonido_risa.play()
intro = True
while intro:

    lista_eventos = pygame.event.get()

    fondo_intro = pygame.transform.scale(fondo_intro, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo_intro, (0, 0))

    nombre_usuario, ingreso_enter = obtener_nombre.obtener_nombre_usuario(ventana_ppal, fondo_intro)
    if ingreso_enter and patron_usuario.match(nombre_usuario):
        intro = False

sonido_risa.stop()
pygame.display.set_caption("Frida - Nivel 1")

flag_run = True
while flag_run:

    if flag_sonido == False:
        sonido_fondo.play()
        flag_sonido = True

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

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

    mostrar_vidas_y_tiempo(fuente, segundos, frida, ventana_ppal, nombre_usuario)

    colisionar = colision.colisionar(frida, enemigos)

    if not frida.muerta:
        if not colisionar:
            frida.actualizar_pantalla(ventana_ppal)
        else:
            frida.restar_vida()
    else:
        flag_run = False
        pantalla_final_perdido = True

    for enemigo_ in enemigos:
        enemigo_.update(ventana_ppal)

    for bloque_ in bloques:
        bloque_.actualizar_pantalla(ventana_ppal)

    if len(enemigos) == 0 and sonido_risa_fin_nivel_reproducido == False:
        sonido_una_risa.play()
        sonido_risa_fin_nivel_reproducido = True
        flag_run = False

    frida.disparar(lista_teclas, enemigos, ventana_ppal)

    pygame.display.flip()

    pygame.time.delay(7)

sonido_fondo.stop()

frida = Personaje(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)
enemigo = Enemigo(bloque_cinco.rect_bloque.x,bloque_cinco.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_dos = Enemigo(bloque_cuatro.rect_bloque.x * 1.6,bloque_cuatro.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_tres = Enemigo(bloque_tres.rect_bloque.x,bloque_tres.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigos = [enemigo, enemigo_dos, enemigo_tres]

segundos = "30"
fin_tiempo = False
flag_sonido = False

if pantalla_final_perdido:
    flag_run_nivel_dos = False
else:
    flag_run_nivel_dos = True

pygame.display.set_caption("Frida - Nivel 2")

while flag_run_nivel_dos:

    if flag_sonido == False:
        sonido_nivel_dos.play()
        flag_sonido = True

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run_nivel_dos = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

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

    fondo_nivel_dos = pygame.transform.scale(fondo_nivel_dos, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo_nivel_dos, (0, 0))

    mostrar_vidas_y_tiempo(fuente, segundos, frida, ventana_ppal, nombre_usuario)

    colisionar = colision.colisionar(frida, enemigos)

    if not frida.muerta:
        if not colisionar:
            frida.actualizar_pantalla(ventana_ppal)
        else:
            frida.restar_vida()
    else:
        flag_run_nivel_dos = False

    for enemigo_ in enemigos:
        enemigo_.update(ventana_ppal)

######################################################
        # enemigo_.disaprar(ventana_ppal)
        ## Ver la funcion enemigo y la clase disparo !
######################################################



    for bloque_ in bloques:
        bloque_.actualizar_pantalla(ventana_ppal)

    if len(enemigos) == 0 and sonido_risa_fin_nivel_reproducido == False:
        sonido_una_risa.play()
        sonido_risa_fin_nivel_reproducido = True
        flag_run = False

    frida.disparar(lista_teclas, enemigos, ventana_ppal)

    pygame.display.flip()

    pygame.time.delay(7)

sonido_nivel_dos.stop()

pygame.display.set_caption("Fin")
musica_fin.play()
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