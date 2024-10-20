from systeme.system_exploration import Exploration
from systeme.system_combat import Combat
from classe.class_character import Heros

def main():
    print("Bienvenue dans le jeu RPG !")
    nom = input("Entrez le nom de votre personnage : ")
    personnage = Heros(nom)
    exploration = Exploration(personnage)

    while personnage.est_vivant():
        exploration.afficher_carte()
        print("\nQue voulez-vous faire ?")
        action = input("(explorer/inventaire/quitter/north/south/east/west) : ").lower()
        
        if action == "explorer":
            monstre = exploration.explorer()
            if monstre:
                combat = Combat(personnage, monstre)
                combat.combattre()
        elif action == "inventaire":
            menu_inventaire(personnage)
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
        action = input("(ouvrir inventaire/check statut/retour) : ").lower()
        if action == "ouvrir inventaire":
            ouvrir_inventaire(personnage)
        elif action == "check statut":
            afficher_statut(personnage)
        elif action == "retour":
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
