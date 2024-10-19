from classe.super_class import Item

class PotionSoin(Item):
    def __init__(self, valeur):
        super().__init__("Potion de soin", valeur)

    def utiliser(self, personnage):
        personnage.hp = min(personnage.hp_max, personnage.hp + self.valeur)
        print(f"{personnage.nom} a été soigné de {self.valeur} points de vie. HP actuel : {personnage.hp} / {personnage.hp_max}")

class PotionAttaque(Item):
    def __init__(self, valeur):
        super().__init__("Potion d'attaque", valeur)

    def utiliser(self, personnage):
        personnage.attaque += self.valeur
        print(f"{personnage.nom} a reçu un boost d'attaque de {self.valeur}. Attaque actuelle : {personnage.attaque}")

class PotionDefense(Item):
    def __init__(self, valeur):
        super().__init__("Potion de defense", valeur)

    def utiliser(self, personnage):
        personnage.defense += self.valeur
        print(f"{personnage.nom} a reçu un boost de défense de {self.valeur}. Défense actuelle : {personnage.defense}")

class Fumigene(Item):
    def __init__(self, valeur):
        super().__init__("Fumigène", valeur)

    def utiliser(self, personnage):
        personnage.esquive += self.valeur
        print(f"{personnage.nom} a utilisé un fumigène. Esquive augmentée de {self.valeur} pour 2 tours")

class Bombe(Item):
    def __init__(self, valeur):
        super().__init__("Bombe", valeur)

    def utiliser(self, personnage, monstre):
        monstre.hp = max(0, monstre.hp - self.valeur)
        print(f"Vous avez utilisé une bombe infligeant {self.valeur} points de dégâts au {monstre.nom}.")

