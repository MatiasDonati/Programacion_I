#ORDENAMIENTO
import time 

lista = [2,3,5,2,5,6,1,3,2,5,7]
lista_dos = ["vaso", "silla", "cortina","mesa","rueda","pedal","planta","arco","tango","utn"]

print(lista)
print(lista_dos)      


comienzo_tiempo = time.time()
for i in range(len(lista)-1):       
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:           
            aux = lista[i]    
            lista[i] = lista[j]        
            lista[j] = aux
            aux = lista_dos[i]    
            lista_dos[i] = lista_dos[j]        
            lista_dos[j] = aux
        elif lista[i] == lista[j] and lista_dos[i] > lista_dos[j]:
            aux = lista[i]    
            lista[i] = lista[j]        
            lista[j] = aux
            aux = lista_dos[i]    
            lista_dos[i] = lista_dos[j]        
            lista_dos[j] = aux



            

fin_tiempo = time.time()
    
total = fin_tiempo - comienzo_tiempo


print(lista)
print(lista_dos)    
print(total)
