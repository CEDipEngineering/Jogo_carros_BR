# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:00:55 2019

@author: André Luis Silva Lop
"""

import pygame
import random
from consts import WIDTH
from consts import HEIGHT


class Inimigo(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, img, col = 1, size = 15, boss = False):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.35 / 2)
        self.speedy = 0
        self.boss = boss
        self.speedx = 0
        self.size = size
        self.col = col
        self.rect.centerx = col * (WIDTH/5)-self.rect.width
        self.rect.top = random.randint(-300,-100)
        self.HP = 1
        if self.boss:
            self.rect.centerx = WIDTH/2
            self.rect.y = 5
            self.speedx = random.randint(-5,5)
        
        
    def update(self):
        if self.HP <=0:
            self.kill()
            self.boss = False
        if self.boss:
            if self.rect.x <= 0:
                self.speedx = random.randint(2,7)
                self.rect.x = 1
            if self.rect.x >= WIDTH - self.rect.width:
                self.speedx = random.randint(-7,-2)
                self.rect.x = WIDTH - self.rect.width -1
            self.rect.x += self.speedx    

        pass
    
    
    def updateSpeed(self, speedy):
        if not self.boss:
            self.rect.top += speedy
        else:
            pass
            
        
        