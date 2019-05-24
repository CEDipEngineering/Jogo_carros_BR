# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:01:00 2019

@author: Carlos Dip
"""

import json 

WIDTH = 1080
WIDTH_STREET = 480
HEIGHT = 720
FPS = 60 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


consts = {'WIDTH': WIDTH, 'HEIGHT': HEIGHT,
          'FPS': FPS, 'WHITE': WHITE,
          'BLACK': BLACK, 'RED': RED,
          'GREEN': GREEN, 'BLUE': BLUE,
          'YELLOW': YELLOW, 'WIDTH_STREET': WIDTH_STREET}


with open('consts.txt','w') as consts_txt:
    x = json.dumps(consts, indent = 4, sort_keys = True )
    consts_txt.write(x)

