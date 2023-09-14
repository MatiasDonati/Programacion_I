# MATIAS EDUARDO DONATI

from data_stark import lista_personajes
from funciones import *

# Desafío #02:
# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
# género NB
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú

femenino_mas_alto = None
masculino_mas_alto = None
masculino_mas_debil = None
nb_mas_debil = None
nb_suma_fuerza = 0
nb_cantidad = 0

for personaje in lista_personajes:

    match(personaje["genero"]):
        case "NB":
            # A
            print(personaje["nombre"])
            # E
            if nb_mas_debil == None or int(personaje["fuerza"]) < nb_mas_debil:
                nb_mas_debil = int(personaje["fuerza"])
                # D
                nb_mas_debil = personaje["nombre"]
            nb_suma_fuerza += int(personaje["fuerza"])
            nb_cantidad += 1
        case "F":
            if femenino_mas_alto == None or float(personaje["altura"]) > femenino_mas_alto:
                femenino_mas_alto = float(personaje["altura"])
                # B
                nombre_femenino_mas_alto = personaje["nombre"]
        case _:
            if masculino_mas_alto == None or float(personaje["altura"]) > masculino_mas_alto:
                masculino_mas_alto = float(personaje["altura"])
                # C
                nombre_fmasculino_mas_alto = personaje["nombre"]

            if masculino_mas_debil == None or int(personaje["fuerza"]) < masculino_mas_debil:
                masculino_mas_debil = int(personaje["fuerza"])
                # D
                nombre_masculino_mas_debil = personaje["nombre"]

tipos_de_ojos = set(personaje["color_ojos"] for personaje in lista_personajes)
print(tipos_de_ojos)

# for personaje in lista_personajes:
#     if personaje["color_ojos"] == "Blue":
#         print(personaje["nombre"])













# flag = True
# while flag:

#     opcion_elegida = input(f"""\n-A - {inciso_a} \n-B - {inciso_b}\n-C - {inciso_c}\n-D - {inciso_d}\n-E - {inciso_e} \n-0 - SALIR\nElija la opcion que quiera conocer: """).upper()
#     while opcion_elegida != "A" and  opcion_elegida != "B" and  opcion_elegida != "C" and opcion_elegida != "D" and opcion_elegida != "E"and opcion_elegida != "0":
#         opcion_elegida = input("OPCION INCORRECTA\nElija la opcion que quiera conocer: A-B-C-D-E o FIN para salir: ").upper()

#     match opcion_elegida:
#         case 'A':
#             for personaje in lista_personajes:
#                 for clave in personaje:
#                     print(f"{clave}: {personaje[clave]}")
#                 print("\n")
#         case 'B':
#             for personaje in lista_personajes_con_fuerza_mayor:
#                 print('')
#                 for clave in personaje:
#                     if clave == "identidad" or clave == "peso":
#                         print(f"{clave}: {personaje[clave]}")
#                 print('')
#         case 'C':
#             print(f"\n{mensaje_c}")
#         case 'D':
#             print(f"\n{mensaje_d}")
#         case 'E':
#             for personaje in lista_superan_fuerza_femenina_promedio:
#                 for clave in personaje:
#                     print(f"{clave}: {personaje[clave]}")
#                 print('')

#         case '0':
#             print('Hasta Pronto!!!')
#             flag = False