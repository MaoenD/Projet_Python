import random
from classe.class_character import Slime, Gobelin, Squelette, Orc, Troll, Dragon, ChauveSouris, VerDeSable
from classe.super_class import Map

class Foret(Map):
    def generer_map(self):
        grille = [["Forêt"] * self.taille for _ in range(self.taille)]
        grille[9][5] = "SortieForêt"
        return grille

    def changement_map(self, position):
        return position == [9, 5]

    def prochaine_map(self):
        return "plage", [0, 0]
    
    def zone_safe(self, position):
        return position == [9, 5] or position == [0, 0]
    
    def get_monstres(self):
        return [Gobelin(), Orc(), Troll(), Slime()]
    
    def spawn_monstre(self, position):
        if random.choice([True, False]):
            return random.choice(self.get_monstres())
        return None

class Plage(Map):
    def generer_map(self):
        grille = [["Plage"] * self.taille for _ in range(self.taille)]
        grille[0][5] = "SortiePlage"
        return grille

    def changement_map(self, position):
        return position == [0, 5]

    def prochaine_map(self):
        return "grotte", [9, 0]
    
    def zone_safe(self, position):
        return position == [0, 5] or position == [9, 0]
    
    def get_monstres(self):
        return [Squelette(), Orc(), Troll(), Slime()]
    
    def spawn_monstre(self, position):
        if random.choice([True, False]):
            return random.choice(self.get_monstres())
        return None

class Grotte(Map):
    def generer_map(self):
        grille = [["Grotte"] * self.taille for _ in range(self.taille)]
        grille[9][9] = "SortieGrotte"
        return grille

    def changement_map(self, position):
        return position == [9, 9]

    def prochaine_map(self):
        return "desert", [0, 5]
    
    def zone_safe(self, position):
        return position == [9, 9] or position == [0, 5]
    
    def get_monstres(self):
        return [ChauveSouris(), Troll(), Slime()]
    
    def spawn_monstre(self, position):
        if random.choice([True, False]):
            return random.choice(self.get_monstres())
        return None

class Desert(Map):
    def generer_map(self):
        grille = [["Désert"] * self.taille for _ in range(self.taille)]
        grille[5][0] = "SortieDésert"
        return grille

    def changement_map(self, position):
        return position == [5, 0]

    def prochaine_map(self):
        return "volcan", [9, 9]
    
    def zone_safe(self, position):
        return position == [5, 0] or position == [9, 9]
    
    def get_monstres(self):
        return [VerDeSable(), Slime()]
    
    def spawn_monstre(self, position):
        if random.choice([True, False]):
            return random.choice(self.get_monstres())
        return None

class Volcan(Map):
    def generer_map(self):
        grille = [["Volcan"] * self.taille for _ in range(self.taille)]
        grille[0][0] = "SortieVolcan"
        return grille

    def changement_map(self, position):
        return position == [0, 0]

    def prochaine_map(self):
        return None, None
    
    def zone_safe(self, position):
        return position == [0, 0]
    
    def get_monstres(self):
        return [Dragon()]
    
    def spawn_monstre(self, position):
        if position == [5, 5]:
            return Dragon()
        return None

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
        self.carte_active.grille = self.carte_active.generer_map()

    def afficher_carte(self):
        for y, ligne in enumerate(self.carte_active.grille):
            for x, zone in enumerate(ligne):
                if zone == "Forêt" or zone == "SortieForêt":
                    couleur = "\033[32m"  # Vert 
                elif zone == "Plage" or zone == "SortiePlage":
                    couleur = "\033[37m"  # Blanc 
                elif zone == "Grotte" or zone == "SortieGrotte":
                    couleur = "\033[34m"  # Bleu
                elif zone == "Désert" or zone == "SortieDésert":
                    couleur = "\033[93m"  # Jaune 
                elif zone == "Volcan" or zone == "SortieVolcan":
                    couleur = "\033[31m"  # Rouge 
                else:
                    couleur = "\033[0m"

                if [y, x] == self.position:
                    print(f"{couleur}P\033[0m", end=" ")
                else:
                    print(f"{couleur}X\033[0m", end=" ")
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
            return
        
        if self.carte_active.zone_safe(self.position):
            print("Vous êtes dans une zone sûre.")
        else:

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
            self.carte_active.grille = self.carte_active.generer_map()
            print(f"Vous avez changé de zone pour arriver dans la zone {self.carte_active.nom}.")
        else:
            print("Vous êtes dans la zone du boss.")

    def initialiser_monstres(self):
        self.monstres.extend([Gobelin(), Squelette(), Orc(), Troll(), Dragon(), ChauveSouris(), VerDeSable()])

    def explorer(self):
        print("Vous explorez la zone")

        monstre = self.carte_active.spawn_monstre(self.position)

        if monstre:
            print(f"Vous avez rencontré un {monstre.nom} de niveau {monstre.niveau} avec {monstre.hp} HP!")
            return monstre
        else:
            print("Rien ne se passe.")
            return None


