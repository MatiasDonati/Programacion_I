import pygame

def girar_imagenes(lista_original, flip_x, flip_y)->list:
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def reescalar_imagenes(diccionario_animaciones, tamaño:tuple):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            superficie = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(superficie, tamaño)

personaje_quieto = [pygame.image.load("./imgs2/bruja/idle/idle_1.png")]

personaje_izquierda = [pygame.image.load("./imgs2/bruja/walk/walk_1.png"),
                       pygame.image.load("./imgs2/bruja/walk/walk_2.png"),
                       pygame.image.load("./imgs2/bruja/walk/walk_3.png"),
                       pygame.image.load("./imgs2/bruja/walk/walk_4.png"),
                       pygame.image.load("./imgs2/bruja/walk/walk_5.png"),
                       pygame.image.load("./imgs2/bruja/walk/walk_6.png"),
                       pygame.image.load("./imgs2/bruja/walk/walk_7.png"),
                       pygame.image.load("./imgs2/bruja/walk/walk_8.png")]

personaje_derecha = girar_imagenes(personaje_izquierda, True, False)

personaje_salta = [pygame.image.load("./imgs2/bruja/jump/jump_1.png"),
                       pygame.image.load("./imgs2/bruja/jump/jump_2.png"),
                       pygame.image.load("./imgs2/bruja/jump/jump_3.png"),
                       pygame.image.load("./imgs2/bruja/jump/jump_4.png"),
                       pygame.image.load("./imgs2/bruja/jump/jump_5.png")]

explosion = [pygame.image.load("./imgs2/explosion//1.png"),
                       pygame.image.load("./imgs2/explosion//2.png"),
                       pygame.image.load("./imgs2/explosion//3.png"),
                       pygame.image.load("./imgs2/explosion//4.png"),
                       pygame.image.load("./imgs2/explosion//5.png"),
                       pygame.image.load("./imgs2/explosion//6.png"),
                       pygame.image.load("./imgs2/explosion//7.png"),
                       pygame.image.load("./imgs2/explosion//8.png"),
                       pygame.image.load("./imgs2/explosion//9.png"),
                       pygame.image.load("./imgs2/explosion//10.png")]

img_fueguito = pygame.image.load('./imgs/fueguito.png')
img_fueguito_derecha = pygame.transform.scale(img_fueguito, (100, 60))
img_fueguito_izquierda = pygame.transform.flip(img_fueguito_derecha, True, False)