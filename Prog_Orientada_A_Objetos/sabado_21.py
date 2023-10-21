
class Alumno:

    def __init__(self, nombre, apellido, edad, materias) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.materias = materias

    @property
    # tiene que tener el nombre de la propiedad
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad == 0:
            print('La edad no puede ser 0!')
        else:
            self.__edad= nueva_edad


    # def set_edad(self, edad_nueva):
    #     self.__edad = edad_nueva

    def mostrar_nombre(self):
        return f"{self.__nombre}, {self.__apellido}"


alumno_uno = Alumno("Matias", "Donati", 36, ["Matematica", "Ingles", "Programacion", "Laboratorio", "Spd"])

alumno_uno.edad = 0
print(alumno_uno.edad)
alumno_uno.edad = 67
print(alumno_uno.edad)


# print(alumno_uno.get_edad()) #llamando al metodo
# print(alumno_uno.edad) #llamando a la propiedad

# print(alumno_uno.edad)
# alumno_uno.set_edad(45)
# print(alumno_uno.edad)

# print(alumno_uno.mostrar_nombre())
# print(alumno_uno.edad)

# print(alumno_uno)
# print(alumno_uno.materias)
# print(alumno_uno.materias[1])
# print(type(alumno_uno.materias))
# print(type(alumno_uno.edad))

# for i in alumno_uno.materias:
#     print(i)



