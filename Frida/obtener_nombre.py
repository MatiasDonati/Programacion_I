import pygame
import constantes
from botones_inicio import *


def obtener_nombre_usuario(ventana_ppal, fondo_intro):
    nombre = ""
    input_activo = True
    ingreso_enter = False

    pygame.freetype.init()
    fuente = pygame.freetype.Font(None, 36)

    boton = Boton(constantes.ANCHO_VENTANA // 2 - 100, 410, 200, 50, (74, 95, 96), (87, 67, 58), "Comenzar", accion=click_boton)
    boton_dos = Boton(constantes.ANCHO_VENTANA // 2 - 100, 470, 200, 50, (74, 95, 96), (87, 67, 58), "Jugabilidad", accion=click_boton)
    boton_tres = Boton(constantes.ANCHO_VENTANA // 2 - 100, 530, 200, 50, (74, 95, 96), (87, 67, 58), "Records", accion=click_boton)
    boton_cuatro = Boton(constantes.ANCHO_VENTANA // 2 - 100, 590, 200, 50, (74, 95, 96), (87, 67, 58), "Salir", accion=click_boton)

    lista_botones = [boton, boton_dos, boton_tres, boton_cuatro]

    evento = None

    while input_activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_activo = False
                    ingreso_enter = True
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Se clickeo en: {event.pos}")

            evento = event

        fondo_intro = pygame.transform.scale(fondo_intro, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
        ventana_ppal.blit(fondo_intro, (0, 0))

        # Renderizar texto con color (AGREGA constantes.NEGRO O EL COLOR QUE DESEES)
        texto_superficie, texto_rect = fuente.render("¡FRIDA!", constantes.NEGRO)
        texto_superficie_2, texto_rect_2 = fuente.render("Ingresa tu nombre y presiona Enter:", constantes.NEGRO)
        texto_superficie_3, texto_rect_3 = fuente.render(nombre, constantes.NEGRO)

        x_TEXTO_INTRO = constantes.ANCHO_VENTANA // 2 - texto_rect_2.width // 2
        y_TEXTO_INTRO = constantes.ALTO_VENTANA // 3 - texto_rect_2.height // 2

        ventana_ppal.blit(texto_superficie, (x_TEXTO_INTRO, y_TEXTO_INTRO))
        ventana_ppal.blit(texto_superficie_2, (x_TEXTO_INTRO, y_TEXTO_INTRO + 50))

        x_nombre = constantes.ANCHO_VENTANA // 2 - texto_rect_3.width // 2
        y_nombre = y_TEXTO_INTRO + 100

        ventana_ppal.blit(texto_superficie_3, (x_nombre, y_nombre))

        for boton_actual in lista_botones:
            boton_actual.actualizar(evento)
            boton_actual.dibujar(ventana_ppal)


        pygame.display.flip()

    return nombre, ingreso_enter

def click_boton():
    print("Se clickeo en en Boton.. =) ")