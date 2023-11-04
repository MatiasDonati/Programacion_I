from configuraciones import *
from class_personaje import *
from pygame.locals import *

##############################INICIALIZACIONES##########################################

#############Pantalla##########
#ANCHO W - ALTO H
ANCHO,ALTO = 1200,800
FPS = 18 #para desacelerar la pantalla

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles

#Fondo
fondo = pygame.image.load("./fondo.jpg").convert() #Acelera el juego y hace que consuma menos recursos
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

#Personaje
diccionario_animaciones = {}
diccionario_animaciones['derecha'] = personaje_derecha
diccionario_animaciones['izquierda'] = personaje_izquierda
diccionario_animaciones['quieto'] = personaje_quieto
diccionario_animaciones['salta'] = personaje_salta

mario = Personaje(diccionario_animaciones,100, ALTO - ALTO * 1/7, (70, 60), 10, 'quieto')

piso = pygame.Rect(0, 745, ANCHO, 20)

mario.rectangulo.bottom = piso.top

bandera = True
while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            bandera = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        mario.que_hace = 'derecha'
    elif teclas[pygame.K_LEFT]:
        mario.que_hace = 'izquierda'
    elif teclas[pygame.K_UP]:
        mario.que_hace = 'salta'
    else:
        mario.que_hace = 'quieto'


    PANTALLA.blit(fondo, (0, 0))

    mario.actualizar(PANTALLA, piso)

    pygame.draw.rect(PANTALLA, "red", piso, 3)
    pygame.display.update()

pygame.quit()