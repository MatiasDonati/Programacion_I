import pygame
import constantes
from constantes import *
import bloque
from personaje import *
from enemigo import *
from enemigo_final import *
from configuraciones import *
from base_datos import *
import colision
import recompensas
from disparo import *
from textos import *
import obtener_nombre
import re
import random
import sonidos
import json
from elementos import *
from fondos_niveles import *
from json_lectura import *
import mostrar_botones_inicio

import gestor_de_fuentes

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.mixer.init()

#Fuente del Texto
# pygame.freetype.init()
# fuente = pygame.freetype.Font(None, 36)
import pygame.font

ruta_gotica = './fuente/VinaSans-Regular.ttf'

try:
    fuente = pygame.font.Font(ruta_gotica, 36)
except pygame.error:
    print(f"Error al cargar la fuente desde {ruta_gotica}. Verifica la ruta del archivo de fuente.")
    fuente = pygame.font.Font(None, 36)

# fuente = gestor_de_fuentes.cargar_fuente('./fuente/VinaSans-Regular/ttf', 38)

#timer segundos en juego
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,1000)

leer_json()

pygame.display.set_caption("Frida")

"""
# PANTALLA INICIO # PANTALLA INICIO # PANTALLA INICIO # PANTALLA INICIO # PANTALLA INICIO # PANTALLA INICIO
# PANTALLA INICIO # PANTALLA INICIO # PANTALLA INICIO # PANTALLA INICIO # PANTALLA INICIO # PANTALLA INICIO
"""

sonidos.sonido_risa.play()
intro = True
while intro:

    mostrar_botones_inicio.mostrar_botones_inicio(ventana_ppal, fondo_intro, fuente)

    nombre_usuario, ingreso_enter = obtener_nombre.obtener_nombre_usuario(ventana_ppal, fondo_intro, fuente)

    print('Hola')

    if ingreso_enter and patron_usuario.match(nombre_usuario):
        intro = False

sonidos.sonido_risa.stop()

"""
# NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO
# NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO # NVEL UNO
"""

pygame.display.set_caption("Frida - Nivel 1")
se_rio = False
flag_run = True
while flag_run:

    if flag_sonido == False:
        sonidos.sonido_fondo.play()
        flag_sonido = True

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    if int(segundos) <= 5:
                        volumen = volumen - 0.1
                        sonidos.sonido_fondo.set_volume(volumen)
                    if int(segundos) == 0:
                        fin_tiempo = True
                        # segundos = 'Tiempo Terminado'
                        sonidos.sonido_fondo.stop()
                        if len(enemigos) == 0:
                            flag_run = False
                            if se_rio == False:
                                sonidos.score_final.play()
                                se_rio = True
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
                audio_random = random.choice(sonidos.lista_sonidos_score)
                audio_random.play()

        if len(lista_recompensas) == 0:
            sonidos.score_final.play()
            flag_run = False
            frida.scoring += int(segundos)

        if sonido_risa_fin_nivel_reproducido == False:
            sonidos.sonido_una_risa.play()
            sonidos.musica_recompensas.play()
            sonidos.sonido_fondo.stop()
            sonido_risa_fin_nivel_reproducido = True

            """
            flag_run = False
            """

    frida.disparar(lista_teclas, enemigos, ventana_ppal, enemigo_final)

    pygame.display.flip()

    pygame.time.delay(7)

sonidos.sonido_fondo.stop()
sonidos.musica_recompensas.stop()

"""
# NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS
# NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS # NVEL DOS
"""

if pantalla_final_perdido:
    flag_run_nivel_dos = False
else:
    flag_run_nivel_dos = True
    segundos = "30"
    fin_tiempo = False
    flag_sonido = False
    frida.rect_frida.y = ALTO_VENTANA-ALTO_BRUJA
    frida.rect_frida.x = ANCHO_VENTANA/2
    se_rio = False
    sonido_risa_fin_nivel_reproducido = False
    lista_recompensas = [gatito, gatito_dos, pocion, escoba, barita_magica]
    enemigos = [enemigo, enemigo_dos, enemigo_tres]
    for enemigo_ in enemigos:
        enemigo_.muerto = False
        enemigo_.vidas = 3

pygame.display.set_caption("Frida - Nivel 2")

while flag_run_nivel_dos:

    if flag_sonido == False:
        sonidos.danzon.play()
        flag_sonido = True

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    if int(segundos) <= 5:
                        volumen = volumen - 0.1
                        sonidos.sonido_fondo.set_volume(volumen)
                    if int(segundos) == 0:
                        fin_tiempo = True
                        sonidos.sonido_fondo.stop()
                        if len(enemigos) == 0:
                            # flag_run = False
                            flag_run_nivel_dos = False
                            if se_rio == False:
                                sonidos.score_final.play()
                                se_rio = True
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
        enemigo_.disparar(ventana_ppal, frida)

    for bloque_ in bloques:
        bloque_.actualizar_pantalla(ventana_ppal)

    if len(enemigos) == 0:

        random.shuffle(lista_recompensas)

        for recompensa in lista_recompensas:
            recompensa.actualizar(ventana_ppal)
            if colision.agarrar_recompensa(frida, recompensa):
                lista_recompensas.remove(recompensa)
                audio_random = random.choice(sonidos.lista_sonidos_score)
                audio_random.play()

        if len(lista_recompensas) == 0:
            sonidos.score_final.play()
            flag_run_nivel_dos = False
            frida.scoring += int(segundos)

        if sonido_risa_fin_nivel_reproducido == False:
            sonidos.sonido_una_risa.play()
            sonidos.danzon.stop()
            sonidos.musica_recompensas.play()
            sonido_risa_fin_nivel_reproducido = True

    frida.disparar(lista_teclas, enemigos, ventana_ppal)

    pygame.display.flip()

    pygame.time.delay(7)

sonidos.danzon.stop()
sonidos.musica_recompensas.stop()

"""
# NVEL TRES # NVEL TRES # NVEL TRES # NVEL TRES # NVEL TRES # NVEL TRES
# NVEL TRES # NVEL TRES # NVEL TRES # NVEL TRES # NVEL TRES # NVEL TRES
"""

if pantalla_final_perdido:
    flag_nivel_tres = False
else:
    pygame.display.set_caption("Frida - Nivel 3")
    flag_nivel_tres = True
    flag_segundos_enemigo_final = False
    musica_enemigo_final_flag = True
    flag_sonido_final = True
    segundos = "30"
    fin_tiempo = False
    flag_sonido = False
    frida.rect_frida.y = ALTO_VENTANA-ALTO_BRUJA
    frida.rect_frida.x = ANCHO_VENTANA/2
    frida.vidas = 5
    sonido_risa_fin_nivel_reproducido = False
    flag_sonido_final = True
    recompensa_flag = True
    lista_recompensas = [gatito, gatito_dos, pocion, escoba, barita_magica]
    enemigos = [enemigo, enemigo_dos, enemigo_tres, enemigo_cuatro, enemigo_cinco]
    for enemigo_ in enemigos:
        enemigo_.muerto = False
        enemigo_.vidas = 3

while flag_nivel_tres:

    if flag_sonido == False:
        sonidos.sonido_nivel_dos.play()
        flag_sonido = True

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                if fin_tiempo == False:
                    segundos = int(segundos) - 1
                    if int(segundos) <= 5:
                        volumen = volumen - 0.1
                        sonidos.sonido_fondo.set_volume(volumen)
                    if int(segundos) == 0:
                        fin_tiempo = True
                        sonidos.sonido_fondo.stop()
                        if len(enemigos) == 0:
                            lista_recompensas = []
                        else:
                            flag_nivel_tres = False
                        if enemigo_final:
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
            sonidos.sonido_nivel_dos.stop()
            sonidos.sonido_una_risa.play()
            sonidos.musica_recompensas.play()
            recompensa_flag = False

        random.shuffle(lista_recompensas)

        for recompensa in lista_recompensas:
            recompensa.actualizar(ventana_ppal)
            if colision.agarrar_recompensa(frida, recompensa):
                lista_recompensas.remove(recompensa)
                audio_random = random.choice(sonidos.lista_sonidos_score)
                audio_random.play()

        if len(lista_recompensas) == 0:

            bloques = []

            if tiempo_inicio_if == None:
                tiempo_inicio_if = pygame.time.get_ticks()

            if enemigo_final_en_accion == False:
                enemigo_final.rect_enemigo_final.y = ALTO_VENTANA - 500
                frida.volar = True
                enemigo_final_en_accion = True
                frida.scoring += int(segundos)
                segundos = '40'

            enemigo_final.update(ventana_ppal)
            enemigo_final.disparar(ventana_ppal, frida)
            sonidos.sonido_nivel_dos.stop()
            mostrar_vidas_fantasma(fuente,ventana_ppal, enemigo_final)

            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido = tiempo_actual - tiempo_inicio_if

            if tiempo_transcurrido > 10000:
                enemigo_final.velocidad = 6

            if tiempo_transcurrido > 20000:
                enemigo_final.velocidad = 8

            if flag_sonido_final:
                sonidos.musica_recompensas.stop()
                sonidos.score_final.play()
                sonidos.risa_fantasma.play()
                flag_sonido_final = False

            if tiempo_transcurrido > 3000:
                if musica_enemigo_final_flag:
                    sonidos.musica_enemigo_final.play()
                    musica_enemigo_final_flag = False


        if sonido_risa_fin_nivel_reproducido == False:
            sonidos.sonido_una_risa.play()
            sonido_risa_fin_nivel_reproducido = True

    frida.disparar(lista_teclas, enemigos, ventana_ppal, enemigo_final)

    pygame.display.flip()

    pygame.time.delay(7)

sonidos.sonido_nivel_dos.stop()
sonidos.musica_enemigo_final.stop()

if enemigo_final.muerto:
    sonidos.musica_fin_ganado.play()
    sonidos.sonido_una_risa.play()
else:
    sonidos.musica_fin.play()
    # sonidos.risa_fantasma.play()

"""
# PANTALLA FINAL # PANTALLA FINAL # PANTALLA FINAL # PANTALLA FINAL # PANTALLA FINAL # PANTALLA FINAL
# PANTALLA FINAL # PANTALLA FINAL # PANTALLA FINAL # PANTALLA FINAL # PANTALLA FINAL # PANTALLA FINAL
"""
##################################################################
########### ESTO AL JSON ############################################

######################todo lo que es de inicializacion ##############
 ###     PROBABLEMENTE FLAGS DE JUEGOS HAY Q VOLVER A TRUE ##################
##################################################################
y_incremento = 0

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
        mensaje = "No te des por vencido aun vencido!"
        mensaje_dos = 'INTENTALO DE NUEVO'

    if int(segundos) == 0:
        mensaje = "TE QUEDASTE SIN TIEMPO!"

    texto_superficie= fuente.render(mensaje, True, constantes.NEGRO)
    texto_rect = texto_superficie.get_rect()

    texto_superficie_dos = fuente.render(mensaje_dos,True, constantes.NEGRO)
    texto_rect_dos = texto_superficie_dos.get_rect()

    texto_superficie_scorings = fuente.render('Mejores puntajes',True, constantes.NEGRO)
    texto_rect_scorings = texto_superficie_scorings.get_rect()

    ventana_ppal.blit(texto_superficie_scorings, (ANCHO_VENTANA // 2 - texto_rect_scorings.width // 2, 400 - y_incremento))

    if flag_cargar_usuario == False:
        crear_y_cargar_datos(nombre_usuario, frida.scoring)
        flag_cargar_usuario = True
    lista_datos = consultar_datos()

    posicion_vertical_usuario = 500

    for usuario in lista_datos:
        mensaje_usuario = f"* {usuario['nombre']} - {usuario['score']} puntos"
        texto_superficie_usuario = fuente.render(mensaje_usuario,True, constantes.NEGRO)
        texto_rect_usuario = texto_superficie_usuario.get_rect()



        ventana_ppal.blit(texto_superficie_usuario, (ANCHO_VENTANA // 2 - texto_rect_usuario.width // 2, posicion_vertical_usuario - y_incremento))
        posicion_vertical_usuario += texto_rect_usuario.height + 5

    if frida.muerta == False:
        y_incremento += 1
        with open('texto_final.txt', 'r') as archivo:
            posicion_vertical_db = ALTO_VENTANA + 50  # Empieza por debajo de la pantalla
            for linea in archivo:
                mensaje_db = linea.strip()
                texto_superficie_db = fuente.render(mensaje_db, True, constantes.NEGRO)
                texto_rect_db = texto_superficie_db.get_rect()

                # Calcula la posición x para centrar el texto
                posicion_x_db = (ANCHO_VENTANA - texto_rect_db.width) // 2

                ventana_ppal.blit(texto_superficie_db, (posicion_x_db, posicion_vertical_db - y_incremento))
                posicion_vertical_db += texto_rect_db.height + 5

    ventana_ppal.blit(texto_superficie, (ANCHO_VENTANA // 2 - texto_rect.width // 2, 200 - y_incremento))
    ventana_ppal.blit(texto_superficie_dos, (ANCHO_VENTANA // 2 - texto_rect_dos.width // 2, 300 - y_incremento))

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
