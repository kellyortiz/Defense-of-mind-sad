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
from Pontuação import pontuacao
import importlib

pygame.init()

screen = pygame.display.set_mode((800, 650), 0, 32)

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 16)

menu = pygame.image.load("img/menu.png").convert_alpha()
tela = pygame.image.load("img/game.jpg").convert_alpha()

pygame.display.set_caption('Defense of mind sad')

clock = pygame.time.Clock()

rects = []

rects.append(pygame.rect.Rect(109, 188, 72, 313))
rects.append(pygame.rect.Rect(181, 188, 122, 72))
rects.append(pygame.rect.Rect(230, 62, 72, 126))
rects.append(pygame.rect.Rect(302, 62, 125, 72))
rects.append(pygame.rect.Rect(355, 138, 72, 314))

reiniciar = False
new_wave = 75
w = []
ticks = 22
moves = 1
maximo = []
ignore = []
vida.iniciar_vida()
torre_familia = []
torre_honestidade = []
torre_bobeira = []
torre_amizade = []
torre_roquei = []
sala_controle = pygame.image.load("img/sala_controle.png").convert_alpha()
long_memory = pygame.image.load("img/long_therm_memory.png").convert_alpha()
tiros = []
tiro_roquei = 13
tiro_bobeira = 9
tiro_amizade = 9
tiro_familia = 13
tiro_honestidade = 9

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

def criar_tiro(x, y, tipo):
    todos = []
    for i in range(4):
        tiro = [255, x, y, tipo]
        todos.append(tiro)
    return todos

def atualizar_tiro(tipo):
    for i in tiros:
        for j in range(len(i)):
            if(j == 0):
                i[0][1] +=3
                i[0][2] +=3
            if(j == 1):
                i[1][1] +=3
                i[1][2] -=3
            if(j == 2):
                i[2][1] -=3
                i[2][2] +=3
            if(j == 3):
                i[3][1] -=3
                i[3][2] -=3

def desenhar_tiro():
    for t in tiros:
        for j in range(len(t)):
            pygame.draw.circle(screen, (t[j][0], t[j][0], t[j][0]), (t[j][1], t[j][2]), 10)

def destruir_bolinha():
    pass


while True:
    screen.fill((255, 255, 255))
    for i in range(len(rects)):
        pygame.draw.rect(screen, (255, 0, 0), rects[i])
    screen.blit(tela, (4, 0))
    screen.blit(menu, (548, 0))

    qtde_roquei = game_font.render(str(3 - len(torre_roquei)), 1, (255, 0 , 0))
    screen.blit(qtde_roquei, (645, 168))

    qtde_bobeira = game_font.render(str(1 - len(torre_bobeira)), 1, (255, 0 , 0))
    screen.blit(qtde_bobeira, (761, 168))

    qtde_familia = game_font.render(str(1 - len(torre_familia)), 1, (255, 0 , 0))
    screen.blit(qtde_familia, (761, 301))

    qtde_honestidade = game_font.render(str(2 - len(torre_honestidade)), 1, (255, 0 , 0))
    screen.blit(qtde_honestidade, (701, 420))

    qtde_amizade = game_font.render(str(1 - len(torre_amizade)), 1, (255, 0 , 0))
    screen.blit(qtde_amizade, (645, 301))
    
    vidas = game_font.render(str(vida.get_vida()), 1, (0, 0, 0))
    screen.blit(vidas, (686, 45))

    pontos = game_font.render(str(pontuacao.get_pontuacao()), 1, (0, 0, 0))
    screen.blit(pontos, (696, 99))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0):
                print(pygame.mouse.get_pos())
                x,y = pygame.mouse.get_pos()
                if ((x > 593 and x < 660) and (y > 175 and y < 230) and (len(torre_roquei) < 3)):
                    torre_roquei.append(roquei.criar_roquei())
                    for i in range(len(torre_roquei)):
                        if(torre_roquei[i]["img"] == "torres/img/island/roquei.png"):
                            torre_roquei[i]["img"] = pygame.image.load(torre_roquei[i]["img"]).convert_alpha()
                elif((x > 710 and x < 780) and (y > 175 and y < 245) and (len(torre_bobeira) < 1)):
                    torre_bobeira.append(bobeira.criar_bobeira())
                    for i in range(len(torre_bobeira)):
                        if(torre_bobeira[i]["img"] == "torres/img/island/bobeira.png"):
                            torre_bobeira[i]["img"] = pygame.image.load(torre_bobeira[i]["img"]).convert_alpha()
                elif((x > 593 and x < 660) and (y > 307 and y < 370) and (len(torre_amizade) < 1)):
                    torre_amizade.append(amizade.criar_amizade())
                    for i in range(len(torre_amizade)):
                        if(torre_amizade[i]["img"] == "torres/img/island/amizade.png"):
                            torre_amizade[i]["img"] = pygame.image.load(torre_amizade[i]["img"]).convert_alpha()
                elif((x > 710 and x < 780) and (y > 307 and y < 370) and (len(torre_familia) < 1)):
                    torre_familia.append(familia.criar_familia())
                    for i in range(len(torre_familia)):
                        if(torre_familia[i]["img"] == "torres/img/island/familia.png"):
                            torre_familia[i]["img"] = pygame.image.load(torre_familia[i]["img"]).convert_alpha()
                elif((x > 655 and x < 720) and (y > 427 and y < 478) and (len(torre_honestidade) < 2)):
                    torre_honestidade.append(honestidade.criar_honestidade())
                    for i in range(len(torre_honestidade)):
                        if(torre_honestidade[i]["img"] == "torres/img/island/honestidade.png"):
                            torre_honestidade[i]["img"] = pygame.image.load(torre_honestidade[i]["img"]).convert_alpha()

                elif((x > 613 and x < 749) and (y > 577 and y < 631)):
                    iniciar()
        elif(evento.type == pygame.MOUSEBUTTONUP):
            if(evento.button == 1):
                stop = False
                for i in range(len(torre_roquei)):
                    torre_roquei[i]["posicionado"] = True
                    for i in range(len(torre_roquei)):
                        if(torre_roquei[i]["valido"] == False):
                            del(torre_roquei[i])
                            stop = True
                            break
                    if(stop):
                        break
                for i in range(len(torre_bobeira)):
                    torre_bobeira[i]["posicionado"] = True
                    for i in range(len(torre_bobeira)):
                        if(torre_bobeira[i]["valido"] == False):
                            del(torre_bobeira[i])
                            stop = True
                            break
                    if(stop):
                        break
                for i in range(len(torre_amizade)):
                    torre_amizade[i]["posicionado"] = True
                    for i in range(len(torre_amizade)):
                        if(torre_amizade[i]["valido"] == False):
                            del(torre_amizade[i])
                            stop = True
                            break
                    if(stop):
                        break
                for i in range(len(torre_familia)):
                    torre_familia[i]["posicionado"] = True
                    for i in range(len(torre_familia)):
                        if(torre_familia[i]["valido"] == False):
                            del(torre_familia[i])
                            stop = True
                            break
                    if(stop):
                        break
                for i in range(len(torre_honestidade)):
                    torre_honestidade[i]["posicionado"] = True
                    for i in range(len(torre_honestidade)):
                        if(torre_honestidade[i]["valido"] == False):
                            del(torre_honestidade[i])
                            stop = True
                            break
                    if(stop):
                        break
                
        elif(evento.type == pygame.MOUSEMOTION):
            for i in range(len(torre_roquei)):
                if(torre_roquei[i]["posicionado"] == False):
                    mouse_x, mouse_y = evento.pos
                    torre_roquei[i]["x"] = mouse_x-35
                    torre_roquei[i]["y"] = mouse_y-43
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

    memory_rect = pygame.rect.Rect(430, 387, 106, 72)
    for i in range(len(torre_roquei)):
        screen.blit(torre_roquei[i]["img"], (torre_roquei[i]["x"], torre_roquei[i]["y"]))
        if(torre_roquei[i]["posicionado"] == False):
            color = (255, 255, 0)
            roquei_rect = pygame.rect.Rect(torre_roquei[i]["x"]+7, torre_roquei[i]["y"]+7, 71, 64)
            if(torre_roquei[i]["x"] >= 493):
                color = (255, 0, 0)
            for r in rects:
                if(r.colliderect(roquei_rect)):
                    color = (255, 0, 0)
            for t in torre_bobeira:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 62, 77)
                if(rect_torre.colliderect(roquei_rect)):
                    color = (255, 0, 0)
            for t in torre_familia:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 61, 49)
                if(rect_torre.colliderect(roquei_rect)):
                    color = (255, 0, 0)
            for t in range(len(torre_roquei)-1):
                rect_torre = pygame.rect.Rect(torre_roquei[t]["x"]+17, torre_roquei[t]["y"]+17, 43, 45)
                if(rect_torre.colliderect(roquei_rect)):
                    color = (255, 0, 0)
            for t in torre_amizade:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 49, 61)
                if(rect_torre.colliderect(roquei_rect)):
                    color = (255, 0, 0)
            for t in torre_honestidade:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 61, 54)
                if(rect_torre.colliderect(roquei_rect)):
                    color = (255, 0, 0)
            if(memory_rect.colliderect(roquei_rect)):
               color = (255, 0, 0)
            pygame.draw.circle(screen, color, (torre_roquei[i]["x"]+35, torre_roquei[i]["y"]+43), 100, 2)
            if(color == (255, 0, 0)):
                torre_roquei[i]["valido"] = False
            else:
                torre_roquei[i]["valido"] = True
                
    for i in range(len(torre_bobeira)):
        screen.blit(torre_bobeira[i]["img"], (torre_bobeira[i]["x"], torre_bobeira[i]["y"]))
        if(torre_bobeira[i]["posicionado"] == False):
            color = (255, 255, 0)
            bobeira_rect = pygame.rect.Rect(torre_bobeira[i]["x"]+7, torre_bobeira[i]["y"]+7, 71, 64)
            if(torre_bobeira[i]["x"] >= 479):
                color = (255, 0, 0)
            for r in rects:
                if(r.colliderect(bobeira_rect)):
                    color = (255, 0, 0)
            for t in range(len(torre_bobeira)-1):
                rect_torre = pygame.rect.Rect(torre_bobeira[t]["x"]+17, torre_bobeira[t]["y"]+17, 62, 77)
                if(rect_torre.colliderect(bobeira_rect)):
                    color = (255, 0, 0)
            for t in torre_familia:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 61, 49)
                if(rect_torre.colliderect(bobeira_rect)):
                    color = (255, 0, 0)
            for t in torre_roquei:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 43, 45)
                if(rect_torre.colliderect(bobeira_rect)):
                    color = (255, 0, 0)
            for t in torre_amizade:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 49, 61)
                if(rect_torre.colliderect(bobeira_rect)):
                    color = (255, 0, 0)
            for t in torre_honestidade:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 61, 54)
                if(rect_torre.colliderect(bobeira_rect)):
                    color = (255, 0, 0)
            if(memory_rect.colliderect(bobeira_rect)):
               color = (255, 0, 0)
            pygame.draw.circle(screen, color, (torre_bobeira[i]["x"]+40, torre_bobeira[i]["y"]+66), 156, 2)
            if(color == (255, 0, 0)):
                torre_bobeira[i]["valido"] = False
            else:
                torre_bobeira[i]["valido"] = True
                
    for i in range(len(torre_amizade)):
        screen.blit(torre_amizade[i]["img"], (torre_amizade[i]["x"], torre_amizade[i]["y"]))
        if(torre_amizade[i]["posicionado"] == False):
            color = (255, 255, 0)
            amizade_rect = pygame.rect.Rect(torre_amizade[i]["x"]+7, torre_amizade[i]["y"]+7, 71, 64)
            if(torre_amizade[i]["x"] >= 492):
                color = (255, 0, 0)
            for r in rects:
                if(r.colliderect(amizade_rect)):
                    color = (255, 0, 0)
            for t in torre_bobeira:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 62, 77)
                if(rect_torre.colliderect(amizade_rect)):
                    color = (255, 0, 0)
            for t in torre_familia:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 61, 49)
                if(rect_torre.colliderect(amizade_rect)):
                    color = (255, 0, 0)
            for t in torre_roquei:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 43, 45)
                if(rect_torre.colliderect(amizade_rect)):
                    color = (255, 0, 0)
            for t in range(len(torre_amizade)-1):
                rect_torre = pygame.rect.Rect(torre_amizade[t]["x"]+17, torre_amizade[t]["y"]+17, 49, 61)
                if(rect_torre.colliderect(amizade_rect)):
                    color = (255, 0, 0)
            for t in torre_honestidade:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 61, 54)
                if(rect_torre.colliderect(amizade_rect)):
                    color = (255, 0, 0)
            if(memory_rect.colliderect(amizade_rect)):
               color = (255, 0, 0)
            pygame.draw.circle(screen, color, (torre_amizade[i]["x"]+34, torre_amizade[i]["y"]+52), 212, 2)
            if(color == (255, 0, 0)):
                torre_amizade[i]["valido"] = False
            else:
                torre_amizade[i]["valido"] = True

    for i in range(len(torre_familia)):
        screen.blit(torre_familia[i]["img"], (torre_familia[i]["x"], torre_familia[i]["y"]))
        if(torre_familia[i]["posicionado"] == False):
            color = (255, 255, 0)
            familia_rect = pygame.rect.Rect(torre_familia[i]["x"]+7, torre_familia[i]["y"]+7, 71, 64)
            if(torre_familia[i]["x"] >= 480):
                color = (255, 0, 0)
            for r in rects:
                if(r.colliderect(familia_rect)):
                    color = (255, 0, 0)
            for t in torre_bobeira:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 62, 77)
                if(rect_torre.colliderect(familia_rect)):
                    color = (255, 0, 0)
            for t in range(len(torre_familia)-1):
                rect_torre = pygame.rect.Rect(torre_familia[t]["x"]+17, torre_familia[t]["y"]+17, 61, 49)
                if(rect_torre.colliderect(familia_rect)):
                    color = (255, 0, 0)
            for t in torre_roquei:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 43, 45)
                if(rect_torre.colliderect(familia_rect)):
                    color = (255, 0, 0)
            for t in torre_amizade:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 49, 61)
                if(rect_torre.colliderect(familia_rect)):
                    color = (255, 0, 0)
            for t in torre_honestidade:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 61, 54)
                if(rect_torre.colliderect(familia_rect)):
                    color = (255, 0, 0)
            if(memory_rect.colliderect(familia_rect)):
               color = (255, 0, 0)
            pygame.draw.circle(screen, color, (torre_familia[i]["x"]+39, torre_familia[i]["y"]+39), 156, 2)
            if(color == (255, 0, 0)):
                torre_familia[i]["valido"] = False
            else:
                torre_familia[i]["valido"] = True
                
    for i in range(len(torre_honestidade)):
        screen.blit(torre_honestidade[i]["img"], (torre_honestidade[i]["x"], torre_honestidade[i]["y"]))
        if(torre_honestidade[i]["posicionado"] == False):
            color = (255, 255, 0)
            honestidade_rect = pygame.rect.Rect(torre_honestidade[i]["x"]+7, torre_honestidade[i]["y"]+7, 71, 64)
            if(torre_honestidade[i]["x"] >= 479):
                color = (255, 0, 0)
            for r in rects:
                if(r.colliderect(honestidade_rect)):
                    color = (255, 0, 0)
            for t in torre_bobeira:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 62, 77)
                if(rect_torre.colliderect(honestidade_rect)):
                    color = (255, 0, 0)
            for t in torre_familia:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 61, 49)
                if(rect_torre.colliderect(honestidade_rect)):
                    color = (255, 0, 0)
            for t in torre_roquei:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 43, 45)
                if(rect_torre.colliderect(honestidade_rect)):
                    color = (255, 0, 0)
            for t in torre_amizade:
                rect_torre = pygame.rect.Rect(t["x"]+17, t["y"]+17, 49, 61)
                if(rect_torre.colliderect(honestidade_rect)):
                    color = (255, 0, 0)
            for t in range(len(torre_honestidade)-1):
                rect_torre = pygame.rect.Rect(torre_honestidade[t]["x"]+17, torre_honestidade[t]["y"]+17, 61, 54)
                if(rect_torre.colliderect(honestidade_rect)):
                    color = (255, 0, 0)
            if(memory_rect.colliderect(honestidade_rect)):
               color = (255, 0, 0)
            pygame.draw.circle(screen, color, (torre_honestidade[i]["x"]+39, torre_honestidade[i]["y"]+39), 128, 2)
            if(color == (255, 0, 0)):
                torre_honestidade[i]["valido"] = False
            else:
                torre_honestidade[i]["valido"] = True
                
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
                print(maximo)
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
##                print(i-1)
##                print(ignore)
                if not(i-1 in ignore):
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
                        if(vidas == 0):
                            finalizar()
                        start += 1
                        if(len(w[j]) == 0):
                            reiniciar = True
                else:
                    print(i-1)
                    print(False)
        for t in range(len(tiros)):
            aux = False
            for i in range(len(tiros[t])):
                tiros_rect = pygame.rect.Rect(tiros[t][i][1], tiros[t][i][2], 20, 20)
                
                for b in w:
                    
                    for j in w[b]:
                        if not(j in ignore):
                            bolinha_rect = pygame.rect.Rect(w[b][j]["x"], w[b][j]["y"], 22, 22)
                            if(bolinha_rect.colliderect(tiros_rect)):
##                                print(j)
##                                print(tiros[t][i])
                                tiros[t].remove(tiros[t][i])
                                destruir_bolinha()
                                ignore.append(j)
##                                print(ignore)
                                del w[b][j]
##                                start += 1
                                aux = True
                                break
                    if(aux):
                        break
                if(aux):
                    break
            if(aux):
                if(len(w[b]) == 0):
                    print(len(w[b]))
                    reiniciar = True
                break
                            
        if(reiniciar == True):
            ignore = []
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

    if(tiro_roquei == 0):
        tiro_roquei = 13
        for i in range(len(torre_roquei)):
            if(torre_roquei[i]["posicionado"] == True):
                aux_tiro = False
                roquei_rect = pygame.rect.Rect(torre_roquei[i]["x"]-60, torre_roquei[i]["y"]-60, 200, 200)
                for b in w:
                    for j in w[b]:
                        bolinha_rect = pygame.rect.Rect(w[b][j]["x"], w[b][j]["y"], 22, 22)
                        if(bolinha_rect.colliderect(roquei_rect)):
                            tiro = criar_tiro(torre_roquei[i]["x"]+35, torre_roquei[i]["y"]+43, 2)
                            tiros.append(tiro)
                            aux_tiro = True
                            break
                    if(aux_tiro):
                        break
    else:
        tiro_roquei -= 1

    if(tiro_bobeira == 0):
        tiro_bobeira = 9
        for i in range(len(torre_bobeira)):
            if(torre_bobeira[i]["posicionado"] == True):
                aux_tiro = False
                bobeira_rect = pygame.rect.Rect(torre_bobeira[i]["x"]-110, torre_bobeira[i]["y"]-85, 312, 312)
                for b in w:
                    for j in w[b]:
                        bolinha_rect = pygame.rect.Rect(w[b][j]["x"], w[b][j]["y"], 22, 22)
                        if(bolinha_rect.colliderect(bobeira_rect)):
                            tiro = criar_tiro(torre_bobeira[i]["x"]+35, torre_bobeira[i]["y"]+43, 1)
                            tiros.append(tiro)
                            aux_tiro = True
                            break
                    if(aux_tiro):
                        break
    else:
        tiro_bobeira -= 1

    if(tiro_amizade == 0):
        tiro_amizade = 9
        for i in range(len(torre_amizade)):
            if(torre_amizade[i]["posicionado"] == True):
                aux_tiro = False
                amizade_rect = pygame.rect.Rect(torre_amizade[i]["x"]-160, torre_amizade[i]["y"]-160, 424, 424)
                for b in w:
                    for j in w[b]:
                        bolinha_rect = pygame.rect.Rect(w[b][j]["x"], w[b][j]["y"], 22, 22)
                        if(bolinha_rect.colliderect(amizade_rect)):
                            
                            tiro = criar_tiro(torre_amizade[i]["x"]+35, torre_amizade[i]["y"]+43, 1)
                            tiros.append(tiro)
                            aux_tiro = True
                            break
                    if(aux_tiro):
                        break
    else:
        tiro_amizade -= 1

    if(tiro_familia == 0):
        tiro_familia = 13
        for i in range(len(torre_familia)):
            if(torre_familia[i]["posicionado"] == True):
                aux_tiro = False
                familia_rect = pygame.rect.Rect(torre_familia[i]["x"]-110, torre_familia[i]["y"]-85, 312, 312)
                for b in w:
                    for j in w[b]:
                        bolinha_rect = pygame.rect.Rect(w[b][j]["x"], w[b][j]["y"], 22, 22)
                        if(bolinha_rect.colliderect(familia_rect)):
                            tiro = criar_tiro(torre_familia[i]["x"]+35, torre_familia[i]["y"]+43, 1)
                            tiros.append(tiro)
                            aux_tiro = True
                            break
                    if(aux_tiro):
                        break
    else:
        tiro_familia -= 1

    if(tiro_honestidade == 0):
        tiro_honestidade = 9
        for i in range(len(torre_honestidade)):
            if(torre_honestidade[i]["posicionado"] == True):
                aux_tiro = False
                honestidade_rect = pygame.rect.Rect(torre_honestidade[i]["x"]-85, torre_honestidade[i]["y"]-85, 256, 256)
                for b in w:
                    for j in w[b]:
                        bolinha_rect = pygame.rect.Rect(w[b][j]["x"], w[b][j]["y"], 22, 22)
                        if(bolinha_rect.colliderect(honestidade_rect)):
                            
                            tiro = criar_tiro(torre_honestidade[i]["x"]+35, torre_honestidade[i]["y"]+43, 1)
                            tiros.append(tiro)
                            aux_tiro = True
                            break
                    if(aux_tiro):
                        break
    else:
        tiro_honestidade -= 1

    screen.blit(sala_controle, (70, 437))
    screen.blit(long_memory, (430, 387))
    atualizar_tiro(1)
    atualizar_tiro(2)
    desenhar_tiro()
    pygame.display.update()
    time_passed = clock.tick(25)
