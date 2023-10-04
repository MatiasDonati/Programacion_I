import copy

alumno = { "nombre":"Juan", "apellido":"perez", "edad":20,"notas":[85,90,78]}


def obtener_propiedad(diccionario,clave):
    existe = diccionario.get(clave, "La propiedad no existe")
    if existe == "La propiedad no existe":
        print("la clave no existe se agrega")
        diccionario[clave] = ""
    else:
        return diccionario[clave]

def eliminar_propiedad(diccionario,clave):
    if clave in diccionario:
        valor = diccionario.pop(clave)
        print(valor)
    else:
        print("la clave no existe")

def mostrar(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}:{valor}")




mostrar(alumno)
eliminar_propiedad(alumno,"edad")

copia_superficial = copy.copy(alumno)
print("copia sup")
mostrar(copia_superficial)
'''
copia_duda = alumno
print("copia ...")
mostrar(copia_duda)
'''
copia_profunda = copy.deepcopy(alumno)
print("copia profunda")
mostrar(copia_profunda)


copia_superficial["nombre"]= "maria"
copia_superficial["notas"].append(100)

'''
copia_duda["nombre"]= "anabella"
copia_duda["notas"].append(45)
'''
copia_profunda["nombre"]= "renatto"
copia_profunda["notas"].append(98)


print("Diccionario original")
print(alumno)
print(id(alumno["notas"]))
print("diccionario con copy")
print(copia_superficial)
print(id(copia_superficial["notas"]))
'''
print("copia duda")
print(copia_duda)
'''
print("copia profunda")
print(copia_profunda)
print(id(copia_profunda["notas"]))

