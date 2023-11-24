import constantes

def mostrar_vidas_y_tiempo(fuente, segundos, frida, ventana_ppal, nombre_usuario):

    segundos_texto, segundos_rect = fuente.render(str(segundos), constantes.GRIS)
    ventana_ppal.blit(segundos_texto, (10, 10))

    texto_vidas, texto_rect = fuente.render(f'Vidas: {str(frida.vidas)}', constantes.GRIS)
    ventana_ppal.blit(texto_vidas, (constantes.ANCHO_VENTANA - texto_rect.width - texto_rect.width * 0.5, 10))

    nombre, nombre_rect = fuente.render(f'Jugador: {str(nombre_usuario)}', constantes.GRIS)
    scoring, scoring_rect = fuente.render(f'Puntos: {frida.scoring}', constantes.GRIS)

    suma_rect = nombre_rect.width + scoring_rect.width + 5  # Ajusta el espacio entre "nombre" y "scoring"

    x_nombre = (constantes.ANCHO_VENTANA - suma_rect) // 2
    y_nombre = 10  # Ajusta la posición vertical según tus necesidades
    ventana_ppal.blit(nombre, (x_nombre, y_nombre))

    x_scoring = x_nombre + nombre_rect.width + 10  # Ajusta el espacio entre "nombre" y "scoring"
    y_scoring = y_nombre  # Mantiene la misma altura vertical
    ventana_ppal.blit(scoring, (x_scoring, y_scoring))
