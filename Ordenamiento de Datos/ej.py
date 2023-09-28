
lista_numeros = [8, 5, 1, 4, 6, 9, 2, 10, 3, 7]




for i in range(len(lista_numeros)):
    for j in range(i+1, len(lista_numeros)):
        if lista_numeros[i] > lista_numeros[j]:
            aux = lista_numeros[i]
            lista_numeros[i] = lista_numeros[j]
            lista_numeros[j] = aux

print(lista_numeros)





# for i in range(len(lista_numeros)-1):
   
#     for j in range(i+1, len(lista_numeros)):
#         if lista_numeros[i] > lista_numeros[j]:
#             aux = lista_numeros[i]
#             lista_numeros[i] = lista_numeros[j]
#             lista_numeros[j] = aux
# print(lista_numeros)






# #Bubble Sort ordenamiento de burbuja

# lista = [2,5,3,1,6,4]
# print("Lista desordenada")
# print (lista)    

# for i in range(len(lista)-1):
#     for j in range(i+1, len(lista)):
#         if(lista[i] > lista[j]):
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux
# print("Lista ordenada")
# print (lista)    



# #Ahora que haya swap solo cuando se tenga que ordenar
# #Bubble  sort  (improved) ordenamiento de burbuja mejorado 
# lista = [2,5,3,1,6,4]
# print("Lista desordenada")
# print (lista)

# flag_swap = True

# while flag_swap == True:
#     flag_swap = False 
#     for i in range(len(lista)-1):
#         if(lista[i] > lista[i+1]):
#             aux = lista[i]
#             lista[i] = lista[i+1]
#             lista[i+1] = aux
#             flag_swap = True 
# # va a ser un bucle infinito hasta que diga que la bandera sea false, como lo recorre por primera vez
# #en el for y lo recorre hasta que se termine, en algun momento va a entrar al if y levanta la bandera.
# #Recorres todo el for antes de salir.
# print("Lista ordenada")
# print (lista)    

