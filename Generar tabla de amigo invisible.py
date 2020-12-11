# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:19:15 2020

@author: Maria Rollan
"""

import random
import pandas as pd


nombres = ['Inés', 'María', 'Clara', 'Mari', 'Fer', 'Ana', 'Nacho', 'Belén', 'Agustín', 'Mina']
regalos = []
repetido = False


for x in nombres:
    print('\n \n', x)
    
    #Generamos un número aleatorio de la longitud de los participantes
    aleatorio = random.randint(0,len(nombres)-1)
    print('La persona a regalar es ', nombres[aleatorio])
    
    #Comprobamos si ya se ha asignado un regalado a esa persona
    for z in regalos:
        if z == nombres[aleatorio]:
            print(z, 'es igual a ', nombres[aleatorio], ', el nombre ya está cogido')
            repetido = True
            
    #Mientras el nombre sea el del usuario o ya se le haya asignado un regalador se repite el random
    while nombres[aleatorio] == x or repetido:
        #Generamos un nuevo aleatorio y ponemos el repetido en False para volver a comprobar
        aleatorio = random.randint(0,len(nombres)-1)
        repetido = False
        print('La persona a regalar es ', nombres[aleatorio])

        #Comprobamos si esa persona ya se le ha asignado regalador
        for z in regalos:
            if z == nombres[aleatorio]:
                print(z, 'es igual a ', nombres[aleatorio], 'el nombre ya está cogido')
                repetido = True

            
    #Cuando encontramos un nombre adecuado lo agregamos
    regalos.append(nombres[aleatorio])
    


#Creamos una tabla con las dos listas y lo guardamos en un csv
tabla = pd.DataFrame()
tabla ['Regaladores'] = nombres
tabla ['Regalados'] = regalos

tabla.to_csv('D:/Users/María Rollán/Documents/Programación y frikadas/Amigo invisible/amigo_invisible.csv')



        

