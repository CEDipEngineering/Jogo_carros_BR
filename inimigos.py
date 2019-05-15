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
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-50)
        self.radius = int(self.rect.width * .85 / 2)
        self.speedy = 0
    def update(self):
#        self.rect.top += self.speedy
        pass
    
    def updateSpeed(self, speedy):
        self.rect.top += speedy
        
#        
#        # loading eneies again
#        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
#            
#            self.rect.x = random.randrange(WIDTH - self.rect.width)
#            
#            self.rect.y = random.randrange(-100, -40)
#            
#            self.speedx = random.randrange(-3, 3)
#            
#            self.speedy = random.randrange(2, 9)
#            
