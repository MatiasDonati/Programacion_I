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
            pass