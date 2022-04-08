#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

import math

# Paramètres
horizon=3

global poids;
poids = [1.9998600041999308, -0.9998600090996368, -0.9997600275979776]
#poids = [2,-1,-1]

def dot(v1,v2):
    """ Hypothèse : len(v1)==len(v2)
    """
    return sum([v1[i]*v2[i] for i in range(len(v1))])

def estimation(jeu,coup,horizon):
    """
    Implémentation de l'algorithme minimax
    """
    copie=game.getCopieJeu(jeu)
    game.joueCoup(copie,coup)
    if horizon==0 or game.finJeu(copie):
        return evaluation(copie)
    
    listeCoupsVal = game.getCoupsValides(copie)
    
    if joueur==game.getJoueur(copie): # si joueur ami
        val=-math.inf
        for nouvCoup in listeCoupsVal:
            val=max(val,estimation(copie,nouvCoup,horizon-1))
        return val           
    
    else: # si joueur ennemi
        val=math.inf
        for nouvCoup in listeCoupsVal:
            val=min(val,estimation(copie,nouvCoup,horizon-1))      
        return val

def evaluation(jeu):
    """jeu->int
    Hypothèse : coup est valide (assuré dans saisieCoup)
    Évalue la qualité d'un coup
    """
    if(game.finJeu(jeu)):
        if(joueur==game.getGagnant(jeu)):
            return 1000
        if(game.getGagnant(jeu)==3-joueur):
            return -1000
        if(game.getGagnant(jeu)==0):
            return -50
        
    param=[]
    
    # différence de score
    diffScores = game.getScore(jeu,joueur)-game.getScore(jeu,3-joueur)
    param.append(diffScores)

    # nombre de cases vides
    nbCasesVides=0
    for i in range(0,6):
        if(game.getCaseVal(jeu,joueur-1,i)==0):
            nbCasesVides=nbCasesVides+1
    param.append(nbCasesVides)

    # nombre de cases vulnerables
    nbCasesVulnerables=0
    for i in range(0,6):
        if(game.getCaseVal(jeu,joueur-1,i)==1 or game.getCaseVal(jeu,joueur-1,i)==2 ):
            nbCasesVulnerables=nbCasesVulnerables+1
    param.append(nbCasesVulnerables)
    
            
    return dot(poids,param)
    

def decision(jeu):
    #On fait la décision
    listeCoups = game.getCoupsValides(jeu)
    meilleurScore = -math.inf
    if game.getJoueur(jeu) == joueur:
        listeCoups.reverse()
    
    meilleurCoup = listeCoups[0]
    for coup in listeCoups:
        scoreEval = estimation(jeu,coup,horizon)
        if meilleurScore < scoreEval:
            meilleurCoup = coup
            meilleurScore = scoreEval
    return meilleurCoup

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    global joueur # attention : ne pas nommer un paramètre de fonction "joueur" !
    joueur = game.getJoueur(jeu)
    meilleurCoup=decision(jeu)
    return meilleurCoup
