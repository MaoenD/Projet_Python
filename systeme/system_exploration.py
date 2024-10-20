import random
from classe.class_character import Slime, Gobelin, Squelette, Orc, Troll, Dragon

class Exploration:
    def __init__(self, personnage):
        self.personnage = personnage
        self.monstres = []
        self.niveau_slime = 1
        self.initialiser_monstres()
        self.carte = self.carte()
        self.position = [2, 2]

    def carte(self):
        return [
            ["Forêt", "Forêt", "Forêt", "Forêt", "Forêt"],
            ["Forêt", "Forêt", "Forêt", "Forêt", "Forêt"],
            ["Forêt", "Forêt", "Départ", "Forêt", "Forêt"],
            ["Forêt", "Forêt", "Forêt", "Forêt", "Forêt"],
            ["Forêt", "Forêt", "Forêt", "Forêt", "Forêt"]
        ]

    def afficher_carte(self):
        for y, ligne in enumerate(self.carte):
            for x, zone in enumerate(ligne):
                if [y, x] == self.position:
                    print("P", end=" ")
                else:
                    print("X", end=" ")
            print()

    def deplacer(self, direction):
        y, x = self.position
        if direction == "north" and y > 0:
            self.position[0] -= 1
        elif direction == "south" and y < len(self.carte) - 1:
            self.position[0] += 1
        elif direction == "west" and x > 0:
            self.position[1] -= 1
        elif direction == "east" and x < len(self.carte[0]) - 1:
            self.position[1] += 1
        else:
            print("Vous ne pouvez pas aller dans cette direction.")
        
        self.description_zone()

        monstre = self.explorer()
        if monstre:
            from systeme.system_combat import Combat
            combat = Combat(self.personnage, monstre)
            combat.combattre()

    def description_zone(self):
        y, x = self.position
        zone = self.carte[y][x]
        
        if zone == "Départ":
            print("Vous êtes à votre point de départ.")
        elif zone == "Forêt":
            print("Vous êtes dans une forêt dense.")
        elif zone == "Vide":
            print("Il n'y a rien ici.")

    def initialiser_monstres(self):
        self.monstres.append(Gobelin())
        self.monstres.append(Squelette())
        self.monstres.append(Orc())
        self.monstres.append(Troll())
        self.monstres.append(Dragon())

    def explorer(self):
        print("Vous explorez la forêt...")
        if random.choice([True, False]):
            if random.choice([True, False]):
                monstre = Slime(niveau=self.niveau_slime)
                self.niveau_slime += 5
            else:
                monstre = random.choice(self.monstres)
            print(f"Vous avez rencontré un {monstre.nom} de niveau {monstre.niveau}!")
            return monstre
        else:
            print("Rien ne se passe.")
            return None
