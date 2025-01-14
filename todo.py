taches = []

def ajouter_tache(tache):
    taches.append(tache)
    print(f"Tâche ajoutée : {tache}")

def lister_taches():
    print("Liste des tâches :")
    for i, tache in enumerate(taches, 1):
        print(f"{i}. {tache}")

def supprimer_tache(numero):
    if 1 <= numero <= len(taches):
        tache_supprimee = taches.pop(numero - 1)
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
    main()

