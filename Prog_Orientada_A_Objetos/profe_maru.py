class Persona:
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #Este metodo es de la clase padre
    def mostrar_nombre(self):
        return f"{self._nombre}, {self._apellido}"

class Alumno(Persona):

    def __init__(self,nombre,apellido,edad,materias):
        super().__init__(nombre,apellido,edad)
        self.materias = materias
        self.notas = 0



    '''
    def get_edad(self):
        return self.__edad

    def set_edad(self,edad_nueva):
        self.__edad = edad_nueva
    '''

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,nueva_edad):
        if nueva_edad < 0:
            print("Che una edad no puede ser cero!!!")
        else:
            self._edad = nueva_edad



class Docente(Persona):

    def __init__(self,nombre,apellido,edad,catedra):
        super().__init__(nombre,apellido,edad)
        self.__catedra = catedra


    def cobrar_sueldo(self):
        pass

    def tomar_examen(self):
        pass


alumno_uno = Alumno("Marina","Cardozo",22,["Programacion"])
profe = Docente("German","Scarafilo",25,"Programacion")


print(alumno_uno)
print(alumno_uno.mostrar_nombre())
print(alumno_uno.materias)

print("Edad!")

#print(alumno_uno.get_edad()) esto seria llamando al metodo
print(alumno_uno.edad) #esto seria llamando a la propiedad

print("modificacion")

alumno_uno.edad = 35
print(alumno_uno.edad)



lista_universidad = []

lista_universidad.append(alumno_uno)
lista_universidad.append(profe)

for item in lista_universidad:
    print(item.mostrar_nombre())


