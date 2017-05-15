import pygame
import sys
import importlib

pygame.init()

def menu(estado):
    screen = pygame.display.set_mode((800,650),0,32)
    fundo = 'img/gameover.png'
    background = pygame.image.load(fundo).convert()
    
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 769 and x < 784) and (y > 23 and y < 49):
                        return mmenu(evento)
                        estado = False
        pygame.display.update()
        screen.blit(background, (0, 0))
        pygame.display.flip()

def mmenu(estado):
    screen = pygame.display.set_mode((600,600),0,32)
    if("menu" in sys.modules):
        importlib.reload(sys.modules["menu"])
    else:
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

    
