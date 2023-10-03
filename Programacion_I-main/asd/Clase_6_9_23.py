lista_empleados = []

for _ in range(3):
    dic_empleados = {}
    nombre = input('nombre: ')
    apellido = input('apellido: ')
    edad = input("edad: ")
    dic_empleados['nombre'] = nombre
    dic_empleados['apellido'] = apellido
    dic_empleados['edad'] = edad
    lista_empleados.append(dic_empleados)

for indice in range(len(lista_empleados)):
   print(lista_empleados[indice])