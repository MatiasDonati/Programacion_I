import pygame
import colores
import personaje
import cono
import aguila
import riccardo_fort
import riccardo_iorio

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

# tamaño ventana
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

#imagem fondo
#fondo = pygame.image.load('./imgs/playa.jpg')


# titulo ventana
pygame.display.set_caption("TITULO DEL JUEGUITO")

# timer
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer, 100)

#esconder mouse
#pygame.mouse.set_visible(False)

# creacion elementos
player = personaje.crear(ANCHO_VENTANA-700, ALTO_VENTANA-200, 200, 200)
obstaculo = cono.crear(ANCHO_VENTANA-300 , ALTO_VENTANA-150, 150, 150)
obstaculo_dos = aguila.crear(ANCHO_VENTANA/2 , ALTO_VENTANA-500, 150, 150)
obst_ricardo_fort = riccardo_fort.crear(ANCHO_VENTANA-100 , ALTO_VENTANA-750, 150, 150)
obst_ricardo_iorio = riccardo_iorio.crear(ANCHO_VENTANA-700 , ALTO_VENTANA-750, 150, 150)



#sonido colicion
sonido_colision = pygame.mixer.Sound('./sounds/colision.mp3')
sonido_colision_aguila = pygame.mixer.Sound('./sounds/aguila.mp3')
sonido_colision_iorio = pygame.mixer.Sound('./sounds/yo_tengo_pajaros.mp3')
sonido_colision_iorio_dos = pygame.mixer.Sound('./sounds/pr_pr_pr.mp3')
sonido_colision_fort = pygame.mixer.Sound('./sounds/saca_la_mano.mp3')
colisionando = True

# logica del juego
flar_run = True
while flar_run:
    lista_eventos = pygame.event.get()

    #colision
    if player["rect_avatar"].colliderect(obstaculo["rect_avatar"]):

        if colisionando:
            sonido_colision.play()
        colisionando = False
    else:
        colisionando = True

    if player["rect_avatar"].colliderect(obstaculo_dos["rect_avatar"]):

        if colisionando:
            sonido_colision_aguila.play()
        colisionando = False
    else:
        colisionando = True

    if player["rect_avatar"].colliderect(obst_ricardo_fort["rect_avatar"]):

        if colisionando:
            sonido_colision_fort.play()
        colisionando = False
    else:
        colisionando = True

    if player["rect_avatar"].colliderect(obst_ricardo_iorio["rect_avatar"]):

        if colisionando:
            sonido_colision_iorio.play()
        colisionando = False
    else:
        colisionando = True

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
    ventana_ppal.fill(colores.NEGRO)
    #fonde con imagen
    #fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    #ventana_ppal.blit(fondo, (0, 0))

    personaje.actualizar_pantalla(player, ventana_ppal)
    cono.actualizar_pantalla(obstaculo, ventana_ppal)
    aguila.actualizar_pantalla(obstaculo_dos, ventana_ppal)
    riccardo_iorio.actualizar_pantalla(obst_ricardo_iorio, ventana_ppal)
    riccardo_fort.actualizar_pantalla(obst_ricardo_fort, ventana_ppal)

    # otros elementos

    pygame.display.flip()
pygame.quit()
