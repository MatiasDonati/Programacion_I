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
# F
if nb_cantidad != 0:
    fuerza_promedio_nb = nb_suma_fuerza / nb_cantidad

# G y H - PERFECTO !!
# I y J ARMAR DICCIONARIO AGRUPADOS POR COLOR DE OJOS E INTELIGENCIA
def contar_cantidad_pelos_u_ojos(color_de_ojos_o_pelo):

    if color_de_ojos_o_pelo == "G":
        color_de_ojos_o_pelo = "color_ojos"
    # ACA TIENE Q SER SOLO H!!
    else:
        color_de_ojos_o_pelo = "color_pelo"

    tipos_de_ojos_o_pelo = set(personaje[color_de_ojos_o_pelo] for personaje in lista_personajes)

    contador_colores_ojos_o_pelo = {}
    suma_contadores_ojos_o_pelo = 0

    for color_ojo_o_pelo in tipos_de_ojos_o_pelo:
        contador = 0
        for personaje in lista_personajes:
            if personaje[color_de_ojos_o_pelo] == color_ojo_o_pelo:
                contador += 1
                # Agregar una clave que "nombres" y que su valor sea una lista con 'personaes["nombre"].

        contador_colores_ojos_o_pelo[color_ojo_o_pelo] = contador

    for cantidad_color in contador_colores_ojos_o_pelo:
        suma_contadores_ojos_o_pelo += contador_colores_ojos_o_pelo[cantidad_color]

    if suma_contadores_ojos_o_pelo == len(lista_personajes):
        for clave in contador_colores_ojos_o_pelo:
            print(f"{clave}: {contador_colores_ojos_o_pelo[clave]}\n""")
    else:
        print(f"ERROR.\nLa suma de las cantidades de tipos de {color_de_ojos_o_pelo} no concuerda con la cantidad de personajes")

# DEPENDIENDO SI ES G o H SE GIJA EN PELO O COLOR DE OJOS
# DEPENDIENDO SI ES G o H SE GIJA EN PELO O COLOR DE OJOS
g_o_h = "G"
respuesta_g_o_h = contar_cantidad_pelos_u_ojos(g_o_h)


# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia

def listar_superheroes_por_color_de_ojos():
    superheroes_por_color_de_ojos = {}

    for personaje in lista_personajes:
        color_ojos = personaje["color_ojos"]

        # Comprobar si el color de ojos ya existe en el diccionario
        if color_ojos in superheroes_por_color_de_ojos:
            # Si existe, agregar el personaje a la lista correspondiente
            superheroes_por_color_de_ojos[color_ojos].append(personaje)
        else:
            # Si no existe, crear una nueva lista con el personaje
            superheroes_por_color_de_ojos[color_ojos] = [personaje]

    # Imprimir la lista de superhéroes por color de ojos
    for color_ojos, superheroes in superheroes_por_color_de_ojos.items():
        print(f"Color de ojos: {color_ojos}")
        for heroe in superheroes:
            print(f"Nombre: {heroe['nombre']}")
        print("\n")

# Llamar a la función para listar superhéroes por color de ojos
listar_superheroes_por_color_de_ojos()


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