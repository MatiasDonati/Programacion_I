import pygame
import colores
import personaje
import cono

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

# tamaño ventana
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))


# titulo ventana
pygame.display.set_caption("TITULO DEL JUEGUITO")

# timer
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer, 100)

# creacion elementos
player = personaje.crear(ANCHO_VENTANA/2, ALTO_VENTANA-200, 200, 200)
obstaculo = cono.crear(ANCHO_VENTANA/2, ALTO_VENTANA-200, 200, 200)

# logica del juego
flar_run = True
while flar_run:
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flar_run = False

        # if evento.type == pygame.USEREVENT:
        #     if evento.type == timer:
        #         pass

    lista_teclas = pygame.key.get_pressed()

    velocidad_base = 2
    velocidad_shift = 6

    velocidad = velocidad_shift if lista_teclas[pygame.K_RSHIFT] else velocidad_base

    if lista_teclas[pygame.K_LEFT]:
        personaje.update(player, -velocidad, 0)
    if lista_teclas[pygame.K_RIGHT]:
        personaje.update(player, velocidad, 0)
    if lista_teclas[pygame.K_UP]:
        personaje.update(player, 0, -velocidad)
    if lista_teclas[pygame.K_DOWN]:
        personaje.update(player, 0, velocidad)

    # Volcar cambios
    ventana_ppal.fill(colores.BLANCO)
    personaje.actualizar_pantalla(player, ventana_ppal)
    cono.actualizar_pantalla(obstaculo, ventana_ppal)
    # otros elementos

    pygame.display.flip()
pygame.quit()
