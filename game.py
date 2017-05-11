import pygame
from pygame.locals import *
from sys import exit
from waves import wave
from torres import familia
from torres import honestidade
from torres import roquei
from torres import bobeira

pygame.init()

screen = pygame.display.set_mode((800, 650), 0, 32)
menu = pygame.image.load("img/menu.png").convert_alpha()
tela = pygame.image.load("img/game.jpg").convert_alpha()

pygame.display.set_caption('Defense of mind sad')

clock = pygame.time.Clock()

new_wave = 75
w = []
ticks = 22
moves = 1
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(tela, (4, 0))
    
    if(len(w) == 0):
        if(new_wave > 0):
            new_wave -= 1
            cont = 0
        else:
            wave.criar_wave()
            wave.definir_wave()
            w = wave.get_wave()
            cont = 1
            new_wave = 75
    else:
        for i in w:
            x = 150
            y = 200
            for j in w[i]:
                img = pygame.image.load(w[i][j]["img"]).convert_alpha()
                screen.blit(img, (w[i][j]["x"], w[i][j]["y"]))
                x += 10
        for i in range(1, cont):
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
                    
        if(cont < 11):
            if not(ticks):
                cont += 1
                ticks = 22
            else:
                ticks -= 1
    screen.blit(menu, (548, 0))
    pygame.display.update()
    time_passed = clock.tick(25)
