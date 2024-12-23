from abc import ABC, abstractmethod

class Personnage(ABC):
    def __init__(self, nom, niveau=1, hp=100, attaque=10, defense=5):
        self.nom = nom
        self.niveau = niveau
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self.defense = defense
        self.multiplicateur_critique = 1.5
        self.chance_critique = 0.2
        self.xp = 0
        self.inventaire = []
        self.equipement = {"Épée": None, "Bouclier": None, "Casque": None, "Armure": None}
        
    @abstractmethod
    def attaquer(self, cible):
        pass

    def utiliser_objet(self, objet, monstre=None):
        if objet in self.inventaire:
            if objet.__class__.__name__ == "Bombe":
                objet.utiliser(self, monstre)
            else:
                objet.utiliser(self)
            self.inventaire.remove(objet)

    def gagner_xp(self, montant):
        self.xp += montant
        if self.xp >= self.niveau * 10:
            self.niveau += 1
            self.hp_max += 10
            self.hp = self.hp_max
            self.attaque += 2
            self.defense += 1

    def est_vivant(self):
        return self.hp > 0

    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
    
    def get_chance_critique(self):
        return self.chance_critique

    def get_multiplicateur_critique(self):
        return self.multiplicateur_critique

class Attaquant(ABC):
    @abstractmethod
    def attaquer(self, cible):
        pass

class Item(ABC):
    def __init__(self, nom, valeur):
        self.nom = nom
        self.valeur = valeur

    @abstractmethod
    def utiliser(self, personnage):
        pass

class Coffre(ABC):
    def __init__(self, item):
        self.item = item
        self.ouvert = False

    @abstractmethod
    def ouvrir(self):
        pass

class Map(ABC):
    def __init__(self, nom, taille=10):
        self.nom = nom
        self.taille = taille
        self.grille = self.generer_map()
        self.coffres = {}
        self.def_coffres()
    
    @abstractmethod
    def generer_map(self):
        pass

    @abstractmethod
    def changement_map(self, position):
        pass

    @abstractmethod
    def prochaine_map(self):
        pass

    @abstractmethod
    def zone_safe(self, position):
        pass

    @abstractmethod
    def get_monstres(self):
        pass

    @abstractmethod
    def spawn_monstre(self, position):
        pass

    @abstractmethod
    def def_coffres(self):
        pass