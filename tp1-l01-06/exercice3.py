
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes//(365*24*60*60)
    secondes -= annees*(365*24*60*60)
    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = secondes//(7*24*60*60)
    secondes -= semaines*(7*24*60*60)
    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = secondes//(24*60*60)
    secondes -= jours*(24*60*60)
    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = secondes//(60*60)
    secondes -= heures*(60*60)
    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = secondes//60
    secondes -= minutes*60
    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondes

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrez les secondes: "))
    print(decomposer(secondes))
