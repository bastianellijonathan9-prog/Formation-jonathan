# Mes racines du code
ma_boite = "mon cerveau"
heure = 21

print("Dans " + ma_boite + ", il est " + str(heure) + "h")

if heure < 12:
    print("matin")
elif heure < 19:
    print("après-midi")
else:
    print("soir ou nuit")

compteur = 0
while compteur < 3:
    print("racine n°" + str(compteur))
    compteur = compteur + 1
