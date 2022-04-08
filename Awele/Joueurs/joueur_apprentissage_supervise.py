def apprentissage():
    epsilon = 1
    resJeu = 10
    j = 0
    game.joueur1.poids = [2,-1, -1]
    #meilleursPoids = open('poids', 'w')
    while j<500:
        epsilon=epsilon*0.99
        i = random.randrange(0,len(game.joueur1.poids))
        # i : le paramètre modifié
        s = random.randrange(-1,1,2)
        # s : choix entre 1 et -1
        game.joueur1.poids[i] = game.joueur1.poids[i]*s*epsilon
        stats1 = stats(10,1)
        
        #On change la place  des joueurs,le joueur apprenti est dans la place 2
        tmp = game.joueur2
        game.joueur2 = game.joueur1
        game.joueur1 = tmp
        stats2 = stats(10,2)
        
        
        nouvResJeu = stats1[1] +  stats2[1]
        #nouvResJeu : tuple ResJeu: int
        
        #On reprend le joueur 1 pour apprenti
        tmp = game.joueur2
        game.joueur2 = game.joueur1
        game.joueur1 = tmp
        
        
        if nouvResJeu > resJeu:
            resJeu = nouvResJeu
            with open('poids.txt', 'a') as meilleursPoids:
                meilleursPoids.write(str(game.joueur1.poids)+"\n")
            print(game.joueur1.poids)
            print("En tant que premier joueur :")
            afficheStats(stats1)
            print("En tant que deuxième joueur :")
            afficheStats(stats2)
            
        if(resJeu==20):
            break
        j+=1
    rgs=regression(joueur1.evaluations,sum(evaluations)/len(evaluations)) #La régression des évaluations

def regression(listescore,somme):
    w=0
    for score in listescore:
        if((score-somme)<1):
            somme=score
        w=w+(score-somme)*(score-somme)
    
    return w