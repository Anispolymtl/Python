def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    positionInitialV1 = 0
    positionInitialV2 = distance
    temps = positionInitialV2/(v1-v2)    
    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    positionRencontre = v1*temps 
    

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance)) 
