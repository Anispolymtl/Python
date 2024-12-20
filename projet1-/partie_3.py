# Initilisation des variables 
c = 300000
n = 0 
i = 0.08


# Calcul du capital au bout de 20 années 
while n <= 20 :
    n = n + 1 
    c = c + (c*i)


# Affichage du capital au bout de 20 années 
print ("Capital au bout de 20 années :", c)
