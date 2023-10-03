from data_stark import lista_personajes
from funciones_4 import *

# MATIAS EDUARDO DONATI
# DESAFIO STARK 4

while True:

    opcion_usuario = stark_marvel_app_3()
    while not re.match(r'^[1-5Ss]$', opcion_usuario):
        print(f'\n"{opcion_usuario}" no es una opcion correcta...\nIntentelo de nuevo.\n')
        opcion_usuario = stark_marvel_app_3()

    match opcion_usuario:
        case '1':
            stark_imprimir_nombres_con_iniciales(lista_personajes)
        case '2':
           stark_generar_codigos_heroes(lista_personajes)
        case '3':
            stark_normalizar_datos(lista_personajes)
        case '4':
            stark_imprimir_indice_nombre(lista_personajes)
        case '5':
            stark_navegar_fichas(lista_personajes)
        case _:
            print('Hasta luego!')
            break