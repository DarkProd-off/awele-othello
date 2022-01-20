#!/usr/bin/env python
# -*- coding: utf-8 -*-
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

tailleX = 2
tailleY = 4

#Init plateau
plateau = []

#Lignes
for p in range(tailleX):
	plateau.append([])

	#Colonnes
	for w in range(tailleY):
		plateau[p].append(0)


jeu = game.initialiseJeu()

game.affiche(jeu)