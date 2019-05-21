# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:31:57 2019

@author: Carlos Dip
"""
import pygame
from consts import HEIGHT
from consts import WIDTH
class Player (pygame.sprite.Sprite):
    
    def __init__(self, img):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.size = 15
        self.acc = 0
        self.accY = 0
        self.speed = 0
        self.speedY = 0
        self.power = 0.5
        self.SpeedLimit = 4
        self.xpos = WIDTH / 2
        self.rect.centerx = self.xpos
        self.ypos = HEIGHT - self.size
        self.rect.bottom = self.ypos
        self.firerate = 20
        self.burstfire = 0
        self.HP = 5
        
        #Criando atributos de tanque de gasolina 
        
#        espaco_tanque = 0
#        gasolina = [0, 10, 20, 30, 40, 50, 60, 70, 80, 100]
        

        
    def update(self):
        # Physics
        
        if abs(self.speed) <= self.SpeedLimit:
            self.speed += self.acc
        else:
            if self.speed > 0:
                self.speed = self.SpeedLimit
            else:
                self.speed = -self.SpeedLimit
                
        if abs(self.speedY) <= self.SpeedLimit:
            self.speedY += self.accY
        else:
            if self.speedY > 0:
                self.speedY = self.SpeedLimit
            else:
                self.speedY = -self.SpeedLimit
        
        self.xpos += self.speed
        self.ypos += self.speedY
        
        # Position
        self.rect.centerx = self.xpos
        self.rect.bottom = self.ypos
        
        #Keep in screen (Crash into walls)
        if self.xpos >= WIDTH:
            self.xpos = WIDTH
            self.speed = 0
            self.acc = 0
        if self.xpos <= 0:
            self.xpos = 0
            self.speed = 0
            self.acc = 0
            
        #Keep in the bottom area
        if self.ypos <= HEIGHT - 200:
            self.ypos = HEIGHT - 200
            self.speedY = 0
            self.accY = 0
        if self.ypos >= HEIGHT - self.size:
            self.ypos = HEIGHT - self.size
            self.speedY = 0
            self.accY = 0