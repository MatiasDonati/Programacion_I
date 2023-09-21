# # Ej1
# nombre = input('Nombre: ')
# sueldo = input('Sueldo: ')
# sueldo = float(sueldo)

# while sueldo <= 0:
#     sueldo = input('Sueldo.. mayor a 0: ')
#     sueldo = float(sueldo)

# aumento_sueldo = sueldo + sueldo * 0.1
# print(f"El sueldo {sueldo} con un incremento del 10% es: {aumento_sueldo}")

# # Ej2
# edad = input('edad: ')
# edad = int(edad)
# if edad > 18:
#     mensaje='Mayor de 18'
# elif edad >=13 and edad <=17:
#     mensaje='Entre 13 y 17'
# else:
#     mensaje='menor de 13'
# print(mensaje)

# # Ej3
# numeros = []
# for _ in range(5):
#     numero = input('ingresa Numero entero destinto de cero: ')
#     numero = int(numero)
#     numeros.append(numero)

# print(f"{numeros}")

# cantidad_numeros_pares = 0
# cantidad_numeros_impares = 0
# numero_menor = None
# par_mas_grande = None
# suma_positivos = 0
# cantidad_negativos = 0
# suma_negativos = 0
# producto_negativos = 1

# for indice in range (len(numeros)):
#     if numeros[indice] %2 == 0:
#         cantidad_numeros_pares += 1
#         if par_mas_grande == None or par_mas_grande < numeros[indice]:
#             par_mas_grande = numeros[indice]
#     else:
#         cantidad_numeros_impares += 1

#     if numero_menor == None or numero_menor > numeros[indice]:
#         numero_menor = numeros[indice]

#     if numeros[indice] > 0:
#         suma_positivos += numeros[indice]
#     else:
#         producto_negativos = producto_negativos * numeros[indice]

# print(f"numeros pares: {cantidad_numeros_pares}\n numeros impares: {cantidad_numeros_impares}")
# print(f"el numero mas chico es: {numero_menor}")
# print(f"el numero par mas grande es: {par_mas_grande}")
# print(f"suma de los positivos: {suma_positivos}")
# print(f"prodcuto de los negativos: {producto_negativos}")

# # Ej4
# edad = input("edad: ")
# edad=int(edad)
# estado_civil = input("estado civil: ")

# if edad < 18 and estado_civil != "Soltero":
#     print("Es muy pequeño para NO ser soltero.")

# # Ej5
# '''
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final:
# -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
# descuento del 10% Mar del Plata tiene un descuento del 20%
# -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
# un aumento del 10% Mar del Plata tiene un aumento del 20%
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
# aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
# precio sin descuento.
# Validar el ingreso de datos
# '''

# estacion = input('estacion(Invierno/Verano/Otoño/Primavera): ').upper()
# localidad = input('localidad(Bariloche/Cataratas/Mar delPlata/Córdoba): ').upper()

# porcentaje = 0
# estadia_base = 15000

# match(estacion):
#     case "INVIERNO":
#         match(localidad):
#             case "BARILOCHE":
#                 porcentaje = 20
#             case "MAR DEL PLATA":
#                 porcentaje = -20
#             case _:
#                 porcentaje = -10
#     case "VERANO":
#         match(localidad):
#             case "BARILOCHE":
#                 porcentaje = -20
#             case "MAR DEL PLATA":
#                 porcentaje = 20
#             case _ :
#                 porcentaje = 10
#     case _ :
#         match(localidad):
#             case "CORDOBA":
#                 porcentaje = 0
#             case _ :
#                 porcentaje = 10

# precio_final = estadia_base + (estadia_base * (porcentaje / 100))

# if porcentaje > 0:
#     tipo = "aumento"
# else:
#     tipo = "descuento"

# print(f"En {estacion} en la ciudad de {localidad} hay un {tipo} de {abs(porcentaje)}% \n Precio final por estadia:{precio_final}")

# # Ejercicio 6:
# # Utilizar For
# # Dada la siguiente lista:
# # [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# # mostrar el mayor.

# numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mayor = None

# for numero in numeros:
#     if mayor == None or numero > mayor:
#         mayor = numero

# print(mayor)

# # Ejercicio 7:
# # Dada la siguiente lista:
# # [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# # mostrar solo los números pares.

# numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# pares = []

# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)

# print(pares)

# # Ejercicio 8:
# # Dada la siguiente lista:
# # [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
# # mostrar el número repetido

# lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
# bandera = False
# for numero in lista_numeros:
#     contador = 0
#     for dato in lista_numeros:
#         if numero == dato:
#             contador += 1
#             if contador == 2:
#                 numero_repetido = numero
#                 bandera = True
#                 break
#     if bandera == True:
#         break
# print(numero_repetido)

# /******************************************************************************
# ejercicio 8
# *******************************************************************************/
numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 3, 12, 48, 78, 29, 58]

repetidos = []

for indice in range(len(numeros)):
    for indice_dos in range(indice + 1, len(numeros)):
        if numeros[indice] == numeros[indice_dos] and numeros[indice] not in repetidos:
            repetidos.append(numeros[indice])

print(repetidos)


# # Ejercicio 9:
# # Dadas las siguientes listas:
# # edades = [25,36,18,23,45]
# # nombre = ["Juan","Ana","Sol","Mario","Sonia"]
# # y considerando que la posición en la lista corresponde a la misma persona,
# # mostar el nombre de la persona más joven

# edades = [25,36,18,23,45]
# nombre = ["Juan","Ana","Sol","Mario","Sonia"]
# edad_menor = None

# for indice in range(len(edades)):
#     if edad_menor == None or edades[indice] < edad_menor:
#         edad_menor = edades[indice]
#         nombre_menor = nombre[indice]

# print(f"La persona mas joven es {nombre_menor}")

# Ejercicio 10:
# Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
# respectivas listas. Validar el ingreso de datos según su criterio.
# Datos:
# nombre, sexo (f/m), nota (validar).
# Una vez cargados los datos:
# Mostrar el nombre del hombre con nota más baja
# Mostrar el promedio de notas de las mujeres
# Ejemplo:


# nombres = ["Juan","Pedro","Sol","Paco","Ana"]
# sexo = ["m","m","f","m","f"]
# nota = [6,8,10,8,5]

# nota_mas_baja = None
# cantidad_mujeres = 0
# suma_notas_mujeres = 0
# nombres = []
# sexos = []
# notas = []
# for _ in range(5):

#     nombre = input('Nombre: ')
#     while nombre == None or len(nombre) < 4:
#         nombre = input('Nombre: ')
#     nombres.append(nombre)

#     sexo = input('Sexo: ')
#     while sexo == None or sexo != "m" and sexo != "f":
#         sexo = input('Sexo: ')
#     sexos.append(sexo)

#     nota = input('Nota: ')
#     while nota.isdigit() == False or int(nota) < 0 or int(nota) > 10:
#         nota = input('Nota: ')
#     nota = int(nota)
#     notas.append(nota)

# for indice in range(len(nombres)):
#     if nota_mas_baja == None or nota[indice] < nota_mas_baja:
#         nombre_nota_mas_baja = nombres[indice]
    
#     if sexo[indice] == "f":
#         cantidad_mujeres  += 1
#         suma_notas_mujeres += nota[indice]

# promedio_notas_mujeres = suma_notas_mujeres / cantidad_mujeres

# print(f"{nombre_nota_mas_baja} es que tiene la nota mas baja\nEl promedio de la notas de las mujeres es {promedio_notas_mujeres}")
