import pygame
import constantes

def obtener_nombre_usuario(ventana_ppal, fondo_intro):
    nombre = ""
    input_activo = True
    ingreso_enter = False

    # Cargar fuente (esto debe hacerse dentro de la función)
    pygame.freetype.init()
    fuente = pygame.freetype.Font(None, 36)

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

        fondo_intro = pygame.transform.scale(fondo_intro, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
        ventana_ppal.blit(fondo_intro, (0, 0))

        # Renderizar texto con color (AGREGA constantes.NEGRO O EL COLOR QUE DESEES)
        texto_superficie, texto_rect = fuente.render("¡FRIDA!", constantes.NEGRO)
        texto_superficie_2, texto_rect = fuente.render("Ingresa tu nombre y presiona Enter:", constantes.NEGRO)
        texto_superficie_3, texto_rect = fuente.render(nombre, constantes.NEGRO)

        x_TEXTO_INTRO = constantes.ANCHO_VENTANA // 2 - texto_rect.width // 2
        y_TEXTO_INTRO = constantes.ALTO_VENTANA // 2 - texto_rect.height // 2

        ventana_ppal.blit(texto_superficie, (x_TEXTO_INTRO, y_TEXTO_INTRO))
        ventana_ppal.blit(texto_superficie_2, (x_TEXTO_INTRO, y_TEXTO_INTRO + 50))
        ventana_ppal.blit(texto_superficie_3, (x_TEXTO_INTRO, y_TEXTO_INTRO + 100))

        pygame.display.flip()

    return nombre, ingreso_enter
