from configuraciones import *
 
class Personaje:
    def __init__(self, animaciones, pos_x, pos_y, tamaño:tuple, velocidad, direccion) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, tamaño)
        self.rectangulo = pygame.Rect(pos_x, pos_y, *tamaño)
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.velocidad = velocidad
        self.turbo = False
        self.turbo_velocidad = 20
        self.direccion = direccion
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones[self.direccion]
        self.gravedad = 1
        self.desplazamiento_y = 0
        self.potencia_salto = -10
        self.limite_velocidad_salto = 10
        self.esta_saltando = False

    def aplicar_gravedad(self, pantalla, piso):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

            if self.rectangulo.colliderect(piso):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.rectangulo.bottom = piso.top

    def desplazar(self):
        velocidad_actual = self.velocidad
        if self.turbo:
            velocidad_actual = self.turbo_velocidad
        if self.direccion == 'izquierda':
            velocidad_actual *= -1

        limite_izquierdo = 0
        #hacer dinamino el valor de pantalla ordenandolo en una variable, quiza un archivo de constantes
        limite_derecho = 1200 - self.rectangulo.width

        self.rectangulo.x += velocidad_actual

        if self.rectangulo.x < limite_izquierdo:
            self.rectangulo.x = limite_izquierdo
        elif self.rectangulo.x > limite_derecho:
            self.rectangulo.x = limite_derecho

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1

    def actualizar (self, pantalla, piso):

            match self.direccion:
                case 'derecha':
                    if not self.esta_saltando:
                        self.animacion_actual = self.animaciones['derecha']
                        self.animar(pantalla)
                    self.desplazar()
                case 'izquierda':
                    if not self.esta_saltando:
                        self.animacion_actual = self.animaciones['izquierda']
                        self.animar(pantalla)
                    self.desplazar()
                case 'quieto':
                    if not self.esta_saltando:
                        self.animacion_actual = self.animaciones['quieto']
                        self.animar(pantalla)
                case 'salta':
                    if not self.esta_saltando:
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
                        self.animacion_actual = self.animaciones['salta']

            self.aplicar_gravedad(pantalla, piso)

    def presionar_tecla(self, lista_eventos):
        self.direccion = 'quieto'

        if lista_eventos[pygame.K_RIGHT]:
            self.direccion = 'derecha'
        if lista_eventos[pygame.K_LEFT]:
            self.direccion = 'izquierda'
        if lista_eventos[pygame.K_UP]:
            self.direccion = 'salta'
        if lista_eventos[pygame.K_LSHIFT]:
            self.turbo = True
        else:
            self.turbo = False

