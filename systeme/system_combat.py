from classe.class_item import Bombe, Fumigene
from classe.class_character import Heros, Monstre
import random

class Combat:
    def __init__(self, personnage, monstre):
        self.personnage = personnage
        self.monstre = monstre

    def combattre(self):
        while self.monstre.est_vivant() and self.personnage.est_vivant():
            print(f"{self.personnage.nom} (HP: {self.personnage.hp}) vs {self.monstre.nom} (HP: {self.monstre.hp})")
            action = input("(attaquer/utiliser objet/fuir) : ").lower()
            if action == "attaquer":
                dommage = self.personnage.attaquer(self.monstre)
                print(f"Vous avez infligé {dommage} points de dégâts au {self.monstre.nom}.")
            elif action == "utiliser objet":
                if self.personnage.inventaire:
                    print("Inventaire :")
                    for i, objet in enumerate(self.personnage.inventaire):
                        print(f"{i + 1}. {objet.nom}")
                    choix = int(input("Choisissez un objet à utiliser : ")) - 1
                    if 0 <= choix < len(self.personnage.inventaire):
                        self.personnage.utiliser_objet(self.personnage.inventaire[choix])
                    else:
                        print("Choix invalide.")
                else:
                    print("Votre inventaire est vide.")
            elif action == "fuir":
                if self.personnage.esquive > self.monstre.tacle:
                    print("Vous avez réussi à fuir !")
                    return False
                elif self.personnage.esquive == self.monstre.tacle:
                    if random.random() < 0.5:
                        print("Vous avez réussi à fuir !")
                        return False
                    else:
                        print(f"{self.monstre.nom} vous a rattrapé, vous ne pouvez pas fuir !")
                else:
                    chance_fuite = self.personnage.esquive / (2 * self.monstre.tacle)
                    if random.random() < chance_fuite:
                        print("Vous avez réussi à fuir !")
                        return False
                    else:
                        print(f"{self.monstre.nom} vous a rattrapé, vous ne pouvez pas fuir !")
            else:
                print("Action non reconnue.")
                continue

            if self.monstre.est_vivant():
                dommage = self.monstre.attaquer(self.personnage)
                print(f"Le {self.monstre.nom} vous a infligé {dommage} points de dégâts.")

        if self.personnage.est_vivant():
            print(f"Vous avez vaincu le {self.monstre.nom} !")
            self.personnage.gagner_xp(self.monstre.niveau * 10)
            if random.random() < 0.8 and self.monstre.nom != "Slime":
                bombe = Bombe(self.monstre.niveau * 10)
                print(f"Le {self.monstre.nom} a laissé tomber une bombe !")
                self.personnage.ajouter_objet(bombe)
            elif random.random() < 0.8 and self.monstre.nom != "Slime":
                fumigene = Fumigene(self.monstre.niveau * 5)
                print(f"Le {self.monstre.nom} a laissé tomber un fumigène !")
                self.personnage.ajouter_objet(fumigene)
            elif self.monstre.nom == "Slime":
                drop_potion = self.monstre.drop_potion()
                print(f"Le {self.monstre.nom} a laissé tomber {drop_potion.nom} !")
                self.personnage.ajouter_objet(drop_potion)
            return True
        else:
            print("Vous êtes mort. Fin du jeu.")
            return False
