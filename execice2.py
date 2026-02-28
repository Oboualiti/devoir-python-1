
contact = ["Bouchra", "Ahmed", "Sara"]

while True: [cite: 29, 34]
    
    print("1. Ajouter un contact") [cite: 31]
    print("2. Afficher tous les contacts") [cite: 32]
    print("3. Quitter") [cite: 33]
    
    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom du contact à ajouter : ")
        contacts.append(nom) [cite: 40]
    elif choix == "2":
        # Utilisation de enumerate() pour la numérotation [cite: 32, 34]
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact}")
    elif choix == "3":
        print("Fin du programme.")
        break [cite: 29, 33]
    else:
        print("Choix invalide.") [cite: 34]