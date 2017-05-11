import pygame
from pygame.locals import *
from sys import exit
from bolinhas import wave
from torres import familia
from torres import honestidade
from torres import roquei

pygame.init()

screen = pygame.display.set_mode((800, 650), 0, 32)
menu = pygame.image.load("menu.png").convert_alpha()
pygame.display.set_caption('Hello World')

wave.criar_wave()
wave.definir_wave()

w = wave.get_wave()

familias = familia.criar_familia()
familias = familia.criar_familia()
familias["img"] = pygame.image.load(familias["img"]).convert_alpha()
honestidades = honestidade.criar_honestidade()
honestidades = honestidade.criar_honestidade()
honestidades["img"] = pygame.image.load(honestidades["img"]).convert_alpha()
torreRoquei = roquei.criar_roquei()
torreRoquei = roquei.criar_roquei()
torreRoquei["img"] = pygame.image.load(torreRoquei["img"]).convert_alpha()
clock = pygame.time.Clock()

ticks = 22
cont = 1
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(pygame.Surface(screen.get_size()), (0, 0))
    for i in w:
        x = 0
        y = 50
        for j in w[i]:
            
            img = pygame.image.load(w[i][j]["img"]).convert_alpha()
            screen.blit(img, (w[i][j]["x"], w[i][j]["y"]))
            x += 10
    
    for i in range(1, cont):
        w["nojinho"][i-1]["x"] += w["nojinho"][i-1]["velocidade_atual"]

    if (cont < 11):
        if not(ticks):
            cont += 1
            ticks = 22
        else:
            ticks -= 1
    screen.blit(familias["img"], (100, 100))
    screen.blit(honestidades["img"], (200, 200))
    screen.blit(menu, (552, 0))
    pygame.display.update()
    time_passed = clock.tick(25)
