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
        case 3:
            heroes_F = obtener_dato_cantidad(lista_personajes, "F", "genero")
            mas_alta = obtener_maximo(lista_personajes, "altura")
            femenino_con_alura_maxima = obtener_dato_cantidad(lista_personajes, mas_alta, "altura")
            stark_imprimir_heroes(femenino_con_alura_maxima)
        case 4:
            