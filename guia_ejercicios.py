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




# print()
# input("aca ingreso el mensaje")