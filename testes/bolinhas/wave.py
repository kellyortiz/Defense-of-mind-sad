from bolinhas import nojinho
from bolinhas import medo
from bolinhas import raiva
from bolinhas import tristeza
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
        qtde_bolinhas = 12
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
        sentimento = "medo"
        qtde_bolinhas = 4
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
    elif(turn == 2):
        sentimento = "medo"
        qtde_bolinhas = 12
        nw = {sentimento: qtde_bolinhas}
        new_wave.update(nw)
        sentimento = "raiva"
        qtde_bolinhas = 4
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

def _definir_qtde_sentimentos():
    i = random.randint(1, 4)
    opcoes = ("nojinho", "medo", "raiva", "tristeza")
    sentimentos = []
    for j in range(i):
        sentimentos.append(opcoes[j])
    return sentimentos

def _definir_total_bolinhas():
    s = _definir_qtde_sentimentos()
    bolinhas = {}
    for i in s:
        b = {i: random.randint(10, turn*(random.randint(10, 20)))}
        bolinhas.update(b)
    return bolinhas

def iniciar_wave():
    for i in waves:
        print(waves)
