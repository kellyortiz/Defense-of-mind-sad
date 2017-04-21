vida = 30
vidaAtual = 1
def iniciar_vida():
    global vida
    vida = 30
    
def reduzir_vida():
    global vida
    vida -= vidaAtual

def get_vida():
    return vida

def set_vida(life):
    global vida
    vidaAtual = life
    vida = life

