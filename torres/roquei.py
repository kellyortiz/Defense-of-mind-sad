from torres import torres

alcance = 0
dano = 0
velocidade = 0
disponivel = 0
tempo = 0
tipoTiro = ""
img = ""
posicionado = False
x = 0
y = 0

def iniciar_torres():
    global alcance
    global dano
    global velocidade
    global disponivel
    global tempo
    global tipoTiro
    global img
    global posicionado
    global x
    global y
    
    alcance = 50
    dano = 2
    velocidade = 2
    disponivel = 2
    tempo = 120
    tipoTiro = "b"
    img = "torres/img/island/roquei.png"
    posicionado = False
    x = 0
    y = 0

def _diminuir_disponibilidade():
    global disponivel
    disponivel -= 1

def criar_roquei():
    _diminuir_disponibilidade()
    torre = torres.criar_torre(alcance, velocidade, tipoTiro, dano, tempo, img, posicionado, x, y)
    return torre

def get_disponibilidade():
    return disponivel

iniciar_torres()
