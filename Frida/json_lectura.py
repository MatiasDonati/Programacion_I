import json
import re

def leer_json():
    with open('inicializacion.json', 'r') as archivo_json:
        configuracion = json.load(archivo_json)
    return configuracion

configuracion = leer_json()

ingreso_nombre = configuracion["ingreso_nombre"]
patron_usuario = re.compile(configuracion["patron_usuario"])
flag_cargar_usuario = configuracion["flag_cargar_usuario"]
segundos = configuracion["segundos"]
fin_tiempo = configuracion["fin_tiempo"]
flag_sonido = configuracion["flag_sonido"]
volumen = configuracion["volumen"]
sonido_risa_fin_nivel_reproducido = configuracion["sonido_risa_fin_nivel_reproducido"]
tiempo_inicio_if = configuracion["tiempo_inicio_if"]
enemigo_final_en_accion = configuracion["enemigo_final_en_accion"]
pantalla_final_perdido = configuracion["pantalla_final_perdido"]
se_rio = configuracion["se_rio"]


ruta_gotica = configuracion["ruta_gotica"]
intro = configuracion["intro"]
se_rio_nueva = configuracion["se_rio"]
flag_run = configuracion["flag_run"]
y_incremento = configuracion["y_incremento"]
flag_final = configuracion["flag_final"]
flag_mensaje_w = configuracion["flag_mensaje_w"]

