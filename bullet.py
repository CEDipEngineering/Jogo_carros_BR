# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:43:59 2019

@author: Carlos Dip
"""

import json
import pygame

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


## BULLET CLASS
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, img, playerx, playery, playerxspeed):
        
        ## MAIN CONSTRUCTOR
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        ## GIVES THE BULLET AN X SPEED EQUAL TO THE INPUT, ALLOWING FOR SLANTED SHOOTING
        self.xspeed = playerxspeed
        
        self.yspeed = -10
        
        self.image.set_colorkey((0,0,0))
        
        ## SPAWNS THE BULLET AT THE PLAYER
        self.xpos = playerx
        self.ypos = playery
        
        self.rect = self.image.get_rect()
        
        self.rect.centerx = self.xpos
        
        self.rect.bottom = self.ypos
        
        ## COLLISION RADIUS
        self.radius = int(self.rect.width * 0.85 / 2)
        
    def update(self):
        
        ## MOVES BULLET
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        
        
        ## KEEPS BULLET INSIDE STREET, KILLING IT OTHERWISE
        if self.rect.bottom <=0 or self.rect.centerx >= (WIDTH-WIDTH_STREET)/2 + WIDTH_STREET or self.rect.centerx <= (WIDTH-WIDTH_STREET)/2 or self.rect.y >= HEIGHT:   
            self.kill()
            
    
        