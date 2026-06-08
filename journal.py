evenements = []
score = 0
survivants_sauves = 0
 
def enregistrer(message):
    evenements.append(message)
 
def sauvegarder():
    # journal.txt
    f = open("journal.txt", "w")
    for ligne in evenements:
        f.write(ligne + "\n")
    f.close()
 
    # resultats.txt
    f = open("resultats.txt", "w")
    f.write("Score final : " + str(score) + "\n")
    f.write("Survivants sauves : " + str(survivants_sauves) + "\n")
    f.close()