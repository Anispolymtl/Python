# -*- coding: utf-8 -*-

def indiceMinimum(vec): 
    #To do: Trouve l’indice et la valeur minimum dans un vecteur
    indice, minimum = -1, -1
    for i in vec: 
        indice += 1
        if i == -1: 
            continue
        else: 
            if minimum == -1:
                minimum = i
            else: 
                if minimum>i:
                    minimum = i 
        
    return vec.index(minimum), minimum

    
def noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis):
    #To do: Cherche le nœud non visité ayant le poids minimum autour d’un nœud spécifique
    #To do: utiliser la fonction indiceMinimum(vec)
    #1) extraire la ligne du neoud de la matrice
    list_mat = matrice[noeud]

    #2) affecter -1 pour chauqe noeud des noeuds_vis de la ligne
    for i in noeuds_vis:
        list_mat[i] = -1     

    #3) Trouve l’indice et la valeur minimum de la ligne
    indice, minimum = indiceMinimum(list_mat)
    
    return indice, minimum


def noeudMinimalNonVisites(matrice,noeuds_vis):
    #To do: Cherche le poids minimum entre un des nœuds visités et un de ses nœuds voisins
    #To do: utiliser la fonction noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)        
    for i in noeuds_vis:        
        arrive, poids = noeudMinimalNonVisitesDeNoeud(matrice, i , noeuds_vis)
        depart = matrice[arrive].index(poids)
    return depart, arrive    

def noeudsVoisins(matrice, noeud):
    #To do: Cherche les nœuds voisins et leur poids par rapport à un nœud initial.
    poids = []
    noeuds = []
    for i in matrice[noeud]:
        if i == -1:
            continue
        elif i != -1 : 
            poids.append(i)
            noeuds.append(matrice[noeud].index(i))

    return (noeuds, poids)

def dijkstra(matrice, depart, arrive):
    #To do: Calcule le plus court chemin entre un nœud de départ et un nœud d’arrivée.
    noeudVisites = []
    distanceMin = []
    predecesseursn = []    
    for n in matrice:
        distanceMin.append(-1)
        predecesseursn.append(-1)
    distanceMin[depart] = 0
    noeudCourant = depart
    while len(noeudVisites) != len(matrice) and noeudCourant != arrive:
        voisin, poids2 = noeudsVoisins(matrice, noeudCourant)
        x = 0
        for i in voisin:            
            distance = distanceMin[noeudCourant] + poids2[x]
            if distance < distanceMin[voisin[x]] or distanceMin[voisin[x]] == -1:
                distanceMin[voisin[x]] = distance
                predecesseursn[voisin[x]] = noeudCourant
            x += 1        
        noeudVisites.append(noeudCourant)
        noeudCourant, a = noeudMinimalNonVisitesDeNoeud(matrice, noeudCourant, noeudVisites)
    distance = distanceMin[arrive]                          
    
    return distance,predecesseursn


if __name__ == '__main__':
    vec     = [-1, 4, 6, -1, -1, 3, 5]
    indice, minimum = indiceMinimum(vec)
    txt = "la valeur minimale du vecteur est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud   = 1
    noeuds_vis = [1, 2, 3]
    indice, minimum = noeudMinimalNonVisitesDeNoeud(matrice, noeud, noeuds_vis)
    txt = "le poids minimum du noeud non visités est {} à la position {}"
    print(txt.format(minimum, indice))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 1
    noeudsVoisins(matrice, noeud)
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    noeud = 3
    noeuds, poids = noeudsVoisins(matrice, noeud)
    txt = "les noeuds voisin sont {} et leur poids {} rapport à un noeud {}"
    print(txt.format(noeuds, poids, noeud))
    
    matrice = [[-1, 20, 56, -1], [20, -1, 12, 17], [56, 12, -1, -1], [-1, 17, -1, -1]]
    depart  = 0
    arrive  = 3
    indice, prédécesseurs = dijkstra(matrice, depart, arrive)
    txt = "la distance la plus cours entre un noeud de départ {} et un noeud d’arrivée {} est {} avec les prédécesseurs {}"
    print(txt.format(depart, arrive, indice, prédécesseurs))
        