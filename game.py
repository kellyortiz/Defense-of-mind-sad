import pygame
from pygame.locals import *
import sys
from waves import wave
from torres import familia
from torres import honestidade
from torres import roquei
from torres import bobeira
from torres import amizade
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
    screen.fill((255, 255, 255))
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
                    torre_bobeira.append(bobeira.criar_bobeira())
                    for i in range(len(torre_bobeira)):
                        if(torre_bobeira[i]["img"] == "torres/img/island/bobeira.png"):
                            torre_bobeira[i]["img"] = pygame.image.load(torre_bobeira[i]["img"]).convert_alpha()
                elif((x > 593 and x < 660) and (y > 307 and y < 370)):
                    print("Amizade")
                    torre_amizade.append(amizade.criar_amizade())
                    print(torre_amizade)
                    for i in range(len(torre_amizade)):
                        if(torre_amizade[i]["img"] == "torres/img/island/amizade.png"):
                            torre_amizade[i]["img"] = pygame.image.load(torre_amizade[i]["img"]).convert_alpha()
                elif((x > 710 and x < 780) and (y > 307 and y < 370)):
                    print("Familia")
                    torre_familia.append(familia.criar_familia())
                    for i in range(len(torre_familia)):
                        if(torre_familia[i]["img"] == "torres/img/island/familia.png"):
                            torre_familia[i]["img"] = pygame.image.load(torre_familia[i]["img"]).convert_alpha()
                elif((x > 655 and x < 720) and (y > 427 and y < 478)):
                    print("Honestidade")
                    torre_honestidade.append(honestidade.criar_honestidade())
                    for i in range(len(torre_honestidade)):
                        if(torre_honestidade[i]["img"] == "torres/img/island/honestidade.png"):
                            torre_honestidade[i]["img"] = pygame.image.load(torre_honestidade[i]["img"]).convert_alpha()

                elif((x > 613 and x < 749) and (y > 577 and y < 631)):
                    print(True)
                    iniciar()
        elif(evento.type == pygame.MOUSEBUTTONUP):
            if(evento.button == 1):
                for i in range(len(torre_roquei)):
                    torre_roquei[i]["posicionado"] = True
                for i in range(len(torre_bobeira)):
                    torre_bobeira[i]["posicionado"] = True
                for i in range(len(torre_amizade)):
                    torre_amizade[i]["posicionado"] = True
                for i in range(len(torre_familia)):
                    torre_familia[i]["posicionado"] = True
                for i in range(len(torre_honestidade)):
                    torre_honestidade[i]["posicionado"] = True
                
        elif(evento.type == pygame.MOUSEMOTION):
            for i in range(len(torre_roquei)):
                if(torre_roquei[i]["posicionado"] == False):
                    mouse_x, mouse_y = evento.pos
                    torre_roquei[i]["x"] = mouse_x-35
                    torre_roquei[i]["y"] = mouse_y-43
                    pygame.draw.circle(screen, (255, 255, 0), (mouse_x, mouse_y), 100, 2)
            for i in range(len(torre_bobeira)):
                if(torre_bobeira[i]["posicionado"] == False):
                    mouse_x, mouse_y = evento.pos
                    torre_bobeira[i]["x"] = mouse_x-40
                    torre_bobeira[i]["y"] = mouse_y-66
            for i in range(len(torre_amizade)):
                if(torre_amizade[i]["posicionado"] == False):
                    mouse_x, mouse_y = evento.pos
                    torre_amizade[i]["x"] = mouse_x-34
                    torre_amizade[i]["y"] = mouse_y-52
            for i in range(len(torre_familia)):
                if(torre_familia[i]["posicionado"] == False):
                    mouse_x, mouse_y = evento.pos
                    torre_familia[i]["x"] = mouse_x-39
                    torre_familia[i]["y"] = mouse_y-39
            for i in range(len(torre_honestidade)):
                if(torre_honestidade[i]["posicionado"] == False):
                    mouse_x, mouse_y = evento.pos
                    torre_honestidade[i]["x"] = mouse_x-39
                    torre_honestidade[i]["y"] = mouse_y-39

    for i in range(len(torre_roquei)):
        screen.blit(torre_roquei[i]["img"], (torre_roquei[i]["x"], torre_roquei[i]["y"]))
        if(torre_roquei[i]["posicionado"] == False):
            pygame.draw.circle(screen, (255, 255, 0), (torre_roquei[i]["x"]+35, torre_roquei[i]["y"]+43), 100, 2)

    for i in range(len(torre_bobeira)):
        screen.blit(torre_bobeira[i]["img"], (torre_bobeira[i]["x"], torre_bobeira[i]["y"]))

    for i in range(len(torre_amizade)):
        screen.blit(torre_amizade[i]["img"], (torre_amizade[i]["x"], torre_amizade[i]["y"]))

    for i in range(len(torre_familia)):
        screen.blit(torre_familia[i]["img"], (torre_familia[i]["x"], torre_familia[i]["y"]))

    for i in range(len(torre_honestidade)):
        screen.blit(torre_honestidade[i]["img"], (torre_honestidade[i]["x"], torre_honestidade[i]["y"]))

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
        
