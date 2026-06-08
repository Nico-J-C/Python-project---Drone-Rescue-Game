import random as rd
import plateau as pl
import tempetes as tp
import drone as dr

#Ensemble des cases adjacentes
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1), (1, 0), (1, 1)
]

def cases_adjacent(i, j):
    return {
        (i + di, j + dj)
        for di, dj in DIRECTIONS
        if 0 <= i + di <= 11 and 0 <= j + dj <= 11
    }
def verifier_proximite_drones(tempete, dr):
    cases = cases_adjacent(*tempete["position"])

    for nom, drone in dr.items():
        if drone["position"] in cases and drone["etat"] == "actif":
            drone["etat"] = "inactif"
            drone["tours_inactif"] = 3
            print(f"{nom} est désactivé par la tempête {tempete['nom']} pour 2 tours !")

            
def deplacement_tempete(tempete, directiont):
    i, j = tempete["position"]
 

    def deplacer(tempete, new_i, new_j):
        """Met à jour la position du drone dans le dict ET dans la matrice."""
        old_i, old_j = tempete["position"]
        # Effacer l'ancienne case (redevient vide, sauf si c'est la base)
        if (old_i, old_j) == (pl.ih, pl.jh):
            pl.matrice[old_i][old_j] = "H "
        else:
            pl.matrice[old_i][old_j] = ". "
        # Écrire la nouvelle case
        pl.matrice[new_i][new_j] = tempete["nom"]
        tempete["position"] = (new_i, new_j)
       
 
    # Calcul de la nouvelle position selon la direction
    nouvelles_positions = {
        "N":  (i - 1, j)     if i > 0               else None,
        "S":  (i + 1, j)     if i < 11              else None,
        "W":  (i, j - 1)     if j > 0               else None,
        "E":  (i, j + 1)     if j < 11              else None,
        "NW": (i - 1, j - 1) if i > 0  and j > 0  else None,
        "NE": (i - 1, j + 1) if i > 0  and j < 11 else None,
        "SW": (i + 1, j - 1) if i < 11 and j > 0  else None,
        "SE": (i + 1, j + 1) if i < 11 and j < 11 else None,
    }
 
    nouvelle_pos = nouvelles_positions.get(directiont)
 
    if nouvelle_pos is None:
        print("Direction invalide ou bord du plateau atteint.")
        return
 
    new_i, new_j = nouvelle_pos
    case = pl.matrice[new_i][new_j]
 
    # Vérifier si la case est bloquée
    if case in ("B ", "H ", "D1", "D2", "D3", "D4", "D5", "D6", "T1", "T2", "T3", "T4"):
        print("La tempête ne peut pas se déplacer dans cette direction (obstacle).")
        nouvelle_dir = input("Entrez une nouvelle direction (W, E, N, S, NW, NE, SW, SE) ou 0 pour ne pas bouger : ")
        return deplacement_tempete(tempete, nouvelle_dir)
 
    deplacer(tempete, new_i, new_j)

