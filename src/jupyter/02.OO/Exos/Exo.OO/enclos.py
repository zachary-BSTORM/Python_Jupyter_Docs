class Enclos():
    
    def __init__(self, nom, capacite_max, taille):
        self.nom = nom
        self.capacite_max = capacite_max
        self.taille = taille
        self.liste_animaux = []
        
    def ajouter_animal(self, animal):
        if len(self.liste_animaux) < self.capacite_max:
            self.liste_animaux.append(animal)
            print(f"{animal.nom} a été ajouté à l'enclos {self.nom}")
        else:
            print(f"L'enclos {self.nom} est plein")
            
    def retirer_animal(self, animal):
        if animal in self.liste_animaux:
            self.liste_animaux.remove(animal)
            print(f"{animal.nom} a été retiré de l'enclos {self.nom}")
        else:
            print(f"{animal.nom} n'est pas dans l'enclos {self.nom}")
            
    def afficher_animaux(self):
        if len(self.liste_animaux) > 0:
            print(f"Animaux dans l'enclos {self.nom}:")
            for animal in self.liste_animaux:
                print(f"{animal.nom}")
        else:
            print(f"L'enclos {self.nom} est vide")
            
    def routine(self):
        for animal in self.liste_animaux:
            animal.Manger()
            animal.soigneur.entretenir(animal)