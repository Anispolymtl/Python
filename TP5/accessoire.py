from enum import Enum

from elements_tiktok import ElementViral


class TypeAccessoire(Enum):
    CHAPEAU = 0
    CHAUSSURES = 1
    BIJOU = 2
    VETEMENT = 3

    def __str__(self):
        return self.name


# TODO J'hérite de ElementViral
class Accessoire(ElementViral):

    # TODO Implantez mon constructeur
    def __init__(self,nom: str, niveau_mignonnerie: int, type_accessoire: TypeAccessoire  ) -> None:
        self.nom = nom
        self.niveau_mignonnerie = niveau_mignonnerie
        self.type_accessoire = type_accessoire

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  type : TYPE_ACCESSOIRE, nom : NOM_ACCESSOIRE, niveau de mignonnerie : NIVEAU_DE_MIGNONNERIE
        #  TypeAccessoire a déjà une implantation de __str__. Utilisez-là!
        return f"type : {str(self.type_accessoire)}, nom : {self.nom}, niveau de mignonnerie : {self.niveau_mignonnerie}"
        

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

    def score_viral(self) -> int:
        # TODO Retourne 10 000 fois le niveau de mignonnerie multiplié par un facteur donné
        multiplicateur = 0
        if self.type_accessoire == TypeAccessoire.CHAPEAU:
            multiplicateur = 1.5
        elif self.type_accessoire == TypeAccessoire.CHAUSSURES:
            multiplicateur = 1.2
        elif self.type_accessoire == TypeAccessoire.BIJOU:
            multiplicateur = 0.8
        elif self.type_accessoire == TypeAccessoire.VETEMENT:
            multiplicateur = 1

        return self.niveau_mignonnerie*multiplicateur*10000