import pygame
from pygame.locals import *

from gui.GUI_button_image import *
from gui.GUI_form import *
from gui.GUI_form_contenedor_nivel import *
from niveles2.manejador_niveles import Manejador_niveles

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image):
        super().__init__(screen, x,y,w,h,color_background,color_border,active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self.slave = aux_image

        self._btn_level_1 = Button_Image(screen=self._slave,
                        x = 100,
                        y = 100,
                        master_x = x,
                        master_y = y,
                        w = 100,
                        h = 150,
                        color_background = (255,0,0),
                        color_border = (255, 0, 255),
                        onclick = self.entrar_nivel,
                        onclick_param = "nivel_uno",
                        path_image="imagenes/1.png")
        self._btn_level_2 = Button_Image(screen=self._slave,
                        x = 250,
                        y = 100,
                        master_x = x,
                        master_y = y,
                        w = 100,
                        h = 150,
                        color_background = (255,0,0),
                        color_border = (255, 0, 255),
                        onclick = self.entrar_nivel,
                        onclick_param = "nivel_dos",
                        path_image="imagenes/2.png")
        self._btn_level_3 = Button_Image(screen=self._slave,
                        x = 100,
                        y = 250,
                        master_x = x,
                        master_y = y,
                        w = 100,
                        h = 150,
                        color_background = (255,0,0),
                        color_border = (255, 0, 255),
                        onclick = self.entrar_nivel,
                        text = "",
                        font = "Verdana",
                        font_size = 15,
                        onclick_param = "nivel_tres",
                        path_image="imagenes/3.png")
        
        self._btn_home = Button_Image(screen=self._slave,
                        x = 400,
                        y = 400,
                        master_x = x,
                        master_y = y,
                        w = 50,
                        h = 50,
                        color_background = (255,0,0),
                        color_border = (255, 0, 255),
                        onclick = self.btn_home_click,
                        onclick_param = "",
                        path_image="imagenes/home.png")

        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
    
    def on(self, parametro):
        print("hola", parametro)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        frm_contenedor_nivel = FormContenedorNivel(self._master, nivel, (255,0,0))
        self.show_dialog(frm_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()