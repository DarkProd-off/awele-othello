#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

import sys
sys.path.append("..")
import game

tailleX = 8 #Normalement fix forcé à 8
tailleY = 8

def initialiseJeu():
    """Jeu othello"""

    #Init plateau
    plateau = []

    #Lignes
    for i in range(tailleX):
        plateau.append([])
		#Colonnes
        for k in range(tailleY):
            if((i==3 and k==3) or (i==4 and k==4)):
                plateau[i].append('B')
            elif((i==4 and k==3) or (i==3 and k==4)):
                plateau[i].append('N')
            else:
                 plateau[i].append('X')

    return [plateau, 1, None, [], (0,0)]

