import pygame
from pygame.locals import *

from gui.GUI_button import *
from gui.GUI_slider import *
from gui.GUI_textbox import *
from gui.GUI_label import *
from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_form_menu_score import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()    

        # CONTROLES #

        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray","White","Red","Blue",2, font="Comic Sans", font_size=15, font_color="Black")
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Red","Blue", self.btn_play_click, "Nombre","Pause", font="Comic Sans", font_size=15, font_color="White")
        self.label_volumen = Label(self._slave, 650, 190, 100, 50,"20%","Comic Sans",15,"White","Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100,200,300,15,self.volumen,"Blue", "white")
        self.btn_tabla = Button_Image(self._slave, x, y, 255,100,50,50,"Menu_BTN.png",self.btn_tabla_click, "lalal")
        #

        #Agrego los controles a lista
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        #

        pygame.mixer.music.load("Vengeance (Loopable).wav")

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)

    def btn_play_click(self, texto):
        # print(texto)
        # nombre = self.txtbox.get_text()
        # print(nombre)
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        # self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):
        # print("hola")
        dic_score = [{"Jugador": "Gio", "Score": 1000},
                     {"Jugador": "Fausto", "Score": 900},
                     {"Jugador": "Gonza", "Score": 750}]
        
        form_puntaje = FormMenuScore(self._master,
                                     250,
                                     25,
                                     500,
                                     500,
                                     (220,0,220),
                                     "White",
                                     True,
                                     "Window.png",
                                     dic_score,
                                     100,
                                     10,
                                     10
                                     )
        
        self.show_dialog(form_puntaje)