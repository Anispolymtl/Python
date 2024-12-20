# Initialisation des variables 

capital = 8000 # en dollars
nb_jours = 72 # en jours
taux_annuel = 0.065# pourcentage / 100 

# Calcul du taux périodique 
t = (0.065)/365

# Calcul des intérêts 
I = capital*t*nb_jours

# Calcul de la valeur acquise
V =  capital + I

# Affichage des interets et de la valeur acquise 
print("Les intérêt gagnés après 72 jours sont :", I)
print("La valeur acquise après 72 jours est :", V)
