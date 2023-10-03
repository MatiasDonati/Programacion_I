from data_stark import lista_personajes
from funciones_3 import *

# MATIAS EDUARDO DONATI
# DESAFIO STARK 3

opcion_elegida = None
flag_normalizar_datos = True

while opcion_elegida == None or opcion_elegida != 0:
    opcion_elegida = stark_marvel_app()
    while flag_normalizar_datos and opcion_elegida != 1:
        print('\nDeberá normalizar los Datos ingresando la opcion número 1.\n')
        opcion_elegida = stark_marvel_app()
    flag_normalizar_datos = False

    match opcion_elegida:
        case 1:
            if stark_normalizar_datos(lista_personajes):
                stark_normalizar_datos(lista_personajes)
                print('\nDatos Normalizados\n')
            else:
                print('\nHubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente\n')
        case 2:
            heroes_NB = obtener_dato_cantidad(lista_personajes, "NB", "genero")
            if stark_imprimir_heroes(heroes_NB) == False:
                print('\nNo hay heroes con los valores indicados.\n')
            else:
                stark_imprimir_heroes(heroes_NB)
        case 3 | 4:
            valor = "F"
            if opcion_elegida == 4:
                valor = "M"
            heroes = obtener_dato_cantidad(lista_personajes, valor, "genero")
            mas_alto = obtener_maximo(heroes, "altura")
            heroe_con_altura_maxima = obtener_dato_cantidad(heroes, mas_alto, "altura")
            stark_imprimir_heroes(heroe_con_altura_maxima)
        case 5 | 6:
            valor = "M"
            if opcion_elegida == 6:
                valor = "NB"
            lista_genero = obtener_dato_cantidad(lista_personajes, valor, "genero")
            mas_debil = obtener_minimo(lista_genero, "fuerza")
            mas_debil = obtener_dato_cantidad(lista_genero, mas_debil, "fuerza")
            if stark_imprimir_heroes(mas_debil) == False:
                print('\nNo hay heroes con los valores indicados.\n')
            else:
                stark_imprimir_heroes(mas_debil)
        case 7:
            heroes_NB = obtener_dato_cantidad(lista_personajes, "NB", "genero")
            promedio = calcular_promedio(heroes_NB, "fuerza")
            if promedio == False:
                print('\nNo hay heroes con los valores indicados\n')
            else:
                print(f'El promedio es: {promedio}')

        case 8 | 9:
            lista_ojos_pelo = []
            clave = "color_ojos"
            if opcion_elegida == 9:
                clave = "color_pelo"

            for heroe in lista_personajes:
                tipos_de_ojo_o_pelo = set(heroe[clave] for heroe in lista_personajes)

            for tipo_ojo_o_pelo in tipos_de_ojo_o_pelo:
                contador = 0
                for heroe in lista_personajes:
                    if tipo_ojo_o_pelo == heroe[clave]:
                        contador += 1

                diccionario_color_pelo_u_ojo = {}
                diccionario_color_pelo_u_ojo[tipo_ojo_o_pelo] = contador

                lista_ojos_pelo.append(diccionario_color_pelo_u_ojo)

            stark_imprimir_heroes(lista_ojos_pelo)

        case 10 | 11:

            clave = "color_ojos"
            if opcion_elegida == 11:
                clave = "inteligencia"

            lista_gral = []

            for heroe in lista_personajes:
                tipo_ojo_o_inteligencia = set(heroe[clave] for heroe in lista_personajes)

            for ojo_o_inteligencia in tipo_ojo_o_inteligencia:
                print(f"# {ojo_o_inteligencia}")
                print('')
                for heroe in lista_personajes:
                    if heroe[clave] == ojo_o_inteligencia:
                        print(obtener_nombre_y_dato(heroe, clave))
                        print('')
        case _:
            print('\nHasta Pronto!\n')