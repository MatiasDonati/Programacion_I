import re
# MATIAS EDUARDO DONATI
# DESAFIO STARK 4


def extraer_iniciales(nombre_heroe):

    if len(nombre_heroe) == 0:
        return 'N/A'

    palabras = nombre_heroe.split()

    lista_iniciales = []

    for palabra in palabras:

        if palabra.lower() == 'the':
            continue

        palabra = palabra.replace('-', ' ')

        inicial = palabra[0].upper()

        lista_iniciales.append(inicial)

    salida = '.'.join(lista_iniciales)

    return salida

# print(extraer_iniciales("Howard the Duck"))

def definir_iniciales_nombre():
    pass