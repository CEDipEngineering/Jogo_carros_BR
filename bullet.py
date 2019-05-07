# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:43:59 2019

@author: Carlos Dip
"""

import pygame


class Bullet(pygame.sprite.Sprite):
    
    def __init(self, img, playerx ,playery , playerxspeed):
        
        
        self.image = img
        self.xspeed = playerxspeed
        self.yspeed = -10
        self.xpos = playerx
        self.ypos = playery
#        self.
#        self.
#        self.
        self.rect = self.image.get_rect()
        
        
    def update(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed
        
        if self.rect.bottom <=0 or self.rect.centerx >= WIDTH or self.rect.centerx <=0:
            self.kill()
            
        
        