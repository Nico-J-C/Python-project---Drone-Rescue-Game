import random as rd
import drone as dr
import tempetes as tp
import survivant as sv
matrice = []

# 1. Création de la matrice 12 par 12
for i in range(12):
    ligne = []
    for j in range(12):
        ligne.append(". ") 
    matrice.append(ligne)

# Placement des pièces sur le plateau : on les places de manière aléatoire sur le plateau pour avoir un plateau différent à chaque partie. On vérifie à chaque fois de ne pas écraser une autre pièce. 
# 2. Placement des drones : numérotés de D1 à D6
for d in range(1, 7):
    id, jd = int(rd.randrange(12)), int(rd.randrange(12))
    while matrice[id][jd] != ". ":
            id, jd = int(rd.randrange(12)), int(rd.randrange(12))
    matrice[id][jd] = "D"+str(d)
    getattr(dr,"D"+str(d))["position"] = (id, jd)
    getattr(dr,"D"+str(d))["nom"] = "D"+str(d) 
    getattr(dr,"D"+str(d))["charge"] = "non"
    getattr(dr,"D"+str(d))["survivant"] = "non"
    getattr(dr,"D"+str(d))["tours_inactif"] = 0
    getattr(dr,"D"+str(d))["batterie"] = 40
    getattr(dr,"D"+str(d))["etat"] = "actif"

# 3. Placement des Tempêtes
for k in range(1, 5):
    i, j = int(rd.randrange(12)), int(rd.randrange(12))
    while matrice[i][j] != ". ":
        i, j = int(rd.randrange(12)), int(rd.randrange(12))
    matrice[i][j] = "T" + str(k)
    getattr(tp,"T"+str(k))["position"] = (i, j)
    getattr(tp,"T"+str(k))["nom"] = "T"+str(k) 


# 4. Placement des Bâtiments : il y en a un nombre aléatoire compris entre 8 et 16
for b in range(rd.randint(8, 16)):
    ib, jb = rd.randrange(12), rd.randrange(12)
    while matrice[ib][jb] != ". ":
        ib, jb = int(rd.randrange(12)), int(rd.randrange(12))
    matrice[ib][jb] = "B "

# 5. Placement des Survivants : S
for s in range(0, 10):
    i, j = rd.randrange(12), rd.randrange(12)
    while matrice[i][j] != ". ":
        i, j = rd.randrange(12), rd.randrange(12)
    matrice[i][j] = "S" + str(s)
    getattr(sv,"S"+str(s))["position"] = (i, j)
    getattr(sv,"S"+str(s))["Transporté"] = "non"

# 6. Placement de H, on enregistre la position de l'hôpital pour pouvoir y déposer les survivants et recharger les drones
ih, jh = rd.randrange(12), rd.randrange(12)
while matrice[ih][jh] != ". ":
    ih, jh = rd.randrange(12), rd.randrange(12)
matrice[ih][jh] = "H "
    
