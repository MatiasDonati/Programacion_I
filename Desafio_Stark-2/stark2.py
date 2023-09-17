from data_stark import lista_personajes
from funciones import *

# MATIAS EDUARDO DONATI
# DESAFIO STARK 2

inciso_a =  "Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB"
inciso_b = "Recorrer la lista y determinar cuál es el superhéroe más alto de género F"
inciso_c =  "Recorrer la lista y determinar cuál es el superhéroe más alto de género M"
inciso_d = "Recorrer la lista y determinar cuál es el superhéroe más débil de género M"
inciso_e = "Recorrer la lista y determinar cuál es el superhéroe más débil de género NB"
inciso_f =  "Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB"
inciso_g =  "Determinar cuántos superhéroes tienen cada tipo de color de ojos."
inciso_h =  "Determinar cuántos superhéroes tienen cada tipo de color de pelo."
inciso_i =  "Listar todos los superhéroes agrupados por color de ojos."
inciso_j =  "Listar todos los superhéroes agrupados por tipo de inteligencia"
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú

flag = True
while flag:

    opcion_elegida = input(f"""\n-A - {inciso_a} \n-B - {inciso_b}\n-C - {inciso_c}\n-D - {inciso_d}\n-E - {inciso_e}\n-F - {inciso_f}\n-G - {inciso_g}\n-H - {inciso_h}\n-I - {inciso_i}\n-J - {inciso_j}\n-0 - SALIR\nElija la opcion que quiera conocer: """).upper()

    match opcion_elegida:
        case 'A':
            print(f"{opcion_elegida}: {recorrer_lista_NB(lista_personajes)}")
        case 'B':
            print(f"{opcion_elegida}: {mostrar_femenino_mas_alto(lista_personajes)}")
        case 'C':
            print(f"{opcion_elegida}: {mostrar_femenino_mas_alto(lista_personajes)}")
        case 'D':
            print(f"{opcion_elegida}: {mostrar_masculino_mas_debil(lista_personajes)}")
        case 'E':
            pass
        case 'F':
            pass
        case 'G':
            pass
        case 'H':
            pass
        case 'I':
           pass
        case 'J':
           pass
        case '0':
            print('Hasta Pronto.')
            flag = False
        case _:
            print("\nOPCION INCORRECTA\nElija la opcion que quiera conocer: A-B-C-D-E o FIN para salir: ")