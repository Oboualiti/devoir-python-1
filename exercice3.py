mot_de_passe_correct = "python123" [cite: 49]
saisie = ""


while saisie != mot_de_passe_correct:
    saisie = input("Entrez le mot de passe : ") [cite: 46]
    if saisie != mot_de_passe_correct:
        print("Incorrect, réessayez.")

print("Accès autorisé.") [cite: 48]