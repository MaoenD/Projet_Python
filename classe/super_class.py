from abc import ABC, abstractmethod

class Personnage(ABC):
    def __init__(self, nom, niveau=1, hp=100, attaque=10, defense=5):
        self.nom = nom
        self.niveau = niveau
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self.defense = defense
        self.xp = 0
        self.inventaire = []

    @abstractmethod
    def attaquer(self, cible):
        pass

    def utiliser_objet(self, objet):
        if objet in self.inventaire:
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

class Map(ABC):
    def __init__(self, nom, taille=10):
        self.nom = nom
        self.taille = taille
        self.grille = self.generer_map()

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
