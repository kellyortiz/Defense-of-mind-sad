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


pygame.display.set_caption('Defense of mind sad')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    
    screen.blit(menu, (552, 0))
    pygame.display.update()
    time_passed = clock.tick(25)
