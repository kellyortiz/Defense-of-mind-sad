import pygame
import sys

pygame.init()

def menu(estado):
    screen = pygame.display.set_mode((600,360),0,32)
    fundo = 'gameover.png'
    background = pygame.image.load(fundo).convert()
    
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    if (x > 560 and x < 580) and (y > 10 and y < 35):
                        return mmenu(evento)
                        estado = False
        pygame.display.update()
        screen.blit(background, (0, 0))
        pygame.display.flip()

def mmenu(estado):
    screen = pygame.display.set_mode((600,600),0,32)
    import menu.py
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                        
        screen.fill((0,0,0))
        pygame.display.flip()
        
        
Switch = "menu"

while Switch == "menu":
    Switch = menu(True)
    if Switch == "sair":
        pygame.quit()
        sys.exit()
    while Switch == "mmenu":
        Switch = mmenu(True)

    
