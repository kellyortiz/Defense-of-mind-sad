def criar_bolinha(hp, velocidade):
    bolinha = {"hp_total":hp, "hp_atual":hp, "velocidade_padrao":velocidade, "velocidade_atual":velocidade}
    return bolinha


def diminuir_hp(dano, hpAtual):
    hpAtual -= dano
    return hpAtual

