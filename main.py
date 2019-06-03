# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:07:56 2019

@author: Carlos Dip
"""
import pygame
from os import path
import json
import random
from inimigos import Inimigo
from obstaculos import Obstaculo
from bullet import Bullet       
from Player import Player


pygame.init()
pygame.mixer.init()

with open('consts.txt', 'r') as consts_txt:
    conteudo = consts_txt.read()
    consts = json.loads(conteudo)
    

FPS = consts['FPS']
HEIGHT = consts['HEIGHT']
WIDTH = consts['WIDTH']
WIDTH_STREET = consts['WIDTH_STREET']
BLACK = consts['BLACK']
RED = consts['RED']
WHITE = consts['WHITE']
YELLOW = consts['YELLOW']
GREEN = consts['GREEN']
NEON_BLUE = consts['NEON_BLUE']

img_dir = path.join(path.dirname(__file__), 'Assets')
img_dir = path.join(img_dir,'img')
snd_dir = path.join(path.dirname(__file__), 'Assets')
snd_dir = path.join(snd_dir,'snd')
fnt_dir = path.join(path.dirname(__file__), 'Assets')
fnt_dir = path.join(fnt_dir,'fonts')

std_width = int(WIDTH_STREET/10)


#Carrega os sons do jogo

pygame.mixer.music.load(path.join(snd_dir, 'Automation.mp3'))
pygame.mixer.music.set_volume(0.8)


 

#função para renderizar texto:

def text_format(message,font, textSize, textColor):
    newFont=pygame.font.Font(None,textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText


#carregando a intro do jogo (tela)

def game_intro(stage, passtype = 'wait'):
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.play(loops=-1)
    stages = {'beginfase1': assets['beginfase1'], 
              'beginfase2': assets['beginfase2'], 
              'victory': assets['victory'],
              'game_over': assets['game_over'],
              'controls': assets['controls']}
    menu=True
    if stage not in stages:
        screen.blit(background, (WIDTH/2 - WIDTH_STREET/2,0))
        title = text_format("Road to Victory", font, 70, BLACK)
        text_start2 = text_format("Press right key to start", font, 35, BLACK)
        text_start = text_format("START", font, 75, BLACK)
        text_quit = text_format("QUIT", font, 75, BLACK)
        text_quit2 = text_format("Close screen to quit", font, 35, BLACK)
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
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        return True
                    elif event.key==pygame.K_ESCAPE:
                        return False 
            
        
    elif passtype == 'wait':
        screen.blit(stages[stage], (0,0))
        pygame.display.update()
        clock.tick(FPS)
        time_elapsed = pygame.time.get_ticks() + 5000
        time2 = pygame.time.get_ticks()
        while time2 < time_elapsed:
            time2 = pygame.time.get_ticks()
        return True
    
    elif passtype == 'key':
        screen.blit(stages[stage], (0,0))
        pygame.display.update()
        clock.tick(FPS)
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        return True
                    elif event.key==pygame.K_ESCAPE:
                        return False 
        
        
def carregar():
        screen.fill(BLACK)
        screen.blit(background, (WIDTH/2 - WIDTH_STREET/2,0))
        time_elapsed = pygame.time.get_ticks() + 3000
        time2 = pygame.time.get_ticks()
        while time2 < time_elapsed:
            time2 = pygame.time.get_ticks()
            screen.blit(background, (WIDTH/2 - WIDTH_STREET/2,0))
            text_iniciate = text_format(str(1 + int((time_elapsed-time2)/1000)), font, 100, RED)
            iniciate_rect = text_iniciate.get_rect()
            screen.blit(text_iniciate, (WIDTH/2 - (iniciate_rect[2]/2), 200))
            pygame.display.update()
        
        pass
        
        
        

def load_fase_screen(img, fase):
    
    
    with open("highscore{0}.txt".format(fase), "r") as highscore_txt:
        list_score = json.loads(highscore_txt.read())
    
    ass_score = max(list_score)
    
    high = highscore(ass_score, fase)
    
    new_high = str(high)
    total = text_format(new_high, font, 50, YELLOW)
    screen.blit(img, (0,0))
    screen.blit(total, (375,465))
    pygame.display.update()
    time_elapsed = pygame.time.get_ticks() + 1000
    time4 = pygame.time.get_ticks()
    while time4 < time_elapsed:
        time4 = pygame.time.get_ticks()
    pass
    


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
    assets['boss_img'] = pygame.image.load(path.join(img_dir, 'Red2.png')).convert_alpha()
    assets['shoot_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'shot.wav'))
    assets['boom_sound'] = pygame.mixer.Sound(path.join(snd_dir, 'Boom.wav'))
    assets['big_shot'] = pygame.image.load(path.join(img_dir,'bullet_5.png'))
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "life.ttf"), 28)
    assets["game_over"] =  pygame.image.load(path.join(img_dir, "game_over.png")).convert_alpha()
    assets["victory"] =  pygame.image.load(path.join(img_dir, "victory.png")).convert_alpha()
    assets['beginfase1'] = pygame.image.load(path.join(img_dir,"BeginFase1.png")).convert()
    assets['beginfase2'] = pygame.image.load(path.join(img_dir,"BeginFase2.png")).convert()
    assets['controls'] = pygame.image.load(path.join(img_dir,"Controles.png")).convert()
    
    return assets

def Transform_Imgs(assets):
    assets['player_img'] = pygame.transform.rotate(assets['player_img'], +90)
    assets['boss_img'] = pygame.transform.rotate(assets['boss_img'], +90)
    assets['player_img'] = pygame.transform.scale(assets['player_img'], (std_width,95))
    assets['boss_img'] = pygame.transform.scale(assets['boss_img'], (std_width,95))
    assets['big_shot'] = pygame.transform.scale(assets['big_shot'], (30,60))
    assets['big_shot'] = pygame.transform.rotate(assets['big_shot'], +180)
    assets['riogsul'] = pygame.transform.scale(assets['riogsul'], (WIDTH, HEIGHT))
    assets['riogsul2'] = pygame.transform.scale(assets['riogsul2'], (WIDTH, HEIGHT))
    assets['mob_img'] = pygame.transform.scale(assets['mob_img'], (std_width,95))
    assets['obstaculo1_img'] = pygame.transform.scale(assets['obstaculo1_img'], (std_width,95))
    assets['obstaculo2_img'] = pygame.transform.scale(assets['obstaculo2_img'], (std_width,95))
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH_STREET, HEIGHT))
    assets['game_over'] = pygame.transform.scale(assets['game_over'], (WIDTH, HEIGHT))
    assets['victory'] = pygame.transform.scale(assets['victory'], (WIDTH, HEIGHT))
    assets['beginfase1'] = pygame.transform.scale(assets['beginfase1'], (WIDTH, HEIGHT))
    assets['beginfase2'] = pygame.transform.scale(assets['beginfase2'], (WIDTH, HEIGHT))
    assets['controls'] = pygame.transform.scale(assets['controls'], (WIDTH, HEIGHT))
    
    return assets
    
def highscore(score, fase):
    
    fn = "highscore{0}.txt".format(fase)
    
    with open(fn, "r") as highscore_txt:
        content = highscore_txt.read()
        list_score = json.loads(content)
    
    list_score.append(score)

    
    if len(list_score) > 5:
        list_score.remove(min(list_score))
        
    with open(fn, "w") as highscore_txt:
        x = json.dumps(list_score)
        highscore_txt.write(x)
        
    high_score = max(list_score)
        
    
    return  high_score   

    
    
            
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
score_font = assets['score_font']

#carregando o plano de fundo (para tela inicial)
background = assets['background']
background_rect = background.get_rect()
shoot_sound = assets['shoot_sound']
boom_sound = assets['boom_sound'] 
shoot_sound.set_volume(0.15)



player = Player(assets['player_img'])
clock = pygame.time.Clock()

bossshots = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()            
inimigos = pygame.sprite.Group()
tiros = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

for j in range(1,6):
    dado = random.randint(1,25)
    if dado <= 5:
        a = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]),j)
        all_sprites.add(a)
        obstaculos.add(a)
    else:
        a = Inimigo(assets['mob_img'],j)
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
    game_on = game_intro(0)
    background = assets['background']
    background_posY = 0
    background_aceleration = 10 
    background_maxspeed = 7.5
    SPECIAL = False
    try:
        while game_on:
            try:
                running = game_intro('beginfase1', passtype = 'key')
                game_intro('controls', passtype = 'key')
                load_fase_screen(assets['riogsul'],1)
                carregar()
                BossAlive = False
                BossKilled = False
                BossTested = True
                counter = 0
                while running:
                    if not BossAlive and BossTested:
                        BossKilled = False
                    elif BossAlive:
                        BossKilled = False
                        BossTested = False
                    else:
                        BossKilled = True
                    
                    if BossKilled:
                        running = False
                    
                    if player.HP <= 0:
                        game_intro('game_over', passtype = 'key')
                        running = game_intro('beginfase1', passtype = 'key')
                        game_intro('controls', passtype = 'key')
                        if running:
                            fired = False
                            fired_cooldown = 0
                            Shots_Fired = 0
                            r_down = False
                            l_down = False
                            frame_count = 0
                            game_on = True
                            background = assets['background']
                            background_posY = 0
                            background_aceleration = 10 
                            background_maxspeed = 7.5
                            BossAlive = False
                            BossKilled = False
                            BossTested = True
                            SPECIAL = False
                            counter = 0
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
                            if event.key == pygame.K_LSHIFT and not SPECIAL:
                                SPECIAL = True
                                SpecialFrames = 0
                                
                    
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
                                player.resetFireRate()
                                
                    if keys[pygame.K_SPACE] and not fired:
                        if Shots_Fired<=player.burstfire:
                            bullet = Bullet(assets['bullet_img'], player.rect.centerx, player.rect.top, player.speed)
                            all_sprites.add(bullet)
                            tiros.add(bullet)
                            Shots_Fired += 1
                            shoot_sound.play()
                        else:
                            Shots_Fired = 0
                            fired = True
                        
                    if fired:
                        fired_cooldown += 1
                    if fired_cooldown >= player.firerate:
                        fired_cooldown = 0
                        fired = False
                    hits = pygame.sprite.groupcollide(inimigos, tiros, False, True)
                    
               
                    for hit in hits:
                        hit.HP -= 1
                        counter += 500
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
                            
                    hitsobst = pygame.sprite.groupcollide(obstaculos, tiros, True, True)
                    for hit in hitsobst:
                        all_sprites.add(hit)
                        obstaculos.add(hit)
                    
                    if BossAlive and frame_count%20 == 0:
                        dadoi = random.randint(0,10)
                        if dadoi <2:
                            b = Bullet(assets['big_shot'], Boss.rect.centerx, Boss.rect.bottom, 0)
                        else:
                            b = Bullet(assets['bullet_img'], Boss.rect.centerx, Boss.rect.bottom, 0)
                        b.yspeed = 10
                        bossshots.add(b)
                        all_sprites.add(b)
                        
                    
                       
                
                    
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
                        boom_sound.play()
        
                        
                    hit_obst = pygame.sprite.spritecollide(player, obstaculos, True, pygame.sprite.collide_circle)            
                    if hit_obst:
                        player.HP -= 1
                        all_sprites.add(player)
                        o = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]), random.randint(1,5))  
                        all_sprites.add(o)
                        obstaculos.add(o)
                        boom_sound.play()
                    
                    screen.fill(BLACK)
                    
                    if SPECIAL and SpecialFrames<=300:
                        player.firerate = 0.01
                        SpecialFrames +=1
                    else:
                        player.resetFireRate()
                        
                    
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
                    if frame_count == 60*25:
                        for enemy in inimigos:
                            enemy.kill()
                        for obst in obstaculos:
                            obst.kill()
                        Boss = Inimigo(assets['boss_img'] , 3, boss = True)
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
                    
                    text_surface = score_font.render(chr(9829) * player.HP, True, RED)
                    text_rect = text_surface.get_rect()
                    text_rect.bottomleft = (10, HEIGHT - 10)
                    screen.blit(text_surface, text_rect)
                    
                    text_surface = score_font.render("{:08d}".format(counter), True, YELLOW)
                    text_rect = text_surface.get_rect()
                    text_rect.topleft = (10, 10)
                    screen.blit(text_surface, text_rect)
                    
                    if BossAlive:
                        text_surface = score_font.render(chr(9829) * int(Boss.HP/2), True, NEON_BLUE)
                        text_rect = text_surface.get_rect()
                        text_rect.bottomleft = ((WIDTH-WIDTH_STREET)/2 + WIDTH_STREET +10, HEIGHT - 10)
                        screen.blit(text_surface, text_rect)
                    
                    
                    # Depois de desenhar tudo, inverte o display.
                    pygame.display.flip()
                    frame_count += 1
            finally:
                running = False
                running2 = False
            
            score = counter 
            highscore(score,1)
            
            ###-----------------------------------------------------------###
            ###------------------FASE 1 ^ -------------FASE 2 v ----------###
            ###-----------------------------------------------------------###
                        
            
                
            
            
            try:
                for enemy in inimigos:
                    enemy.kill()
                for obst in obstaculos:
                    obst.kill()
                
                for j in range(1,6):
                    dado = random.randint(1,25)
                    if dado <= 5:
                        a = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]),j)
                        a.HP = 2
                        all_sprites.add(a)
                        obstaculos.add(a)

                    else:
                        a = Inimigo(assets['mob_img'],j)
                        a.HP = 2
                        all_sprites.add(a)
                        inimigos.add(a)
                    
                running2 = game_intro('beginfase2', passtype = 'key')
                load_fase_screen(assets['riogsul2'],2)
                game_intro('controls', passtype = 'key')
                carregar()
                Boss2Alive = False
                Boss2Killed = False
                Boss2Tested = True
                frame_count = 0
                player.HP = 5
                counter = 0
                player.resetFireRate()
                SPECIAL = False
                while running2:
                    if not Boss2Alive and Boss2Tested:
                        Boss2Killed = False
                    elif Boss2Alive:
                        Boss2Killed = False
                        Boss2Tested = False
                    else:
                        Boss2Killed = True
                    
                    if Boss2Killed:
                        running2 = False
                    
                    if player.HP <= 0:
                        
                        game_intro('game_over', passtype = 'key')
                        running2 = game_intro('beginfase2', passtype = 'key')
                        game_intro('controls', passtype = 'key')
                        if running2:
                            fired = False
                            fired_cooldown = 0
                            Shots_Fired = 0
                            r_down = False
                            l_down = False
                            frame_count = 0
                            game_on = True
                            background = assets['background']
                            background_posY = 0
                            background_aceleration = 10 
                            background_maxspeed = 7.5
                            Boss2Alive = False
                            Boss2Killed = False
                            Boss2Tested = True
                            SPECIAL = False
                            counter = 0
                            carregar()
                            for mob in inimigos:
                                mob.kill()
                            for i in range(1,6):
                                a = Inimigo(assets['mob_img'],i)
                                if a != None:
                                    all_sprites.add(a)
                                    inimigos.add(a)
                                    a.HP = 2
                            player.HP = 5
                            
                    keys = pygame.key.get_pressed()  #checking pressed keys
                    # Ajusta a velocidade do jogo.
                    clock.tick(FPS)
                    
                    # Processa os eventos (mouse, teclado, botão, etc).
                    for event in pygame.event.get():
                        
                        # Verifica se foi fechado
                        if event.type == pygame.QUIT:
                            running2 = False
                        
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
                            if event.key == pygame.K_LSHIFT and not SPECIAL:
                                SPECIAL = True
                                SpecialFrames = 0
                    
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
                                player.resetFireRate()
                                
                    if keys[pygame.K_SPACE] and not fired:
                        if Shots_Fired<=player.burstfire:
                            bullet = Bullet(assets['bullet_img'], player.rect.centerx, player.rect.top, player.speed)
                            all_sprites.add(bullet)
                            tiros.add(bullet)
                            Shots_Fired += 1
                            shoot_sound.play()
                        else:
                            Shots_Fired = 0
                            fired = True
                        
                    if fired:
                        fired_cooldown += 1
                    if fired_cooldown >= player.firerate:
                        fired_cooldown = 0
                        fired = False
                    hits = pygame.sprite.groupcollide(inimigos, tiros, False, True)
                    
                    
                    for hit in hits:
                        counter += 500
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
                            a.HP = 2
                        if hit.boss and hit.HP <= 0:
                            Boss2Alive = False
                            
                    hitsobst = pygame.sprite.groupcollide(obstaculos, tiros, True, True)
                    for hit in hitsobst:
                        
                        all_sprites.add(hit)
                        obstaculos.add(hit)
                            
                    if Boss2Alive and frame_count%15 == 0:
                        dadoi = random.randint(0,10)
                        if dadoi <2:
                            b = Bullet(assets['big_shot'], Boss.rect.centerx, Boss.rect.bottom, 0)
                        else:
                            b = Bullet(assets['bullet_img'], Boss.rect.centerx, Boss.rect.bottom, 0)
                        b.yspeed = 10
                        bossshots.add(b)
                        all_sprites.add(b)
                        #
                        
                    
                        
                    
                    
                    hit = pygame.sprite.spritecollide(player, inimigos, True, pygame.sprite.collide_circle)            
                    if hit:
                        boom_sound.play()
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
                        a.HP = 2
                    hit = pygame.sprite.spritecollide(player, bossshots, True, pygame.sprite.collide_circle)            
                    if hit:
                        player.HP -= 1
                        all_sprites.add(player)
                        boom_sound.play()
        
                        
                    hit_obst = pygame.sprite.spritecollide(player, obstaculos, True, pygame.sprite.collide_circle)            
                    if hit_obst:
                        player.HP -= 1
                        all_sprites.add(player)
                        o = Obstaculo(random.choice([assets['obstaculo1_img'],assets['obstaculo2_img']]), random.randint(1,5))  
                        all_sprites.add(o)
                        obstaculos.add(o)
                        boom_sound.play()
                    
                    screen.fill(BLACK)
                    
                    if SPECIAL and SpecialFrames<=300:
                        player.firerate = 0.01
                        SpecialFrames +=1
                    else:
                        player.resetFireRate()
                    
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
                            a.HP = 2             
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
                            a.HP = 2
        
                    all_sprites.update()        
                    if frame_count == 60*20:
                        for enemy in inimigos:
                            enemy.kill()
                        for obst in obstaculos:
                            obst.kill()
                        Boss = Inimigo(assets['boss_img'] , 3, boss = True)
                        all_sprites.add(Boss)
                        inimigos.add(Boss)
                        Boss.HP = 20
                        Boss2Alive = True
                            
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
                    
                    text_surface = score_font.render("{:08d}".format(counter), True, YELLOW)
                    text_rect = text_surface.get_rect()
                    text_rect.topleft = (10, 10)
                    screen.blit(text_surface, text_rect)
                    
                    text_surface = score_font.render(chr(9829) * player.HP, True, RED)
                    text_rect = text_surface.get_rect()
                    text_rect.bottomleft = (10, HEIGHT - 10)
                    screen.blit(text_surface, text_rect)
                    
                    if Boss2Alive:
                        text_surface = score_font.render(chr(9829) * int(Boss.HP/2), True, NEON_BLUE)
                        text_rect = text_surface.get_rect()
                        text_rect.bottomleft = ((WIDTH-WIDTH_STREET)/2 + WIDTH_STREET +10, HEIGHT - 10)
                        screen.blit(text_surface, text_rect)
                        
                    # Depois de desenhar tudo, inverte o display.
                    pygame.display.flip()
                    frame_count += 1
            finally:
                running2 = False
                running = False
                game_on = False
                
            
            score = counter 
            highscore(score, 2)
            
            game_intro('victory', passtype = 'key')
            pygame.quit()
            pass
    finally:
        pass
            



Main()