# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:43:23 2019

@author: André Luis Silva Lop
"""
import json
                                                  
                                                  
dic_tanque = {'Rio Grande do Sul': {'fase1': 30, 'fase2': 40}, 'Santa Catarina': 
    {'fase1': 80}, 'Parana': {'fase1': 80}, 'Sao Paulo': {'fase1': 90, 'fase2': 100},
    'Rio de Janeiro': {'fase1': 70}, 'Minas Gerais': {'fase1': 80, 'fase2': 100}, 
    'Distro Federal': {'fase1': 100, 'fase2': 100, 'fase3': 100}}
    



with open('dic_tanque.txt','w') as dic_tanque_txt:
    x = json.dumps(dic_tanque, indent = 4, sort_keys = True )
    dic_tanque_txt.write(x)


    
    