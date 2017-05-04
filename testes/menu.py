import pygame
import sys

pygame.init()

def menu(estado):
    screen = pygame.display.set_mode((900,500),0,32)
    fundo = 'iniciar.png'
    background = pygame.image.load(fundo).convert()
    
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 12 and x < 333) and (y > 132 and y < 220):
                        return jogo(evento)
                        estado = False
                        
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 12 and x < 288) and (y > 242 and y < 332):
                        return novojogo(evento)
                        estado = False
                        
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 12 and x < 338) and (y > 362 and y < 451):
                        return tutorial(evento)
                        estado = False
        
        pygame.display.update()
        screen.blit(background, (0, 0))
        pygame.display.flip()

    
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 220 and x < 280) and (y > 300 and y < 320):
                        pygame.quit()
                        sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 560 and x < 600) and (y > 580 and y < 600):
                        return "menu"
                        estado = False
                        
        screen.blit(fundo,(0,0))
        screen.blit(voltar,(560,580))
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
        
def novojogo(estado):
    screen = pygame.display.set_mode((600,600),0,32)
    import game.py
    while estado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                        
        screen.fill((0,0,0))
        pygame.display.flip()
        
def tutorial(estado):
    screen = pygame.display.set_mode((600,600),0,32)
    import tutorial.py
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
    while Switch == "jogo":
        Switch = jogo(True)
    while Switch == "novojogo":
        Switch = novojogo(True)
    while Switch == "tutorial":
        Switch = tutorial(True)

    
