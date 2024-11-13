from classe.super_class import Coffre
from classe.class_item import Epee, Bouclier, Casque, Armure

class Coffre_Epee(Coffre):
    def __init__(self):
        super().__init__(Epee(valeur=10, multiplicateur_critique=0.5))

    def ouvrir(self):
        if not self.ouvert:
            self.ouvert = True
            print(f"Vous avez trouvé une {self.item.nom} dans le coffre.")
        else:
            print("Coffre vide, vous avez déjà récupéré l'objet.")

class Coffre_Bouclier(Coffre):
    def __init__(self):
        super().__init__(Bouclier(5))

    def ouvrir(self):
        if not self.ouvert:
            self.ouvert = True
            print(f"Vous avez trouvé un {self.item.nom} dans le coffre.")
        else:
            print("Coffre vide, vous avez déjà récupéré l'objet.")

class Coffre_Casque(Coffre):
    def __init__(self):
        super().__init__(Casque(valeur=3, chance_critique=0.3))

    def ouvrir(self):
        if not self.ouvert:
            self.ouvert = True
            print(f"Vous avez trouvé un {self.item.nom} dans le coffre.")
        else:
            print("Coffre vide, vous avez déjà récupéré l'objet.")

class Coffre_Armure(Coffre):
    def __init__(self):
        super().__init__(Armure(7))

    def ouvrir(self):
        if not self.ouvert:
            self.ouvert = True
            print(f"Vous avez trouvé une {self.item.nom} dans le coffre.")
        else:
            print("Coffre vide, vous avez déjà récupéré l'objet.")