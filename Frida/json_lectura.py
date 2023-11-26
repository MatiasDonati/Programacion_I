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

# def leer_json_nivel_tres():
#     with open('configuracion_nivel_tres.json', 'r') as archivo_json:
#         configuracion_nivel_tres = json.load(archivo_json)
#     return configuracion_nivel_tres

# configuracion_nivel_tres = leer_json_nivel_tres()
# # Asignar variables
# titulo_nivel = configuracion_nivel_tres["titulo_nivel"]
# flag_nivel_tres = configuracion_nivel_tres["flag_nivel_tres"]
# flag_segundos_enemigo_final = configuracion_nivel_tres["flag_segundos_enemigo_final"]
# musica_enemigo_final_flag = configuracion_nivel_tres["musica_enemigo_final_flag"]
# flag_sonido_final = configuracion_nivel_tres["flag_sonido_final"]
# segundos = configuracion_nivel_tres["segundos"]
# fin_tiempo = configuracion_nivel_tres["fin_tiempo"]
# flag_sonido = configuracion_nivel_tres["flag_sonido"]
# frida_posicion_inicial = configuracion_nivel_tres["frida_posicion_inicial"]
# frida_vidas = configuracion_nivel_tres["frida_vidas"]
# sonido_risa_fin_nivel_reproducido = configuracion_nivel_tres["sonido_risa_fin_nivel_reproducido"]
# flag_sonido_final = configuracion_nivel_tres["flag_sonido_final"]
# recompensa_flag = configuracion_nivel_tres["recompensa_flag"]
# lista_recompensas = configuracion_nivel_tres["lista_recompensas"]
# enemigos = configuracion_nivel_tres["enemigos"]