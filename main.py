#Main.py
#Main Program othello or awele

import sys
sys.path.append("..")

import awele
sys.path.append("../..")

import game
game.game = awele
sys.path.append("../Joueurs")

import joueur_humain
import joueur_random

game.joueur1 = joueur_humain 
game.joueur2 = joueur_random 