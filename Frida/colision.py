def colisionar(frida, enemigos):
    for enemigo_actual in enemigos:
        if frida.rect_frida.colliderect(enemigo_actual.rect_enemigo):
            print('COlision !!@#!@#!@#!@#@!')
