from data_stark import lista_personajes
from funciones import *

# MATIAS EDUARDO DONATI
# DESAFIO STARK 3

inciso_a =  "Normalizar Datos"
# inciso_b = "Recorrer la lista y determinar cuál es el superhéroe más alto de género F"
# inciso_c =  "Recorrer la lista y determinar cuál es el superhéroe más alto de género M"
# inciso_d = "Recorrer la lista y determinar cuál es el superhéroe más débil de género M"
# inciso_e = "Recorrer la lista y determinar cuál es el superhéroe más débil de género NB"
# inciso_f =  "Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB"
# inciso_g =  "Determinar cuántos superhéroes tienen cada tipo de color de ojos."
# inciso_h =  "Determinar cuántos superhéroes tienen cada tipo de color de pelo."
# inciso_i =  "Listar todos los superhéroes agrupados por color de ojos."
# inciso_j =  "Listar todos los superhéroes agrupados por tipo de inteligencia"
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú

flag = True
while flag:

    opcion_elegida = input(f"""\n-A - {inciso_a} \n B- \n-0 - SALIR\nElija la opcion que quiera conocer: """).upper()

    match opcion_elegida:
        case 'A':
            if stark_normalizar_datos(lista_personajes):
                print('\nDatos Normalizados')
            else:
                print('\nHubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente')
        case 'B':
            print(obtener_nombre_y_dato(lista_personajes[8], 'fuerza'))
        case '0':
            print('Hasta Pronto.')
            flag = False
        case _:
            print("\nOPCION INCORRECTA\nElija la opcion que correcta que quiera conocer  ó '0' para salir: ")