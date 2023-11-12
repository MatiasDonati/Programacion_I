def colisionar(frida, enemigos):
    retorno = False
    for enemigo_actual in enemigos:
        if frida.rect_frida.colliderect(enemigo_actual.rect_enemigo):
            retorno = True
    return retorno

def matar_enemigo(proyectil, enemigos):
    retorno = False
    for enemigo_actual in enemigos:
        if proyectil.rectangulo.colliderect(enemigo_actual.rect_enemigo):
            return enemigo_actual
    return retorno
