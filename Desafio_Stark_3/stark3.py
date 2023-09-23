from data_stark import lista_personajes
from funciones import *

# MATIAS EDUARDO DONATI
# DESAFIO STARK 3

inciso_a = "Normalizar Datos"
inciso_b = "Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB"
inciso_c = "Recorrer la lista y determinar cuál es el superhéroe más ALTO de género F"
inciso_d = "Recorrer la lista y determinar cuál es el superhéroe más ALTO de género M"
inciso_e = "Recorrer la lista y determinar cuál es el superhéroe más DEBIL de género M"
inciso_f =  "Recorrer la lista y determinar cuál es el superhéroe más DEBLI de género NB"
inciso_g =  "Recorrer la lista y determinar la FUERZA PROMEDIO de los superhéroes de género NB"
inciso_h =  "Determinar CUANTOS superhéroes tienen cada TIPO DE COLOR DE OJOS."
inciso_i =  "Determinar CUANTOS superhéroes tienen cada TIPO DE COLOR DE PELO."
inciso_j =  "Listar todos los superhéroes AGRUPADOS por TIPO DE OJOS"
inciso_k =  "Listar todos los superhéroes AGRUPADOS por TIPO DE INTELIGENCIA"
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú

def mostar_menu():
    flag = True
    while flag:

        opcion_elegida = input(f"""\n-A - {inciso_a}\n-0 - Salir\nElija la opcion que quiera conocer: """).upper()

        match opcion_elegida:
            case 'A':
                if stark_normalizar_datos(lista_personajes):
                    print('\nDatos Normalizados')
                else:
                    print('\nHubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente')
            case '0':
                print('Hasta Pronto.')
                flag = False
            case _:
                print("\nOPCION INCORRECTA\nElija la opcion que correcta que quiera conocer  ó '0' para salir: ")