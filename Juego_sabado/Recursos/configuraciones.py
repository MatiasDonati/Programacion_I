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

personaje_quieto = [pygame.image.load("./0.png")]

personaje_derecha = [pygame.image.load("./1.png"),
                    pygame.image.load("./2.png")]

personaje_izquierda = girar_imagenes(personaje_derecha, True, False)

personaje_salta = [pygame.image.load('./3.png')]