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
        
        # Class Constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Loading background image
        inim_img = img
        
        # Scaling #precisa ver a escala do fundo
        self.image = pygame.transform.scale(inim_img, (50, 38))
        
        # no Back
        self.image.set_colorkey((0,0,0))
        
        # Positionig details
        self.rect = self.image.get_rect()
        
        # random x location
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # random y location
        self.rect.y = random.randrange(0, HEIGHT/2)
        
        # colision radius
        self.radius = int(self.rect.width * .85 / 2)
        
#    # update cars location
    def update(self):
        self.rect.x += 0 
        self.rect.y += 0
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
