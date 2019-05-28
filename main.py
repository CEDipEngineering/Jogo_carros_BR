# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:07:56 2019

@author: Carlos Dip
"""
import pygame
from os import path
import json
import random
import time
from inimigos import Inimigo
from obstaculos import Obstaculo
from bullet import Bullet       
from Player import Player


pygame.init()

with open('consts.txt', 'r') as consts_txt:
    conteudo = consts_txt.read()
    consts = json.loads(conteudo)
    
with open('dic_tanque.txt', 'r') as dic_tanque_txt:
    conteudo = dic_tanque_txt.read()
    tanque = json.loads(conteudo)

FPS = consts['FPS']
HEIGHT = consts['HEIGHT']
WIDTH = consts['WIDTH']
WIDTH_STREET = consts['WIDTH_STREET']
BLACK = consts['BLACK']
RED = consts['RED']
WHITE = consts['WHITE']
img_dir = path.join(path.dirname(__file__), 'Assets')
img_dir = path.join(img_dir,'img')
std_width = int(WIDTH_STREET/10)


#carregando a intro do jogo (tela)


 

#função para renderizar texto:

def text_format(message,font, textSize, textColor):
    newFont=pygame.font.Font(None,textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText


#carregando a intro do jogo (tela)

def game_intro():
    
    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = "start"
                    return True
                elif event.key==pygame.K_ESCAPE:
                    selected = "quit"
                    return False 
    
    
    
        screen.blit(background, (WIDTH/2 - WIDTH_STREET/2,0))
        title = text_format("Road to Victory", font, 50, WHITE)
        if selected == "start":
            text_start = text_format("START", font, 75, BLACK)
            text_start2 = text_format("Press right key to start", font, 35, BLACK)
        else:
            text_start = text_format("START", font, 75, BLACK)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 75, WHITE)
        else:
            text_quit = text_format("QUIT", font, 75, BLACK)
            text_quit2 = text_format("Press ESC to quit", font, 35, BLACK)
                        
        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()
        screen.blit(title, (WIDTH/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (WIDTH/2 - (start_rect[2]/2), 300))
        screen.blit(text_start2, (WIDTH/2 - (start_rect[2]/2) - 50, 350))
        screen.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 400))
        screen.blit(text_quit2, (WIDTH/2 - (quit_rect[2]/2) - 40, 450))
        pygame.display.update()
        clock.tick(FPS)
#        screen.set_caption("Python - Pygame Simple Main Menu Selection")
        
def carregar():
    screen.fill(BLACK)
    screen.blit(background, (WIDTH/2 - WIDTH_STREET/2,0))
    i =  3
    while i != 0:
        text_iniciate = text_format("{0}".format(i), font, 100, RED)
        
     
        
        
     
        iniciate_rect = text_iniciate.get_rect()
        screen.blit(text_iniciate, (WIDTH/2 - (iniciate_rect[2]/2), 200))
        pygame.display.update()
        time.sleep(2)
        screen.blit(background, (WIDTH/2 - WIDTH_STREET/2,0))
        i = i - 1

def load_fase_screen(img):
    

    image = pygame.transform.scale(img, (WIDTH,HEIGHT))
    screen.blit(image, (0,0))
    pygame.display.update()
    time.sleep(5)


def load_assets(img_dir):
    assets = {}
    assets['player_img'] = pygame.image.load(path.join(img_dir, 'Cyan1.png')).convert_alpha()
    assets['bullet_img'] = pygame.image.load(path.join(img_dir, 'bullet_3.png')).convert_alpha()
    assets['mob_img'] = pygame.image.load(path.join(img_dir, "Blue2.png")).convert()
    assets['background'] = pygame.image.load(path.join(img_dir, 'road.png')).convert()
    assets['riogsul'] = pygame.image.load(path.join(img_dir, 'riogsul.png')).convert()
    assets['riogsul2'] = pygame.image.load(path.join(img_dir, 'riogsul2.png')).convert()
    assets['obstaculo1_img'] = pygame.image.load(path.join(img_dir, 'roadblock.png')).convert_alpha()
    assets['obstaculo2_img'] = pygame.image.load(path.join(img_dir, 'cone.png')).convert_alpha()
    
    return assets

def Transform_Imgs(assets):
    assets['player_img'] = pygame.transform.rotate(assets['player_img'], +90)
    assets['player_img'] = pygame.transform.scale(assets['player_img'], (std_width,95))
    assets['mob_img'] = pygame.transform.scale(assets['mob_img'], (std_width,95))
    assets['obstaculo1_img'] = pygame.transform.scale(assets['obstaculo1_img'], (std_width,95))
    assets['obstaculo2_img'] = pygame.transform.scale(assets['obstaculo2_img'], (std_width,95))
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH_STREET, HEIGHT))
    
    return assets
    
def highscore(score):
    
    list_score = []
    list_score.append(score)
    high_score = max(list_score)
    if len(list_score) > 5:
        list_score.remove(min(list_score))
    
    return list_score, high_score   

    
    
            
#    for index in range(len(list_core)):
#    
#        if list_core[index] > list_core[index-1]:
#            high_score = list_core[index]
#            return high_score
#        else:
#            high_score = high_score[index-1] 
#            return high_score 
#        
    
   
font = pygame.font.SysFont("comicsansms", 72)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
assets = load_assets(img_dir)
assets = Transform_Imgs(assets)

#carregando o plano de fundo (para tela inicial)
background = assets['background']
background_rect = background.get_rect()




player = Player(assets['player_img'])
clock = pygame.time.Clock()

bossshots = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()            
inimigos = pygame.sprite.Group()
tiros = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

for i in range(1,6):
    dado = random.randint(1,25)
    if dado <= 5:
        a = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]),i)
        all_sprites.add(a)
        obstaculos.add(a)
    else:
        a = Inimigo(assets['mob_img'],i)
        all_sprites.add(a)
        inimigos.add(a)    

    
    
all_sprites.add(player)




def Main():
    #Variáveis
    fired = False
    fired_cooldown = 0
    Shots_Fired = 0
    r_down = False
    l_down = False
    frame_count = 0
    
    background = assets['background']
    background_posY = 0
    background_aceleration = 10 
    background_maxspeed = 7.5

    
    try:
        running = game_intro()
        load_fase_screen(assets['riogsul'])
#        load_fase_screen(assets['riogsul2'])
        carregar()
        BossAlive = False
        while running:
            if player.HP <= 0:
                running = game_intro()
                if running:
                    carregar()
                    for mob in inimigos:
                        mob.kill()
                    for i in range(1,6):
                        a = Inimigo(assets['mob_img'],i)
                        if a != None:
                            all_sprites.add(a)
                            inimigos.add(a)
                    player.HP = 5
                    
            keys = pygame.key.get_pressed()  #checking pressed keys
            # Ajusta a velocidade do jogo.
            clock.tick(FPS)
            
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                
                # Verifica se foi fechado
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        l_down = True
                        player.acc -= player.power
                    if event.key == pygame.K_d:
                        r_down = True
                        player.acc += player.power
                        
                    if event.key == pygame.K_w:
                        player.accY -= player.power
                    if event.key == pygame.K_s:
                        player.accY += player.power
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key == pygame.K_LSHIFT:
                        player.firerate = 0.01
            
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        l_down = False
                        player.acc = 0
                        if r_down:
                            player.acc += player.power
                           
                    if event.key == pygame.K_d:
                        r_down = False
                        player.acc = 0
                        if l_down:
                            player.acc -= player.power
                            
                    if event.key == pygame.K_w:
                        player.accY = 0
                    if event.key == pygame.K_s:
                        player.accY = 0
                    if event.key == pygame.K_LSHIFT:
                        player.firerate = 10
                        
            if keys[pygame.K_SPACE] and not fired:
                if Shots_Fired<=player.burstfire:
                    bullet = Bullet(assets['bullet_img'], player.rect.centerx, player.rect.top, player.speed)
                    all_sprites.add(bullet)
                    tiros.add(bullet)
                    Shots_Fired += 1
                else:
                    Shots_Fired = 0
                    fired = True
                
            if fired:
                fired_cooldown += 1
            if fired_cooldown >= player.firerate:
                fired_cooldown = 0
                fired = False
            hits = pygame.sprite.groupcollide(inimigos, tiros, False, True)
            
            counter = 0
            for hit in hits:
                hit.HP -= 1
                if hit.HP <= 0 and not hit.boss:
                    dado = random.randint(1,25)
                    i = -1 
                    if dado <= 5:
                        a = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]),hit.col)
                        all_sprites.add(a)
                        obstaculos.add(a)
                    else:
                        a = Inimigo(assets['mob_img'],hit.col)
                        all_sprites.add(a)
                        inimigos.add(a)
                if hit.boss and hit.HP <= 0:
                    BossAlive = False
                    
                    
            if BossAlive and frame_count%20 == 0:
                b = Bullet(assets['bullet_img'], Boss.rect.centerx, Boss.rect.bottom, 0)
                b.yspeed = 10
                bossshots.add(b)
                all_sprites.add(b)
                
            
                
            score = counter 
            highscore(score)
            
            hit = pygame.sprite.spritecollide(player, inimigos, True, pygame.sprite.collide_circle)            
            if hit:
                player.HP -= 1
                all_sprites.add(player)
                dado = random.randint(1,25)
                if dado <= 5:
                    a = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]), hit[0].col)
                    all_sprites.add(a)
                    obstaculos.add(a)
                else:
                    a = Inimigo(assets['mob_img'],hit[0].col)
                    all_sprites.add(a)
                    inimigos.add(a)   
            
            hit = pygame.sprite.spritecollide(player, bossshots, True, pygame.sprite.collide_circle)            
            if hit:
                player.HP -= 1
                all_sprites.add(player)

                
            hit_obst = pygame.sprite.spritecollide(player, obstaculos, True, pygame.sprite.collide_circle)            
            if hit_obst:
                player.HP -= 1
                all_sprites.add(player)
                o = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]), random.randint(1,5))  
                all_sprites.add(o)
                obstaculos.add(o)
            
            screen.fill(BLACK)
            
            
            
            for car in inimigos:
                car.updateSpeed(background_aceleration)
                if car.rect.y >=HEIGHT:
                    car.kill()
                    dado = random.randint(1,25)
                    if dado <= 5:
                        a = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]),car.col)
                        all_sprites.add(a)
                        obstaculos.add(a)
                    else:
                        a = Inimigo(assets['mob_img'], car.col)
                        all_sprites.add(a)
                        inimigos.add(a)   
                                
            for objeto in obstaculos:
                objeto.updateSpeed(background_aceleration)
                if objeto.rect.y >=HEIGHT:
                    objeto.kill()
                    dado = random.randint(1,25)
                    if dado <= 5:
                        a = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]), objeto.col)
                        all_sprites.add(a)
                        obstaculos.add(a)
                    else:
                        a = Inimigo(assets['mob_img'], objeto.col)
                        all_sprites.add(a)
                        inimigos.add(a)     

            all_sprites.update()        
            if frame_count == 60*10:
                for enemy in inimigos:
                    enemy.kill()
                Boss = Inimigo(assets['mob_img'] , 3, boss = True)
                all_sprites.add(Boss)
                inimigos.add(Boss)
                Boss.HP = 10
                BossAlive = True
                    
            ##----Background movement----##
            if background_aceleration >= background_maxspeed:
                background_aceleration = background_maxspeed
            else:
                background_aceleration += 0           
            relative_y = background_posY % background.get_rect().height
            screen.blit(background, ((WIDTH-WIDTH_STREET)/2,relative_y - background.get_rect().height))
            if relative_y < HEIGHT:
                screen.blit(background, ((WIDTH-WIDTH_STREET)/2,relative_y))
            background_posY += background_aceleration
            ##---------------------------##
            
            
            
            all_sprites.draw(screen)
            
            
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
            frame_count += 1
    finally:
        pygame.quit()
Main()