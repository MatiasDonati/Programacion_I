import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, size: tuple, midbottom: tuple, color: tuple = (255, 0, 0) ,speed: int = 10):
        super().__init__()

        self.image = pygame.surface.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom
        # self.speed_x = 0
        # self.speed_y = 0
        self.speed = speed

    def update(self):
        # self.rect.x += self.speed_x
        # self.rect.y += self.speed_y
        self.rect.y -= self.speed

    def stop(self):
        self.speed = 0
    # def random_position(self):