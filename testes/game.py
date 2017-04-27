import pygame
from pygame.locals import *
from sys import exit
from bolinhas import wave

pygame.init()

screen = pygame.display.set_mode((800, 650), 0, 32)

pygame.display.set_caption('Hello World')

wave.criar_wave()
wave.definir_wave()

w = wave.get_wave()

##print(w)

clock = pygame.time.Clock()

for i in w:
    print(i)
    print(len(w[i]))
    print(w[i])

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
##            screen.blit(img, (x, y))
    for i in range(1, cont):
        w["nojinho"][i-1]["x"] += 2

    if (cont < 11):   
        if not(ticks):
            cont += 1
            ticks = 22
        else:
            ticks -= 1

##    w["nojinho"][0]["x"] += 0.9
    pygame.display.update()
    time_passed = clock.tick(25)
    
