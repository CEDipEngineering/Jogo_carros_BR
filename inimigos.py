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
    def __init__(self, img, col):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.speedy = 0
        self.BOSS = False
        self.rect.x = col * (WIDTH-self.rect.width)/5
        self.rect.top = random.randint(-100,-50)
    def update(self):
#        self.rect.top += self.speedy
        pass
    
    def updateSpeed(self, speedy):
        self.rect.top += speedy
    
            
        
        