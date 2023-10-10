from data_stark import lista_personajes

# MATIAS EDUARDO DONATI
# DESAFIO STARK 1

mayor_fuerza = None
menor_altura = None
suma_peso_masculinos = 0
cantidad_masculinos = 0
cantidad_femenino = 0
suma_fuerza_femenino = 0

inciso_a = "Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe"
inciso_b = "Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)"
inciso_c = "Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)"
inciso_d = "Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)"
inciso_e = "Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino"

# A "Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe"

for personaje in lista_personajes:

# B "Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)"

    if mayor_fuerza == None or int(personaje["fuerza"]) > mayor_fuerza:
        mayor_fuerza = int(personaje["fuerza"])
        mayor_fuerza_peso = personaje["peso"]
        mayor_fuerza_identidad = personaje["identidad"]

# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)

    if menor_altura == None or float(personaje["altura"]) < menor_altura:
        menor_altura = float(personaje["altura"])
        menor_altura_nombre = personaje["nombre"]
        menor_altura_identidad = personaje["identidad"]

# D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)

    if personaje["genero"] == "M":
        cantidad_masculinos += 1
        suma_peso_masculinos += float(personaje["peso"])
    else:
        cantidad_femenino += 1
        suma_fuerza_femenino += float(personaje["fuerza"])

mensaje_c = f"{menor_altura_nombre} es el personaje mas bajo y es de identidad: {menor_altura_identidad}"

promedio_peso_masculinos = suma_peso_masculinos / cantidad_masculinos
promedio_peso_masculinos_redondeado = round(promedio_peso_masculinos, 2)
promedio_fuerza_femenino = suma_fuerza_femenino / cantidad_femenino

mensaje_d = f"El peso promedio de los superhéroes masculinos es {promedio_peso_masculinos_redondeado}"

# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino

lista_superan_fuerza_femenina_promedio = []

lista_personajes_con_fuerza_mayor = []

for personaje in lista_personajes:
    if int(personaje["fuerza"]) > promedio_fuerza_femenino:
        diccionario = {}
        diccionario['Nombre'] = personaje["nombre"]
        diccionario['Peso'] = personaje["peso"]
        lista_superan_fuerza_femenina_promedio.append(diccionario)

    if int(personaje["fuerza"]) == mayor_fuerza:
        lista_personajes_con_fuerza_mayor.append(personaje)

flag = True
while flag:

    opcion_elegida = input(f"""\n-A - {inciso_a} \n-B - {inciso_b}\n-C - {inciso_c}\n-D - {inciso_d}\n-E - {inciso_e} \n-0 - SALIR\nElija la opcion que quiera conocer: """).upper()
    while opcion_elegida != "A" and  opcion_elegida != "B" and  opcion_elegida != "C" and opcion_elegida != "D" and opcion_elegida != "E"and opcion_elegida != "0":
        opcion_elegida = input("OPCION INCORRECTA\nElija la opcion que quiera conocer: A-B-C-D-E o '0' para salir: ").upper()

    match opcion_elegida:
        case 'A':
            print(f"{opcion_elegida}: ")
            for personaje in lista_personajes:
                for clave in personaje:
                    print(f"{clave}: {personaje[clave]}")
                print("\n")
        case 'B':
            print(f"{opcion_elegida}: ")
            for personaje in lista_personajes_con_fuerza_mayor:
                print('')
                for clave in personaje:
                    if clave == "identidad" or clave == "peso":
                        print(f"{clave}: {personaje[clave]}")
                print('')
        case 'C':
            print(f"\n{opcion_elegida}: {mensaje_c}")
        case 'D':
            print(f"\n{opcion_elegida}: {mensaje_d}")
        case 'E':
            print(f"{opcion_elegida}:\n")
            for personaje in lista_superan_fuerza_femenina_promedio:
                for clave in personaje:
                    print(f"{clave}: {personaje[clave]}")
                print('')
        case '0':
            print('Hasta Pronto!!!')
            flag = False