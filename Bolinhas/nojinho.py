from Bolinhas import bolinhas

hp = 0
velocidade = 0

def criar_nojinho(wave):
    iniciar_velocidade()
    if (wave != 1):
        definir_hp(wave)
    else:
        iniciar_hp()
        
    bolinha = bolinhas.criar_bolinha(hp, velocidade, 'bolinhas/img/balls/desgusting.png')
    return bolinha

def iniciar_hp():
    global hp
    hp = 5

def iniciar_velocidade():
    global velocidade
    velocidade = 3

def definir_hp(wave):
    global hp
    hp = ((wave * 2) + 3)

def get_hp():
    return hp

def set_hp(valor):
    global hp
    hp = valor
    
def diminuir_hp(dano, hpAtual):
    return bolinhas.diminuir_hp(dano, hpAtual)
