import os

FICHIER_TACHES = "taches.txt"

def charger_taches():
    """Charge les tâches depuis le fichier."""
    if os.path.exists(FICHIER_TACHES):
        with open(FICHIER_TACHES, "r", encoding="utf-8") as fichier:
            return [ligne.strip() for ligne in fichier.readlines()]
    return []

def sauvegarder_taches():
    """Sauvegarde les tâches dans le fichier."""
    with open(FICHIER_TACHES, "w", encoding="utf-8") as fichier:
        for tache in taches:
            fichier.write(tache + "\n")

taches = []

def ajouter_tache(tache):
    taches.append(tache)
    sauvegarder_taches()
    print(f"Tâche ajoutée : {tache}")

def lister_taches():
    print("Liste des tâches :")
    for i, tache in enumerate(taches, 1):
        print(f"{i}. {tache}")

def supprimer_tache(numero):
    if 1 <= numero <= len(taches):
        tache_supprimee = taches.pop(numero - 1)
        sauvegarder_taches()
        print(f"Tâche supprimée : {tache_supprimee}")
    else:
        print("Numéro de tâche invalide.")

def main():
    while True:
        print("\nOptions : [1] Ajouter une tâche [2] Lister les tâches [3] supprimer une tâche [4] Quitter")
        choix = input("Choisissez une option : ")
        if choix == "1":
            tache = input("Entrez une tâche : ")
            ajouter_tache(tache)
        elif choix == "2":
            lister_taches()
        elif choix == "3":
            lister_taches()
            if taches:
                try:
                    numero = int(input("Entrez le numéro de la tâche à supprimer : "))
                    supprimer_tache(numero)
                except ValueError:
                    print("Veuillez entrer un numéro valide.")
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    # Charger les tâches au démarrage
    taches = charger_taches()
    lister_taches()
    main()

