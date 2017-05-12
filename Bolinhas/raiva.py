from Bolinhas import bolinhas

hp = 0
velocidade = 0

def criar_raiva(wave):
    iniciar_hp()
    iniciar_velocidade()
    if (wave != 1):
        definir_hp(wave)
    bolinha = bolinhas.criar_bolinha(hp, velocidade, "bolinhas/img/balls/raiva.png")
    return bolinha

def iniciar_hp():
    global hp
    hp = 10

def iniciar_velocidade():
    global velocidade
    velocidade = 4

def definir_hp(wave):
    global hp
    hp = ((wave * 2) + 10)

def get_hp():
    return hp

def set_hp(valor):
    global hp
    hp = valor
    
def diminuir_hp(dano, hpAtual):
    return bolinhas.diminuir_hp(dano, hpAtual)
