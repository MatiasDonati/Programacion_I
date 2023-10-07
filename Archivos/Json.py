# # JSON ARCHIVOS
import json

# producto1 = {"descripcion": "coca-cola", "precio":3.5, "stock": 2}
# producto2 = {"descripcion": "pepsi", "precio":2.3, "stock": 9}
# producto3 = {"descripcion": "mirinda", "precio":1.52, "stock": 8}

# lista_productos = [producto1, producto2, producto3]

# data_json = {}
# data_json ["productos"] = lista_productos
# print(data_json)

# with open('productos.json', 'w') as archivo:
#     json.dump(data_json, archivo, indent=4)

with open('productos.json', 'r') as archivo:
    data = json.load(archivo)

for producto in data["productos"]:
    print(producto)

