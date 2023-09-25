from data_stark import lista_personajes
from funciones import *

# MATIAS EDUARDO DONATI
# DESAFIO STARK 3

opcion_elegida = None

while opcion_elegida == None or opcion_elegida != 0:
    opcion_elegida = stark_marvel_app(lista_personajes)

    match opcion_elegida:
        case 1:
            if stark_normalizar_datos(lista_personajes):
                stark_normalizar_datos(lista_personajes)
                print('\nDatos Normalizados\n')
            else:
                print('\nHubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente\n')
        case 2:
            heroes_NB = obtener_dato_cantidad(lista_personajes, "NB", "genero")
            stark_imprimir_heroes(heroes_NB)
        case 3 | 4:
            valor = "F"
            if opcion_elegida == 4:
                valor = "M"
            heroes = obtener_dato_cantidad(lista_personajes, valor, "genero")
            mas_alto = obtener_maximo(heroes, "altura")
            heroe_con_altura_maxima = obtener_dato_cantidad(heroes, mas_alto, "altura")
            stark_imprimir_heroes(heroe_con_altura_maxima)
        case 5 | 6:
            valor = "M"
            if opcion_elegida == 6:
                valor = "NB"
            lista_genero = obtener_dato_cantidad(lista_personajes, valor, "genero")
            mas_debil = obtener_minimo(lista_genero, "fuerza")
            mas_debil = obtener_dato_cantidad(lista_genero, mas_debil, "fuerza")
            stark_imprimir_heroes(mas_debil)
        case 7:
            pass