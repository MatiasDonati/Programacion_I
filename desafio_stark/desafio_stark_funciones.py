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
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú
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

# G y H
# I y J ARMAR DICCIONARIO AGRUPADOS POR COLOR DE OJOS E INTELIGENCIA

def contar_cantidad_pelos_u_ojos(color_de_ojos_o_pelo):

    if color_de_ojos_o_pelo == "G":
        color_de_ojos_o_pelo = "color_ojos"
    # ACA TIENE Q SER SOLO H!!
    else:
        color_de_ojos_o_pelo = "color_pelo"

    tipos_de_ojos_o_pelo = set(personaje[color_de_ojos_o_pelo] for personaje in lista_personajes)

    contador_colores_ojos_o_pelo = {}
    lista_contador_colores_ojos_o_pelo = []
    suma_contadores_ojos_o_pelo = 0

    for color_ojo_o_pelo in tipos_de_ojos_o_pelo:
        contador = 0
        lista_nombres_mismo_color_ojos_o_pelo = []
        for personaje in lista_personajes:
            if personaje[color_de_ojos_o_pelo] == color_ojo_o_pelo:
                contador += 1
                lista_nombres_mismo_color_ojos_o_pelo.append(personaje["nombre"])

        diccionario_colores_o_pelo = {}
        diccionario_colores_o_pelo[color_ojo_o_pelo] = contador
        diccionario_colores_o_pelo["nombres"] = lista_nombres_mismo_color_ojos_o_pelo

        lista_contador_colores_ojos_o_pelo.append(diccionario_colores_o_pelo)

    for cantidad_color in lista_contador_colores_ojos_o_pelo:
        suma_contadores_ojos_o_pelo += list(cantidad_color.values())[0]

    if suma_contadores_ojos_o_pelo == len(lista_personajes):
        for color in lista_contador_colores_ojos_o_pelo:
            primera_clave = list(color.keys())[0]
            primer_valor = list(color.values())[0]
            segunda_clave = list(color.keys())[1]
            segundo_valor = list(color.values())[1]
            print(f"{primera_clave}: {primer_valor}")
            print(f"{segunda_clave}: {segundo_valor}")

    else:
        print(f"ERROR.\nLa suma de las cantidades de tipos de {color_de_ojos_o_pelo} no concuerda con la cantidad de personajes")

    return lista_contador_colores_ojos_o_pelo

    # HACER FUNCIONES QUE RECIBA A LISTA Y AHI HACER CADA INCISO !
    # HACER FUNCIONES QUE RECIBA A LISTA Y AHI HACER CADA INCISO !
    # HACER FUNCIONES QUE RECIBA A LISTA Y AHI HACER CADA INCISO !

# DEPENDIENDO SI ES G o H SE FIJA EN PELO O COLOR DE OJOS
# g_o_h = "G"
# contar_cantidad_pelos_u_ojos(g_o_h)

# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia

# def listar_superheroes_por_color_de_ojos():
#     superheroes_por_color_de_ojos = {}

#     for personaje in lista_personajes:
#         color_ojos = personaje["color_ojos"]

#         # Comprobar si el color de ojos ya existe en el diccionario
#         if color_ojos in superheroes_por_color_de_ojos:
#             # Si existe, agregar el personaje a la lista correspondiente
#             superheroes_por_color_de_ojos[color_ojos].append(personaje)
#         else:
#             # Si no existe, crear una nueva lista con el personaje
#             superheroes_por_color_de_ojos[color_ojos] = [personaje]

#     # Imprimir la lista de superhéroes por color de ojos
#     for color_ojos, superheroes in superheroes_por_color_de_ojos.items():
#         print(f"Color de ojos: {color_ojos}")
#         for heroe in superheroes:
#             print(f"Nombre: {heroe['nombre']}")
#         print("\n")

# # Llamar a la función para listar superhéroes por color de ojos
# listar_superheroes_por_color_de_ojos()

flag = True
while flag:

    opcion_elegida = input(f"""\n-A - {inciso_a} \n-B - {inciso_b}\n-C - {inciso_c}\n-D - {inciso_d}\n-E - {inciso_e}\n-F - {inciso_f}\n-G - {inciso_g}\n-H - {inciso_h}\n-I - {inciso_i}\n-J - {inciso_j}\n-0 - SALIR\nElija la opcion que quiera conocer: """).upper()

    match opcion_elegida:
        case 'A':
            pass
        case 'B':
            pass
        case 'C':
           pass
        case 'D':
           pass
        case 'E':
            pass
        case 'F':
            pass
        case 'G':
            lista_contador_colores_ojos_o_pelo = contar_cantidad_pelos_u_ojos(opcion_elegida)
            # for color in lista_contador_colores_ojos_o_pelo:
            #     primera_clave = list(color.keys())[0]
            #     primer_valor = list(color.values())[0]
            #     segunda_clave = list(color.keys())[1]
            #     segundo_valor = list(color.values())[1]
            #     print(f"{primera_clave}: {primer_valor}")
            #     print(f"{segunda_clave}: {segundo_valor}")
        case 'H':
            contar_cantidad_pelos_u_ojos(opcion_elegida)
        case 'I':
           pass
        case 'J':
           pass
        case '0':
            print('Hasta Pronto!!!')
            flag = False
        case _:
            print("\nOPCION INCORRECTA\nElija la opcion que quiera conocer: A-B-C-D-E o FIN para salir: ")