#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 07:56:09 2019

@author: joaopedrochacon
"""

import pygame
import random
from consts import WIDTH
from consts import HEIGHT

class Obstaculo(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, img, col = 1, size = 15):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.35 / 2)
        self.speedy = 0
        self.size = size
        self.col = col
        self.rect.centerx = col * (WIDTH/5)-self.rect.width
        self.rect.top = random.randint(-300,-100)
    
    def updateSpeed(self, speedy):
        self.rect.top += speedy
        
            