import pygame
from pygame.locals import *

from gui.GUI_checkbox import *
from gui.GUI_button import *
from gui.GUI_form_menu_play import *
from gui.GUI_picture_box import *
from gui.GUI_slider import *
from gui.GUI_textbox import *
from gui.GUI_label import *
from gui.GUI_form import *
from gui.GUI_button_image import *
from gui.GUI_form_menu_score import *

class FormPrincipal(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()    

        # CONTROLES #

        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray","White","Red","Blue",2, font="Comic Sans", font_size=15, font_color="Black")
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Red","Blue", self.btn_play_click, "Nombre","Pause", font="Comic Sans", font_size=15, font_color="White")
        self.slider_volumen = Slider(self._slave, x, y, 100,200,500,15,self.volumen,"Blue", "White")
        self.label_volumen = Label(self._slave, 650, 190, 100, 50,"20%","Comic Sans",15,"White","imagenes/Table.png")
        self.checkbox = CheckBox(self._slave, x, y, 100, 230, 50, 50, "imagenes/on.png", "imagenes/off.png")       
        self.picture_box = PictureBox(self._slave, 300, 230, 100, 50, "imagenes/imagen.jpg")

        self.btn_tabla = Button_Image(self._slave, x, y, 225, 100, 50, 50, "imagenes/Menu_BTN.png", self.btn_tabla_click, "")
        self.btn_jugar = Button_Image(self._slave, x, y, 300, 100, 50, 50, "imagenes/Play.png", self.btn_jugar_click, "a")
        #

        #Agrego los controles a lista
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.checkbox)
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_jugar)
        #

        pygame.mixer.music.load("sounds/Vengeance (Loopable).wav")

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

                if self.checkbox.get_esta_prendido():
                    self._color_background = "Red"
                else:
                    self._color_background = "#898ac0"

        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)

    

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        # self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_jugar_click(self, param):
        frm_jugar = FormMenuPlay(screen=self._master,
                    x = self._master.get_width() / 2 - 250,
                    y = self._master.get_height() / 2 - 250,
                    w = 500,
                    h = 500,
                    color_background = (220,0,220),
                    color_border = (255,255,255),
                    active = True,path_image="imagenes/Window.png")
        self.show_dialog(frm_jugar)

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
                                     "imagenes/Window.png",
                                     dic_score,
                                     100,
                                     10,
                                     10
                                     )
        
        self.show_dialog(form_puntaje)

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