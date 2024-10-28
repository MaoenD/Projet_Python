import random
from classe.class_character import Slime, Gobelin, Squelette, Orc, Troll, Dragon
from classe.super_class import Map

class Foret(Map):
    def generer_map(self):
        grille = [["Forêt"] * self.taille for _ in range(self.taille)]
        grille[9][5] = "SortieForêt"
        return grille

    def changement_map(self, position):
        return position == [9, 5]

    def prochaine_map(self):
        return "plage", [0, 5]

class Plage(Map):
    def generer_map(self):
        grille = [["Plage"] * self.taille for _ in range(self.taille)]
        grille[0][5] = "SortiePlage"
        return grille

    def changement_map(self, position):
        return position == [0, 5]

    def prochaine_map(self):
        return "grotte", [9, 9]

class Grotte(Map):
    def generer_map(self):
        grille = [["Grotte"] * self.taille for _ in range(self.taille)]
        grille[9][9] = "SortieGrotte"
        return grille

    def changement_map(self, position):
        return position == [9, 9]

    def prochaine_map(self):
        return "desert", [5, 0]

class Desert(Map):
    def generer_map(self):
        grille = [["Désert"] * self.taille for _ in range(self.taille)]
        grille[5][0] = "SortieDésert"
        return grille

    def changement_map(self, position):
        return position == [5, 0]

    def prochaine_map(self):
        return "volcan", [0, 0]

class Volcan(Map):
    def generer_map(self):
        grille = [["Volcan"] * self.taille for _ in range(self.taille)]
        grille[0][0] = "SortieVolcan"
        return grille

    def changement_map(self, position):
        return position == [0, 0]

    def prochaine_map(self):
        return None, None

class Exploration:
    def __init__(self, personnage):
        self.personnage = personnage
        self.monstres = []
        self.niveau_slime = 1
        self.initialiser_monstres()
        self.cartes = {
            "foret": Foret("Forêt"),
            "plage": Plage("Plage"),
            "grotte": Grotte("Grotte"),
            "desert": Desert("Désert"),
            "volcan": Volcan("Volcan")
        }
        self.carte_active = self.cartes["foret"]
        self.position = [5, 5]

    def afficher_carte(self):
        for y, ligne in enumerate(self.carte_active.grille):
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
        elif direction == "south" and y < self.carte_active.taille - 1:
            self.position[0] += 1
        elif direction == "west" and x > 0:
            self.position[1] -= 1
        elif direction == "east" and x < self.carte_active.taille - 1:
            self.position[1] += 1
        else:
            print("Vous ne pouvez pas aller dans cette direction.")
        
        self.description_zone()

        if self.carte_active.changement_map(self.position):
            self.changer_carte()

        monstre = self.explorer()
        if monstre:
            from systeme.system_combat import Combat
            combat = Combat(self.personnage, monstre)
            combat.combattre()

    def description_zone(self):
        y, x = self.position
        zone = self.carte_active.grille[y][x]

    def changer_carte(self):
        prochaine, position = self.carte_active.prochaine_map()
        if prochaine:
            self.carte_active = self.cartes[prochaine]
            self.position = position
            print(f"Vous changé de zone pour arriver dans la zone {self.carte_active.nom}.")
        else:
            print("Vous êtes dans la zone du boss. Fin de l'aventure !")

    def initialiser_monstres(self):
        self.monstres.extend([Gobelin(), Squelette(), Orc(), Troll(), Dragon()])

    def explorer(self):
        print("Vous explorez la zone...")
        if random.choice([True, False]):
            monstre = random.choice(self.monstres)
            print(f"Vous avez rencontré un {monstre.nom} de niveau {monstre.niveau}!")
            return monstre
        else:
            print("Rien ne se passe.")
            return None
