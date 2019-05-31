# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:00:55 2019

@author: André Luis Silva Lop
"""

import pygame
import random
import json


## IMPORTING FILE FROM CONSTS AND RECREATING THE DICTIONARY WITH IMPORTANT VARIABLES 
with open('consts.txt', 'r') as consts_txt:
    conteudo = consts_txt.read()
    consts = json.loads(conteudo)

## RENAMING VARIABLES LOCALLY
FPS = consts['FPS']
HEIGHT = consts['HEIGHT']
WIDTH = consts['WIDTH']
WIDTH_STREET = consts['WIDTH_STREET'] 
BLACK = consts['BLACK']
RED = consts['RED']

## ENEMY CLASS
class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, img, col = 1, size = 15, boss = False):
        
        ## MAIN CONSTRUCTOR
        pygame.sprite.Sprite.__init__(self)
        
        ## SETTING UP SPRITE IMAGE
        self.image = img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        ## COLLISION RADIUS
        self.radius = int(self.rect.width * 0.85 / 2)
        
        self.speedy = 0
        ## BOOLEAN FOR WHETHER ENEMY IS BOSS OR NOT
        self.boss = boss
        
        self.speedx = 5
        
        self.size = size
        
        self.col = col
        
        self.rect.centerx = ((WIDTH-WIDTH_STREET)/2) + (col * WIDTH_STREET/5 - self.rect.width)
        
        self.rect.top = random.randint(-300,-100)
        
        self.HP = 1
        
        if self.boss:
        
            self.rect.centerx = ((WIDTH-WIDTH_STREET)/2) + (col * WIDTH_STREET/5 - self.rect.width)
            
            self.rect.y = 5
            
            self.speedx = random.randint(-5,5)
            if self.speedx == 0:
                self.speedx = random.randint(-5,5)
            if self.speedx == 0:
                self.speedx = random.randint(-5,5)


    def update(self):
        if self.HP <=0:
            self.kill()
            self.boss = False
        if self.boss:
            if self.rect.x <= (WIDTH-WIDTH_STREET)/2:
                self.speedx = random.randint(2,7)
                self.rect.x = (WIDTH-WIDTH_STREET)/2
            if self.rect.x >= (WIDTH-WIDTH_STREET)/2 + WIDTH_STREET - self.rect.width:
                self.speedx = random.randint(-7,-2)
                self.rect.x = (WIDTH-WIDTH_STREET)/2 + WIDTH_STREET - self.rect.width
            self.rect.x += self.speedx    

        pass
    
    
    def updateSpeed(self, speedy):
        if not self.boss:
            self.rect.top += speedy
        else:
            pass
            
        
        