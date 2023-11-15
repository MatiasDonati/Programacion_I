

def colisionar(frida, enemigos):
    retorno = False
    for enemigo_actual in enemigos:
        if frida.rect_frida.colliderect(enemigo_actual.rect_enemigo):
            retorno = True
    return retorno

def matar_enemigo(proyectil, enemigo_actual):
    if proyectil != None and proyectil.rectangulo.colliderect(enemigo_actual.rect_enemigo):
        return True
    return False

def atacar_a_frida(proyectil, frida):
    if proyectil != None and proyectil.rectangulo.colliderect(frida.rect_frida):
        return True
    return False