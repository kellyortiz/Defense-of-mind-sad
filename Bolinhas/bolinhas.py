
def criar_bolinha(hp, velocidade, img):
    bolinha = {"hp_total":hp, "hp_atual":hp, "velocidade_padrao":velocidade, "velocidade_atual":velocidade, "x": 80, "y": 450, "img": img}
    
    return bolinha


def diminuir_hp(dano, hpAtual):
    hpAtual -= dano
    return hpAtual

