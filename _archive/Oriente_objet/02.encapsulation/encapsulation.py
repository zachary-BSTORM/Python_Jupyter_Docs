# Maintenant que nous avons la possibilité de créer des classes, nous pouvons limiter l'accès à certain attributs
# on retrouve trois niveaux d'accès:
# - Public : accessible de partout
# - Protégé : accessible uniquement dans la classe et ses sous-classes
# - Privé : accessible uniquement dans la classe

#####################################################################################################################################
# Attention python ne fait pas de vrai encapsulation, il utilise des conventions de nommage pour indiquer le niveau d'accès
# donc il simule un niveau d'accès par des conventions de nommage
# par defaut, tous les attributs sont publics
#####################################################################################################################################


# pour définir un attribut PRIVATE , il suffit de le préfixer par un double underscore __
## un attribut privé est accessible uniquement dans la classe
## a l'execution, python va renommer l'attribut pour le rendre inaccessible
## par exemple, si on a un attribut __name, python va le renommer en _Chien__name

# pour définir un attribut PROTECTED , il suffit de le préfixer par un underscore _
## un attribut protected est accessible dans la classe et ses sous-classes

# pour définir un attribut PUBLIC , il suffit de ne pas le préfixer
## un attribut public est accessible de partout




#============================================================================================================================
         
class Rectangle():

    # Constructeur
    # def __init__(self , l , h):
    #     # Attributs  
    #     self.largeur = l
    #     self.hauteur = h
    
    # on precise ici le self qui est une référence à l'instance de la classe
    def __init__(self,l,h):
        self.set_largeur(l)
        self.set_hauteur(h)
        
    # Méthode de la classe Rectangle
    
    def Surface(self):
        return self.largeur * self.hauteur
    
    def __str__(self):
        return f"Rectangle de largeur {self.largeur} et de hauteur {self.hauteur} et de surface {self.Surface()}"
    
    
    #============================================================================================================================
    # pour acceder a nos attributs nous pouvons definir ce qu'on appelle les getters et setters:
    # un getter est une méthode qui permet d'accéder à la valeur d'un attribut
    # un setter est une méthode qui permet de modifier la valeur d'un attribut
    #============================================================================================================================    
    
    # Méthode pour changer la largeur et la hauteur
    #on appelle ça un setter
    def set_hauteur(self, h):
        if h > 0:
            self.hauteur = h
            
    def set_largeur(self, l):
        if l > 0:
            self.largeur = l
            
    # Méthode pour recuperer la largeur et la hauteur
    #on appelle ça un getter
    
    def get_hauteur(self):
        return self.hauteur
    
    def get_largeur(self):
        return self.largeur
    
        
    #============================================================================================================================


    # le mot clé property permet de creer des attributs de classe sans utiliser de parenthèses
    
    @property
    def hauteur(self):
        return self.__hauteur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @hauteur.getter
    def hauteur(self):
        return self.__hauteur
    
    @largeur.getter
    def largeur(self):
        return self.__largeur
    
    @hauteur.setter
    def hauteur(self, h):
        if h > 0:
            self.__hauteur = h
            
    @largeur.setter
    def largeur(self, l):
        if l > 0:
            self.__largeur = l
            
    @hauteur.deleter
    def hauteur(self):
        del self.__hauteur
        
    @largeur.deleter
    def largeur(self):
        del self.__largeur
        
    