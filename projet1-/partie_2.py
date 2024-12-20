# Initialisation des variables 
C = 2600
C2 = 2600 - 60 
t1 = 0.045/365 
t2 = 0.10 / 365 
n = 0
cc1 = 0
cc2 = 0

# Calcul du montant du capital avec le premier placement au 100ème jour de l'année 
Capital1 = C + C*t1*100

# Calcul du montant du capital avec le deuxième placement au 300ème jour de l'année 
Capital2 = (C2 + (C2*t2*300))

# /!\ AVEC UNE BOUCLE/!\ Calcul du jour à partir duquel le deuxième placement rapporte plus que le premier
while cc2 <= cc1:
    n = n+1
    cc1 =C + C*t1*n 
    cc2 =C2 + C2+t2*n


# Affichage des valeurs calculées
print("Montant du capital avec le premier placement au 100ème jour :", Capital1)
print("Montant du capital avec le deuxième placement au 300ème jour :", Capital2)
print("Jour à partir duquel le deuxième placement rapporte plus que le premier :", n)