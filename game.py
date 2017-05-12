import pygame
from pygame.locals import *
from sys import exit
from waves import wave
from torres import familia
from torres import honestidade
from torres import roquei
from torres import bobeira

def remover_wave(index):
    global w
    del w[index]

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
while True:
    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if ((x > 593 and x < 660) and (y > 175 and y < 230)):
                        print("Roquei")
                    elif((x > 710 and x < 780) and (y > 175 and y < 245)):
                        print("Bobeira")
                    elif((x > 593 and x < 660) and (y > 307 and y < 370)):
                        print("Amizade")
                    elif((x > 710 and x < 780) and (y > 307 and y < 370)):
                        print("Familia")
                    elif((x > 655 and x < 720) and (y > 427 and y < 478)):
                        print("Honestidade")

    screen.blit(tela, (4, 0))
    
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
    screen.blit(menu, (548, 0))
    pygame.display.update()
    time_passed = clock.tick(25)
