import random
from abc import ABC, abstractmethod
from classe.class_personnage_rpg import Gobelin, Orc, Troll, Squelette, Dragon, Slime

class Instance(ABC):
    def __init__(self, personnage, difficulte='normale'):
        self.personnage = personnage
        self.difficulte = difficulte
        self.niveau_actuel = 1
        self.monstres_possibles = []
        self.initialiser_monstres()

    @abstractmethod
    def initialiser_monstres(self):
        pass

    @abstractmethod
    def generer_monstre(self):
        pass

    def prochaine_etape(self):
        self.niveau_actuel += 1
        if self.niveau_actuel % 5 == 0:
            self.monstres_possibles.append(Dragon())
        return self.niveau_actuel

class InstanceForet(Instance):
    def initialiser_monstres(self):
        self.monstres_possibles = [Gobelin(), Squelette(), Slime()]

    def generer_monstre(self):
        if random.random() < 0.3:
            return Slime(niveau=self.niveau_actuel)
        else:
            return random.choice(self.monstres_possibles)

class InstanceCaverne(Instance):
    def initialiser_monstres(self):
        self.monstres_possibles = [Orc(), Troll(), Dragon()]

    def generer_monstre(self):
        if random.random() < 0.5:
            return Troll()
        else:
            return random.choice(self.monstres_possibles)