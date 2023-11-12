#PARA TENER MODO RECTANGULOS DE LOS PERSONAJES

DEBUG = False

#la cambia a false o true
def cambiar_modo():
    global DEBUG
    DEBUG = not DEBUG

def obtener_modo():
    return DEBUG