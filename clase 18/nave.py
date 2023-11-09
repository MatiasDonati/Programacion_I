import pygame
from laser import Laser
from config import *

class Nave(pygame.sprite.Sprite):
    # def __init__(self, path_imagen: str, size: tuple, center: tuple, sound_laser: pygame.mixer.Sound):
    def __init__(self, path_imagen: str, size: tuple, center: tuple):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed_x = 0
        self.speed_y = 0
        self.sound_laser = pygame.mixer.Sound("./assets/sounds/laser.mp3")
        # self.sound_laser = sound_laser
        self.playing = True
        self.playing_volume = True
        # self.sonido = pygame.mixer.Sound("./sounds/laser.mp3")

    def update(self):
        if self.playing:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= WIDTH:    
            # elif self.rect.right >= screen.get_width:
                self.rect.right = WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            elif self.rect.bottom >= HEIGHT:    
            # elif self.rect.right >= screen.get_width:
                self.rect.bottom = HEIGHT

    def reset(self):
        self.rect.center = START_POS
        self.speed_x = 0
        self.speed_y = 0

    def shot(self, sprites, lasers):
    # def fire(self, sprites, lasers):
        if self.playing:
            laser = Laser(SIZE_LASER, self.rect.midtop, COLOR_LASER, SPEED_LASER)
            if self.playing_volume:
                self.sound_laser.play()
            
            sprites.add(laser)
            lasers.add(laser)

    def stop(self):
        self.playing = False

    def play(self):
        self.playing = True

    def stop_volume(self):
        self.playing_volume = False
        pygame.mixer.music.pause()
    #     self.sound_laser.stop()
    def play_volume(self):
        self.playing_volume = True
        pygame.mixer.music.play(-1)
    
