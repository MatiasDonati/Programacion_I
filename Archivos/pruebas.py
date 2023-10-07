lista = ["Pepe", "Juan", "Maria"]

with open("mi_archivo_prueba.txt","w") as archivo:
    for iter in lista:
        archivo.write(f"{iter}\n")


archivo = open("mi_archivo_prueba.txt","r")
lista = archivo.readlines()
lista2 = [2, 3]


with open("mi_archivo_prueba.txt","r") as archivo:
    for nombre in archivo:
        lista2.append(nombre)

print(lista2)




