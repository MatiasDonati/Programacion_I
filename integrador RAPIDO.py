# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:

# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.
# Se debe informar lo siguient e:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.


# lista_tipo = []
# lista_precio = []
# lista_cantidad = []
# lista_fabricante = []
# lista_marca = []

# for _ in range(5):

#     tipo = input('Tipo: ')
#     while tipo != "barbijo" and tipo != "jabón" and tipo != "alcohol":
#         tipo = input('Tipo: ')
#     lista_tipo.append(tipo)

#     precio = input('Precio: ')
#     while int(precio) < 100 or int(precio) > 300:
#         precio = input('Precio: ')
#     precio = int(precio)
#     lista_precio.append(precio)

#     cantidad = input('Canitdad: ')
#     while int(cantidad) <= 0 or int(cantidad) > 1000:
#         cantidad = input('Canitdad: ')
#     cantidad = int(cantidad)
#     lista_cantidad.append(cantidad)

#     marca = input('Marca: ')
#     while marca == None:
#         marca = input('Marca: ')
#     lista_marca.append(marca)

#     fabricante = input('Fabricante: ')
#     while fabricante == None:
#         fabricante = input('Fabricante: ')
#     lista_fabricante.append(fabricante)

lista_tipo = ["barbijo", "jabón", "alcohol", "jabón", "alcohol"]
lista_precio = [150, 200, 250, 180, 220]
lista_cantidad = [500, 1000, 750, 800, 600]
lista_fabricante = ["Fabricante1", "Fabricante2", "Fabricante3", "Fabricante4", "Fabricante5"]
lista_marca = ["MarcaA", "MarcaB", "MarcaC", "MarcaD", "MarcaE"]

barbijo_mas_caro = None
cantidad_barbijos_mas_caro = 0
fabricante_barbijos_mas_caros = ""
mayor_cantidad = None
suma_jabones = 0

for indice in range (len(lista_tipo)):
    # A
    if lista_tipo[indice] == "barbijo":
        if barbijo_mas_caro == None or lista_precio[indice] > barbijo_mas_caro:
            barbijo_mas_caro = lista_precio[indice]
            cantidad_barbijos_mas_caro += lista_cantidad[indice]
            fabricante_barbijos_mas_caros = lista_fabricante[indice]
    # C
    elif lista_tipo[indice] == "jabón":
        suma_jabones += lista_cantidad[indice]
    # B
    if mayor_cantidad == None or lista_cantidad[indice] > mayor_cantidad:
        mayor_cantidad = lista_cantidad[indice]
        fabricante_mayor_cantidad = lista_fabricante[indice]


print(f"A - Del mas caro de los barbijos, son {cantidad_barbijos_mas_caro} cantidad y de {fabricante_barbijos_mas_caros}\nB - El fabricante del item con mas unidades es {fabricante_mayor_cantidad}\nC - En total hay {suma_jabones} jabones")