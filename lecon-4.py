age = 17
a_invitation = False
nom = "Alex"

print("Bienvenue " + nom)

if age >= 18:
    print("Entrée autorisée.")
elif a_invitation == True:
    print("Entrée spéciale pour invité·e.")
else:
    print("Refusée. Repasse dans " + str(18 - age) + " an(s).")
