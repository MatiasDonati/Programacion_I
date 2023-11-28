import pygame.font

def cargar_fuente(ruta, tamaño):
    try:
        fuente = pygame.font.Font(ruta, tamaño)
    except pygame.error:
        print(f"Error al cargar la fuente desde {ruta}. Verifica la ruta del archivo de fuente.")
        fuente = pygame.font.Font(None, tamaño)
    return fuente
