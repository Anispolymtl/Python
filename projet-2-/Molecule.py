# -*- coding: utf-8 -*-
# Nom_du_fichier: Molecule.py
# Creer le      : 
# Creer par     : Anis MENOUAR
# Version num   : 
# Modifier le   : 

from random import randint, randrange

def creerMolecule(x, y, dx, dy, rayon):
    #TODO 3.1.1 Créer le dictionnaire pour représenter une molécule

    description_molecule = {"x": x,
                "y": y,    
                "dx": dx,
                "dy": dy,
                "rayon": rayon}

    return description_molecule



def moleculesSeTouche(mol_1, mol_2):
    #TODO 3.1.2 Implémenter la formule pour vérifier si deux molécules se touche
    # Renvoi vrai si les molécules se touchent, faux si non
    import math
    distante_ente_molecule = math.sqrt((mol_1["x"]-mol_2["x"])**2 + (mol_1["y"]-mol_2["y"])**2)
    somme_rayon = mol_1["r"]+mol_2["r"]
    if distante_ente_molecule < somme_rayon :
        return True 
    else:
        return False 
    


def deplacerMolecule(mol):
    #TODO 3.1.3 Faire le déplacement de la molécule
    deplacement_molecule_x = mol["x"] + mol["x"] 
    deplacement_molecule_y = mol["y"] + mol["y"]

    return mol

    
#####################################################
# Donner
#####################################################
def ajusteDirApresCollision(mol_1, mol_2):
    deltaX = mol_2['x'] - mol_1['x']
    dVx = 0;

    if (deltaX == 0.0):
        dVy = mol_2['y'] - mol_1['y']
    else:
        r = (mol_2['y'] - mol_1['y']) / deltaX
        dVx = (mol_2['dx'] - mol_1['dx'] + (mol_2['dy'] - mol_1['dy']) * r) / (1 + r * r)
        dVy = r * dVx

    mol_1['dx'] += dVx
    mol_1['dy'] += dVy
    mol_2['dx'] -= dVx
    mol_2['dy'] -= dVy

    return mol_1, mol_2

def creerListMolecules(hauteur,xmin,xmax,nbMolecules):
    #TODO 3.1.5 Remplir la liste de molécule comme déctrit dans le README
    # vous pouvez utiliser rayon = randrange(10,30,2) et randint pour x,y,dx,dy
    MIN_SPEED = 10 
    MAX_SPEED = 20
    list_molecule = []
    for data_molecule in list_molecule:
        rayon = randrange(10,30,2)
        x=randint(xmin + rayon,xmax - rayon)
        y=randint(0 + rayon,hauteur - rayon)
        dx = randint(10,20)
        dy = randint(10,20) 
        data_molecule = {"rayon" : rayon, "x" : x, "y":y, "dx":dx, "dy":dy}
        list_molecule.append(data_molecule)
    
    return list_molecule

def inverseDirMolecule(mol, paroiG, paroiD, hauteur):
    #TODO 3.1.6 Implémenter la fonction décrite dans le README
    # inverseDirMolecule inverse la direction de la molécule
    # Cette fonction reçoit en entrer quatre paramètres:
    # la molécule les parois gauche et droit du chaque côté du réservoir et la hauteurdu reservoir.
    # Si la molécule touche une des parois du réservoir un faut la reposition à la limite
    # du réservoir et inverser sa direction en vitesse.
    x, y, dx, dy, rayon = mol['x'], mol['y'], mol['dx'], mol['dy'], mol['rayon']
    # Si la molécule touche la paroi gauche du réservoir en x
    if x - rayon <= paroiG:
        # Repositionner la molécule et changer sa direction dx
        x = paroiG +rayon
        dx = -dx

    # Si la molécule touche la paroi droite du réservoir en x
    elif x + rayon >= paroiD:
        # Repositionner la molécule et changer sa direction dx
        x = paroiD - rayon
        dx = -dx

    # Si la molécule touche la paroi gauche du réservoir en x
    if y - rayon <= 0:
        # Repositionner la molécule et changer sa direction dy
        y = rayon 
        dy =-dy

    # Si la molécule touche la paroi droite du réservoir en y
    elif y + rayon >= hauteur:
        # Repositionner la molécule et changer sa direction dy
        y = hauteur - rayon 
        dy= -dy
        
    mol['x'], mol['y'], mol['dx'], mol['dy'] = x, y, dx, dy

    return mol

if __name__ == '__main__':
    # Test creerMolecule
    x, y, dx, dy, rayon = 5, 2, -3, 4, 5
    mol = creerMolecule(x, y, dx, dy, rayon)
    text = "La position de la molecule est ({},{}), sa vitesse est ({},{}) "
    text += "et son rayon est {}"
    
    print(text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
    
    # Test moleculesSeTouche
    
    mol_1  = creerMolecule(x, y, dx, dy, rayon)
    mol_2  = mol_1
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
       
    mol_2  = creerMolecule(x, y+rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+rayon, dx, dy, rayon/4)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+2*rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    # Test deplacerMolecule
    
    old_text = "Avant le deplacement \n\t" + text
    print(old_text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
    
    mol = deplacerMolecule(mol)
    new_text = "Apres le deplacement \n\t" + text
    print(new_text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
