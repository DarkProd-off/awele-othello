import sys
sys.path.append("..")
import game
game.game="awele"


plateau = []



for i in range(8):
    plateau.append([]) 
    for j in range(8): 
        plateau[i].append(j) 

jeu = [plateau, 1, [], [], ('0','0')]

print(game.affiche(jeu))


