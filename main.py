# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:07:56 2019

@author: Carlos Dip
"""
import pygame
from os import path
import json


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
BLACK = consts['BLACK']
RED = consts['RED']
img_dir = path.join(path.dirname(__file__), 'Assets')
img_dir = path.join(img_dir,'img')





def load_assets(img_dir):
    assets = {}
    assets['player_img'] = pygame.image.load(path.join(img_dir, 'Red1.png')).convert()
    assets['player_img'] = pygame.transform.rotate(assets['player_img'], -90)
    assets['player_img'] = pygame.transform.scale(assets['player_img'], (25,25))
    assets['bullet_img'] = pygame.image.load(path.join(img_dir, 'Temp_car_sprite.png')).convert()
    assets['mob_img'] = pygame.image.load(path.join(img_dir, "Blue2.png")).convert()
    return assets


screen = pygame.display.set_mode((WIDTH, HEIGHT))
assets = load_assets(img_dir)
class Player (pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets['player_img']
        self.rect = self.image.get_rect()
        self.size = 15
        self.acc = 0
        self.speed = 0
        self.power = 0.15
        self.SpeedLimit = 4
        self.xpos = WIDTH / 2
        self.rect.centerx = self.xpos
        self.rect.bottom = HEIGHT - self.size
        
        #Criando atributos de tanque de gasolina 
        
#        espaco_tanque = 0
#        gasolina = [0, 10, 20, 30, 40, 50, 60, 70, 80, 100]
        

        
    def update(self):
        # Physics
        
        if abs(self.speed) <= self.SpeedLimit:
            self.speed += self.acc
        else:
            if self.speed > 0:
                self.speed = self.SpeedLimit
            else:
                self.speed = -self.SpeedLimit
        
        self.xpos += self.speed
        
        
        # Position
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 15
        self.rect.centerx = self.xpos
        
        #Keep in screen (Crash into walls)
        if self.xpos >= WIDTH:
            self.xpos = WIDTH
            self.speed = 0
            self.acc = 0
        if self.xpos <= 0:
            self.xpos = 0
            self.speed = 0
            self.acc = 0
        
        #código de implementação do tanque de gasolina 
#        
#        for i in range(gasolina):
#            self.espaco_tanque = gasolina[i]

#        if self.espaco_tanque <= 40:
#            tanque['Rio Grande de Sul].load
#        elif sel.espaco_tanque 
#            necessário idear condições melhores
       
            
            
            
            
            
            
            # Friction -- BETA
#        if self.acc>0:
#            self.acc-=0.9
#        elif self.acc<0:
#            self.acc+=0.9
#        else:
#            self.acc = 0
        

from inimigos import Inimigo
from bullet import Bullet       


player = Player()
clock = pygame.time.Clock()
#background = pygame.Rect(0,0,WIDTH,HEIGHT)

all_sprites = pygame.sprite.Group()            
inimigos = pygame.sprite.Group()
#b = Bullet(assets['bullet_img'])

for i in range(10):
    a = Inimigo(assets['mob_img'])
    all_sprites.add(a)
    inimigos.add(a)
    
    
all_sprites.add(player)




def Main():
    try:
        running = True
        while running:
            
            # Ajusta a velocidade do jogo.
            clock.tick(FPS)
            
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                
                # Verifica se foi fechado
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.acc -= player.power
                    if event.key == pygame.K_RIGHT:
                        player.acc += player.power
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(assets['bullet_img'], player.rect.centerx, player.rect.bottom, player.speed)
                        all_sprites.add(bullet)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                         
    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.acc = 0
                    if event.key == pygame.K_RIGHT:
                        player.acc = 0
                        
            all_sprites.update()
            
            screen.fill((0,0,0))
    #        screen.blit(background)
            
            all_sprites.draw(screen)
            
            
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
            
    finally:
        pygame.quit()
Main()