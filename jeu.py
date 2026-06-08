import plateau as pl
import deplacement_drone as ddr
import tempetes as tp
import drone as dr
import deplacement_survivants as dps 
import survivant as sv
import deplacement_tempetes as ddt
import random as rd
import journal
#on initialise les scores : nombre de tours (n) = 0 et le nombre de survivants sauvés (Score) = 0
Score = 0
n=0

liste_directiont = ["N","E","S","W","NE","SE","SW","NW"]
drones_dict = {nom: getattr(dr, nom) for nom in ["D1", "D2", "D3", "D4", "D5", "D6"]}
#On initialise toutes les survivants à sauvé : non ; et les drones à etat : actif
for i in range(0,10) : 
    getattr(sv,"S"+str(i))["Sauvé"] = "non"
for i in range(1,7) :
    getattr(dr,"D"+str(i))["etat"] = "actif"

#Le jeu est toujours en cours si les batterie ne sont pas vide ou que les survivants ne sont pas encore tous sauvés
while (dr.D1["batterie"]>0 or dr.D2["batterie"]>0 or dr.D3["batterie"]>0 or dr.D4["batterie"]>0 or dr.D5["batterie"]>0 or dr.D6["batterie"]>0) and (sv.S0["Sauvé"]=="non" or sv.S1["Sauvé"]=="non" or sv.S2["Sauvé"]=="non" or sv.S3["Sauvé"]=="non" or sv.S4["Sauvé"]=="non" or sv.S5["Sauvé"]=="non" or sv.S6["Sauvé"]=="non" or sv.S7["Sauvé"]=="non" or sv.S8["Sauvé"]=="non" or sv.S9["Sauvé"]=="non") :
      liste_tempetes = ["T1", "T2", "T3", "T4"]
      #En avançant d'un tour, il faut le nombre de tours inactifs des drones baisse de 1 et redevienne actif en arrivant à 0
      for nom in ["D1", "D2", "D3", "D4", "D5", "D6"]:
            drone_état = getattr(dr, nom)
            if drone_état["tours_inactif"] > 0:
                  drone_état["tours_inactif"] -= 1
                  if drone_état["tours_inactif"] == 0:
                        drone_état["etat"] = "actif"
                        print(f"{nom} est de nouveau actif !")
      #Le nombre de tour avance de 1
      n = n+1
      journal.enregistrer("Tour numero " + str(n))
      print("Tour numéro", n)
      print("tour du joueur 1 (Drone)")
      print("Voici le plateau :") 
      #En imprimant le plateau case par case, on évite d'avoir des crochet, des virgules et des apostrophe entre les cases
      for ligne in pl.matrice:
            for case in ligne:
                  print(case, end="  ")
            print()

      #On donne les informations essentielles sur chacun des drones au joueur
      print("information sur les drones : \nDrone D1 : position", dr.D1["position"], ", batterie :", dr.D1["batterie"], ", état :", dr.D1["etat"], ", Nom du survivant transporté", dr.D1["nom_survivant"])
      print("Drone D2 : position", dr.D2["position"], ", batterie :", dr.D2["batterie"], ", état :", dr.D2["etat"], ", Nom du survivant transporté", dr.D2["nom_survivant"])
      print("Drone D3 : position", dr.D3["position"], ", batterie :", dr.D3["batterie"], ", état :", dr.D3["etat"], ", Nom du survivant transporté", dr.D3["nom_survivant"])
      print("Drone D4 : position", dr.D4["position"], ", batterie :", dr.D4["batterie"], ", état :", dr.D4["etat"], ", Nom du survivant transporté", dr.D4["nom_survivant"])
      print("Drone D5 : position", dr.D5["position"], ", batterie :", dr.D5["batterie"], ", état :", dr.D5["etat"], ", Nom du survivant transporté", dr.D5["nom_survivant"])
      print("Drone D6 : position", dr.D6["position"], ", batterie :", dr.D6["batterie"], ", état :", dr.D6["etat"], ", Nom du survivant transporté", dr.D6["nom_survivant"])

      #On utilise une boucle while et non une boucle for car si un drone est inactif la bouble for se termine et passe à la valeur d'après. On saute alors le tour d'un drone. 
      déplacement = 0
      while déplacement<3 :
            nom_drone = input("sélectionnez un drone (D1, D2, D3, D4, D5 ou D6) : ")
            drone_choisi = getattr(dr, nom_drone)
            while drone_choisi["etat"] == "inactif":
                  print(f"{nom_drone} est inactif encore {drone_choisi['tours_inactif']} tour(s), choisissez un autre.")
                  nom_drone = input("sélectionnez un drone (D1, D2, D3, D4, D5 ou D6) : ")
                  drone_choisi = getattr(dr, nom_drone)
            direction  = input("Entrez une direction pour le drone (W, E, N, S, NW, NE, SW, SE) ou 0 pour ne pas bouger : ")
            ddr.deplacement_drone(drone_choisi, direction)
            journal.enregistrer(nom_drone + " : " + str(drone_choisi["position"]) + " -> direction " + direction)
            # Après le déplacement, on vérifie tous les survivants
            for nom_s in ["S0","S1","S2","S3","S4","S5","S6","S7","S8","S9"]:
                  survivant = getattr(sv, nom_s)
                  if (survivant["Sauvé"] == "non" and drone_choisi["position"] == survivant["position"]):  
                        dps.ramasser_survivant(drone_choisi, nom_s, survivant)
                        journal.enregistrer(nom_drone + " ramasse " + nom_s)
                        break  # on s'arrête, un drone ne peut porter qu'un seul survivant
            déplacement = déplacement + 1 
      print("Tour du joueur 2 : Tempêtes") 
      print("information sur les tempêtes : \nTempête T1 : position", tp.T1["position"])
      print("Tempête T2 : position", tp.T2["position"])
      print("Tempête T3 : position", tp.T3["position"])
      print("Tempête T3 : position", tp.T3["position"])
      for k in range(2) :
            nom_tempete = input("sélectionnez une tempete (T1, T2, T3, T4) : ")
            directiont  = input("Entrez une direction pour la tempete (W, E, N, S, NW, NE, SW, SE) : ")

            ddt.deplacement_tempete(getattr(tp, nom_tempete), directiont) 
            journal.enregistrer(nom_tempete + " -> direction " + directiont)
            ddt.verifier_proximite_drones(getattr(tp, nom_tempete), drones_dict)
            #On retire le nom de la tempête choisi de la liste des tempête. à la fin il ne reste plus que les 2 drones non déplacés qui ont une chance sur deux de se déplacer aléatoirement
            liste_tempetes.remove(nom_tempete)
      for i in liste_tempetes : 
            #Une chance sur deux de se déplacer
            a = rd.randint(0,1)
            if a==1 : 
                  #On choisi aléatoirement dans la liste des directions une des huit directions
                  b = rd.randint(0,7)
                  ddt.deplacement_tempete(getattr(tp, i), liste_directiont[b])
                  ddt.verifier_proximite_drones(getattr(tp, i), drones_dict)
      #On compte le nombre de survivants restants pour informer les joueurs
      Score = 0
      for nom_s in ["S0", "S1","S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9"] : 
            if getattr(sv, nom_s)["Sauvé"] == "oui" : 
                  Score += 1
      print ("Le joueur 1 à sauvé ", Score, " survivants. Il en reste ", 10-Score)
      journal.enregistrer("Score : " + str(Score))
      journal.enregistrer("Survivants restants : " + str(10 - Score))
      journal.sauvegarder()
#On donne les deux cas de fin :
if (dr.D1["batterie"]==0 and dr.D2["batterie"]==0 and dr.D3["batterie"]==0 and dr.D4["batterie"]==0 and dr.D5["batterie"]==0 and dr.D6["batterie"]==0) : 
      print ("Le joueur 2 (Tempête a gagné)")
if (sv.S0["Sauvé"]=="oui" and sv.S1["Sauvé"]=="oui" and sv.S2["Sauvé"]=="oui" and sv.S3["Sauvé"]=="oui" and sv.S4["Sauvé"]=="oui" and sv.S5["Sauvé"]=="oui" and sv.S6["Sauvé"]=="oui" and sv.S7["Sauvé"]=="oui" and sv.S8["Sauvé"]=="oui" and sv.S9["Sauvé"]=="oui") :
      print ("Le joueur 1 (Drones a gagné)")
journal.score = Score
journal.survivants_sauves = Score
journal.sauvegarder()