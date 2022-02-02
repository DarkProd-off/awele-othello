#!/usr/bin/env python
# -*- coding: utf-8 -*-
import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain


jeu = game.initialiseJeu()

game.affiche(jeu)


'''def partie():
	jeu = game.initialiseJeu()

	while not game.finJeu(jeu):
		coup = game.saisieCoup(jeu)
		game.joueCoup(jeu, coup)
		game.affiche(jeu)

	game.affiche(jeu)
	return game.getGagnant(jeu)

print("Le gagnant est: " + str(partie()))'''