import random
from classe.super_class import Item, Personnage, Attaquant
from classe.class_item import Armure, Bouclier, Casque, Epee, PotionSoin, PotionAttaque, PotionDefense

CRITIQUE = "\033[38;5;226m"
RESET = "\033[0m"

class Heros(Personnage, Attaquant):
    def __init__(self, nom, niveau=1, hp=100, attaque=10, defense=5, esquive=15):
        super().__init__(nom, niveau, hp, attaque, defense)
        self.esquive = esquive

    def equiper(self, objet):
        if isinstance(objet, Item):
            if isinstance(objet, Epee):
                self.equipement["Épée"] = objet
            elif isinstance(objet, Bouclier):
                self.equipement["Bouclier"] = objet
            elif isinstance(objet, Casque):
                self.equipement["Casque"] = objet
            elif isinstance(objet, Armure):
                self.equipement["Armure"] = objet
            self.inventaire.remove(objet)
            objet.utiliser(self)

    def attaquer(self, cible):
        critique = random.random() < 0.2
        dommage = max(0, self.attaque - cible.defense)
        if critique:
            dommage = int(dommage * 1.5)
            print(f"{CRITIQUE}Coup critique ! {RESET}")
        if self.niveau < cible.niveau:
            diff = cible.niveau - self.niveau
            dommage *= (1 - 0.1 * diff)
        elif self.niveau > cible.niveau:
            diff = self.niveau - cible.niveau
            dommage *= (1 + 0.1 * diff)
        dommage = max(0, int(dommage))
        cible.hp -= dommage
        return dommage

class Monstre(Personnage, Attaquant):
    def __init__(self, nom, niveau=1, hp=100, attaque=10, defense=5, tacle=5):
        super().__init__(nom, niveau, hp, attaque, defense)
        self.tacle = tacle

    def attaquer(self, cible):
        dommage = max(0, self.attaque - cible.defense)
        if self.niveau < cible.niveau:
            diff = cible.niveau - self.niveau
            dommage *= (1 + 0.1 * diff)
        elif self.niveau > cible.niveau:
            diff = self.niveau - cible.niveau
            dommage *= (1 - 0.1 * diff)
        dommage = max(0, int(dommage))
        cible.hp -= dommage
        return dommage

class Gobelin(Monstre):
    def __init__(self):
        super().__init__("Gobelin", niveau=1, hp=30, attaque=5, defense=2, tacle=5)

class ChauveSouris(Monstre):
    def __init__(self):
        super().__init__("Chauve-Souris", niveau=1, hp=30, attaque=5, defense=3, tacle=2)

class VerDeSable(Monstre):
    def __init__(self):
        super().__init__("Ver de Sable", niveau=4, hp=75, attaque=15, defense=25, tacle=8)

class Orc(Monstre):
    def __init__(self):
        super().__init__("Orc", niveau=3, hp=50, attaque=10, defense=5, tacle=7)

class Troll(Monstre):
    def __init__(self):
        super().__init__("Troll", niveau=4, hp=70, attaque=15, defense=7, tacle=10)

class Squelette(Monstre):
    def __init__(self):
        super().__init__("Squelette", niveau=2, hp=40, attaque=7, defense=3, tacle=15)

class Dragon(Monstre):
    def __init__(self):
        super().__init__("Dragon", niveau=5, hp=100, attaque=20, defense=10, tacle=100)

class Slime(Monstre):
    def __init__(self, niveau=1):
        super().__init__("Slime", niveau=niveau, hp=20 + (niveau * 5), attaque=3 + (niveau * 2), defense=1 + (niveau), tacle=3)

    def drop_potion(self):
        potions = [
            PotionSoin(self.niveau * 10),
            PotionAttaque(5),
            PotionDefense(5)
        ]
        return random.choice(potions)