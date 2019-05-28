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
WIDTH_STREET = consts['WIDTH_STREET'] 
BLACK = consts['BLACK']
RED = consts['RED']

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, img, playerx, playery, playerxspeed):
        pygame.sprite.Sprite.__init__(self)
        
        
        self.image = img
        self.xspeed = playerxspeed
        self.yspeed = -10
        self.image.set_colorkey((0,0,0))
        self.xpos = playerx
        self.ypos = playery
        self.rect = self.image.get_rect()
        self.rect.centerx = self.xpos
        self.rect.bottom = self.ypos
        self.radius = int(self.rect.width * 0.85 / 2)
        
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        
        if self.rect.bottom <=0 or self.rect.centerx >= (WIDTH-WIDTH_STREET)/2 + WIDTH_STREET or self.rect.centerx <= (WIDTH-WIDTH_STREET)/2 or self.rect.y >= HEIGHT:
            self.kill()
            
    
        