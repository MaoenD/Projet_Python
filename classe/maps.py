import random
from classe.class_character import Slime, Gobelin, Squelette, Orc, Troll, Dragon, ChauveSouris, VerDeSable
from classe.super_class import Map
from classe.coffre import Coffre_Epee, Coffre_Bouclier, Coffre_Casque, Coffre_Armure

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
        return position == [9, 5] or position == [0, 0] or position == [2, 2]
    
    def get_monstres(self):
        return [Gobelin(), Orc(), Troll(), Slime()]
    
    def spawn_monstre(self, position):
        if random.choice([True, False]):
            return random.choice(self.get_monstres())
        return None
    
    def def_coffres(self):
        self.coffres[(2, 2)] = Coffre_Epee()

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
        return position == [0, 5] or position == [9, 0] or position == [4, 4]
    
    def get_monstres(self):
        return [Squelette(), Orc(), Troll(), Slime()]
    
    def spawn_monstre(self, position):
        if random.choice([True, False]):
            return random.choice(self.get_monstres())
        return None
    
    def def_coffres(self):
        self.coffres[(4, 4)] = Coffre_Bouclier()

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
        return position == [9, 9] or position == [0, 5] or position == [6, 6]
    
    def get_monstres(self):
        return [ChauveSouris(), Troll(), Slime()]
    
    def spawn_monstre(self, position):
        if random.choice([True, False]):
            return random.choice(self.get_monstres())
        return None
    
    def def_coffres(self):
        self.coffres[(6, 6)] = Coffre_Casque()

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
        return position == [5, 0] or position == [9, 9] or position == [8, 8]
    
    def get_monstres(self):
        return [VerDeSable(), Slime()]
    
    def spawn_monstre(self, position):
        if random.choice([True, False]):
            return random.choice(self.get_monstres())
        return None
    
    def def_coffres(self):
        self.coffres[(8, 8)] = Coffre_Armure()

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
    
    def def_coffres(self):
        self.coffres = {}