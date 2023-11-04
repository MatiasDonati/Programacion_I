from configuraciones import *
from class_personaje import *
from pygame.locals import *

##############################INICIALIZACIONES##########################################
ANCHO,ALTO = 1200,800
FPS = 18 #para desacelerar la pantalla
pygame.display.set_caption("Frida")

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) # en pixeles

#Fondo
fondo = pygame.image.load("./imgs/fondos/nebulosa.jpg").convert() #Acelera el juego y hace que consuma menos recursos
fondo = pygame.transform.scale(fondo, (ANCHO,ALTO))

#Personaje
diccionario_animaciones = {}
diccionario_animaciones['derecha'] = personaje_derecha
diccionario_animaciones['izquierda'] = personaje_izquierda
diccionario_animaciones['quieto'] = personaje_quieto
diccionario_animaciones['salta'] = personaje_salta

bruja = Personaje(diccionario_animaciones,100, ALTO - ALTO * 1/7, (150, 120), 10, 'quieto')
piso = pygame.Rect(0, 745, ANCHO, 20)

bruja.rectangulo.bottom = piso.top

bandera = True
while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            bandera = False

    #Eventos de teclas
    teclas = pygame.key.get_pressed()
    bruja.presionar_tecla(teclas)


    PANTALLA.blit(fondo, (0, 0))

    bruja.actualizar(PANTALLA, piso)

    pygame.draw.rect(PANTALLA, "red", piso, 3)
    pygame.display.update()

pygame.quit()