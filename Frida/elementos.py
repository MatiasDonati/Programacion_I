from constantes import *
import bloque
from personaje import *
from enemigo import *
from enemigo_final import *
import recompensas

bloque_uno = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_dos = bloque.Bloque(ANCHO_VENTANA - ANCHO_BLOQUE - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 1.1 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_tres = bloque.Bloque(ANCHO_VENTANA /2 - ANCHO_BLOQUE /2  ,(ALTO_VENTANA - ALTO_BRUJA * 3) - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_cuatro = bloque.Bloque(ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloque_cinco = bloque.Bloque(ANCHO_VENTANA - ANCHO_BLOQUE - ANCHO_VENTANA * 0.5/4, ALTO_VENTANA - ALTO_BRUJA * 6 - ALTO_BLOQUE, ANCHO_BLOQUE, ALTO_BLOQUE)
bloques = [bloque_uno, bloque_dos, bloque_tres, bloque_cuatro, bloque_cinco]

#Frida
frida = Personaje(ANCHO_VENTANA/2,ALTO_VENTANA-ALTO_BRUJA,ANCHO_BRUJA, ALTO_BRUJA)

#enemigos
enemigo = Enemigo(bloque_cinco.rect_bloque.x,bloque_cinco.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_dos = Enemigo(bloque_cuatro.rect_bloque.x * 1.6,bloque_cuatro.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_tres = Enemigo(bloque_tres.rect_bloque.x,bloque_tres.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_cuatro = Enemigo(bloque_uno.rect_bloque.x,bloque_uno.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigo_cinco = Enemigo(bloque_dos.rect_bloque.x,bloque_dos.rect_bloque.y - ALTO_ENEMIGO,ANCHO_ENEMIGO, ALTO_ENEMIGO + ALTO_ENEMIGO * 2/8, bloques, diccionario_animaciones, 'quieto')
enemigos = [enemigo, enemigo_dos, enemigo_tres]

#Enemigo final - Fantasma
enemigo_final = EnemigoFinal(0, -1000, 150, 150, diccionario_enemigo_final,'derecha')


#Recompensas
posicion_iniciales_recompensas = [
    (bloque_uno.rect_bloque.centerx, bloque_uno.rect_bloque.y - ALTO_ENEMIGO),
    (bloque_dos.rect_bloque.centerx, bloque_dos.rect_bloque.y - ALTO_ENEMIGO),
    (bloque_tres.rect_bloque.centerx, bloque_tres.rect_bloque.y - ALTO_ENEMIGO),
    (bloque_cuatro.rect_bloque.centerx, bloque_cuatro.rect_bloque.y - ALTO_ENEMIGO),
    (bloque_cinco.rect_bloque.centerx, bloque_cinco.rect_bloque.y - ALTO_ENEMIGO),
    ]

random.shuffle(posicion_iniciales_recompensas)

gatito = recompensas.Recompensa(posicion_iniciales_recompensas[0][0], posicion_iniciales_recompensas[0][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'gatito')
gatito_dos = recompensas.Recompensa(posicion_iniciales_recompensas[1][0], posicion_iniciales_recompensas[1][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'gatito_dos')
pocion = recompensas.Recompensa(posicion_iniciales_recompensas[2][0], posicion_iniciales_recompensas[2][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'pocion')
escoba = recompensas.Recompensa(posicion_iniciales_recompensas[3][0], posicion_iniciales_recompensas[3][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'escoba')
barita_magica = recompensas.Recompensa(posicion_iniciales_recompensas[4][0], posicion_iniciales_recompensas[4][1], ANCHO_ENEMIGO, ALTO_ENEMIGO, 'barita')
lista_recompensas = [gatito, gatito_dos, pocion, escoba, barita_magica]