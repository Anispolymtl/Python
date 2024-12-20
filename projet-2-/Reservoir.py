# -*- coding: utf-8 -*-
# Nom_du_fichier: Reservoir.py
# Creer le      : 
# Creer par     : Anis MENOUAR 
# Version num   : 
# Modifier le   : 

import matplotlib.pyplot as plt
from IPython.display import clear_output
from Molecule import moleculesSeTouche, deplacerMolecule, creerListMolecules
from Molecule import ajusteDirApresCollision, inverseDirMolecule


def creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD):
    #TODO 3.2.1 Créer le structure de données d'un réservoir
    # Utiliser creerListMolecules (voir 3.1.5)
    moleculesG = creerListMolecules(hauteur, 0, posParoi, nbMoleculesG)
    moleculesD = creerListMolecules(hauteur, posParoi, largeur, nbMoleculesD)
    import math
    nbCollisions = math.factorial(nbMoleculesG + nbMoleculesD) // (2 * math.factorial(nbMoleculesG + nbMoleculesD - 2)) 
    #r=2, car dans notre situation, chaque collision implique deux molécules

    #Dictionnaire du réservoir 
    reservoir = {"hauteur": hauteur,
        "largeur": largeur,
        "posParoi": posParoi,
        "moleculesG": moleculesG,
        "moleculesD": moleculesD,
        "collisions": [0] * nbCollisions}
    return reservoir



def colision(reservoir):
    #TODO 3.2.2 Vérifier si il y a des collisions entre des molécules dans un réservoir
    # Pour chaque molécule vérifier si elles est en collision avec une autre molécule du réservoir
    lCG = []  
    lCD = []  
    for i in range(len(reservoir['GAUCHE']['molécules'])):
        lCG.append([0] * len(reservoir['GAUCHE']['molécules']))

    for i in range(len(reservoir['GAUCHE']['molécules'])):
        for j in range(i + 1, len(reservoir['GAUCHE']['molécules'])):
            if reservoir['GAUCHE']['molécules'][i].moleculesSeTouche(reservoir['GAUCHE']['molécules'][j]):
                lCG[i][j] = 1
                lCG[j][i] = 1
                reservoir['GAUCHE']['molécules'][i].ajusteDirection(reservoir['GAUCHE']['molécules'][j])

    for i in range(len(reservoir['DROITE']['molécules'])):
        lCD.append([0] * len(reservoir['DROITE']['molécules']))
    for i in range(len(reservoir['DROITE']['molécules'])):
        for j in range(i + 1, len(reservoir['DROITE']['molécules'])):
            if reservoir['DROITE']['molécules'][i].moleculesSeTouche(reservoir['DROITE']['molécules'][j]):
                lCD[i][j] = 1
                lCD[j][i] = 1
                reservoir['DROITE']['molécules'][i].ajusteDirection(reservoir['DROITE']['molécules'][j])

  
    reservoir['GAUCHE']['collisions'] = lCG
    reservoir['DROITE']['collisions'] = lCD

    return reservoir


def inverseDirMolecules(reservoir):
    #TODO 3.2.3 Ajuster la direction des molécules qui touchent aux parois dans chaque réservoir
    # Faire appel à inverseDirMolecule(mol, paroiG, paroiD, hauteur) (3.2.3)
    for mol in reservoir['gauche']:
        if mol['position'] <= 0 and mol['direction'] == -1:
            inverseDirMolecule(mol, 'gauche', 'droite', reservoir['hauteur'])
    for mol in reservoir['droite']:
        if mol['position'] >= reservoir['longueur'] and mol['direction'] == 1:
            inverseDirMolecule(mol, 'droite', 'gauche', reservoir['hauteur'])
    return reservoir

def getTemperature(reservoir, cote):
    #TODO 3.2.4 Calcule la température de chaque côté du réservoir.
    # Utiliser la formule dans le Readme
    N = len(reservoir[cote]['molécules'])
    # énergie
    import math
    E = 0
    for molecule in reservoir[cote]['molécules']:
        v = math.sqrt(molecule['dx']**2 + molecule['dy']**2)
        E += 0.5 * v**2
    T = E / N
    
    return T


#####################################################
# Donner
#####################################################
def affichage(reservoir, ax):
    txt = "Température côté Gauche: {:.2f}C \t\t\t\t\t Température côté Droit: {:.2f}C".expandtabs()

    ax.plot([reservoir['posPar'], reservoir['posPar']], [0, reservoir['h']], 'k-', linewidth=10)
    ax.axis([-20, reservoir['l'] + 20, -20, reservoir['h'] + 20])
    ax.title.set_text(txt.format(getTemperature(reservoir, "Gauche"), getTemperature(reservoir, "Droite"))) 

    for k in [['mG', 'ro'], ['mD', 'go']]:
        for i in range(len(reservoir[k[0]])):
            inte = min(max((abs(reservoir[k[0]][i]['dx']) + abs(reservoir[k[0]][i]['dy'])) / 60, 0.2), 1)
            ax.plot(reservoir[k[0]][i]['x'], reservoir[k[0]][i]['y'], k[1], alpha=inte, ms=reservoir[k[0]][i]['rayon'])
            reservoir[k[0]][i] = deplacerMolecule(reservoir[k[0]][i])

    plt.pause(0.01)
    clear_output() 
    

def deplacerMolecules(reservoir, ax):
    # TODO 3.2.6
    # deplacer_molecule deplace les molecules du reservoir
    # Cette function recoit comme parametre un objet de type reservoire est execute les etapes suivantes:
    # 1) Inverser la direction des molecules du reservoir
    inverseDirMolecules(reservoir)
    # 2) Afficher les molecules
    affichage(reservoir, ax)
    # 3) Determination des colision des molecules
    colision(reservoir)
    return reservoir

if __name__ == '__main__':
    hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD = 2000, 2000, 1300, 30, 30
    reservoir = creerReservoir(hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD)
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot()
    for i in range(1000):
        reservoir = deplacerMolecules(reservoir, ax)
        ax.clear()