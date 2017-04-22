import tristeza
import random

waves = {}
new_wave = {}
turn = 0

def criar_wave():
    if(turn == 0):
        sentimento = "tristeza"
        qtde_bolinhas = 10
        new_wave = {sentimento: qtde_bolinhas}
    waves.update(new_wave)


def definir_wave(sentimento):
    global new_wave
    new_wave = {}
    if (sentimento in waves):
        for i in range(waves[sentimento]):
            bolinha = {i:tristeza.criar_tristeza(1)}
            new_wave.update(bolinha)
        waves[sentimento] = new_wave
    

def diminuir_wave(indice):
    if(indice in waves["tristeza"]):
        del(waves["tristeza"][indice])

def get_wave(sentimento, indice):
    if(sentimento in waves):
        if(indice in waves[sentimento]):
            return waves[sentimento][indice]
    return None

def iniciar_wave():
    pass


def remover_waves():
    global waves
    global new_wave
    global turn
    waves = {}
    new_wave = {}
    turn = 0
