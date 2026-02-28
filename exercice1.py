
age = int(input("Veuillez saisir votre âge : "))


if age <= 12:
    statut = "Enfant" [cite: 11]
elif age <= 17:
    statut = "Adolescent" [cite: 12]
elif age <= 64:
    statut = "Adulte" [cite: 13]
else:
    statut = "Senior" [cite: 13]


print(f"Votre statut est : {statut}")