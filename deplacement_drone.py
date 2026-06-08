import plateau as pl
import survivant as sv
def deplacement_drone(drone, direction):
    id, jd = drone["position"]
    # Recharge à la base
    if drone["position"] == (pl.ih, pl.jh):
        drone["charge"]="oui"
        drone["batterie"] = min(40, drone["batterie"] + 3)
    if direction == "0" or direction == "PASS":
        return "Le drone ne bouge pas."
    def deplacer(drone, new_id, new_jd):
        """Met à jour la position du drone dans le dict ET dans la matrice."""
        old_id, old_jd = drone["position"]
        # Effacer l'ancienne case (redevient vide, sauf si c'est la base)
        if (old_id, old_jd) == (pl.ih, pl.jh):
            pl.matrice[old_id][old_jd] = "H "
        else:
            pl.matrice[old_id][old_jd] = ". "
        # Écrire la nouvelle case
        pl.matrice[new_id][new_jd] = drone["nom"]
        drone["position"] = (new_id, new_jd)
        # Consommer la batterie
        if drone["survivant"] == "oui":
            drone["batterie"] -= 2
        else:
            drone["batterie"] -= 1
        if (new_id, new_jd) == (pl.ih, pl.jh) and drone["survivant"] == "oui":
            drone["survivant"] = "non"
            print(f"{drone['nom']} a déposé le survivant à l'hôpital ! Il consomme à nouveau 1 de batterie.")
            nom_survivant = drone["nom_survivant"]
            getattr(sv, nom_survivant)["Sauvé"] = "oui"
            getattr(sv, nom_survivant)["Transporté"] = "non"
            print(f"{nom_survivant} est sauvé grâce à {drone['nom']} !")
            drone["nom_survivant"] = None

# Arrivée à l'hôpital avec un survivant

            
    # Calcul de la nouvelle position selon la direction
    nouvelles_positions = {
        "N":  (id - 1, jd)     if id > 0               else None,
        "S":  (id + 1, jd)     if id < 11              else None,
        "W":  (id, jd - 1)     if jd > 0               else None,
        "E":  (id, jd + 1)     if jd < 11              else None,
        "NW": (id - 1, jd - 1) if id > 0  and jd > 0  else None,
        "NE": (id - 1, jd + 1) if id > 0  and jd < 11 else None,
        "SW": (id + 1, jd - 1) if id < 11 and jd > 0  else None,
        "SE": (id + 1, jd + 1) if id < 11 and jd < 11 else None,
    }
 
    nouvelle_pos = nouvelles_positions.get(direction)
 
    if nouvelle_pos is None:
        print("Direction invalide ou bord du plateau atteint.")
        return
 
    new_id, new_jd = nouvelle_pos
    case = pl.matrice[new_id][new_jd]
 
    # Vérifier si la case est bloquée
    if case in ("B ", "T1", "T2", "T3", "T4", "D1", "D2", "D3", "D4","D5","D6"):
        print("Le drone ne peut pas se déplacer dans cette direction (obstacle).")
        nouvelle_dir = input("Entrez une nouvelle direction (W, E, N, S, NW, NE, SW, SE) ou 0 pour ne pas bouger : ")
        return deplacement_drone(drone, nouvelle_dir)
 
    deplacer(drone, new_id, new_jd)