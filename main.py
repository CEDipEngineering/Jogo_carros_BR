# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:07:56 2019

@author: Carlos Dip
"""
import pygame
from os import path
import json

def load_assets(img_dir):
    assets = {}
    assets['player_img'] = 

    return assets
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
assets = load_assets()
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


for i in range(10):
    a = Inimigo(pygame.image.load(path.join(img_dir, "Temp_car_sprite.png")).convert())
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
                        b = Bullet(bullet_img, player.rect.centerx, player.rect.bottom, player.speed)
                        all_sprites.add(b)
    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.acc = 0
                    if event.key == pygame.K_RIGHT:
                        player.acc = 0
                        
            all_sprites.update()
            
            screen.fill((87,87,87))
    #        screen.blit(background)
            
            all_sprites.draw(screen)
            
            
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
            
    finally:
        pygame.quit()
Main()