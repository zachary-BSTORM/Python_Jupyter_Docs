from datetime import date


class Soigneur():
    
    def __init__(self, nom, date_naissance, experience):
        self.nom = nom
        self.date_naissance = date_naissance
        self.experience = experience
        self.nombre_animaux_responsable = 0
    
    def nourir(self, animal):
        print(f"{self.nom} nourrit {animal.nom}")
        animal.appetit = 100
        
    def entretenir(self, animal):
        print(f"{self.nom} s'occupe de {animal.nom}")
        animal.satisfaction = 100
        
    