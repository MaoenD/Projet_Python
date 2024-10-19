from abc import ABC, abstractmethod
from super_class import Item

class Epee(Item):
    def __init__(self, valeur):
        super().__init__("Épée", valeur)

    def utiliser(self, personnage):
        personnage.attaque += self.valeur
        print(f"{personnage.nom} a équipé une épée. Attaque actuelle : {personnage.attaque}")

class Bouclier(Item):
    def __init__(self, valeur):
        super().__init__("Bouclier", valeur)

    def utiliser(self, personnage):
        personnage.defense += self.valeur
        print(f"{personnage.nom} a équipé un bouclier. Défense actuelle : {personnage.defense}")

class Casque(Item):
    def __init__(self, valeur):
        super().__init__("Casque", valeur)

    def utiliser(self, personnage):
        personnage.defense += self.valeur
        print(f"{personnage.nom} a équipé un casque. Défense actuelle : {personnage.defense}")

class Armure(Item):
    def __init__(self, valeur):
        super().__init__("Armure", valeur)

    def utiliser(self, personnage):
        personnage.defense += self.valeur
        print(f"{personnage.nom} a équipé une armure. Défense actuelle : {personnage.defense}")

class Coffre(ABC):
    def __init__(self, item):
        self.item = item

    @abstractmethod
    def ouvrir(self):
        pass

class Coffre_Epee(Coffre):
    def __init__(self):
        super().__init__(Epee(10))

    def ouvrir(self):
        print(f"Vous avez trouvé un {self.item.nom} dans le coffre.")

class Coffre_Bouclier(Coffre):
    def __init__(self):
        super().__init__(Bouclier(5))

    def ouvrir(self):
        print(f"Vous avez trouvé un {self.item.nom} dans le coffre.")

class Coffre_Casque(Coffre):
    def __init__(self):
        super().__init__(Casque(3))

    def ouvrir(self):
        print(f"Vous avez trouvé un {self.item.nom} dans le coffre.")

class Coffre_Armure(Coffre):
    def __init__(self):
        super().__init__(Armure(7))

    def ouvrir(self):
        print(f"Vous avez trouvé un {self.item.nom} dans le coffre.")


# Exemple 

coffre_epee = Coffre_Epee()
coffre_epee.ouvrir()

coffre_bouclier = Coffre_Bouclier()
coffre_bouclier.ouvrir()

coffre_casque = Coffre_Casque()
coffre_casque.ouvrir()

coffre_armure = Coffre_Armure()
coffre_armure.ouvrir()


# super_class personnage

    def equiper(self, objet):
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

# lancer jeu
    def afficher_equipement(self):
        print(f"Équipement actuel de {self.nom}:")
        for type_equipement, item in self.equipement.items():
            if item:
                print(f"{type_equipement}: {item.nom} (+{item.valeur})")
            else:
                print(f"{type_equipement}: Aucun")