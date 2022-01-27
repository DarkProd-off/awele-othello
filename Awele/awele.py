#!/usr/bin/env python
# -*- coding: utf-8 -*-

def initialiseJeu():
	"""Jeu Awele"""
	tailleX = 2
	tailleY = 6

	#Init plateau
	plateau = []

	#Lignes
	for p in range(tailleX):
		plateau.append([])

		#Colonnes
		for w in range(tailleY):
			plateau[p].append(4)

	return [plateau, 1, [], None, (0,0)]

def joueCoup(jeu, coup):
	if coupValide(jeu, coup):
		score = getScores(jeu, jeu[1])

		if jeu[1] == 1:
			
			score1, score2 = jeu[4]
			jeu[4] = (score1 + X, score2) 
		else:
			score1, score2 = jeu[4]
			jeu[4] = (score1, score2 + X) 

		changeJoueur(jeu)

def getGagnant(jeu):
	if jeu[4][0] > jeu[4][1]:
		return 1
	elif jeu[4][0] < jeu[4][1]:
		return 2
	else:
		return 0

def estAffame(jeu, joueur):
	return sum(jeu[0][joueur - 1]) == 0

def estValide(jeu, coup, checkNourrit=False):
	if not (coup[0] == (jeu[1]-1)):
		return False

	g = jeu[0][coup[0]][coup[1]]

	if g == 0:
		return False

	if checkNourrit:
		if coup[0] == 0:
			return g > coup[1]
		if coup[0] == 1:
			return g > (5 - coup[1])

	return True

def listeCoupsValides(jeu):
	affame = estAffame(jeu, jeu[1] % 2 + 1)
	print("Affamé:" + str(affame))

	return [(jeu[1] - 1, c) for c in range(6) if estValide(jeu, (jeu[1] - 1, c), affame)]


def finJeu(jeu):
	return estAffame(jeu, jeu[1])