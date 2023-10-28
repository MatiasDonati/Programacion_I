# Error de sintaxis
# Error de casteo/parseo/logica

def calcular_promedio(cantidad_examenes):
    nota_uno = 0
    nota_dos = 10
    nota_tres = 2

    notas_sumadas = nota_uno + nota_dos + nota_tres

    if cantidad_examenes != 0 and type(cantidad_examenes) == int:
        promedio = notas_sumadas / cantidad_examenes #nunca puede ser cero

    return promedio

# Modo de prueba ... excusa para ver try except
try:
    ingresa_numero = int(input("Ingrese cantidad de examenes"))#esto debe solucionarse con expresion regularw
    print(calcular_promedio(ingresa_numero))
except:
    print('Hubo un error')

print('Mi programa continua')

