pontuacao = 0

def iniciar_pontuacao():
    global pontuacao
    pontuacao = 0

def iniciar_ponto():
    global pontuacao
    pontuacao = 0

def aumentar_pontuacao(ponto):
    pontuacao += ponto

def get_pontuacao():
    return pontuacao

def set_pontuacao(ponto):
    global pontuacao
    pontuacao = ponto
    
