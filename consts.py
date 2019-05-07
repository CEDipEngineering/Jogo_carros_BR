# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:01:00 2019

@author: Carlos Dip
"""
from os import path
import json 

WIDTH = 800
HEIGHT = 100
FPS = 60 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
img_dir = path.join(path.dirname(__file__), 'Assets\img')

consts = {'WIDTH': WIDTH, 'HEIGHT': HEIGHT,
          'FPS': FPS, 'WHITE': WHITE,
          'BLACK': BLACK, 'RED': RED,
          'GREEN': GREEN, 'BLUE': BLUE,
          'YELLOW': YELLOW, 'img_dir': img_dir}


with open('consts.txt','w') as consts_txt:
    x = json.dumps(consts, indent = 4, sort_keys = True )
    consts_txt.write(x)

