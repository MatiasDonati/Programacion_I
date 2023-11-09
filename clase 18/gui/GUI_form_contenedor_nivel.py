import pygame
from pygame.locals import *

from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_label import Label

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel, color_background):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height())
        nivel._slave = self._slave
        self.nivel = nivel
        self.label_home = Label(self._slave, self._w - 100, self._h - 150, 50, 50,"20%","Comic Sans",15,"White","imagenes/Table.png")
        self._btn_home = Button_Image(screen=self._slave,
                        master_x = self._x,
                        master_y = self._y,
                        x = self._w - 100,
                        y = self._h - 100,
                        w = 50,
                        h = 50,
                        path_image="imagenes/home.png",
                        onclick = self.btn_home_click,
                        onclick_param = "",
                        text = "",
                        font = "Verdana",
                        font_size = 15,
                        color_background = (255,0,0),
                        color_border = (255, 0, 255),
                        border_size = -1
                        )
        self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self.label_home)
        self.lista_widgets.append(self._btn_home)

    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
        self.label_home.set_text(f"Niveles")

    def btn_home_click(self, param):
        self.end_dialog()
