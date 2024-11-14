import pickle
from systeme.system_exploration import Exploration
from systeme.system_combat import Combat
from classe.class_character import Heros

ROUGE = "\033[31m"
VERT = "\033[32m"
BLEU = "\033[34m"
AZURE = "\033[38;5;123m"
GOLD = "\033[38;5;220m"
RESET = "\033[0m"


def sauvegarder_partie(personnage, exploration):
    with open("sauvegarde.pkl", "wb") as fichier:
        pickle.dump((personnage, exploration), fichier)
    print(f"{BLEU}Partie sauvegardée avec succès.{RESET}")

def charger_partie():
    try:
        with open("sauvegarde.pkl", "rb") as fichier:
            personnage, exploration = pickle.load(fichier)
        print(f"{ROUGE} Partie chargée avec succès.{RESET}")
        return personnage, exploration
    except FileNotFoundError:
        print(f"{VERT}Aucune sauvegarde trouvée.{RESET}")
        return None, None

def menu_principal():
    print(f"{ROUGE}Bienvenue dans le jeu RPG !{RESET}")
    print("Voulez-vous:")
    print(f"{VERT}(1) lancer une nouvelle partie{RESET}")
    print(f"{BLEU}(2) charger une partie?{RESET}")
    
    while True:
        choix = input("Entrez votre choix : ")
        if choix == "1":
            nom = input("Entrez le nom de votre personnage : ")
            personnage = Heros(nom)
            exploration = Exploration(personnage)
            return personnage, exploration
        elif choix == "2":
            personnage, exploration = charger_partie()
            if personnage is not None and exploration is not None:
                return personnage, exploration
            else:
                print("Aucune sauvegarde n'a été trouvée. Lancement d'une nouvelle partie.")
                nom = input("Entrez le nom de votre personnage : ")
                personnage = Heros(nom)
                exploration = Exploration(personnage)
                return personnage, exploration
        else:
            print("Choix invalide, veuillez entrer 1 ou 2.")

def main():
    personnage, exploration = menu_principal()
    
    while personnage.est_vivant():
        print("\nQue voulez-vous faire ?")
        action = input(f"({GOLD}bag{RESET}/{AZURE}carte{RESET}/{ROUGE}save{RESET}/{VERT}north{RESET}/{VERT}south{RESET}/{VERT}east{RESET}/{VERT}west{RESET}/quit) : ").lower()
        
        if action == "bag":
            menu_inventaire(personnage)
        elif action == "carte":
            menu_carte(exploration)
        elif action == "save":
            sauvegarder_partie(personnage, exploration)
        elif action in ["north", "south", "east", "west"]:
            exploration.deplacer(action)
        elif action == "quit":
            print("Merci d'avoir joué !")
            break
        else:
            print("Action non reconnue.")

def menu_inventaire(personnage):
    while True:
        print(f"{GOLD}\nMenu Inventaire :")
        action = input(f"(bag/status/equiper/retour) : {RESET}").lower()
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
