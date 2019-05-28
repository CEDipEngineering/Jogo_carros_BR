#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 07:56:09 2019

@author: joaopedrochacon
"""

import pygame
import random
import json

with open('consts.txt', 'r') as consts_txt:
    conteudo = consts_txt.read()
    consts = json.loads(conteudo)

FPS = consts['FPS']
HEIGHT = consts['HEIGHT']
WIDTH = consts['WIDTH']
WIDTH_STREET = consts['WIDTH_STREET'] 
BLACK = consts['BLACK']
RED = consts['RED']


class Obstaculo(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, img, col = 1, size = 15):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        self.speedy = 0
        self.size = size
        self.col = col
        self.rect.centerx = ((WIDTH-WIDTH_STREET)/2) + (col * WIDTH_STREET/5 - self.rect.width)
        self.rect.top = random.randint(-300,-100)
    
    def updateSpeed(self, speedy):
        self.rect.top += speedy
        
            