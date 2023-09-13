from data_stark import lista_personajes

mayor_fuerza = None
menor_altura = None
suma_peso_masculinos = 0
cantidad_masculinos = 0
cantidad_femenino = 0
suma_fuerza_femenino = 0

# A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
for personaje in lista_personajes:
    # print(personaje["nombre"].upper()+':')
    # print(personaje["identidad"])
    # print(personaje["empresa"])
    # print(personaje["altura"])
    # print(personaje["peso"])
    # print(personaje["genero"])
    # print(personaje["color_ojos"])
    # print(personaje["color_pelo"])
    # print(personaje["fuerza"])
    # print(personaje["inteligencia"])
    # print("------------\n")

# B Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)

    if mayor_fuerza == None or int(personaje["fuerza"]) > mayor_fuerza:
        mayor_fuerza = int(personaje["fuerza"])
        mayor_fuerza_peso = personaje["peso"]
        mayor_fuerza_identidad = personaje["identidad"]

    mensaje_b = f"El personaje con mayor fuerza es de identidad: {mayor_fuerza_identidad} y pesa: {mayor_fuerza_peso}"

# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)

    if menor_altura == None or float(personaje["altura"]) < menor_altura:
        menor_altura = float(personaje["altura"])
        menor_altura_nombre = personaje["nombre"]
        menor_altura_identidad = personaje["identidad"]

    mensaje_c = f"{menor_altura_nombre} es el personaje mas bajo y es de identidad: {menor_altura_identidad}"

# D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)

    if personaje["genero"] == "M":
        cantidad_masculinos += 1
        suma_peso_masculinos += float(personaje["peso"])
    else:
        cantidad_femenino += 1
        suma_fuerza_femenino += float(personaje["fuerza"])

promedio_peso_masculinos = suma_peso_masculinos / cantidad_masculinos
promedio_fuerza_femenino = suma_fuerza_femenino / cantidad_femenino

mensaje_d = promedio_peso_masculinos

# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino

lista_superan_fuerza_femenina_promedio = []

for personaje in lista_personajes:
    if int(personaje["fuerza"]) > promedio_fuerza_femenino:
        diccionario = {}
        diccionario['Nombre'] = personaje["nombre"]
        diccionario['Peso'] = personaje["peso"]
        lista_superan_fuerza_femenina_promedio.append(diccionario)

# mensaje_e = lista_superan_fuerza_femenina_promedio

flag = True
while flag:

    opcion_elegida = input("Elija la opcion que quiera conocer: A-B-C-D-E o '0' para salir: ").upper()
    while opcion_elegida != "A" and  opcion_elegida != "B" and  opcion_elegida != "C" and opcion_elegida != "D" and opcion_elegida != "E"and opcion_elegida != "FIN":
        opcion_elegida = input("Opcion incorrecta\nElija la opcion que quiera conocer: A-B-C-D-E o FIN para salir: ").upper()

    match opcion_elegida:
        case 'A':
            for personaje in lista_personajes:
                print(personaje["nombre"].upper()+':')
                print(personaje["identidad"])
                print(personaje["empresa"])
                print(personaje["altura"])
                print(personaje["peso"])
                print(personaje["genero"])
                print(personaje["color_ojos"])
                print(personaje["color_pelo"])
                print(personaje["fuerza"])
                print(personaje["inteligencia"])
                print("------------\n")
        case 'B':
            print(mensaje_b)
        case 'C':
            print(mensaje_c)
        case 'D':
            print(mensaje_d)
        case 'E':
            for personaje in lista_superan_fuerza_femenina_promedio:
                print(personaje["Nombre"])
                print(personaje["Peso"])
                print("------------\n")
        case 'FIN':
            print('Hasta Pronto!!!')
            flag = False

            # PONER TODOS LOS SUPERHEROES CON MAYOR FUERZA  NO SOLO EL PRIMERO QUE APARECE//// punto B
            # PONER TODOS LOS SUPERHEROES CON MAYOR FUERZA  NO SOLO EL PRIMERO QUE APARECE//// punto B
            # PONER TODOS LOS SUPERHEROES CON MAYOR FUERZA  NO SOLO EL PRIMERO QUE APARECE//// punto B
            # PONER TODOS LOS SUPERHEROES CON MAYOR FUERZA  NO SOLO EL PRIMERO QUE APARECE//// punto B
            # PONER TODOS LOS SUPERHEROES CON MAYOR FUERZA  NO SOLO EL PRIMERO QUE APARECE//// punto B
            # PONER TODOS LOS SUPERHEROES CON MAYOR FUERZA  NO SOLO EL PRIMERO QUE APARECE//// punto B