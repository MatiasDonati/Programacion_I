from data_stark import lista_personajes
from funciones import *

# MATIAS EDUARDO DONATI
# DESAFIO STARK 3



# MENU

# while True:
#         opcion_ingresada = input("Ingrese la opcion elegida: ")
#         while re.match(r"^[0-9]+$", opcion_ingresada) == None:
#             opcion_ingresada = input("La opcion ingresada debe ser un numero entero: ")
#         while opcion_ingresada != '1':
#             opcion_ingresada = input('Debera normalizar los datos para poder continuar\nIngrese la opcion "1": ')
#         opcion_ingresada = int(opcion_ingresada)

#         match opcion_ingresada:
#             case 1:
#                 if flag_normalizar_datos:
#                     flag_normalizar_datos = False
#                     stark_normalizar_datos(lista_personajes)
#                     print('\nDatos Normalizados\n')
#                 else:
#                     print('\nHubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente\n')
#             case 2:
#                 print(obtener_dato(lista_personajes[2]))
#             case 3:
#                 pass
#             case 4:
#                 pass
#             case 5:
#                 pass
#             case 6:
#                 pass
#             case 7:
#                 pass
#             case 8:
#                 pass
#             case 9:
#                 pass
#             case 10:
#                 pass
#             case 11:
#                 pass
#             case 12:
#                 pass
#             case 0:
#                 print('Hasta pronto.')
#                 break