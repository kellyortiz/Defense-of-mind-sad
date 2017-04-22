pontuacao = 0
ponto = 0

def iniciar_pontuacao():
    global pontuacao
    pontuacao = 0

def iniciar_ponto():
    global ponto
    ponto = 0

def aumentar_pontuacao(ponto):
    pontuacao += ponto

def get_pontuacao():
    return pontuacao

def set_pontuacao(ponto):
    global pontuacao
    pontos = ponto
    pontuacao = ponto
    
