#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

import random


def saisieCoup(jeu):
	""" jeu -> coup
		Retourne un coup a jouer
	"""
	coupsValides = game.getCoupsValides(jeu)
	#print("Liste des coups jouables: "+str(coupsValides))
	if len(coupsValides) > 0:
		selectedCoup = random.choice(coupsValides)
	else:
		selectedCoup = []

	return selectedCoup
