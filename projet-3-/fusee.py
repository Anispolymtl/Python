import math

from constantes import MASSE_VOLUMIQUE_CARBURANT, CHAMP_GRAVITATIONNEL


class Piece:
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float) -> None:
        self.nom = nom
        self.hauteur = hauteur  # En m
        self.masse = masse  # En kg
        self.prix = prix  # En $CAN

    def __str__(self) -> str:
        return f"{self.nom}, hauteur={self.hauteur}m, masse={self.masse}kg, prix={self.prix}$"


class Capsule(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, places: int) -> None:
        super().__init__(nom, hauteur, masse, prix)

        self.places = places  # En personnes

    def __str__(self) -> str:
        return f"Capsule: {super().__str__()}, places={self.places} personne(s)"


class Reservoir(Piece):
    def __init__(self, nom: str, hauteur: float, masse_vide: float, prix: float, capacite: float) -> None:
        super().__init__(nom, hauteur, masse_vide, prix)

        self.capacite = capacite  # En litres

    def __str__(self) -> str:
        return f"Réservoir: {super().__str__()}, capacité={self.capacite}L"

    @property
    def masse_rempli(self) -> float:
        # TODO calculez la masse du réservoir rempli.
        #  Utilisez MASSE_VOLUMIQUE_CARBURANT
        masse_carburant = self.capacite*MASSE_VOLUMIQUE_CARBURANT
        masse_rempli = masse_carburant+self.masse
        return masse_rempli

        


class Moteur(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, impulsion_specifique: int) -> None:
        super().__init__(nom, hauteur, masse, prix)

        self.impulsion_specifique = impulsion_specifique  # En secondes

    def __str__(self) -> str:
        return f"Moteur: {super().__str__()}, impulsion spécifique={self.impulsion_specifique}s"


class Fusee:
    """
    La classe représentant une fusée simple.

    Une fusée a comme attributs publics:
    * Un nom

    Une fusée a comme attributs privés:
    * Une capsule
    * Un réservoir
    * Un moteur
    """

    # TODO Implanter le constructeur avec les différentes pièces comme attributs privés
    def __init__(self, nom: str, capsule: Capsule, reservoir: Reservoir, moteur: Moteur) -> None:
        self.nom = nom
        self._capsule = capsule
        self._reservoir = reservoir
        self._moteur = moteur

    
    def __str__(self) -> str:
        # TODO Implantez la fonction __str__ pour permettre l'affichage de la fusée
        capsule_str = f"Capsule:\n{str(self._capsule)}\n"
        reservoir_str = f"Réservoir:\n{str(self._reservoir)}\n"
        moteur_str = f"Moteur:\n{str(self._moteur)}\n"

        return f"Fusée {self.nom}\n{capsule_str}{reservoir_str}{moteur_str}"
        

    @property
    def masse(self) -> float:
        # TODO Calculez la masse totale de la fusée (incluant le carburant)
        masse_totale = self._capsule.masse + self._reservoir.masse + self._moteur.masse
        return masse_totale
        

    @property
    def hauteur(self) -> float:
        # TODO Calculez la hauteur totale de la fusée
        hauteur_total = self._capsule.hauteur + self._reservoir.hauteur
        return hauteur_total
        

    @property
    def prix(self) -> float:
        # TODO Calculez le prix total de la fusée
        prix_total = self._capsule.prix + self._reservoir.prix + self._moteur.prix
        return prix_total
        

    def calculer_deltav(self) -> float:
        # TODO À partir de la masse, du moteur et du réservoir,
        #  calculez le deltaV disponible de la fusée dans l'atmosphère
        #  Utilisez la constante CHAMP_GRAVITATIONNEL
        m_vide = self._capsule.masse + self._reservoir.masse
        m_remplie = m_vide + self._moteur.masse
        deltaV = self._moteur.impulsion_specifique * CHAMP_GRAVITATIONNEL * math.log(m_remplie / m_vide)
        return deltaV  



if __name__ == '__main__':
    # Reservoir.masse_rempli
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    masse_rempli = reservoir.masse_rempli
    print(f"Une fois rempli, {reservoir.nom} a une masse de {masse_rempli} kg")
    print()

    # Fusee constructeur
    capsule = Capsule("Exigüe", 1.0, 750, 1300.0, 1)
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20.0, 2)
    moteur = Moteur("Pantera Arctic Cat Triple 800", 4, 2000, 14000.0, 199)
    fusee = Fusee("Romano Fafard", capsule, reservoir, moteur)

    # Fusee.masse
    print(f"La masse de la fusée {fusee.nom} est {fusee.masse}kg")
    print()

    # Fusee.hauteur
    print(f"La hauteur de la fusée {fusee.nom} est {fusee.hauteur}m")
    print()

    # Fusee.prix
    print(f"Le prix de la fusée {fusee.nom} est {fusee.prix}$")
    print()

    # Fusee.__str__
    print(f"fusee est de type {type(fusee)}")
    print()
