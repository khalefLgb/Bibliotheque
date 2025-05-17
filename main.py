import json
import os

# Charger la bibliothèque depuis le fichier JSON
def charger_bibliotheque():
    if os.path.exists("bibliotheque.json"):
        with open("bibliotheque.json", "r") as f:
            return json.load(f)
    return []

# Sauvegarder la bibliothèque dans le fichier JSON
def sauvegarder_bibliotheque(bibliotheque):
    with open("bibliotheque.json", "w") as f:
        json.dump(bibliotheque, f, indent=4)

# Afficher tous les livres
def afficher_livres(bibliotheque):
    if not bibliotheque:
        print("Aucun livre dans la bibliothèque.")
        return
    for livre in bibliotheque:
        etat = "Lu" if livre["Lu"] else "Non lu"
        print(f'{livre["ID"]} - {livre["Titre"]} ({livre["Auteur"]}, {livre["Année"]}) - {etat}')

# Ajouter un livre
def ajouter_livre(bibliotheque):
    titre = input("Titre du livre : ")
    auteur = input("Auteur : ")
    annee = int(input("Année de publication : "))
    ID = max([livre["ID"] for livre in bibliotheque], default=0) + 1
    livre = {
        "ID": ID,
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None
    }
    bibliotheque.append(livre)
    print("Livre ajouté avec succès.")

# Supprimer un livre
def supprimer_livre(bibliotheque):
    ID = int(input("ID du livre à supprimer : "))
    for livre in bibliotheque:
        if livre["ID"] == ID:
            bibliotheque.remove(livre)
            print("Livre supprimé.")
            return
    print("Livre non trouvé.")

# Rechercher un livre
def rechercher_livre(bibliotheque):
    mot_cle = input("Mot-clé à rechercher : ").lower()
    resultats = [livre for livre in bibliotheque if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower()]
    if resultats:
        for livre in resultats:
            print(f'{livre["ID"]} - {livre["Titre"]} ({livre["Auteur"]})')
    else:
        print("Aucun résultat trouvé.")

# Marquer un livre comme lu
def marquer_lu(bibliotheque):
    ID = int(input("ID du livre lu : "))
    for livre in bibliotheque:
        if livre["ID"] == ID:
            livre["Lu"] = True
            livre["Note"] = int(input("Note sur 10 : "))
            commentaire = input("Commentaire (optionnel) : ")
            livre["Commentaire"] = commentaire
            print("Livre marqué comme lu.")
            return
    print("Livre non trouvé.")

# Afficher livres selon leur statut (lus ou non lus)
def filtrer_livres(bibliotheque, lu=True):
    livres_filtres = [livre for livre in bibliotheque if livre["Lu"] == lu]
    if not livres_filtres:
        print("Aucun livre correspondant.")
        return
    for livre in livres_filtres:
        print(f'{livre["ID"]} - {livre["Titre"]}')

# Trier les livres
def trier_livres(bibliotheque, critere="Année"):
    try:
        livres_tries = sorted(bibliotheque, key=lambda x: x.get(critere) or 0)
        for livre in livres_tries:
            print(f'{livre["ID"]} - {livre["Titre"]} - {livre["Année"]} ({livre.get(critere)})')
    except KeyError:
        print("Critère invalide.")

# Menu principal
def menu():
    bibliotheque = charger_bibliotheque()
    while True:
        print("\n---------------------- MENU ------------------------------------------")
        print("1. Afficher les livres")
        print("2. Ajouter un livre")
        print("3. Supprimer un livre")
        print("4. Rechercher un livre")
        print("5. Marquer un livre comme lu")
        print("6. Afficher les livres lus")
        print("7. Afficher les livres non lus")
        print("8. Trier les livres")
        print("9. Quitter")
        print("\n----------------------------------------------------------------------")

        choix = input("Votre choix : ")
        if choix == "1":
            afficher_livres(bibliotheque)
        elif choix == "2":
            ajouter_livre(bibliotheque)
        elif choix == "3":
            supprimer_livre(bibliotheque)
        elif choix == "4":
            rechercher_livre(bibliotheque)
        elif choix == "5":
            marquer_lu(bibliotheque)
        elif choix == "6":
            filtrer_livres(bibliotheque, True)
        elif choix == "7":
            filtrer_livres(bibliotheque, False)
        elif choix == "8":
            critere = input("Trier par (Année, Auteur, Note) : ")
            trier_livres(bibliotheque, critere)
        elif choix == "9":
            sauvegarder_bibliotheque(bibliotheque)
            print("Bibliothèque sauvegardée. Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Lancer le programme
if __name__ == "__main__":
    menu()
