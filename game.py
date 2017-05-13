import pygame
from pygame.locals import *
import sys
from waves import wave
from torres import familia
from torres import honestidade
from torres import roquei
from torres import bobeira
from Vida import vida
import importlib

pygame.init()

screen = pygame.display.set_mode((800, 650), 0, 32)
menu = pygame.image.load("img/menu.png").convert_alpha()
tela = pygame.image.load("img/game.jpg").convert_alpha()

pygame.display.set_caption('Defense of mind sad')

clock = pygame.time.Clock()

reiniciar = False
new_wave = 75
w = []
ticks = 22
moves = 1
maximo = []
vida.iniciar_vida()
torre_familia = []
torre_honestidade = []
torre_bobeira = []
torre_amizade = []
torre_roquei = []

def restart():
    global reiniciar
    global new_wave
    global w
    global ticks
    global moves
    global maximo
    reiniciar = False
    new_wave = 75
    w = []
    ticks = 22
    moves = 1
    maximo = []
    wave.zerar_turn()
    vida.iniciar_vida()
    torre_familia = []
    torre_honestidade = []
    torre_bobeira = []
    torre_amizade = []
    torre_roquei = []

def iniciar():
    restart()
    screen = pygame.display.set_mode((800,650),0,32)
    if("menu" in sys.modules):
        importlib.reload(sys.modules["menu"])
    else:
        import menu.py
    screen.fill((0,0,0))
    pygame.display.flip()

def finalizar():
    restart()
    screen = pygame.display.set_mode((800,650),0,32)
    if("gameover" in sys.modules):
        importlib.reload(sys.modules["gameover"])
    else:
        import gameover.py
    screen.fill((0,0,0))
    pygame.display.flip()

while True:
    
    screen.blit(tela, (4, 0))
    screen.blit(menu, (548, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                x,y = pygame.mouse.get_pos()
                print(pygame.mouse.get_pos())
                if ((x > 593 and x < 660) and (y > 175 and y < 230)):
                    print("Roquei")
                    torre_roquei.append(roquei.criar_roquei())
                    for i in range(len(torre_roquei)):
                        if(torre_roquei[i]["img"] == "torres/img/island/roquei.png"):
                            torre_roquei[i]["img"] = pygame.image.load(torre_roquei[i]["img"]).convert_alpha()
                elif((x > 710 and x < 780) and (y > 175 and y < 245)):
                    print("Bobeira")
                elif((x > 593 and x < 660) and (y > 307 and y < 370)):
                    print("Amizade")
                elif((x > 710 and x < 780) and (y > 307 and y < 370)):
                    print("Familia")
                elif((x > 655 and x < 720) and (y > 427 and y < 478)):
                    print("Honestidade")
                elif((x > 613 and x < 749) and (y > 577 and y < 631)):
                    print(True)
                    iniciar()
        elif(evento.type == pygame.MOUSEBUTTONUP):
            if(evento.button == 1):
                for i in range(len(torre_roquei)):
                    torre_roquei[i]["posicionado"] = True
        elif(evento.type == pygame.MOUSEMOTION):
            for i in range(len(torre_roquei)):
                if(torre_roquei[i]["posicionado"] == False):
                    mouse_x, mouse_y = evento.pos
                    torre_roquei[i]["x"] = mouse_x-35
                    torre_roquei[i]["y"] = mouse_y-43
    for i in range(len(torre_roquei)):
        screen.blit(torre_roquei[i]["img"], (torre_roquei[i]["x"], torre_roquei[i]["y"]))
    if(len(w) == 0):
        if(new_wave > 0):
            new_wave -= 1
            cont = 0
            start = 0
            maximo = []
        else:
            wave.criar_wave()
            wave.definir_wave()
            w = wave.get_wave()
            print(wave.turn)
            for i in w:
                maximo.append(len(w[i]))
            cont = 1
            start = 1
            new_wave = 75
    else:
        for i in w:
            x = 150
            y = 200
            for j in w[i]:
                img = pygame.image.load(w[i][j]["img"]).convert_alpha()
                screen.blit(img, (w[i][j]["x"], w[i][j]["y"]))
                x += 10
        for i in range(start, cont):
            for j in w:
                if(w[j][i-1]["x"] <= 130):
                    w[j][i-1]["x"] += w[j][i-1]["velocidade_atual"]
                elif((w[j][i-1]["y"] >= 215) and (w[j][i-1]["x"] <= 252)):
                    w[j][i-1]["y"] -= w[j][i-1]["velocidade_atual"]
                elif(w[j][i-1]["x"] <= 252):
                    w[j][i-1]["x"] += w[j][i-1]["velocidade_atual"]
                elif((w[j][i-1]["y"] >= 94) and (w[j][i-1]["x"] <= 378)):
                    w[j][i-1]["y"] -= w[j][i-1]["velocidade_atual"]
                elif(w[j][i-1]["x"] <= 378):
                    w[j][i-1]["x"] += w[j][i-1]["velocidade_atual"]
                elif(w[j][i-1]["y"] <= 403):
                    w[j][i-1]["y"] += w[j][i-1]["velocidade_atual"]
                elif(w[j][i-1]["x"] <= 456):
                    w[j][i-1]["x"] += w[j][i-1]["velocidade_atual"]
                else:
                    del w[j][i-1]
                    vida.reduzir_vida()
                    vidas = vida.get_vida()
                    print(vidas)
                    if(vidas == 0):
                        print("gameover")
                        finalizar()
                    start += 1
                    if(len(w[j]) == 0):
                        reiniciar = True
        if(reiniciar == True):
            for i in w:
                if(len(w[i]) == 0):
                    del w[i]
                    break
        for i in maximo:
            if(cont <= i):
                if not(ticks):
                    cont += 1
                    ticks = 22
                else:
                    ticks -= 1
    pygame.display.update()
    time_passed = clock.tick(25)
        
