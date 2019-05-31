# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:01:00 2019

@author: Carlos Dip
"""

import json 


## CREATING VARIABLES WITH IMPORTANT GLOBAL VALUES
WIDTH = 1080        ## WIDTH OF SCREEN
WIDTH_STREET = 480  ## WIDTH OF STREET
HEIGHT = 720        ## HEIGHT OF SCREEN
FPS = 60            ## FRAMERATE

## COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (21, 105, 20)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 14)
NEON_BLUE = (4, 217, 255)


## DICTIONARY WITH VALUES 
consts = {'WIDTH': WIDTH, 'HEIGHT': HEIGHT,
          'FPS': FPS, 'WHITE': WHITE,
          'BLACK': BLACK, 'RED': RED,
          'GREEN': GREEN, 'BLUE': BLUE,
          'YELLOW': YELLOW, 'WIDTH_STREET': WIDTH_STREET, 'NEON_BLUE': NEON_BLUE}

## WRITING TO JSON FILE FOR IMPORTING ELSEWHERE
with open('consts.txt','w') as consts_txt:
    x = json.dumps(consts, indent = 4, sort_keys = True )
    consts_txt.write(x)

