from classe.super_class import Coffre
from classe.class_item import Epee, Bouclier, Casque, Armure

class Coffre_Epee(Coffre):
    def __init__(self):
        super().__init__(Epee(valeur=10, crit_bonus=0.5))

    def ouvrir(self):
        print(f"Vous avez trouvé une {self.item.nom} dans le coffre.")

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
        print(f"Vous avez trouvé une {self.item.nom} dans le coffre.")