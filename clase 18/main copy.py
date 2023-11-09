import pygame
import sys
import random
from config import *
from nave import Nave
from asteroide import Asteroide

def generate_asteroids(g_sprites, g_aster, screen: pygame.Surface, count: int = 10):
    if len(g_aster) == 0:
        for i in range(count):
            x = random.randrange(16, screen.get_width() - 16)
            y = random.randrange(-1000, screen.get_height() // 2)
            # y = random.randrange(-500, screen.get_height() // 2)
            asteroide = Asteroide("./images/asteroid.png", SIZE_ASTEROID, (x, y), SPEED_ASTEROID_2)
            g_aster.add(asteroide)
            g_sprites.add(asteroide)

pygame.init()

reloj = pygame.time.Clock()

sonido = pygame.mixer.Sound("./sounds/laser.mp3")

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((0, 255, 0))
fondo = pygame.image.load("./images/espacio.png").convert()
fondo = pygame.transform.scale(fondo, SCREEN_SIZE)

sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
lasers = pygame.sprite.Group()

nave = Nave("./images/nave.png", SIZE_SHIP, START_POS, sonido)
# nave.add(sprites)
sprites.add(nave)

while True:

    reloj.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                nave.speed_x = -SPEED_SHIP
            if event.key == pygame.K_RIGHT:
                nave.speed_x = SPEED_SHIP
            if event.key == pygame.K_UP:
                nave.speed_y = -SPEED_SHIP
            if event.key == pygame.K_DOWN:
                nave.speed_y = SPEED_SHIP

            if event.key == pygame.K_SPACE:
                nave.shot(sprites, lasers)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and nave.speed_x < 0:
                nave.speed_x = 0
            if event.key == pygame.K_RIGHT and nave.speed_x > 0:
                nave.speed_x = 0
            if event.key == pygame.K_UP and nave.speed_y < 0:
                nave.speed_y = 0
            if event.key == pygame.K_DOWN and nave.speed_y > 0:
                nave.speed_y = 0
            # if event.key == pygame.K_SPACE:
                

    if nave.rect.left <= 0:
        nave.rect.left = 0
    elif nave.rect.right >= WIDTH:    
    # elif nave.rect.right >= screen.get_width:
        nave.rect.right = WIDTH
    if nave.rect.top <= 0:
        nave.rect.top = 0
    elif nave.rect.bottom >= HEIGHT:    
    # elif nave.rect.right >= screen.get_width:
        nave.rect.bottom = HEIGHT

    for asteroid in asteroids:
        if asteroid.rect.top >= HEIGHT:
            asteroid.kill()
        
    
    for laser in lasers:
        if laser.rect.bottom <= 0:
            laser.kill()
        else:
            lista = pygame.sprite.spritecollide(laser, asteroids, True)
            if len(lista) != 0:
                laser.kill()
    # lista = pygame.sprite.spritecollide(nave, asteroids, True)
    lista = pygame.sprite.spritecollide(nave, asteroids, False)
    if len(lista) != 0:
        nave.stop()
        # nave.kill()
        # for laser in lasers:
        #     laser.stop()
        for asteroid in asteroids:
            asteroid.stop()

    # pygame.sprite.spritecollide()


    generate_asteroids(sprites, asteroids, screen, MAX_ASTEROIDS)

    # nave.update()
    sprites.update()

    screen.blit(fondo, ORIGIN)

    # screen.blit(nave.image, nave.rect)
    sprites.draw(screen)

    pygame.display.flip()