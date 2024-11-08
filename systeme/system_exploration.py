import random
from classe.class_character import Slime, Gobelin, Squelette, Orc, Troll, Dragon, ChauveSouris, VerDeSable
from classe.super_class import Map
from classe.maps import Foret, Plage, Grotte, Desert, Volcan

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
                    print(f"\033[30mP\033[0m", end=" ")

                elif self.carte_active.changement_map([y, x]):
                    print(f"\033[30mS\033[0m", end=" ")

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
            monstre = self.carte_active.spawn_monstre(self.position)
            if monstre:
                print(f"Vous avez rencontré un {monstre.nom} de niveau {monstre.niveau} avec {monstre.hp} HP!")
                from systeme.system_combat import Combat
                combat = Combat(self.personnage, monstre)
                combat.combattre()
            else:
                print("Rien ne se passe.")

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


