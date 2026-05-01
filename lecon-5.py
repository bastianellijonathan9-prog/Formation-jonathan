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

mot_de_passe = "mer"
essai = ""
tentatives = 0

while essai != mot_de_passe and tentatives < 3:
    essai = input("Devine le mot de passe : ")
    tentatives = tentatives + 1

    if essai == mot_de_passe:
        print("Bravo, tu es entré.")
    elif tentatives >= 3:
        print("Trois erreurs. Verrouillé.")
    else:
        print("Mauvais. Encore " + str(3 - tentatives) + " tentative(s).")
