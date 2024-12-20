import pandas as pd

from constantes import CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS, FICHIER_CAPSULE, FICHIERS_RESERVOIRS, \
    FICHIERS_MOTEURS


def charger_capsules_df(chemin_capsules: str) -> pd.DataFrame:
    # TODO Retournez un dataframe des capsules décrites dans le fichier FICHIER_CAPSULE
    #  Il faut aussi renommer les colonnes pour que celles-ci soient plus lisibles
    charger_capsules_df = pd.read_csv(chemin_capsules + '/' + FICHIER_CAPSULE)
    capsules = charger_capsules_df.rename(columns={
        'n': 'nom',
        'h': 'hauteur',
        'm': 'masse',
        'p': 'prix',
        'pl': 'places'})
    return capsules

def charger_reservoirs_df(chemin_reservoirs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des réservoirs décrits dans
    #  les fichiers FICHIERS_RESERVOIRS
    df_list = [] #Créer une liste pour stocké les df provenant de divers fichier JSON 
    for fichier in FICHIERS_RESERVOIRS:
        chemin_fichier = f"{chemin_reservoirs}/{fichier}"
        df= pd.read_json(chemin_fichier)
        df_list.append(df[['nom', 'hauteur', 'masse', 'prix', 'capacite']])
    charger_reservoirs_df = pd.concat(df_list, ignore_index=True)
    print(charger_reservoirs_df)

    


def charger_moteurs_df(chemin_moteurs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des moteurs décrits dans
    #  les fichiers FICHIERS_MOTEURS
    new_collumns = ['nom', 'hauteur', 'masse', 'prix', 'impulsion_specifique']
    moteurs_df = pd.DataFrame(collumns = new_collumns)
    for fichier in FICHIERS_MOTEURS:
        with open(f"{chemin_moteurs}/{fichier}", 'r') as fiche:
            nom, hauteur, masse, prix, impulsion_specifique = '', '', '', '', ''
            for line in fiche.readlines():
                if line.startswith('nom='):
                    nom = line.split('=')[1].strip()
                elif line.startswith('hauteur='):
                    hauteur = float(line.split('=')[1].strip())
                elif line.startswith('masse='):
                    masse = float(line.split('=')[1].strip())
                elif line.startswith('prix='):
                    prix = float(line.split('=')[1].strip())
                elif line.startswith('impulsion specifique='):
                    impulsion_specifique = int(line.split('=')[1].strip())
            moteurs_df = moteurs_df.append({
                'nom': nom,
                'hauteur': hauteur,
                'masse': masse,
                'prix': prix,
                'impulsion_specifique': impulsion_specifique}, ignore_index=True)
    
    return moteurs_df

def filtrer_moteurs(moteurs_df: pd.DataFrame, impulsion_minimum: int) -> pd.DataFrame:
    # TODO Retourner un sous-ensemble filtré d'un df de moteurs
    #  où l'impulsion spécifique est au dessus d'un certain seuil
    df = moteurs_df[moteurs_df['impulsion_specifique'] > impulsion_minimum]
    
    return df


if __name__ == '__main__':
    # charger_capsules_df
    capsules = charger_capsules_df(CHEMIN_CAPSULES)
    print(capsules)
    print()

    # charger_reservoirs_df
    reservoirs = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    print(reservoirs)
    print()

    # charger_moteurs_df
    moteurs = charger_moteurs_df(CHEMIN_MOTEURS)
    print(moteurs)
    print()

    # filtrer_moteurs
    moteurs_filtres = filtrer_moteurs(moteurs, 220)
    print(moteurs_filtres)
