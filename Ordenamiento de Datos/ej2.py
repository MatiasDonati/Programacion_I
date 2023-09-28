#ORDENAMIENTO
import time 
lista = []

for i in range(0,20000):
    if i%2 == 0:
        lista.append(i+5)
    else:
        lista.append(i*3)
        
lista_numeros = lista

comienzo_tiempo = time.time()
for i in range(len(lista_numeros)-1):
    
    #j = i + 1
    for j in range(i+1, len(lista_numeros)):
        if lista_numeros[i] > lista_numeros[j]:
            #-          8
            aux = lista_numeros[i]
            #8          8
            lista_numeros[i] = lista_numeros[j]
            #5                      5
            lista_numeros[j] = aux
            #8                  8

fin_tiempo = time.time()
    
total = fin_tiempo - comienzo_tiempo

print(lista_numeros)
print(total)