
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

def agarrar_recompensa(frida, recompensa):
    if frida.rect_frida.colliderect(recompensa.rect_recompensa):
        frida.scoring += recompensa.puntuacion
        return True


def colisionar_con_enemigo_final(frida, enemigo_final):
    retorno = False
    if frida.rect_frida.colliderect(enemigo_final.rect_enemigo_final):
        retorno = True
    return retorno


def disparar_enemigo_final(proyectil, enemigo_final):
    if proyectil != None and proyectil.rectangulo.colliderect(enemigo_final.rect_enemigo_final):
        return True
    return False