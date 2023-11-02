import pygame
import constantes
import personaje

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ALTO_BRUJA = constantes.ALTO_BRUJA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
COLOR_FONDO = constantes.GRIS

pygame.init()

# TAMAO DE LA VENTANA
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

# TITULO DE LA VENTANA
pygame.display.set_caption("La Bruja Frida")

#imagen fondo
fondo = pygame.image.load('./imgs/nebulosa.jpg')

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

# CREACIN DE ELEMENTOS
player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)

#Velocidades
velocidad_base = 2
velocidad_shift = 6

#Salto
isJump = False
jumpCount = 10

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

    velocidad = velocidad_shift if lista_teclas[pygame.K_LSHIFT] else velocidad_base

    if lista_teclas[pygame.K_LEFT]:
        personaje.update(player, -velocidad, 0 , "izquierda")

    if lista_teclas[pygame.K_RIGHT]:
        personaje.update(player, velocidad , 0 , "derecha")

    if lista_teclas[pygame.K_UP]:
        personaje.update(player, 0 , velocidad , "arriba")

    if lista_teclas[pygame.K_DOWN]:
        personaje.update(player, 0 , -velocidad , "abajo")

    if not isJump:
        if lista_teclas[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            velocidad = -(jumpCount * abs(jumpCount)) * 0.5  # Cambia el signo de la velocidad vertical

            personaje.update(player, 0, -velocidad, "arriba")
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    #VOLCAR CAMBIOS
    ventana_ppal.fill(COLOR_FONDO)

    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo, (0, 0))

    personaje.actualizar_pantalla(player,ventana_ppal)

    pygame.display.flip()
pygame.quit()