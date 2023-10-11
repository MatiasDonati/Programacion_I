# nombre = "hower the larke"

# nuevo = nombre.split('the')

# print(nuevo)

import re

# numero_str = '6'

# if re.search(r'[^0-9-]', numero_str) or numero_str == "":
#     print('Hola')

correo = 'aasd54@asdg.cr'

# if re.search(r'[a-zA-Z0-9]\@[a-zA-Z0-9]\.com', correo) or correo == "":
#     print('Hola')

# patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# if re.match(patron, correo):
#     print(correo)
# else:
#     print('NO')


# patron = r'^[a-z0-9+]+$'

# cadena = "asd+++++asd"
# resultado = re.match(patron, cadena)

# if resultado:
#     print("La cadena cumple con el patrón.")
# else:
#     print("La cadena NONO cumple con el patrón.")

# patron2 = r'^[0-9][A-Z]\.[a-z]+$'
# patron3 = r'^[a-zA-Z0-9]+@[a-z]+\.[com]$'
# patron3 = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[com]$'

# patron3 = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[com]+$'

# patron = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.(com)$'

# patron4 = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'


# prueba = "Matias2@hotmail.cmo"


# if re.match(patron, prueba):
#     print(prueba)
# else:
#     print('No')

# numero =  '32asd'
# patorn = r"([0-9]+)?[a-z]"

# if re.match(patorn, numero):
#     print(numero)

corre0 = "dsdaDSADAS0909@gmail.com"

patron_mail = r'^[a-zA-Z0-9]+@[a-z]+\.[a-z]+$'

if re.match(patron_mail, corre0):
    print(corre0)