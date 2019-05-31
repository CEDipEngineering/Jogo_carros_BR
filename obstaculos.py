#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 07:56:09 2019

@author: joaopedrochacon
"""
# IMPORTS

import pygame
import random
import json

## READING A JSON FILE FOR CONSTANTS 
with open('consts.txt', 'r') as consts_txt:
    conteudo = consts_txt.read()
    consts = json.loads(conteudo)

## DEFINING CONSTANTS FROM JSON FILE   
FPS = consts['FPS']
HEIGHT = consts['HEIGHT']
WIDTH = consts['WIDTH']
WIDTH_STREET = consts['WIDTH_STREET'] 
BLACK = consts['BLACK']
RED = consts['RED']

## CLASS FOR OBSTACLES IN THE GAME 
class Obstaculo(pygame.sprite.Sprite):
    
    ## CLASS CONSTRUCTOR
    def __init__(self, img, col = 1, size = 15):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2) ## RADIUS FROM THE OBJECTS (TO IMPLEMENT COLISION)
        self.speedy = 0
        self.size = size
        self.col = col
        self.rect.centerx = ((WIDTH-WIDTH_STREET)/2) + (col * WIDTH_STREET/5 - self.rect.width)
        self.rect.top = random.randint(-300,-100)
    
    def updateSpeed(self, speedy):
        self.rect.top += speedy
        
            