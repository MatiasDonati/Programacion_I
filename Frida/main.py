import pygame
import constantes
import bloque
from personaje import *
from enemigo import *
from enemigo_final import *
from configuraciones import *
from base_datos import *
import colision
import recompensas
from disparo import *
from eventos import *
from textos import *
import obtener_nombre
import re
import random
import json
import sonidos


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
patron_usuario = re.compile(r'^(?=.*[a-zA-Z])[a-zA-Z0-9 ]{4,}$')

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Frida")

#Fuente del Texto
pygame.freetype.init()
fuente = pygame.freetype.Font(None, 36)

# with open('ruta_de_tu_json.json', 'r') as archivo_json:
#     datos_json = json.load(archivo_json)

#Imagenes Fondo
fondo = pygame.image.load('./imgs/fondo3.jpg')
fondo_nivel_dos = pygame.image.load('./imgs/fondo_nivel_3.jpg')
fondo_intro = pygame.image.load('./imgs/fondo_inicio.jpg')
fondo_nivel_tres = pygame.image.load('./imgs/findo_nivel_2.jpg')
fondo_fin = pygame.image.load('./imgs/fin.jpg')

# Timer
segundos = "30"
fin_tiempo = False
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,1000)

pygame.mixer.init()
#Musica Nivel 1
sonido_fondo = sonidos.sonido_fondo
flag_sonido = False

#sonido nivel dos
sonido_nivel_dos = sonidos.sonido_nivel_dos
volumen = 0.5
#Danzon
danzon = sonidos.danzon

#Carcajada Introduccion - Varias carcajadas
sonido_risa = sonidos.sonido_risa

#Carcajada
sonido_una_risa = sonidos.sonido_una_risa
sonido_risa_fin_nivel_reproducido = False

#Musica Final Perdido
musica_fin = sonidos.musica_fin

#Musica Final Ganado
musica_fin_ganado = sonidos.musica_fin_ganado

#musica recompensas
musica_recompensas = sonidos.musica_recompensas

#Musica enemigo final
musica_enemigo_final = sonidos.musica_enemigo_final

#Risa Fantasma
risa_fantasma = sonidos.risa_fantasma

#sonidos Score
score_uno = sonidos.score_uno
score_dos = sonidos.score_dos
score_tres = sonidos.score_tres
score_cuatro = sonidos.score_cuatro
lista_sonidos_score = [score_uno, score_dos, score_tres, score_cuatro]
score_final = sonidos.score_final

#Bloques
bloque_uno = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_dos = bloque.Bloque(ANCHO_VENTANA - ANCHO_BLOQUE - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_tres = bloque.Bloque(ANCHO_VENTANA /2 - ANCHO_BLOQUE /2  ,(ALTO_VENTANA - ALTO_BRUJA * 3) - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_cuatro = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_cinco = bloque.Bloque(ANCHO_VENTANA - ANCHO_BLOQUE - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloques = [bloque_uno, bloque_dos, bloque_tres, bloque_cuatro, bloque_cinco]

#Frida
frida = Personaje(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)

#enemigos
enemigo = Enemigo(bloque_cinco.rect_bloque.x,bloque_cinco.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_dos = Enemigo(bloque_cuatro.rect_bloque.x * 1.6,bloque_cuatro.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_tres = Enemigo(bloque_tres.rect_bloque.x,bloque_tres.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_cuatro = Enemigo(bloque_uno.rect_bloque.x,bloque_uno.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_cinco = Enemigo(bloque_dos.rect_bloque.x,bloque_dos.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigos = [enemigo, enemigo_dos, enemigo_tres]


#Enemigo Final
enemigo_final = EnemigoFinal(0, -1000, 150, 150, diccionario_enemigo_final,'derecha')
tiempo_inicio_if = None
enemigo_final_en_accion = False

#Recompensas
posiciones_iniciales = [
    (bloque_uno.rect_bloque.centerx, bloque_uno.rect_bloque.y - ALTO_ENEMIGO),
    (bloque_dos.rect_bloque.centerx, bloque_dos.rect_bloque.y - ALTO_ENEMIGO),
    (bloque_tres.rect_bloque.centerx, bloque_tres.rect_bloque.y - ALTO_ENEMIGO),
    (bloque_cuatro.rect_bloque.centerx, bloque_cuatro.rect_bloque.y - ALTO_ENEMIGO),
    (bloque_cinco.rect_bloque.centerx, bloque_cinco.rect_bloque.y - ALTO_ENEMIGO),
    ]

random.shuffle(posiciones_iniciales)

gatito = recompensas.Recompensa(posiciones_iniciales[0][0], posiciones_iniciales[0][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'gatito')
gatito_dos = recompensas.Recompensa(posiciones_iniciales[1][0], posiciones_iniciales[1][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'gatito_dos')
pocion = recompensas.Recompensa(posiciones_iniciales[2][0], posiciones_iniciales[2][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'pocion')
escoba = recompensas.Recompensa(posiciones_iniciales[3][0], posiciones_iniciales[3][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'escoba')
barita_magica = recompensas.Recompensa(posiciones_iniciales[4][0], posiciones_iniciales[4][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'barita')

lista_recompensas = [gatito, gatito_dos, pocion, escoba, barita_magica]

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

"""
# NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO
# NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO
"""

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
                        # segundos = 'Tiempo Terminado'
                        sonido_fondo.stop()
                        if len(enemigos) == 0:
                            flag_run = False
                            score_final.play()
                        else:
                            pantalla_final_perdido = True
                            flag_run = False

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

    if len(enemigos) == 0:

        random.shuffle(lista_recompensas)

        for recompensa in lista_recompensas:
            recompensa.actualizar(ventana_ppal)
            if colision.agarrar_recompensa(frida, recompensa):
                lista_recompensas.remove(recompensa)
                audio_random = random.choice(lista_sonidos_score)
                audio_random.play()

        if len(lista_recompensas) == 0:
            score_final.play()
            flag_run = False
            frida.scoring += int(segundos)

        if sonido_risa_fin_nivel_reproducido == False:
            sonido_una_risa.play()
            musica_recompensas.play()
            sonido_fondo.stop()
            sonido_risa_fin_nivel_reproducido = True

            """
            flag_run = False
            """

    frida.disparar(lista_teclas, enemigos, ventana_ppal, enemigo_final)

    pygame.display.flip()

    pygame.time.delay(7)

sonido_fondo.stop()
musica_recompensas.stop()


"""
# NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS
# NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS
"""

frida.rect_frida.y = ALTO_VENTANA-ALTO_BRUJA
frida.rect_frida.x = ANCHO_VENTANA/2

lista_recompensas = [gatito, gatito_dos, pocion, escoba, barita_magica]

enemigos = [enemigo, enemigo_dos, enemigo_tres]
for enemigo_ in enemigos:
    enemigo_.muerto = False
    enemigo_.vidas = 3

segundos = "30"
fin_tiempo = False
flag_sonido = False

sonido_risa_fin_nivel_reproducido = False


if pantalla_final_perdido:
    flag_run_nivel_dos = False
else:
    flag_run_nivel_dos = True

pygame.display.set_caption("Frida - Nivel 2")

while flag_run_nivel_dos:

    if flag_sonido == False:
        danzon.play()
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
                        sonido_fondo.stop()
                        if len(enemigos) == 0:
                            flag_run = False
                            score_final.play()
                            flag_run_nivel_dos = False
                        else:
                            pantalla_final_perdido = True
                            flag_run_nivel_dos = False
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
        pantalla_final_perdido = True

    for enemigo_ in enemigos:
        enemigo_.update(ventana_ppal)

######################################################
        enemigo_.disparar(ventana_ppal, frida)
######################################################

    for bloque_ in bloques:
        bloque_.actualizar_pantalla(ventana_ppal)

    if len(enemigos) == 0:
        
        random.shuffle(lista_recompensas)

        for recompensa in lista_recompensas:
            recompensa.actualizar(ventana_ppal)
            if colision.agarrar_recompensa(frida, recompensa):
                lista_recompensas.remove(recompensa)
                audio_random = random.choice(lista_sonidos_score)
                audio_random.play()

        if len(lista_recompensas) == 0:
            score_final.play()
            flag_run_nivel_dos = False
            frida.scoring += int(segundos)

        if sonido_risa_fin_nivel_reproducido == False:
            sonido_una_risa.play()
            danzon.stop()
            musica_recompensas.play()
            sonido_risa_fin_nivel_reproducido = True

    frida.disparar(lista_teclas, enemigos, ventana_ppal)

    pygame.display.flip()

    pygame.time.delay(7)

danzon.stop()
musica_recompensas.stop()


##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 #####
##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 #####
##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 ##### ##### NIVEL 3 #####

frida.rect_frida.y = ALTO_VENTANA-ALTO_BRUJA
frida.rect_frida.x = ANCHO_VENTANA/2
frida.vidas = 5
sonido_risa_fin_nivel_reproducido = False
flag_sonido_final = True
recompensa_flag = True
flag_cargar_usuario = False
lista_recompensas = [gatito, gatito_dos, pocion, escoba, barita_magica]

enemigos = [enemigo, enemigo_dos, enemigo_tres, enemigo_cuatro, enemigo_cinco]
for enemigo_ in enemigos:
    enemigo_.muerto = False
    enemigo_.vidas = 3

musica_enemigo_final_flag = True

flag_sonido_final = True
segundos = "30"
fin_tiempo = False
flag_sonido = False
pygame.display.set_caption("Frida - Nivel 3")
flag_nivel_tres = True
flag_segundos_enemigo_final = False

if pantalla_final_perdido:
    flag_nivel_tres = False
else:
    flag_nivel_tres = True

while flag_nivel_tres:

    if flag_sonido == False:
        sonido_nivel_dos.play()
        flag_sonido = True

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_nivel_tres = False
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
                        sonido_fondo.stop()
                        if len(enemigos) == 0:
                            lista_recompensas = []
                        else:
                            flag_nivel_tres = False

    lista_teclas = pygame.key.get_pressed()
    frida.presionar_tecla(lista_teclas, bloques)

    fondo_nivel_tres = pygame.transform.scale(fondo_nivel_tres, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo_nivel_tres, (0, 0))

    mostrar_vidas_y_tiempo(fuente, segundos, frida, ventana_ppal, nombre_usuario)

    colisionar = colision.colisionar(frida, enemigos)

    if enemigo_final:
        colision_enemigo_final = colision.colisionar_con_enemigo_final(frida, enemigo_final)

        if flag_segundos_enemigo_final == False:
            segundos = "40"
            flag_segundos_enemigo_final = True

        if enemigo_final.muerto:
            flag_nivel_tres = False

    if not frida.muerta:
        if not colision_enemigo_final and not colisionar:
            frida.actualizar_pantalla(ventana_ppal)
        else:
            frida.restar_vida()
    else:
        flag_nivel_tres = False

    for enemigo_ in enemigos:
        enemigo_.update(ventana_ppal)

######################################################
        enemigo_.disparar(ventana_ppal, frida)
######################################################

    for bloque_ in bloques:
        bloque_.actualizar_pantalla(ventana_ppal)


    if len(enemigos) == 0:

        if recompensa_flag:
            sonido_nivel_dos.stop()
            sonido_una_risa.play()
            musica_recompensas.play()
            recompensa_flag = False

        random.shuffle(lista_recompensas)

        for recompensa in lista_recompensas:
            recompensa.actualizar(ventana_ppal)
            if colision.agarrar_recompensa(frida, recompensa):
                lista_recompensas.remove(recompensa)
                audio_random = random.choice(lista_sonidos_score)
                audio_random.play()

        if len(lista_recompensas) == 0:

###################################################################################################################

            bloques = []

            if tiempo_inicio_if == None:
                tiempo_inicio_if = pygame.time.get_ticks()

            if enemigo_final_en_accion == False:
                enemigo_final.rect_enemigo_final.y = ALTO_VENTANA - 500
                frida.volar = True
                enemigo_final_en_accion = True
                frida.scoring += int(segundos)

            enemigo_final.update(ventana_ppal)
            enemigo_final.disparar(ventana_ppal, frida)
            sonido_nivel_dos.stop()
            mostrar_vidas_fantasma(fuente,ventana_ppal, enemigo_final)

            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido = tiempo_actual - tiempo_inicio_if

            if tiempo_transcurrido > 10000:
                enemigo_final.velocidad = 6

            if tiempo_transcurrido > 20000:
                enemigo_final.velocidad = 8

##################################################################################################################

            if flag_sonido_final:
                musica_recompensas.stop()
                score_final.play()
                risa_fantasma.play()
                # musica_enemigo_final.play()
                flag_sonido_final = False

            if tiempo_transcurrido > 3000:
                if musica_enemigo_final_flag:
                    musica_enemigo_final.play()
                    musica_enemigo_final_flag = False


        if sonido_risa_fin_nivel_reproducido == False:
            sonido_una_risa.play()
            sonido_risa_fin_nivel_reproducido = True

    frida.disparar(lista_teclas, enemigos, ventana_ppal, enemigo_final)

    pygame.display.flip()

    pygame.time.delay(7)

sonido_nivel_dos.stop()
musica_enemigo_final.stop()

if enemigo_final.muerto:
    musica_fin_ganado.play()
    sonido_una_risa.play()
else:
    musica_fin.play()
    # risa_fantasma.play()

flag_final = True
while flag_final:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_final = False

    fondo_fin = pygame.transform.scale(fondo_fin, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo_fin, (0, 0))

    if enemigo_final.muerto:
        mensaje = "GANASTE!"
        mensaje_dos = ''
    else:
        mensaje = "ADIOS!"
        mensaje_dos = 'INTENTALO DE NUEVO'

    texto_superficie, texto_rect = fuente.render(mensaje, constantes.NEGRO)
    texto_superficie_dos, texto_rect_dos = fuente.render(mensaje_dos, constantes.NEGRO)

    texto_superficie_scorings, texto_rect = fuente.render('Mejores puntajes', constantes.NEGRO)
    ventana_ppal.blit(texto_superficie_scorings, (500, 400))

    posicion_vertical = 500
    if flag_cargar_usuario == False:
        crear_y_cargar_datos(nombre_usuario, frida.scoring)
        flag_cargar_usuario = True
    lista_datos = consultar_datos()

    for usuario in lista_datos:
        mensaje = f"* {usuario['nombre']} - {usuario['score']} puntos"
        texto_superficie_usuario, texto_rect = fuente.render(mensaje, constantes.NEGRO)
        ventana_ppal.blit(texto_superficie_usuario, (500, posicion_vertical))
        posicion_vertical += texto_rect.height + 5

    ventana_ppal.blit(texto_superficie, (500, 200))
    ventana_ppal.blit(texto_superficie_dos, (500, 300))

    pygame.display.flip()

pygame.quit()