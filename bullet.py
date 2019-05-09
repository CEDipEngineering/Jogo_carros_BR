# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:43:59 2019

@author: Carlos Dip
"""

import json
import pygame


pygame.init()

with open('consts.txt', 'r') as consts_txt:
    conteudo = consts_txt.read()
    consts = json.loads(conteudo)

FPS = consts['FPS']
HEIGHT = consts['HEIGHT']
WIDTH = consts['WIDTH']
BLACK = consts['BLACK']
RED = consts['RED']

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, img, playerx, playery, playerxspeed):
        pygame.sprite.Sprite.__init__(self)
        
        
        self.image = img
        self.xspeed = playerxspeed
        self.yspeed = -10
        self.xpos = playerx
        self.ypos = playery
#        self.
#        self.
#        self.
        self.rect = self.image.get_rect()
        self.rect.centerx = self.xpos
        self.rect.bottom = self.ypos
        
        
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        
        if self.rect.bottom <=0 or self.rect.centerx >= WIDTH or self.rect.centerx <=0:
            self.kill()
            
    
        