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
	
	selectedCoup = random.choice(coupsValides)

	return selectedCoup
