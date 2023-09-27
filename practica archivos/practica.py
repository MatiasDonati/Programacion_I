import json
import re

def parse_json_stark(path:str)->list:

    archivo = open(path, 'r')
    dic_json = json.load(archivo)
    archivo.close()
    return dic_json['heroes']


lista_heroes = parse_json_stark('/Users/matiasdonati/Documents/UTN/Programacion_y_Laboratorio/Programacion/Programacion_I/DesafioStark4/data_stark.json')
# lista_heroes = parse_json_stark('DesafioStark4/data_stark.json')
print(lista_heroes)

def guardar_csv_stark(path:str, lista:list):

    archivo = open(path, 'w')
    for heroe in lista:
        # Se podria hacer con un for
        linea = f"{heroe['nombre']}, {heroe['identidad']}, {heroe['empresa']}, {heroe['altura']}, {heroe['peso']}, {heroe['genero']}, {heroe['color_ojos']}, {heroe['color_pelo']}, {heroe['fuerza']}, {heroe['inteligencia']}\n"
        archivo.write(linea)
    archivo.close()

guardar_csv_stark('sabado_16', lista_heroes)


def parse_csv_stark(path:str)->list:

    with open(path, 'r') as archivo:
        lista_heroes = []

        for linea in archivo:
            heroe = {}
            lista = linea.split(',')
            heroe['nombre'] = lista[0]
            heroe['identidad'] = lista[1]
            heroe['empresa'] = lista[2]
            heroe['altura'] = lista[3]
            heroe['peso'] = lista[4]
            heroe['genero'] = lista[5]
            heroe['color_ojos'] = lista[6]
            heroe['color_pelo'] = lista[7]
            heroe['fuerza'] = lista[8]
            heroe['inteligencia'] = re.sub('\n','',lista[9])
            lista_heroes.append(heroe)

    return lista_heroes

lista_heroes2 = parse_csv_stark('archivo.csv')
print(lista_heroes2)
