from systeme.system_exploration import Exploration
from systeme.system_combat import Combat
from classe.class_character import Heros

def main():
    print("Bienvenue dans le jeu RPG !")
    nom = input("Entrez le nom de votre personnage : ")
    personnage = Heros(nom)
    exploration = Exploration(personnage)

    while personnage.est_vivant():
        print("\nQue voulez-vous faire ?")
        action = input("(bag/carte/quitter/north/south/east/west) : ").lower()
        
        if action == "bag":
            menu_inventaire(personnage)
        elif action == "carte":
            menu_carte(exploration)
        elif action in ["north", "south", "east", "west"]:
            exploration.deplacer(action)
        elif action == "quitter":
            print("Merci d'avoir joué !")
            break
        else:
            print("Action non reconnue.")

def menu_inventaire(personnage):
    while True:
        print("\nMenu Inventaire :")
        action = input("(bag/status/equiper/retour) : ").lower()
        if action == "bag":
            ouvrir_inventaire(personnage)
        elif action == "status":
            afficher_statut(personnage)
        elif action == "equiper":
            equiper_item(personnage)
        elif action == "retour":
            break
        else:
            print("Action non reconnue.")

def equiper_item(personnage):
    if not personnage.inventaire:
        print("Aucun équipement disponible")
        return
    
    print("Équipement :")
    for i, objet in enumerate(personnage.inventaire, 1):
        print(f"{i}. {objet.nom}")
    
    choix = input("Entrez un numéro pour équiper un item : ")
    if choix.isdigit():
        index = int(choix) - 1
        if 0 <= index < len(personnage.inventaire):
            objet = personnage.inventaire[index]
            if isinstance(personnage, Heros):
                personnage.equiper(objet)
        else:
            print("Choix invalide.")
    elif choix == "retour":
        return
    else:
        print("Action non reconnue.")


def menu_carte(exploration):
    while True:
        print("Carte actuelle :")
        exploration.afficher_carte()
        action = input("(retour) : ").lower()
        if action == "retour":
            break
        else:
            print("Action non reconnue.")

def ouvrir_inventaire(personnage):
    if personnage.inventaire:
        print("Inventaire :")
        for objet in personnage.inventaire:
            print(f"- {objet.nom}")
    else:
        print("Votre inventaire est vide.")

def afficher_statut(personnage):
    print(f"XP actuel : {personnage.xp} / {personnage.niveau * 10}")
    print(f"HP actuel : {personnage.hp} / {personnage.hp_max}")

if __name__ == "__main__":
    main()
