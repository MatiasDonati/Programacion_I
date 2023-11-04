import pygame
import constantes
import personaje
import bloque

ANCHO_VENTANA = constantes.ANCHO_VENTANA
ALTO_VENTANA = constantes.ALTO_VENTANA
ALTO_BRUJA = constantes.ALTO_BRUJA
ANCHO_BRUJA = constantes.ANCHO_BRUJA
COLOR_FONDO = constantes.GRIS
ancho_bloque = ANCHO_VENTANA /4
alto_bloque = ALTO_VENTANA / 10

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

#Bloques
bloque_uno = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - alto_bloque, ancho_bloque, alto_bloque)
bloque_dos = bloque.Bloque(ANCHO_VENTANA - ancho_bloque - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - alto_bloque, ancho_bloque, alto_bloque)
bloque_tres = bloque.Bloque(ANCHO_VENTANA /3 ,(ALTO_VENTANA - ALTO_BRUJA * 2) - alto_bloque, ancho_bloque, alto_bloque)


print(ALTO_BRUJA)
print(ALTO_VENTANA - ALTO_BRUJA)


#Velocidades
velocidad_base = 2
velocidad_shift = 6

#Salto
isJump = False
jumpCount = 10

sobre_bloque = False

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

        if not sobre_bloque:
            personaje.update(player, 0 , -6 , "abajo")
       
        if lista_teclas[pygame.K_SPACE]:
            isJump = True
            print(f"Posicion bruja ANTES salto: {player['rect_bruja'].y}")
    else:

        if jumpCount >= -10:
            velocidad = -(jumpCount * abs(jumpCount)) * 0.4  # Cambia el signo de la velocidad vertical
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
        personaje.update(player, 0, - velocidad, "arriba")
   
        if player["rect_bruja"].colliderect(bloque_uno.rect_bloque) or player["rect_bruja"].colliderect(bloque_dos.rect_bloque):
            velocidad -= 10
            jumpCount = 10
            isJump = False
            sobre_bloque = True
            player['rect_bruja'].y = (bloque_uno.rect_bloque.y - ALTO_BRUJA ) + 20


    # ACA HAY ALGO CERCANO A LO QUE QUIEROP HACER !!
    # ACA HAY ALGO CERCANO A LO QUE QUIEROP HACER !!
    if player["rect_bruja"].colliderect(bloque_uno.rect_bloque) == False and player["rect_bruja"].colliderect(bloque_dos.rect_bloque) == False:
          sobre_bloque = False
    else:
        sobre_bloque = True
       
    # if player["rect_bruja"].colliderect(bloque_dos.rect_bloque) == False:
    #       sobre_bloque = False
    # else:
    #     sobre_bloque = True
        # if not player["rect_bruja"].colliderect(bloque_uno.rect_bloque) and not player["rect_bruja"].colliderect(bloque_dos.rect_bloque):
        #         sobre_bloque = False

       


    #VOLCAR CAMBIOS
    ventana_ppal.fill(COLOR_FONDO)

    fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
    ventana_ppal.blit(fondo, (0, 0))

    personaje.actualizar_pantalla(player,ventana_ppal)

    bloque_uno.actualizar_pantalla(ventana_ppal)
    bloque_dos.actualizar_pantalla(ventana_ppal)
    bloque_tres.actualizar_pantalla(ventana_ppal)

    pygame.display.flip()
pygame.quit()