import random

def jouer_jeu():
    nombre_mystere = random.randint(1, 100)
    essais = 0

    print("Bienvenue dans le jeu de devinette !")
    print("Un nombre aléatoire entre 1 et 100 a été choisi. À vous de deviner !")

    while essais < 10:
        essais += 1
        nombre_joueur = int(input("Entrez un nombre : "))

        if nombre_joueur < nombre_mystere:
            print("Le nombre est trop bas.")
        elif nombre_joueur > nombre_mystere:
            print("Le nombre est trop élevé.")
        else:
            print(f"Félicitations ! Vous avez deviné le nombre mystère en {essais} essais.")
            return

    print(f"Dommage, vous avez épuisé toutes vos chances. Le nombre mystère était {nombre_mystere}.")

def jouer():
    while True:
        jouer_jeu()
        rejouer = input("Voulez-vous jouer à nouveau ? (oui/non) ")
        if rejouer.lower() != "oui":
            print("Merci d'avoir joué. À bientôt !")
            break

jouer()
