# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:33:38 2020

@author: Maria Rollan
"""

import pandas as pd


tabla = pd.read_csv('D:/Users/María Rollán/Documents/Programación y frikadas/Amigo invisible/amigo_invisible.csv')

longitud = len(tabla.index)

print('En este sorteo participan:')
for j in range (longitud):
    print(tabla.iloc[j][1])
    
print('\n \n Introduce tu nombre para saber a quien regalas')
tu_nombre = input()

for x in range(longitud): 
    if tabla.iloc[x][1] == tu_nombre:
        print('regalas a ', tabla.iloc[x][2])