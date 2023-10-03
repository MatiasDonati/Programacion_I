import time

lista = []

for i in range(0,20000):
    if i%2 == 0:
        lista.append(i+5)
    else:
        lista.append(i*3)
        
unaLista= lista
comienzo_tiempo = time.time()
def ordenamientoBurbujaCorto(unaLista):
    intercambios = True
    numPasada = len(unaLista)-1
    
    while numPasada > 0 and intercambios:
       intercambios = False
       
       for i in range(numPasada):
           if unaLista[i]>unaLista[i+1]:
               intercambios = True
               temp = unaLista[i]
               unaLista[i] = unaLista[i+1]
               unaLista[i+1] = temp
       numPasada = numPasada-1

ordenamientoBurbujaCorto(unaLista)
fin_tiempo = time.time()
total = fin_tiempo - comienzo_tiempo
print(unaLista)
print(total)

