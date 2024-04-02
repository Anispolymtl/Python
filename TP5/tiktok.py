import json
from typing import List, Union

from animal import Animal
from elements_tiktok import Musique, Filtre


class TikTok:

    # TODO Implantez mon constructeur
    def __init__(self, titre:str) -> None:
        self.titre = titre
        self.__animaux = []
        self.filtre = None
        self.musique = None
    def ajouter_animal(self, animal: Animal) -> 'TikTok':
        # TODO Ajoutez l'animal à la liste et retournez le TikTok mis à jour
        self.__animaux.append(animal)
        return self

    def __lt__(self, autre_tiktok: 'TikTok') -> bool:
        # TODO Surchargez l'opérateur < entre deux objets de type TikToks
        #  Retourne True si le présent TikTok a moins de vues que autre_tiktok
        #  Retourne False sinon
        if self.vues < autre_tiktok.vues:
            return True
        else: 
            return False

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  TITRE (NOMBRE_DE_VUES vues)
        return f"{self.titre} ({self.vues} vues)"

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

    @property
    def vues(self) -> int:
        # TODO Retournez le nombre de vues de votre TikTok selon la formule suivante:
        #  vues = SCORE_MUSIQUE + SCORE_FILTRE + NOMBRE_ANIMAUX* SOMME(SCORE_ANIMAUX)
        somme_animal = 0
        for animal in self.__animaux:
            somme_animal += animal.score_viral()  
        nb_vues = self.musique.score_viral() + self.filtre.score_viral() + len(self.__animaux)* somme_animal
        return nb_vues
    


    def to_json(self):
        # Ne pas modifier
        return json.dumps({
            'titre': self.titre,
            'vues': self.vues,
            'musique': self.musique.titre,
            'filtre': self.filtre.nom,
            'animaux': [
                {
                    'nom': animal.nom,
                    'espèce': type(animal).__name__,
                    'accessoires': [
                        {
                            'nom': accessoire.nom,
                            'type': str(accessoire.type_accessoire)
                        } for accessoire in animal.liste_accessoires
                    ]
                } for animal in self.__animaux
            ]
        }, ensure_ascii=False)


class CompteTikTok:

    # TODO Implantez mon constructeur
    def __init__(self, identifiant :str) -> None:
          self.identifiant = identifiant
          self.__tiktoks = []

    def __len__(self) -> int:
        # TODO Surchargez l'opérateur len pour que len(COMPTE_TIKTOK) retourne le nombre de tiktok du compte
        return len(self.__tiktoks)

    def __iadd__(self, tiktok: TikTok) -> 'CompteTikTok':
        # TODO Surchargez l'opérateur += pour permettre d'ajouter un TikTok à la liste du compte
        #  Doit retourner le compte mis à jour
        self.__tiktoks.append(tiktok)
        return self
        

    @property
    def vues(self) -> int:
        # TODO Retourne le nombre de vues cumulatives du compte c'est à dire la somme des vues des différents TikToks
        somme_vues = 0 
        for tiktok in self.__tiktoks:
            somme_vues += tiktok.vues
        return somme_vues


    def tiktoks_plus_populaires(self) -> List[TikTok]:
        # TODO Retourne une liste triée des TikToks du compte en ordre décroissant de vues
        
        liste_vues = []
        liste_triee = []
        for tiktok in self.__tiktoks:
            liste_vues.append(tiktok.vues)
        liste_vues = sorted(liste_vues)
        
        for tiktok_vue in liste_vues:
            for tiktok2 in self.__tiktoks:
                if tiktok_vue == tiktok2.vues:
                    liste_triee.insert(0,tiktok2)        
        return liste_triee
        
        



