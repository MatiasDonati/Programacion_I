# import os
import sqlite3
# import threading
import time
import pygame
import sys
import random
from banana import Banana
from cherry import Cherry
from config import *
from nave import Nave
from asteroide import Asteroide
from pygame.locals import *
# from gui.GUI_form_principal import FormPrincipal


class Game:
    def __init__(self):
        pygame.init()

        self.reloj = pygame.time.Clock()
        # self.sonido = pygame.mixer.Sound("./sounds/laser.mp3")
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        # self.screen.fill((0, 255, 0))
        # self.fondo = pygame.image.load("./images/espacio.png").convert()
        # self.fondo = pygame.transform.scale(self.fondo, SCREEN_SIZE)
        self.fondo_1 = pygame.transform.scale(pygame.image.load("./assets/images/espacio.png").convert(), SCREEN_SIZE)
        self.fondo_2 = pygame.transform.scale(pygame.image.load("./assets/images/background.jpg").convert(), SCREEN_SIZE)
        self.fondo_3 = pygame.transform.scale(pygame.image.load("./assets/images/heaven.jpg").convert(), SCREEN_SIZE)
        self.sprites = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.cherries = pygame.sprite.Group()
        self.bananas= pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        # nave = Nave("./assets/images/nave.png", SIZE_SHIP, START_POS, self.sonido)
        self.nave = Nave("./assets/images/nave.png", SIZE_SHIP, START_POS)
        self.sprites.add(self.nave)
        self.is_playing = False
        self.is_game_over = False
        self.is_running = False
        self.font = pygame.font.Font("./assets/fonts/kablammo.ttf", 48)
        # self.playing_volume = True
        self.sonido_colision = pygame.mixer.Sound("./assets/sounds/ñam.mp3")
        self.score = 0
        self.text = ""
        self.tiempo = ""
        self.id = 0
        self.flag_1 = True
        self.flag_2 = True
        self.flag_3 = True
        self.live = 3
        self.vida = ""
        self.pause = ""
        self.resume = ""
        self.salir = ""
        self.music_pause = ""
        self.music_resume = ""

        # self.text_rect = ""

    def play(self):
        
        self.is_playing = True
        self.is_running = True
        self.is_game_over = False
        #MUSIQUITA
        pygame.mixer.music.load("./assets/sounds/Vengeance (Loopable).wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)
        while self.is_running:
        # while self.is_playing:
            self.reloj.tick(FPS)
            self.handler_events()
            self.update()
            self.render()

        self.show_start_screen()

    def handler_events(self: pygame.sprite.Group()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.stop_elements()
                    # for sprite in self.sprites:
                    #     sprite.stop()
                        # sprite.paused = True
                if event.key == pygame.K_r:
                    # self.restart_game()
                    self.play_elements()

                if event.key == pygame.K_e:
                    self.game_over()

                if event.key == pygame.K_m:
                    
                    self.nave.play_volume()
                    # self.playing_volume = True
                    # self.nave.sound_laser.play()
                    # self.sonido_colision.play()
                if event.key == pygame.K_p:
                    # self.nave.sound_laser.stop()
                    # self.sonido_colision.stop()
                    
                    self.nave.stop_volume()
                    # self.playing_volume = False
                    
                if event.key == pygame.K_LEFT:
                    self.nave.speed_x = -SPEED_SHIP
                if event.key == pygame.K_RIGHT:
                    self.nave.speed_x = SPEED_SHIP
                if event.key == pygame.K_UP:
                    self.nave.speed_y = -SPEED_SHIP
                if event.key == pygame.K_DOWN:
                    self.nave.speed_y = SPEED_SHIP

                if event.key == pygame.K_SPACE:
                    self.nave.shot(self.sprites, self.lasers)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.nave.speed_x < 0:
                    self.nave.speed_x = 0
                if event.key == pygame.K_RIGHT and self.nave.speed_x > 0:
                    self.nave.speed_x = 0
                if event.key == pygame.K_UP and self.nave.speed_y < 0:
                    self.nave.speed_y = 0
                if event.key == pygame.K_DOWN and self.nave.speed_y > 0:
                    self.nave.speed_y = 0
                # if event.key == pygame.K_SPACE:

    def update(self):

        self.kill_elements_out_screen()

        self.collide_detection()
        # for asteroid in self.asteroids:
        #     if asteroid.rect.top >= HEIGHT:
        #         asteroid.kill()
        
        # for laser in self.lasers:
        #     if laser.rect.bottom <= 0:
        #         laser.kill()
        #     else:
        #         lista = pygame.sprite.spritecollide(laser, self.asteroids, True)
        #         if len(lista) != 0:
        #             laser.kill()
        # lista = pygame.sprite.spritecollide(self.nave, self.asteroids, True)
        # lista = pygame.sprite.spritecollide(self.nave, self.asteroids, False)
        # if len(lista) != 0:

        #     self.stop_elements()
            # self.nave.stop()
            # self.nave.kill()
            # for laser in lasers:
            #     laser.stop()
            # for asteroid in self.asteroids:
            #     asteroid.stop()

            # for laser in self.lasers:
            #     laser.stop()

        # pygame.sprite.spritecollide()

        self.generate_asteroids()
        self.generate_cherries()
        self.generate_bananas()
        # self.generate_asteroids(self.sprites, self.asteroids, self.screen, MAX_ASTEROIDS)
        # self.nave.update()

        self.sprites.update()

    def show_lives_screen(self):
        self.vida = self.font.render("Lives: " + str(self.live), True, (255, 0, 255))
        
        self.screen.blit(self.vida, (30, 100))

    def show_pause_screen(self):
        self.pause = self.font.render("S: Stop ", True, (255, 0, 255))
        self.resume = self.font.render("R: Resume ", True, (255, 0, 255))
        self.music_pause = self.font.render("P: Music pause ", True, (255, 0, 255))
        self.music_resume = self.font.render("M: Music play", True, (255, 0, 255))
        self.salir = self.font.render("E: Exit ", True, (255, 0, 255))
        
        self.screen.blit(self.pause, (WIDTH-350, 50))
        self.screen.blit(self.resume, (WIDTH-350, 100))
        self.screen.blit(self.music_pause, (WIDTH-350, 150))
        self.screen.blit(self.music_resume, (WIDTH-350, 200))
        self.screen.blit(self.salir, (WIDTH-350, 250))

    def render(self):
        #juego / inicio / game_over

        if self.is_game_over:
            self.show_game_over_screen()
        elif self.is_playing:
            if not self.flag_1:
                self.screen.blit(self.fondo_1, ORIGIN)
            if not self.flag_2:
                self.screen.blit(self.fondo_2, ORIGIN)
            if not self.flag_3:
                self.screen.blit(self.fondo_3, ORIGIN)
            self.show_score_screen()
            self.show_lives_screen()
            self.show_pause_screen()
            # self.screen.blit(self.texto, (30, 30))
            # self.screen.blit(self.texto, self.texto_rect)
            # screen.blit(nave.image, nave.rect)
            self.sprites.draw(self.screen)
            # x = 0
            # self.show_cuenta_regresiva(x)
            # hilo_cuenta_regresiva = threading.Thread(target=self.show_cuenta_regresiva, args=(x,))
            # hilo_cuenta_regresiva.start()
            
            # self.show_cuenta_regresiva()
        else:
            self.show_start_screen()
        # if jugando:

        # elif inicio:
        
        # else:

        pygame.display.flip()

    def esperar(self):
        time.sleep(1)

    def show_cuenta_regresiva(self, x):
        # print(segundos)
        segundos = 60
        for i in range(segundos):
        # while segundos > 0:
            # os.system("cls")
            # print(segundos)
            # self.tiempo = self.font.render("Tiempo: " + str(segundos), True, (0, 255, 0))
            # self.screen.blit(self.tiempo, (30, 100))
            time.sleep(1)
            segundos -= 1
            
            
            
            
            # hilo_esperar = threading.Thread(target=self.esperar, args=(self,))
            # hilo_esperar.start()
            
            self.tiempo = None
        segundos = 60
        self.game_over()
        # pygame.display.flip()
            # self.tiempo = self.font.render("Tiempo: " + str(segundos), True, (0, 255, 0))
            # self.screen.blit(self.tiempo, (30, 100))
        #     time.sleep(1)
        #     segundos -= 1
        # print("¡Tiempo finalizado!")

    def generate_asteroids(self):    
    # def generate_asteroids(self, g_sprites, g_aster, screen: pygame.Surface, count: int = 10):
        if len(self.asteroids) == 0:
        # if len(g_aster) == 0:
            # for i in range(count):
            for i in range(MAX_ASTEROIDS):
                # x = random.randrange(16, screen.get_width() - 16)
                # y = random.randrange(-1000, screen.get_height() // 2)
                x = random.randrange(16, WIDTH - 16)
                y = random.randrange(-1000, HEIGHT // 2)
                # y = random.randrange(-500, screen.get_height() // 2)
                if not self.flag_1:
                    asteroide = Asteroide("./assets/images/asteroid.png", SIZE_ASTEROID, (x, y), SPEED_ASTEROID_1)
                if not self.flag_2:
                    asteroide = Asteroide("./assets/images/asteroid.png", SIZE_ASTEROID, (x, y), SPEED_ASTEROID_2)
                if not self.flag_3:
                    asteroide = Asteroide("./assets/images/asteroid.png", SIZE_ASTEROID, (x, y), SPEED_ASTEROID_3)
                self.asteroids.add(asteroide)
                # self.g_aster.add(asteroide)
                self.sprites.add(asteroide)
                # self.g_sprites.add(asteroide)

    def generate_cherries(self):    
    # def generate_asteroids(self, g_sprites, g_aster, screen: pygame.Surface, count: int = 10):
        if len(self.cherries) == 0:
        # if len(g_aster) == 0:
            # for i in range(count):
            for i in range(MAX_CHERRIES):
                # x = random.randrange(16, screen.get_width() - 16)
                # y = random.randrange(-1000, screen.get_height() // 2)
                x = random.randrange(16, WIDTH - 16)
                y = random.randrange(-1000, HEIGHT // 2)
                # y = random.randrange(-500, screen.get_height() // 2)
                if not self.flag_1:
                    cherry = Cherry("./assets/images/Cherries.png", SIZE_CHERRY, (x, y), SPEED_CHERRY_1)
                if not self.flag_2:
                    cherry = Cherry("./assets/images/Cherries.png", SIZE_CHERRY, (x, y), SPEED_CHERRY_2)
                if not self.flag_3:
                    cherry = Cherry("./assets/images/Cherries.png", SIZE_CHERRY, (x, y), SPEED_CHERRY_3)
                self.cherries.add(cherry)
                # self.g_aster.add(asteroide)
                self.sprites.add(cherry)
                # self.g_sprites.add(asteroide)   
                # 
    def generate_bananas(self):    
    # def generate_asteroids(self, g_sprites, g_aster, screen: pygame.Surface, count: int = 10):
        if len(self.bananas) == 0:
        # if len(g_aster) == 0:
            # for i in range(count):
            for i in range(MAX_BANANAS):
                # x = random.randrange(16, screen.get_width() - 16)
                # y = random.randrange(-1000, screen.get_height() // 2)
                x = random.randrange(16, WIDTH - 16)
                y = random.randrange(-1000, HEIGHT // 2)
                # y = random.randrange(-500, screen.get_height() // 2)
                if not self.flag_1:
                    banana = Banana("./assets/images/Bananas.png", SIZE_BANANA, (x, y), SPEED_BANANA_1)
                if not self.flag_2:
                    banana = Banana("./assets/images/Bananas.png", SIZE_BANANA, (x, y), SPEED_BANANA_2)
                if not self.flag_3:
                    banana = Banana("./assets/images/Bananas.png", SIZE_BANANA, (x, y), SPEED_BANANA_3)
                self.bananas.add(banana)
                # self.g_aster.add(asteroide)
                self.sprites.add(banana)
                # self.g_sprites.add(asteroide)    

    def play_elements(self):
        pygame.mixer.music.play(-1)
        self.nave.play()

        for banana in self.bananas:
                banana.kill()
        
        for cherry in self.cherries:
                cherry.kill()

        for asteroid in self.asteroids:
                asteroid.kill()

        for laser in self.lasers:
                laser.kill()


    def stop_elements(self):
        pygame.mixer.music.pause()
        self.nave.stop()
        # self.nave.kill()
        # for laser in lasers:
        #     laser.stop()

        for banana in self.bananas:
            banana.stop()

        for cherry in self.cherries:
            cherry.stop()

        for asteroid in self.asteroids:
            asteroid.stop()

        for laser in self.lasers:
            laser.stop()

        # for sprite in self.sprites:
        #     sprite.stop()
            

    
    def count_score(self):
        self.score += 1

    def show_score_screen(self):
        self.texto = self.font.render("Score: " + str(self.score), True, (255, 0, 255))
        # self.texto_rect = self.texto.get_rect()
        # self.texto_rect.center = CENTER
        # self.screen.blit(self.texto, self.texto_rect)
        self.screen.blit(self.texto, (30, 50))

    def store_score(self):
        with sqlite3.connect("mi_base_de_datos.db") as conexion:
            try:
                
                # sentencia = '''
                #             create table Score
                #             (
                #                 id integer primary key autoincrement,
                #                 score integer
                #             )
                #             '''
                sentencia = 'update Score set score = ? where id = ?'
                
                cursor = conexion.execute(sentencia,(self.score,self.id))
                # print("Dato insertado con exito")
            except Exception as e:
                print("Error")
    def serch_id(self):
        with sqlite3.connect("mi_base_de_datos.db") as conexion:
            try:
                
                sentencia = 'select id from Score'
                
                cursor = conexion.execute(sentencia)
                contador = 0
                for fila in cursor:
                    # print(fila)
                    contador += 1
                
                self.id = contador
                
                # print("Dato insertado con exito")
            except Exception as e:
                print("Error")

    def lose_live(self):
        self.live -= 1
        
    def gain_live(self):
        self.live += 1

    def collide_detection(self):
        # global texto, texto_rect
        for laser in self.lasers:
            lista = pygame.sprite.spritecollide(laser, self.asteroids, True)
            if len(lista) != 0:
                self.count_score()
                # self.serch_id()
                self.store_score()
                laser.kill()
        
        # for cherry in self.cherries:
        # lista_colision_cereza = pygame.sprite.spritecollide(self.nave, self.cherries, True)
        # lista_colision = pygame.sprite.spritecollide(self.nave, cherry, True)

        for cherry in self.cherries:
            lista_colision_cereza = pygame.sprite.spritecollide(self.nave, self.cherries, True)
            if len(lista_colision_cereza) != 0:
            # self.cherries.kill()
                if self.nave.playing_volume:
                    self.sonido_colision.play()
                self.count_score()
                self.store_score()
                cherry.kill()
                

        # if len(lista_colision_cereza) != 0:
        #     self.sonido_colision.play()
        #     self.count_score()
        #     self.store_score()
        #     for cherry in self.cherries:
            # self.cherries.kill()
                # cherry.kill()

        lista_colision_banana = pygame.sprite.spritecollide(self.nave, self.bananas, True)
        if len(lista_colision_banana) != 0:
            if self.nave.playing_volume:
                self.sonido_colision.play()
            self.gain_live()

        # self.show_score_screen()
        pygame.display.flip()
        # lista = pygame.sprite.spritecollide(self.nave, self.asteroids, True)
        lista = pygame.sprite.spritecollide(self.nave, self.asteroids, False)
         
        if len(lista) != 0:
            self.lose_live()
            for asteroid in self.asteroids:
            # if asteroid.rect.top >= HEIGHT:
                asteroid.kill()
            # self.asteroids.empty()
            # print(self.live)
            if self.live <= 0:
                self.game_over()
            # self.stop_elements()

    def kill_elements_out_screen(self):

        for asteroid in self.asteroids:
            if asteroid.rect.top >= HEIGHT:
                asteroid.kill()

        for cherry in self.cherries:
            if cherry.rect.top >= HEIGHT:
                cherry.kill()

        for banana in self.bananas:
            if banana.rect.top >= HEIGHT:
                banana.kill()
        
        for laser in self.lasers:
            if laser.rect.bottom <= 0:
                laser.kill()

    def game_over(self):
        pygame.mixer.music.pause()
        # self.stop_elements()
        self.is_playing = False
        self.is_game_over = True

    def exit(self):
        self.is_running = False

    def show_game_over_screen(self):
        fondo_game_over = pygame.surface.Surface(SCREEN_SIZE)
        fondo_game_over.fill(BLACK)
        texto = self.font.render("Game Over", True, (0, 255, 0))
        texto_rect = texto.get_rect()
        texto_rect.center = CENTER
        self.screen.blit(fondo_game_over, ORIGIN)
        self.screen.blit(texto, texto_rect)
        pygame.display.flip()
        pygame.time.delay(5000)
        # self.is_game_over = False
        # self.restart_game()
        self.is_running = False

    def create_id(self):
        with sqlite3.connect("mi_base_de_datos.db") as conexion:
            try:
                
                sentencia_1 = '''
                    insert into Score(score) values(0)
                    '''
                sentencia_2 = 'select * from Score order by score desc limit 3'
                cursor_1 = conexion.execute(sentencia_1)
                cursor_2 = conexion.execute(sentencia_2)
                global puntajes
                puntajes = []
                for fila in cursor_2:
                    # print(fila)
                    puntajes.append(fila)
                    # print(puntajes)

                # cursor = conexion.execute(sentencia,(self.score,))
                # print("Dato insertado con exito")
            except Exception as e:
                print("Error")

    def show_start_screen(self):
        # Obtener el tiempo de inicio en milisegundos
        # start_ticks = pygame.time.get_ticks()
        # Variable de duración de la cuenta regresiva en segundos
        # duracion_total = 60
        # W,H= 1900,900
        # TAMAÑO_PANTALLA = (W,H)
        self.create_id()
        self.serch_id()
        # PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
        # form_principal = FormPrincipal(PANTALLA, 500, 250, 900, 350, "Gold", "Magenta", 5, True)
        # flag = True
        # global flag_1, flag_2, flag_3
        self.flag_1 = True
        self.flag_2 = True
        self.flag_3 = True
        while self.flag_1 and self.flag_2 and self.flag_3:
            # segundos_transcurridos = (pygame.time.get_ticks() - start_ticks) / 1000

            # if segundos_transcurridos > duracion_total:
            #     break

            # Calcular el tiempo restante en segundos
            # segundos_restantes = duracion_total - int(segundos_transcurridos)

            # Verificar si la cuenta regresiva ha terminado
            # if segundos_restantes <= 0:
            #     break

            # Imprimir los segundos restantes
            # print(segundos_restantes)
        # while flag and flag_1 and flag_2 and flag_3:
            self.reloj.tick(FPS)
            # print(self.reloj.tick(FPS))
            eventos = pygame.event.get()
            for event in eventos:
                
                if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_s:
                    #     flag = False
                    #     print(flag)
                    if event.key == pygame.K_1:
                        self.flag_1 = False
                    if event.key == pygame.K_2:
                        self.flag_2 = False
                    if event.key == pygame.K_3:
                        self.flag_3 = False
                        # self.restart_game()

            # form_principal.update(eventos)

            fondo_game_over = pygame.surface.Surface(SCREEN_SIZE)
            fondo_game_over.fill(BLACK)
            
            texto_1 = self.font.render("Ranking top 3", True, (0, 255, 0))
            texto_2 = self.font.render("Id Jugador  Puntaje", True, (0, 255, 0))
            # texto_4 = self.font.render(str(puntajes), True, (0, 255, 0))
            texto_3 = self.font.render("Su Id Jugador: "+ str(self.id), True, (0, 255, 0))
            texto_4 = self.font.render("Presione 1, 2 o 3 para comenzar", True, (0, 255, 0))
            # texto = self.font.render("Galaga Game \n\nPresione S para comenzar", True, (0, 255, 0))
            # texto_rect = texto.get_rect()
            # texto_rect.center = CENTER
            self.screen.blit(fondo_game_over, ORIGIN)
            # self.screen.blit(texto, texto_rect)
            self.screen.blit(texto_1, (30,30))
            self.screen.blit(texto_2, (30,100))
            self.screen.blit(texto_3, (30,350))
            x = 30
            y = 100
            for puntaje in puntajes:
                y += 50
                self.screen.blit(self.font.render(str(puntaje[0])+"                     "+str(puntaje[1]) , True, (0, 255, 0)), (x,y))
            self.screen.blit(texto_4, (30,450))
            # pygame.display.flip()
            # pygame.time.delay(5000)
            # self.restart_game()
            pygame.display.flip()
        self.restart_game()

    def restart_game(self):
        # self.is_game_over = False
        # self.is_playing = True
        self.live = 3
        self.score = 0
        # self.nave.rect.center = START_POS
        self.sprites.empty()
        self.cherries.empty()
        self.bananas.empty()
        self.asteroids.empty()
        self.lasers.empty()
        self.nave.reset()
        # self.nave.speed_x = 0
        # self.nave.speed_y = 0
        self.sprites.add(self.nave)
        # print(flag_1)
        # print(flag_2)
        # print(flag_3)

        
        self.play()        
        # if not self.flag_1:
        #     self.play()
        # if not self.flag_2:
        #     self.play()
        # if not self.flag_3:
        #     self.play()
