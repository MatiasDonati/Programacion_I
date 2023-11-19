import pygame
import constantes

class Recompensa:
    def __init__(self, x, y, ancho, alto, recompensa):
        match recompensa:
            case 'gatito':
                ruta_img = './imgs/recompensas/gatito.png'
                puntaje = 100
            case 'gatito_dos':
                ruta_img = './imgs/recompensas/gatito_dos.png'
                puntaje = 200
            case 'escoba':
                ruta_img = './imgs/recompensas/escoba.png'
                puntaje = 500
            case 'barita':
                ruta_img = './imgs/recompensas/barita_magica.png'
                puntaje = 1000
            case 'pocion':
                ruta_img = './imgs/recompensas/pocion.png'
                puntaje = 2000

        self.nombre = recompensa
        self.puntuacion = puntaje
        self.surface = pygame.image.load(ruta_img)
        self.surface = pygame.transform.scale(self.surface, (ancho, alto))
        self.rect_recompensa = pygame.Rect(x, y, ancho, alto)
        self.puntaje = puntaje

    def actualizar(self, ventana_ppal):
        ventana_ppal.blit(self.surface, self.rect_recompensa)



