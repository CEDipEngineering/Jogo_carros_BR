# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:39:55 2019

@author: André Luis Silva Lop
"""
import pygame
from os import path
from consts import WIDTH
from consts import HEIGHT
from consts import FPS
from consts import BLACK

img_dir = path.join(path.dirname(__file__), 'Assets')
img_dir = path.join(img_dir,'img')

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Name
pygame.display.set_caption("Jogos carros BR")

clock = pygame.time.Clock()

# Loading Background

background = pygame.image.load(path.join(img_dir, 'road.png')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_posY = 0




try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        relative_y = background_posY % background.get_rect().height
        screen.blit(background, (0,relative_y - background.get_rect().height))
        if relative_y < HEIGHT:
            screen.blit(background, (0,relative_y))
        background_posY += 5
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()