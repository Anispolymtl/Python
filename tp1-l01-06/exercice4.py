import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    acceleration = (vitesseFinale-vitesseInitiale)/duree
    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale =vitesseInitiale*duree+((acceleration*duree**2)/2)+ positionInitiale

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
