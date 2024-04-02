# -*- coding: utf-8 -*-

import random

def saisirMatrice():
    #To do: Saisit une matrice d’adjacence au clavier
    matrice = []
    nbNoeud = int(input("Donner le nombre de noeuds dans la matrice: "))
    nbPoids = int(input("Donner le nombre de poids dans la matrice: "))
    
    matrice = [[-1 for i in range(nbNoeud)] for j in range(nbNoeud)]
    
    for y in range(nbPoids):
        print("\t Saisir le poids ", y) 
        noeud1 = int(input("\t \t Donner le noeud dextrémité 1: "))
        noeud2=  int(input("\t \t Donner le noeud dextrémité 2: "))       
        poid = int(input("\t \t Saisir le poids: ")) 
        matrice[noeud1][noeud2] = poid
        matrice[noeud2][noeud1] = poid
    return matrice

def genereMatriceAleatoire(nb_noeuds):
    #To do: Génère une matrice d’adjacence de manière aléatoire
    matrice = []
    for i in range(nb_noeuds):
        matrice.append([])
        for x in range(nb_noeuds):
            matrice[i].append(-1)
    limite = int(random.randint((nb_noeuds//2)-1, (nb_noeuds//2)+1))
    for y in range(limite):        
        noeud1 = random.randint(0,nb_noeuds-1)
        noeud2 = random.randint(0,nb_noeuds-1)
        while noeud1 == noeud2:
            noeud2 = random.randint(0,nb_noeuds-1)
        poid = random.randint(1,99)
        matrice[noeud1][noeud2] = poid
        matrice[noeud2][noeud1] = poid

    return matrice

def afficheChemin(predecesseurs, depart, arrive):
    #To do: Affiche le chemin entre un nœud de départ et d’arrivé à partir du tableau de prédécesseurs
    
    chemin = [arrive]
    predecesseursn = arrive
    while predecesseursn != depart:
       predecesseursn = predecesseurs[predecesseursn]
       chemin.append(predecesseursn)
    chemin.reverse()
    chemin_final = ''    
    chemin_final = ' ==> '.join(str(n) for n in chemin)
    print(f'Le chemin à parcourir est :\n\t'f'DÉBUT : {chemin_final} : FIN')
    
    
    


if __name__ == '__main__':
    saisirMatrice()
    
    nb_noeuds = 5
    matAlea = genereMatriceAleatoire(nb_noeuds)
    txt = "la matrice aleatoire est: \n\t"
    for i in matAlea:
        for j in i:
            txt += "{}\t".format(j)
        txt += "\n\t"
    print(txt)
    
    predecesseurs = [-1, 0, 0, 2, 5, 2]
    depart = 0
    arrive = 4
    afficheChemin(predecesseurs, depart, arrive)
