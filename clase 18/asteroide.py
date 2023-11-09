import pygame

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, path_imagen: str, size: tuple, center: tuple, speed: int = 10):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        # self.speed_x = 0
        # self.speed_y = 0
        self.speed = speed
        # self.aceleracion = 1.2

    def update(self):
        # self.rect.x += self.speed_x
        # self.rect.y += self.speed_y
        # self.aceleracion += 0.1                
        # self.rect.y += self.speed * self.aceleracion
        self.rect.y += self.speed

    def stop(self):
        self.speed = 0
        # self.playing = False

    # def random_position(self):