import pygame
import sys

pygame.init()

def menu(estado):
    screen = pygame.display.set_mode((900,500),0,32)
    fundo = 'sw.png'
    background = pygame.image.load(fundo).convert()
     
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 80 and x < 110) and (y > 120 and y < 160):
                        return "jogo"
                        estado = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 80 and x < 110) and (y > 120 and y < 160):
                        return "Continuarjogo"
                        estado = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 110 and x < 140) and (y > 160 and y < 200):
                        return "tutorial"
                        estado = False
        pygame.display.update()
        screen.blit(background, (0, 0))
        pygame.display.flip()

def tutorial(estado):
    screen = pygame.display.set_mode((600,600),0,32)
    arquivo = pygame.image.load("tutorial.jpg")
    fundo = pygame.transform.scale(arquivo,(600,600))
    
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 560 and x < 600) and (y > 580 and y < 600):
                        return "menu"
                        estado = False
        pygame.display.flip()

def jogo(estado):
    screen = pygame.display.set_mode((600,600),0,32)
    import game.py
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                        
        screen.fill((0,0,0))
        pygame.display.flip()
        
Switch = "menu"

while Switch == menu(True):
    if Switch == "sair":
        pygame.quit()
        sys.exit()
    while Switch == "tutorial":
        Switch = ajuda(True)
    while Switch == "jogo":
        Switch = jogo(True)
    while Switch == "Continuarjogo":
        Switch = Continuarjogo(True)
