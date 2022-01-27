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

import time

jeu = game.initialiseJeu()

game.affiche(jeu)


def partie():
	jeu = game.initialiseJeu()
	print()
	while not game.finJeu(jeu):
		coup = game.saisieCoup(jeu)
		game.joueCoup(jeu, coup)

	return game.getGagnant(jeu)

print("Le gagnant est: " + str(partie()))

"""
lstCoupsValides = game.listeCoupsValides(jeu)


	for x in range(len(lstCoupsValides)):
		if coupValide(jeu, lstCoupsValides[x]):
			return lstCoupsValides[x]

	return lstCoupsValides[0]
"""