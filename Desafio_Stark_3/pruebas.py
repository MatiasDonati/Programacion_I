import re

# numero = "1.6"

# numero_sin_decimal = numero.replace(".","")

# print(numero_sin_decimal.isdigit())


# name = "Marina Anabella Cardozo"

# print(re.findall("[a-z]+",name))

# texto = "uno 1 dos 2 tres 3 cuatro 44"

# print(re.findall(" ",texto))
# print(re.findall("[0-9]",texto))
# print(re.findall("[0-9]+",texto))
# print(re.findall("[a-z]",texto))
# print(re.findall("[a-z]+",texto))
# print(re.findall("[a-z]{6}",texto))

# texto = "La fecha de inicio es 2023/09/20 y la fecha de finalización es 2023/09/30."


# '''
#   \s ---> todos los caracteres que representan un espacio
#   \d ---> todos los caracteres que representan los decimales
#   \w ----> alfa numericos

# '''
# print(re.findall("[0-9]{4}/[0-9]{2}/[0-9]{2}",texto))
# print(re.findall("\d{4}/\d{2}/\d{2}",texto)) #te retorna una lista con las ocurrencias encontradas

# print(re.search("[0-9]{4}/[0-9]{2}/[0-9]{2}",texto))

# search_match = re.search("[0-9]{4}/[0-9]{2}/[0-9]{2}",texto) #retorna un obj match

# if search_match != None:
#     print("Si encontro una fecha:", search_match.group())
#     print("Posicion inicio: ", search_match.start())
#     print("Posicion fin: ", search_match.end())
# '''
# ingreso = input("Ingrese edad")

# if re.match('[0-9]+',ingreso) != None:
#     numero_parseado = int(ingreso)
#     print(numero_parseado)
# else:
#     print("hubo un error")
# '''
# otro_texto="hola, todo bien?"

# print(re.split("\s+",otro_texto))#esto retora una lista, separadas por el patron 

# otro_texto_bis = "abc abc ccc ddd abc aaa"

# print(re.sub("abc","",otro_texto_bis))
# print(re.sub("abc","xyz",otro_texto_bis))
# print(re.sub("\s+","",otro_texto_bis))

# valor = 5

# # print(re.match(r'^[0-9]+\.[0-9]+$', valor))
# print(valor.replace(".", "").isdigit())

