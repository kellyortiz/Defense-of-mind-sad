from Bolinhas import nojinho
from Bolinhas import medo
from Bolinhas import raiva
from Bolinhas import tristeza
import random

waves = {}
new_wave = {}
turn = 0

def criar_wave():
    global new_wave
    remover_waves()
    if(turn == 0):
        sentimento = "nojinho"
        qtde_bolinhas = 10
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
    elif(turn == 1):
        sentimento = "nojinho"
        qtde_bolinhas = 16
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
    elif(turn == 2):
        sentimento = "medo"
        qtde_bolinhas = 14
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
    elif(turn == 3):
        sentimento = "raiva"
        qtde_bolinhas = 10
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
    elif(turn == 4):
        sentimento = "medo"
        qtde_bolinhas = 20
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
    elif(turn == 5):
        sentimento = "tristeza"
        qtde_bolinhas = 6
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
    else:
        sentimentos = _definir_total_bolinhas()
        for i in sentimentos:
            bolinhas = {i: sentimentos[i]}
            new_wave.update(bolinhas)
    _aumentar_turn()
    waves.update(new_wave)


def definir_wave():
    global new_wave
    new_wave = {}
    for sentimento in waves:
        if(sentimento == "nojinho"):
            for i in range(waves[sentimento]):
                bolinha = {i:nojinho.criar_nojinho(turn)}
                new_wave.update(bolinha)
        elif(sentimento == "medo"):
            for i in range(waves[sentimento]):
                bolinha = {i:medo.criar_medo(turn)}
                new_wave.update(bolinha)
        elif(sentimento == "raiva"):
            for i in range(waves[sentimento]):
                bolinha = {i:raiva.criar_raiva(turn)}
                new_wave.update(bolinha)
        else:
            for i in range(waves[sentimento]):
                bolinha = {i:tristeza.criar_tristeza(turn)}
                new_wave.update(bolinha)
        waves[sentimento] = new_wave
    

def diminuir_wave(indice):
    if(indice in waves["nojinho"]):
        del(waves["nojinho"][indice])

def get_wave():
    return waves


def remover_waves():
    global waves
    global new_wave
    global turn
    waves = {}
    new_wave = {}

def _aumentar_turn():
    global turn
    turn +=1

def zerar_turn():
    global turn
    turn = 0

def _definir_sentimento():
    i = random.randint(0, 3)
    opcoes = ("nojinho", "medo", "raiva", "tristeza")
    sentimento = opcoes[i]
    return sentimento

def _definir_total_bolinhas():
    s = _definir_sentimento()
    bolinhas = {}
    b = {s: random.randint(10, turn*5)}
    bolinhas.update(b)
    return bolinhas

def iniciar_wave():
    for i in waves:
        print(waves)
