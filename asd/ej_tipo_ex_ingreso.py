import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 
Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.


En el parque de diversiones "Aventuras Extremas", un grupo de amigos ha decidido disfrutar
del día probando las diferentes atracciones y luego se reúnen en un restaurante para compartir
un delicioso almuerzo. Antes de que llegue la cuenta, deciden crear un programa para calcular
y dividir los gastos de manera equitativa. Se pide ingresar los siguientes datos hasta que el
usuario lo desee:

Para cada amigo:

- Nombre del amigo,
- Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
- Cantidad de platos principales pedidos (debe ser al menos 1).
- Bebida elegida ("Refresco", "Agua", "Jugo").
- Cantidad de bebidas pedidas (debe ser al menos 1).

Se conocen los siguientes precios base:
El precio unitario de cada plato principal es de $800.
El precio unitario de cada bebida es de $200.
Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente:
A) El total gastado por el grupo (resultante del costo de los platos principales y las
bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al
10% del total gastado).
B) Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
C) Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad).
Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total
(platos principales + bebidas) con una entrada gratuita para otra atracción del parque
"Aventuras Extremas".
E) REALIZAR DOS PUNTO; EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO
DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO
NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):
0.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos
principales del tipo "Pizza" y mostrar la lista completa por print.
1.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido
platos principales del tipo "Hamburguesa" y mostrar la lista completa por print.
2.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos
principales del tipo "Ensalada" y mostrar la lista completa por print.
3.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas
del tipo "Refresco" y mostrar la lista completa por print.
4.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas
del tipo "Agua" y mostrar la lista completa por print.

5.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
6.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
7.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más
de 7 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
8.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
9.- Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos
de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_de_nombres = ["Juan", "María", "Pedro", "Laura", "Carlos",
        "Ana", "Luis", "Elena", "Miguel", "Sofía"]
        self.lista_plato_principal = ["Pizza", "Hamburguesa", "Ensalada", "Pizza",
        "Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza"]
        self.lista_cantidad_de_platos = [2, 1, 3, 2, 2, 4, 3, 1, 1, 3]
        self.lista_bebidas_elegidas = ["Refresco", "Agua", "Jugo", "Refresco",
        "Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]
        self.lista_cantidad_de_bebidas = [2, 1, 5, 3, 2, 5, 1, 2, 1, 3]

    def btn_cargar_on_click(self):

        for _ in range(4):

            nombre = input('Nombre: ')
            self.lista_de_nombres.append(nombre)

            print(nombre)

            plato = input('Plato Elegido: ').upper()
            while plato != "PIZZA" and plato != "HAMBURGUESA" and plato != "ENSALADA":
                plato = input('Plato Elegido: ').upper()
            self.lista_plato_principal.append(plato)

            print(plato)

            cantidad_de_platos = input('Cantidad de platos: ')
            while int(cantidad_de_platos) < 1:
                cantidad_de_platos = input('Cantidad de platos: ')
            cantidad_de_platos = int(cantidad_de_platos)
            self.lista_cantidad_de_platos.append(cantidad_de_platos)

            print(cantidad_de_platos)

            bebida_elegida = input('Bebida elegida: ').upper()
            while bebida_elegida != "REFRESCO" and bebida_elegida != "AGUA" and bebida_elegida != "JUGO":
                bebida_elegida = input('Bebida elegida: ').upper()
            self.lista_bebidas_elegidas.append(bebida_elegida)

            print(bebida_elegida)

            cantidad_de_bebidas = int(input('Cantidad de Bebidas: '))
            while int(cantidad_de_bebidas) < 1:
                cantidad_de_bebidas = input('Cantidad de Bebidas: ')
            self.lista_cantidad_de_bebidas.append(cantidad_de_bebidas)

            print(cantidad_de_bebidas)


    def btn_mostrar_on_click(self):

        precio_por_plato = 800
        precio_por_bebida = 200
        cantidad_total_de_platos = 0
        cantidad_total_de_bebidas = 0
        suma_gastada_platos = 0
        suma_gastada_bebidas = 0
        suma_plato_mas_bebida = 0
        suma_plato_y_bebida_con_propina_10_porciento = 0
        cantidad_de_jugos = 0
        cantidad_de_refresco = 0
        cantidad_de_agua = 0
        suma_gastada_jugo = 0
        promedio_juego_gral = 0
        cantidad_piza = 0
        cantidad_hamburguesa = 0
        cantidad_ensalada = 0
        mayor_cantidad_de_pedidos = None
        ganador_entrada_gratuita = ""
        lista_eligieron_pizza = []
        lista_eligieron_hamburguesa = []
        lista_eligieron_ensalada = []
        lista_eligieron_refresco = []
        lista_eligieron_agua = []
        lista_hicieron_mas_de_3_pedidos = []
        lista_hicieron_mas_de_5_pedidos = []
        lista_hicieron_mas_de_7_pedidos = []
        lista_hicieron_menos_de_3_pedidos = []
        lista_hicieron_menos_de_5_pedidos = []


        for indice in range(len(self.lista_de_nombres)):

            cantidad_total_de_platos += self.lista_cantidad_de_platos[indice]
            cantidad_total_de_bebidas += self.lista_cantidad_de_bebidas[indice]

            if self.lista_bebidas_elegidas[indice] == "Jugo":
                cantidad_de_jugos += 1
            elif self.lista_bebidas_elegidas[indice] == "Refresco":
                lista_eligieron_refresco.append(self.lista_de_nombres[indice])
                cantidad_de_refresco += 1
            else:
                lista_eligieron_agua.append(self.lista_de_nombres[indice])
                cantidad_de_agua += 1

            match self.lista_plato_principal[indice]:
                case "Pizza":
                   lista_eligieron_pizza.append(self.lista_de_nombres[indice])
                   cantidad_piza += self.lista_cantidad_de_platos[indice]
                case "Hamburguesa":
                    lista_eligieron_hamburguesa.append(self.lista_de_nombres[indice])
                    cantidad_hamburguesa += self.lista_cantidad_de_platos[indice]
                case _:
                    lista_eligieron_ensalada.append(self.lista_de_nombres[indice])
                    cantidad_ensalada += self.lista_cantidad_de_platos[indice]

            if mayor_cantidad_de_pedidos == None or mayor_cantidad_de_pedidos < (self.lista_cantidad_de_bebidas[indice] + self.lista_cantidad_de_platos[indice]):
                mayor_cantidad_de_pedidos = self.lista_cantidad_de_bebidas[indice] + self.lista_cantidad_de_platos[indice]
                ganador_entrada_gratuita = self.lista_de_nombres[indice]

            if self.lista_cantidad_de_bebidas[indice] + self.lista_cantidad_de_platos[indice] > 3:
                lista_hicieron_mas_de_3_pedidos.append(self.lista_de_nombres[indice])

            if self.lista_cantidad_de_bebidas[indice] + self.lista_cantidad_de_platos[indice] > 5:
                lista_hicieron_mas_de_5_pedidos.append(self.lista_de_nombres[indice])

            if self.lista_cantidad_de_bebidas[indice] + self.lista_cantidad_de_platos[indice] > 7:
                lista_hicieron_mas_de_7_pedidos.append(self.lista_de_nombres[indice])

            if self.lista_cantidad_de_bebidas[indice] + self.lista_cantidad_de_platos[indice] < 3:
                lista_hicieron_menos_de_3_pedidos.append(self.lista_de_nombres[indice])

            if self.lista_cantidad_de_bebidas[indice] + self.lista_cantidad_de_platos[indice] < 5:
                lista_hicieron_menos_de_5_pedidos.append(self.lista_de_nombres[indice])

        # A
        suma_gastada_platos = cantidad_total_de_platos * precio_por_plato
        suma_gastada_bebidas = cantidad_total_de_bebidas * precio_por_bebida
        suma_plato_mas_bebida = suma_gastada_platos + suma_gastada_bebidas
        suma_plato_y_bebida_con_propina_10_porciento = suma_plato_mas_bebida + suma_plato_mas_bebida * 0.1
        print(+suma_plato_y_bebida_con_propina_10_porciento)

        # B
        suma_gastada_jugo = cantidad_de_jugos * precio_por_bebida
        promedio_juego_gral = suma_gastada_jugo / len(self.lista_de_nombres)
        print(promedio_juego_gral)

        # C
        porcentaje_pizza = (cantidad_piza / cantidad_total_de_platos) * 100
        porcentaje_hamburguesa = (cantidad_hamburguesa / cantidad_total_de_platos) * 100
        porcentaje_ensalada = (cantidad_ensalada / cantidad_total_de_platos) * 100

        print(porcentaje_pizza)
        print(porcentaje_hamburguesa)
        print(porcentaje_ensalada)

        #D
        print(ganador_entrada_gratuita)

        # 0
        print(lista_eligieron_pizza)
        # 1
        print(lista_eligieron_hamburguesa)
        # 2
        print(lista_eligieron_ensalada)
        # 3
        print(lista_eligieron_refresco)
        # 4
        print(lista_eligieron_agua)
        # 5
        print(lista_hicieron_mas_de_3_pedidos)
        # 6
        print(lista_hicieron_mas_de_5_pedidos)
        # 7
        print(lista_hicieron_mas_de_7_pedidos)
        # 8
        print(lista_hicieron_menos_de_3_pedidos)
        # 9
        print(lista_hicieron_menos_de_5_pedidos)

if __name__ == "__main__":
    app = App()
    app.mainloop()


# print()
# input("aca ingreso el mensaje")