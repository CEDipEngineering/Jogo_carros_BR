# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:39:55 2019

@author: André Luis Silva Lop
"""

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Name
pygame.display.set_caption("Jogos carros BR")

clock = pygame.time.Clock()

# Loading Background

background = pygame.image.load(path.join(Assets_dir, 'road.png')).convert()
background_rect = background.get_rect()