import random
from classe.class_character import Slime, Gobelin, Squelette, Orc, Troll, Dragon

class Exploration:
    def __init__(self, personnage):
        self.personnage = personnage
        self.monstres = []
        self.niveau_slime = 1
        self.initialiser_monstres()

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
