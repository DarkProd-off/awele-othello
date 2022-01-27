#!/usr/bin/env python
# -*- coding: utf-8 -*-
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
game.joueur1=joueur_aleatoire
game.joueur2=joueur_aleatoire

import time

jeu = game.initialiseJeu()

#game.affiche(jeu)


def partie():
	jeu = game.initialiseJeu()
	#print()
	while not game.finJeu(jeu):
		coup = game.saisieCoup(jeu)
		game.joueCoup(jeu, coup)

	print(game.getScores(jeu))
	game.affiche(jeu)
	return game.getGagnant(jeu)

print("Le gagnant est: " + str(partie()))