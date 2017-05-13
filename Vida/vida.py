vida = 0

def iniciar_vida():
    global vida
    vida = 30
    
def reduzir_vida():
    global vida
    vida -= 1

def get_vida():
    return vida

def set_vida(life):
    global vida
    vida = life

