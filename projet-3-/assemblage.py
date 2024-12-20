from typing import List

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from constantes import DELTA_V_MINIMUM_PAR_CORPS_CELESTE, CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS
from fichiers_pieces import charger_capsules_df, charger_moteurs_df, charger_reservoirs_df
from fusee import Fusee, Capsule, Reservoir, Moteur


def creer_capsules(capsules_df: pd.DataFrame) -> List[Capsule]:
    # TODO Transformez le dataframe des capsules en liste d'objets de type Capsule
    capsules = []
    for index, row in capsules_df.iterrows():
        capsule = Capsule(row["nom"], row["hauteur"], row["masse"], row["prix"], row["places"])
        capsules.append(capsule)
    return capsules


def creer_moteurs(moteurs_df: pd.DataFrame) -> List[Moteur]:
    # TODO Transformez le dataframe des moteurs en liste d'objets de type Moteur
    moteurs = []
    for index, row in moteurs_df.iterrows():
        moteur = Moteur(row["nom"], row["hauteur"], row["masse"], row["prix"], row["Isp"])
        moteurs.append(moteur)
    return moteurs


def creer_reservoirs(reservoirs_df: pd.DataFrame) -> List[Reservoir]:
    # TODO Transformez le dataframe des reservoir en liste d'objets de type Reservoir
    reservoirs = []
    for index, row in reservoirs_df.iterrows():
        reservoir = Reservoir(row["nom"], row["hauteur"], row["masse"], row["prix"], row["capacité"])
        reservoirs.append(reservoir)
    return reservoirs


def corps_celestes_accessibles(fusee: Fusee) -> List[str]:
    # TODO Retournez la liste des corps célestes accessibles par la fusée.
    #  Utiliser DELTA_V_MINIMUM_PAR_CORPS_CELESTE
    corps_celestes = []
    for nom, delta_v in DELTA_V_MINIMUM_PAR_CORPS_CELESTE.items():
        if fusee.calculer_deltav() > delta_v:
            corps_celestes.append(nom)
    return corps_celestes


def comparer_fusee(fusee_1: Fusee, fusee_2: Fusee) -> None:
    # TODO créer un grouped barplot comparant les fusées passées en paramètre en fonction des trois métriques suivantes:
    #  * Masse / Coût
    #  * DeltaV / Coût
    #  * DeltaV / Masse
    # TODO Générez un dataframe avec trois colonnes; fusée, résultats des différents ratios et type_ratio
    ratios = [
        ("DeltaV par rapport à la masse", fusee_1.delta_v / fusee_1.masse, fusee_2.delta_v / fusee_2.masse),
        ("DeltaV par rapport au prix", fusee_1.delta_v / fusee_1.prix, fusee_2.delta_v / fusee_2.prix),
        ("Hauteur par rapport à la masse", fusee_1.hauteur / fusee_1.masse, fusee_2.hauteur / fusee_2.masse),
    ]
    df_ratios = pd.DataFrame({
    "Fusée": [fusee_1.nom, fusee_2.nom]*3,
    "Ratio": [ratio[1] for ratio in ratios] + [ratio[2] for ratio in ratios],
    "Type_ratio": ["DeltaV par rapport à la masse", "DeltaV par rapport au prix", "Hauteur par rapport à la masse"]*2})

    sns.catplot(data=df_ratios, kind="bar", x="Type_ratio", y="Ratio", hue="Fusée", height=5, aspect=2)

    return df_ratios

if __name__ == '__main__':
    # creer_capsules
    capsules_df = charger_capsules_df(CHEMIN_CAPSULES)
    capsules = creer_capsules(capsules_df)
    for capsule in capsules:
        print(capsule)
    print()

    # creer_moteurs
    moteurs_df = charger_moteurs_df(CHEMIN_MOTEURS)
    moteurs = creer_moteurs(moteurs_df)
    for moteur in moteurs:
        print(moteur)
    print()

    # creer_reservoirs
    reservoirs_df = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    reservoirs = creer_reservoirs(reservoirs_df)
    for reservoir in reservoirs:
        print(reservoir)
    print()

    # corps_celestes_accessibles
    capsule = Capsule("PasDBonSens", 1.5, 840.0, 600.0, 1)
    reservoir_1 = Reservoir("Piscine", 25.0, 9000.0, 13000.00, 6480.0)
    moteur = Moteur("La Puissance", 12.0, 15000.0, 39000.00, 295)
    fusee_1 = Fusee("Romano Fafard", capsule, reservoir_1, moteur)

    deltaV = fusee_1.calculer_deltav()
    corps_celestes = corps_celestes_accessibles(fusee_1)
    print(f"La fusée {fusee_1.nom} peut aller, avec {deltaV:.2f} de deltaV, jusqu'à: {corps_celestes}")
    print()

    # comparer_fusee
    reservoir_2 = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    fusee_2 = Fusee("Romano Fafard Lite", capsule, reservoir_2, moteur)
    comparer_fusee(fusee_1, fusee_2)
