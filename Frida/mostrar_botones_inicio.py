from botones_inicio import *
import pygame
import constantes
from base_datos import *

def mostrar_botones_inicio(ventana_ppal, fondo_intro, fuente):

    boton = Boton(-900, 410, 200, 50, (74, 95, 96), (87, 67, 58), "Comenzar", accion=iniciar_juego)
    boton_dos = Boton(-900, 470, 200, 50, (74, 95, 96), (87, 67, 58), "Jugabilidad", accion=None)
    boton_tres = Boton(-900, 530, 200, 50, (74, 95, 96), (87, 67, 58), "Records", accion=None)
    boton_cuatro = Boton(-900, 590, 200, 50, (74, 95, 96), (87, 67, 58), "Salir", accion=salir)

    boton_volver = Boton(constantes.ANCHO_VENTANA // 2 - 70, 590, 200, 50, (74, 95, 96), (87, 67, 58), "Volver", accion=None)

    lista_botones = [boton, boton_dos, boton_tres, boton_cuatro]

    fondo_intro = pygame.transform.scale(fondo_intro, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
    ventana_ppal.blit(fondo_intro, (0, 0))

    texto_superficie = fuente.render("¡FRIDA!",True, constantes.NEGRO)
    texto_rect = texto_superficie.get_rect()

    ventana_ppal.blit(texto_superficie, (constantes.ANCHO_VENTANA // 2 - texto_rect.width // 2, constantes.ALTO_VENTANA // 3))

    input_activo = True
    instrucciones = False
    records = False

    while input_activo:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Se clickeo en: {event.pos}")

                if boton_dos.rect.collidepoint(event.pos):
                    print('Clickeaste en el botón Jugabilidad')
                    instrucciones = True
                    # print(instrucciones)

                if boton_tres.rect.collidepoint(event.pos):
                    print('Clickeaste en el botón Ver Records')
                    records = True

            if instrucciones == False and records == False:

                texto_superficie = fuente.render("¡FRIDA!",True, constantes.NEGRO)
                texto_rect = texto_superficie.get_rect()

                fondo_intro = pygame.transform.scale(fondo_intro, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
                ventana_ppal.blit(fondo_intro, (0, 0))
                ventana_ppal.blit(texto_superficie, (constantes.ANCHO_VENTANA // 2 - texto_rect.width // 2, constantes.ALTO_VENTANA // 3))


                for boton_actual in lista_botones:
                    boton_actual.rect.x = constantes.ANCHO_VENTANA // 2 - 100
                    boton_actual.actualizar(event)
                    boton_actual.dibujar(ventana_ppal)

                    if boton_actual.pulsado and boton_actual.texto == 'Comenzar':
                        input_activo = False
                        iniciar_juego()
                    elif boton_actual.pulsado and boton_actual.texto == 'Salir':
                        salir()

            elif instrucciones:

                texto_superficie = fuente.render("¡FRIDA!",True, constantes.NEGRO)
                texto_rect = texto_superficie.get_rect()

                fondo_intro = pygame.transform.scale(fondo_intro, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
                ventana_ppal.blit(fondo_intro, (0, 0))
                comando = fuente.render("<-  Izquierda         ->  Derecha",True, constantes.NEGRO)
                comando_rect = comando.get_rect()

                comando_tres = fuente.render("Space - Saltar        R - Hechizo",True, constantes.NEGRO)
                comando_tres_rect = comando_tres.get_rect()

                comando_cinco = fuente.render("         Shift Left  - Turbo",True, constantes.NEGRO)
                comando_cinco_rect = comando_cinco.get_rect()



                ventana_ppal.blit(texto_superficie, (constantes.ANCHO_VENTANA // 2 - texto_rect.width // 2, constantes.ALTO_VENTANA // 4))

                ventana_ppal.blit(comando, (constantes.ANCHO_VENTANA // 2 - comando_rect.width // 2, constantes.ALTO_VENTANA // 2 - 100))
                ventana_ppal.blit(comando_tres, (constantes.ANCHO_VENTANA // 2 - comando_rect.width // 2, constantes.ALTO_VENTANA // 2 + 150 - 150))
                ventana_ppal.blit(comando_cinco, (constantes.ANCHO_VENTANA // 2 - comando_rect.width // 2, constantes.ALTO_VENTANA // 2 + 250 - 150))

                boton_volver.dibujar(ventana_ppal)
                boton_volver.actualizar(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"Se clickeo en: {event.pos}")
                    if boton_volver.rect.collidepoint(event.pos):
                        instrucciones = False
                        records = False

                pygame.display.flip()

            elif records:

                fondo_intro = pygame.transform.scale(fondo_intro, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
                ventana_ppal.blit(fondo_intro, (0, 0))

                texto_superficie_scorings = fuente.render('Mejores puntajes',True, constantes.NEGRO)
                texto_rect = texto_superficie_scorings.get_rect()

                ventana_ppal.blit(texto_superficie_scorings, (constantes.ANCHO_VENTANA // 2 - texto_rect.width // 2, 200))

                posicion_vertical = 300
                lista_datos = consultar_datos()

                if lista_datos:
                    for usuario in lista_datos:
                        mensaje = f"* {usuario['nombre']} - {usuario['score']} puntos"
                        texto_superficie_usuario = fuente.render(mensaje,True,  constantes.NEGRO)
                        texto_rect = texto_superficie_usuario.get_rect()
                        ventana_ppal.blit(texto_superficie_usuario, (constantes.ANCHO_VENTANA // 2 - texto_rect.width // 2, posicion_vertical))
                        posicion_vertical += texto_rect.height + 5


                boton_volver.dibujar(ventana_ppal)
                boton_volver.actualizar(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"Se clickeo en: {event.pos}")
                    if boton_volver.rect.collidepoint(event.pos):
                        instrucciones = False
                        records = False

                pygame.display.flip()


        pygame.display.flip()

    pygame.display.flip()
