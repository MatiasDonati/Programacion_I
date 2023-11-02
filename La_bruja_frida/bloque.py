import pygame
import constantes

class Bloque:
    def __init__(self, x, y, ancho, alto):
        self.surface = pygame.image.load("./imgs/bloque.png")
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_bloque = pygame.Rect(x, y, ancho, alto)
        self.score = 0

    def actualizar_pantalla(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_bloque)
        # pygame.draw.rect(ventana_ppal, constantes.VERDE, self.rect_bloque)
