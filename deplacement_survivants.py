import survivant as sv
import plateau as pl
import drone as dr
def ramasser_survivant(drone, nom_survivant, survivant):
    """Appelée quand un drone arrive sur la case d'un survivant."""
    if drone["position"] == survivant["position"] and drone["survivant"] == "non":
        drone["survivant"] = "oui"
        drone["nom_survivant"] = nom_survivant
        # Effacer le survivant du plateau
        i, j = survivant["position"]
        pl.matrice[i][j] = drone["nom"]
        print(f"{drone['nom']} a ramassé {nom_survivant} !")

