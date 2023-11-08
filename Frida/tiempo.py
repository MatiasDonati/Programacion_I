# import pygame
# import constantes

# fuente = pygame.font.SysFont('Arial', 50)
# segundos = "12"
# fin_tiempo = False
# timer = pygame.USEREVENT + 0
# pygame.time.set_timer(timer,1000)
# #definir musica
# pygame.mixer.init()
# ruta_audio = './audio/DiagramadeVen.mp3'
# sonido_fondo = pygame.mixer.Sound(ruta_audio)
# volumen = 0.12
# sonido_fondo.set_volume(volumen)


# def restar_segundos(ventana_ppal, tipo_evento):

#     if tipo_evento == pygame.USEREVENT:
#         if tipo_evento == timer:
#             if fin_tiempo == False:
#                 segundos = int(segundos) - 1
#                 volumen = volumen - 0.01
#                 sonido_fondo.set_volume(volumen)
#                 if int(segundos) == 0:
#                     fin_tiempo = True
#                     segundos = 'Tiempo Terminado...'
#                     sonido_fondo.stop()



#     segundos_texto, segundos_rect = fuente.render(str(segundos), constantes.NEGRO)
#     ventana_ppal.blit(segundos_texto, (10, 10))