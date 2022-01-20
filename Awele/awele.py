#!/usr/bin/env python
# -*- coding: utf-8 -*-

def initialiseJeu():
	"""Jeu Awele"""
	tailleX = 2
	tailleY = 4

	#Init plateau
	plateau = []

	#Lignes
	for p in range(tailleX):
		plateau.append([])

		#Colonnes
		for w in range(tailleY):
			plateau[p].append(4)

	return [plateau, 1, [], None, (0,0)]

def listeCoupsValides(jeu):

	


