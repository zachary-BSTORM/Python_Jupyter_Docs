from soigneur import Soigneur

class Elephant():
    
    def __init__(self, nom, soigneur, appetit=100, satisfaction=100):
        self.nom = nom
        self.en_vie = True
        self.soigneur = soigneur
        self.__appetit = appetit
        self.__satisfaction = satisfaction

    def _get_appetit(self):
        return self.__appetit
    
    def _set_appetit(self, valeur):
        if 0 <= valeur <= 100:
            self.__appetit = valeur
        else:
            self.__appetit = 0
        
    appetit = property(_get_appetit, _set_appetit)
    
    def _get_satisfaction(self):
        return self.__satisfaction
    
    def _set_satisfaction(self, valeur):
        if 0 <= valeur <= 100:
            self.__satisfaction = valeur
        else:
            self.__satisfaction = 0
            
    satisfaction = property(_get_satisfaction, _set_satisfaction)

    def Manger(self):
        print(f"{self.nom} mange")
        self.appetit = 100
        self.satisfaction = 100
