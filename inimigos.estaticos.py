# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:00:55 2019

@author: André Luis Silva Lop
"""
#loading background

background = pygame.image.load(path.join(Assets_dir, 'road.png')).convert()



class Inimigo(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Class Constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Loading background image
        inim_img = pygame.image.load(path.join(Assets_dir, "enemy1.png")).convert()
        
        # Scaling #precisa ver a escala do fundo
        self.image = pygame.transform.scale(inim_img, (50, 38))
        
        # no Back
        self.image.set_colorkey(BLACK)
        
        # Positionig details
        self.rect = self.image.get_rect()
        
        # random x location
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # random y location
        self.rect.y = random.randrange(-100, -40)
        
        # colision radius
        self.radius = int(self.rect.width * .85 / 2)
        
    # update cars location
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # loading eneies again
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            
            self.rect.y = random.randrange(-100, -40)
            
            self.speedx = random.randrange(-3, 3)
            
            self.speedy = random.randrange(2, 9)