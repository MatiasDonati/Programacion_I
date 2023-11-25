import pygame

#Musica Nivel 1
ruta_audio = './audio/DiagramadeVen.mp3'
sonido_fondo = pygame.mixer.Sound(ruta_audio)
sonido_fondo.set_volume(0.5)

#sonido nivel dos
sonido_nivel_dos = pygame.mixer.Sound('./audio/nivel_2.mp3')
sonido_nivel_dos.set_volume(0.5)

#Danzon
danzon = pygame.mixer.Sound('./audio/MADRUGAR_level_dos.mp3')
danzon.set_volume(1)

#Carcajada Introduccion - Varias carcajadas
ruta_risa = './audio/carcajada.mp3'
sonido_risa = pygame.mixer.Sound(ruta_risa)
sonido_risa.set_volume(0.7)

#Carcajada
sonido_una_risa = pygame.mixer.Sound('./audio/una_carcajada.mp3')
sonido_una_risa.set_volume(0.7)

#Musica Final Perdido
ruta_musica_fin = './audio/besau.mp3'
musica_fin = pygame.mixer.Sound(ruta_musica_fin)
musica_fin.set_volume(1)

#Musica Final Ganado
musica_fin_ganado = pygame.mixer.Sound('./audio/SAXOS.mp3')
musica_fin_ganado.set_volume(1)

#musica recompensas
musica_recompensas = pygame.mixer.Sound('./audio/enemigo_final.mp3')
musica_recompensas.set_volume(1)

#Musica enemigo final
musica_enemigo_final = pygame.mixer.Sound('./audio/ELCUENTITO.mp3')
musica_enemigo_final.set_volume(1)

#Risa Fantasma
risa_fantasma = pygame.mixer.Sound('./audio/risa_fantasma.mp3')
risa_fantasma.set_volume(2)

#sonidos Score
score_uno = pygame.mixer.Sound('./audio/score/score_uno.mp3')
score_uno.set_volume(0.8)
score_dos = pygame.mixer.Sound('./audio/score/score_dos.mp3')
score_dos.set_volume(0.8)
score_tres = pygame.mixer.Sound('./audio/score/score_tres.mp3')
score_tres.set_volume(0.8)
score_cuatro = pygame.mixer.Sound('./audio/score/score_cuatro.mp3')
score_cuatro.set_volume(0.8)

score_final = pygame.mixer.Sound('./audio/score/score_final.mp3')
score_final.set_volume(1)