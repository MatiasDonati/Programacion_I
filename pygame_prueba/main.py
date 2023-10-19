# import pygame

# screen = pygame.display.set_mode([500,500])

# pygame.display.set_caption("PYGAME PRUEBA!")

# screen.fill((255, 255, 255))

# pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

# pygame.joystick

# pygame.mouse

# pygame.key

# pygame.event.get()

# import pygame
# pygame.init() #Se inicializa pygame
# screen = pygame.display.set_mode([500, 500]) #Se crea una ventana
# running = True
# while running:
# # Se verifica si el usuario cerro la ventana
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# screen.fill((255, 255, 255))# Se pinta el fondo de la ventana
# # Se dibuja un círculo azul en el centro
# pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
# pygame.display.flip()# Muestra los cambios en la pantalla
# pygame.quit() # Fin

# JUEGUITOO!!!!
# JUEGUITOO!!!!
# JUEGUITOO!!!!


"""
VER EN EL LABURO QUIZA ES SIN 3
"""
# pip3 install -U pygame
# python -m pygame.examples.aliens

"""
"""
import pygame

pygame.init()

running = True

window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("vamos a hacer un juego!")
while(running):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	window.fill((255, 255, 255)) # Se pinta el fondo de la ventana

	pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
	pygame.display.flip()# Muestra los cambios en la pantalla