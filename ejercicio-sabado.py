# Copyright (C) 2023 <UTN FRA>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
UTN Inversiones, realiza un estudio de mercado para saber cual será la nueva franquicia que se insertará en el 
mercado argentino y en la cual invertir
Las posibles franquicias son las siguientes: 
# Apple,
# Dunkin Donnuts, 
# Ikea o
# Taco Bell.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles
son los gustos de los encuestados:

El programa tendra precargado un menú de opciones en el que debemos programar lo siguiente

1.Cargar voto, está opción agregara a las listas un voto en especifico pidiendo los siguientes datos
    nombre del encuestado.
    edad (no menor a 18)
    genero (Masculino - Femenino - Otro)
    voto (APPLE, DUNKIN, IKEA, TACO)

2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años.
3-Género que predomina en la empresa.
4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino y su edad se encuentre
entre los 18 y 30.
5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados
6-Salir
'''

lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
            "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
            32, 22, 29, 27, 19, 49, 27, 22, 29, 27]

lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
                "Otro", "Marta", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
                "Femenino", "Masculino", "Femenino"]

lista_votos = ["APPLE", "DUNKIN", "IKEA", "APPLE", "TACO", "DUNKIN", "TACO", "APPLE", "TACO", "APPLE",
            "IKEA", "APPLE", "DUNKIN", "DUNKIN", "APPLE", "IKEA", "APPLE", "DUNKIN", "IKEA", "TACO"]

#PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS

cantidad_apple_hasta_35 = 0
cantidad_masculino = 0
cantidad_femenino = 0
cantidad_otro = 0
no_votaron_apple_no_fem_entre_18_y_30 = 0
suma_edades = 0
nombre_votaron_a_IKEA_o_TACO_y_superan_la_edad_promedio = []
edad_votaron_a_IKEA_o_TACO_y_superan_la_edad_promedio = []

for indice in range(len(lista_nombres)):

    match lista_votos[indice]:
        case "APPLE":
            if lista_edades[indice] <= 36:
                cantidad_apple_hasta_35 += 1
        case _:
            if lista_edades[indice] >= 18 and lista_edades[indice] <= 30:
                no_votaron_apple_no_fem_entre_18_y_30 =+ 1

    suma_edades += lista_edades[indice]

    match lista_generos[indice]:
        case "Masculino":
            cantidad_masculino += 1
        case "Femenino":
            cantidad_femenino += 1
        case _:
            cantidad_otro += 1

porcentaje_no_votaron_apple_no_fem_entre_18_y_30 = (no_votaron_apple_no_fem_entre_18_y_30/ len(lista_nombres)) * 100

promedio_edades = suma_edades / len(lista_edades)

if cantidad_masculino > cantidad_femenino and cantidad_masculino > cantidad_otro:
    genero_prediminante = "Masculino"
elif cantidad_masculino > cantidad_otro:
    genero_prediminante = "Femenino"
else:
    genero_prediminante = "Otro"

for indice in range(len(lista_edades)):
    if (lista_votos[indice] == "IKEA" or lista_votos[indice] == "TACO") and lista_edades[indice] > promedio_edades:
        nombre_votaron_a_IKEA_o_TACO_y_superan_la_edad_promedio.append(lista_nombres[indice])
        edad_votaron_a_IKEA_o_TACO_y_superan_la_edad_promedio.append(lista_edades[indice])

while True:

    print("\n1-Cargar Voto\n2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años\n3-Género que predomina en la empresa.\n4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino o su edad se encuentre.\n5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados\n6-Salir")

    opcion = input("Ingrese una opción 1-6:")
    opcion = int(opcion)
    if opcion == 1:
        print("Nooooooooooo")
    elif opcion == 2:
        print(cantidad_apple_hasta_35)
    elif opcion == 3:
        print(genero_prediminante)
    elif opcion == 4:
        print(porcentaje_no_votaron_apple_no_fem_entre_18_y_30)
    elif opcion == 5:
        for indice in range(len(nombre_votaron_a_IKEA_o_TACO_y_superan_la_edad_promedio)):
            print(nombre_votaron_a_IKEA_o_TACO_y_superan_la_edad_promedio[indice])
            print(edad_votaron_a_IKEA_o_TACO_y_superan_la_edad_promedio[indice])
    elif opcion == 6:
        print("Adios")
        break
    else:
        print("Opcion incorrecta (1-6)")