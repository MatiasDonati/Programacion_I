# descripciones = ["coca-cola", "pepsi", "mirinda"]
# precios = [799.82, 642.21, 605.66]
# stock = [5, 4, 8]

# with open("productos.csv", "w") as archivo:
#     for i in range(len(descripciones)):
#         producto_str = f"{descripciones[i]},{precios[i]},{stock[i]}\n"
#         archivo.write(producto_str)

import re

def parser_proodcutos(path:str)->list:

    lista = []

    with open(path, "r") as archivo:
        for linea in archivo:
            registro = re.split(',|\n', linea)
            producto = {}
            producto["descripcion"] = registro[0]
            producto["precio"] = float(registro[1])
            producto["stock"] = int(registro[2])
            lista.append(producto)

    return lista

lista = parser_proodcutos("productos.csv")

for producto in lista:
    print(f"{producto['descripcion']:15} {producto['precio']:15} {producto['stock']:15}")

acum = 0

for num in lista:
    acum += num['precio']

print(acum)

