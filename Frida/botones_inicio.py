import pygame

def iniciar_juego():
    print('Iniciar Juego')

def salir():
    pygame.quit()

class Boton:
    def __init__(self, x, y, ancho, alto, color_normal, color_destacado, texto, accion=None):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color_normal = color_normal
        self.color_destacado = color_destacado
        self.texto = texto
        self.accion = accion
        self.hover = False
        self.pulsado = False

    def dibujar(self, superficie):
        color = self.color_destacado if self.hover else self.color_normal
        pygame.draw.rect(superficie, color, self.rect)

        fuente = pygame.font.Font(None, 36)
        texto_superficie = fuente.render(self.texto, True, (255, 255, 255))
        texto_rect = texto_superficie.get_rect()

        superficie.blit(texto_superficie, (self.rect.x + self.rect.width // 2 - texto_rect.width // 2,
                                           self.rect.y + self.rect.height // 2 - texto_rect.height // 2))

    def actualizar(self, evento):
        if evento.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(evento.pos)
        elif evento.type == pygame.MOUSEBUTTONDOWN and self.hover:
            if self.accion:
                self.accion()
                self.pulsado = True

