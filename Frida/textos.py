import constantes

def mostrar_vidas_y_tiempo(fuente, segundos, frida,  ventana_ppal, nombre_usuario):

    segundos_texto, segundos_rect = fuente.render(str(segundos), constantes.GRIS)
    ventana_ppal.blit(segundos_texto, (10, 10))

    texto_vidas, texto_rect = fuente.render(f'Vidas: {str(frida.vidas)}', constantes.GRIS)
    ventana_ppal.blit(texto_vidas, (constantes.ANCHO_VENTANA - texto_rect.width - texto_rect.width * 0.5 , 10))

    nombre, nombre_rect = fuente.render(f'Jugador: {str(nombre_usuario)}', constantes.GRIS)
    ventana_ppal.blit(nombre, (constantes.ANCHO_VENTANA /2 , 10))