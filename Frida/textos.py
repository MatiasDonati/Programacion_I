import constantes
from constantes import ALTO_VENTANA

def mostrar_vidas_y_tiempo(fuente, segundos, frida, ventana_ppal, nombre_usuario):

    segundos_texto = fuente.render(str(segundos),True, constantes.GRIS)
    segundos_rect = segundos_texto.get_rect()

    ventana_ppal.blit(segundos_texto, (10, 10))

    texto_vidas = fuente.render(f'Vidas: {str(frida.vidas)}', True, constantes.GRIS)
    texto_rect = texto_vidas.get_rect()

    ventana_ppal.blit(texto_vidas, (constantes.ANCHO_VENTANA - texto_rect.width - texto_rect.width * 0.5, 10))

    nombre = fuente.render(f'{str(nombre_usuario)}',True, constantes.GRIS)
    nombre_rect = nombre.get_rect()

    scoring = fuente.render(f'Puntos: {frida.scoring}',True, constantes.GRIS)
    scoring_rect = scoring.get_rect()

    suma_rect = nombre_rect.width + scoring_rect.width + 5  # Ajusta el espacio entre "nombre" y "scoring"

    x_nombre = (constantes.ANCHO_VENTANA - suma_rect) // 2
    y_nombre = 10  # Ajusta la posición vertical según tus necesidades
    ventana_ppal.blit(nombre, (x_nombre, y_nombre))

    x_scoring = x_nombre + nombre_rect.width + 10  # Ajusta el espacio entre "nombre" y "scoring"
    y_scoring = y_nombre  # Mantiene la misma altura vertical
    ventana_ppal.blit(scoring, (x_scoring, y_scoring))


def mostrar_vidas_fantasma(fuente, ventana_ppal, enemigo_final):
    fantasma = fuente.render(f'Fantasma vidas: {str(enemigo_final.vidas)}',True, constantes.GRIS)
    fantasma_rect = fantasma.get_rect()

    x_fantasma = (constantes.ANCHO_VENTANA - fantasma_rect.width) // 2
    y_fantasma = 55
    ventana_ppal.blit(fantasma, (x_fantasma, y_fantasma))
