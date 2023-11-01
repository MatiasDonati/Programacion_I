import pygame
import colores
import personaje

ANCHO_VENTANA = 1200
ALTO_VENTANA = 800

pygame.init()

# TAMAO DE LA VENTANA
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

# TITULO DE LA VENTANA
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

# CREACIN DE ELEMENTOS
player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-150,150,150)

#Velocidades
velocidad_base = 2
velocidad_shift = 6

#LGICA DEL JUEGO
flag_run = True
while flag_run:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                #PASA EL TIEMPO
                pass

    lista_teclas = pygame.key.get_pressed()

    velocidad = velocidad_shift if lista_teclas[pygame.K_RSHIFT] else velocidad_base

    if lista_teclas[pygame.K_LEFT]:

        personaje.update(player,-velocidad, "left")

    if lista_teclas[pygame.K_RIGHT]:
        personaje.update(player,velocidad, "right")

    #VOLCAR CAMBIOS
    ventana_ppal.fill(colores.GRIS)
    personaje.actualizar_pantalla(player,ventana_ppal)

    pygame.display.flip()
pygame.quit()