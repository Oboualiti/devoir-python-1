# Saisie des nombres [cite: 58]
num1 = float(input("Premier nombre : "))
num2 = float(input("Deuxième nombre : "))

print("Opérations : 1: Addition, 2: Soustraction, 3: Multiplication, 4: Division") [cite: 59]
operation = input("Votre choix (1-4) : ")

if operation == "1":
    print(f"Résultat : {num1 + num2}") [cite: 60, 64]
elif operation == "2":
    print(f"Résultat : {num1 - num2}") [cite: 61, 64]
elif operation == "3":
    print(f"Résultat : {num1 * num2}") [cite: 62, 64]
elif operation == "4":
    # Prévention de la division par zéro [cite: 65]
    if num2 != 0:
        print(f"Résultat : {num1 / num2}") [cite: 63, 64]
    else:
        print("Erreur : Division par zéro impossible.") [cite: 65]
else:
    print("Opération non reconnue.")