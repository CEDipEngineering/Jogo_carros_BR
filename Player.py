# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:31:57 2019

@author: Carlos Dip
"""
import pygame
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


## PLAYER CLASS
class Player (pygame.sprite.Sprite):
    
    def __init__(self, img):
        
        ## MAIN CONSTRUCTOR
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        
        self.rect = self.image.get_rect()
        
        self.image.set_colorkey((0,0,0))
        
        self.size = 15
        
        ## PROPERTIES RELATED TO SPEED AND ACCELERATION 
        self.acc = 0
        
        self.accY = 0
        
        self.speed = 0
        
        self.speedY = 0
        
        self.power = 0.5
        
        self.SpeedLimit = 4
        
        ## DEFINING PLAYER STARTING POSTION
        self.xpos = WIDTH / 2
        
        self.rect.centerx = self.xpos
        
        self.ypos = HEIGHT - self.size
        
        self.rect.bottom = self.ypos
        
        ## PLAYER FIRERATE
        self.firerate = 20
        
        self.burstfire = 0
        
        ## PLAYER LIFE
        self.HP = 5
        
        ## COLISION RADIUS
        self.radius = int(self.rect.width * 0.85 / 2)
            

        
    def update(self):
        ## PHYSICS
        
        if abs(self.speed) <= self.SpeedLimit:
            self.speed += self.acc
        else:
            if self.speed > 0:
                self.speed = self.SpeedLimit
            else:
                self.speed = - self.SpeedLimit
                
        if abs(self.speedY) <= self.SpeedLimit:
            self.speedY += self.accY
        else:
            if self.speedY > 0:
                self.speedY = self.SpeedLimit
            else:
                self.speedY = - self.SpeedLimit
        
        self.xpos += self.speed
        self.ypos += self.speedY
        
        ## POSITION
        self.rect.centerx = self.xpos
        self.rect.bottom = self.ypos
        
        ## KEEP IN SCREEN (CRASH INTO WALLS)
        if self.xpos >= (WIDTH-WIDTH_STREET)/2 + WIDTH_STREET - self.rect.width:
            self.xpos = (WIDTH-WIDTH_STREET)/2 + WIDTH_STREET  - self.rect.width
            self.speed = 0
            self.acc = 0
        if self.xpos <= (WIDTH-WIDTH_STREET)/2  + self.rect.width:
            self.xpos = (WIDTH-WIDTH_STREET)/2  + self.rect.width
            self.speed = 0
            self.acc = 0
            
        ## KEEP IN THE BOTTOM AREA
        if self.ypos <= HEIGHT - 200:
            self.ypos = HEIGHT - 200
            self.speedY = 0
            self.accY = 0
        if self.ypos >= HEIGHT - self.size:
            self.ypos = HEIGHT - self.size
            self.speedY = 0
            self.accY = 0
    
    def resetFireRate(self):
        self.firerate = 20