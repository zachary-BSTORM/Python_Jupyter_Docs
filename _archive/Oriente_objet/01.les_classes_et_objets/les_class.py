# Pour creer une classe en python, nous allons utiliser le mot clé class suivi du nom de la classe.
# # Le nom de la classe doit commencer par une majuscule et suivre la convention UpperCamelCase ou PascalCase.
# # les noms de variables et de fonctions doivent commencer par une minuscule et suivre la convention snake_case.

# # Les noms de classes doivent être explicites et décrire la responsabilité de la classe.
# # Les noms de fichiers doivent être explicites et décrire le contenu du fichier.

# donc nous precisons le mot class puis le nom de la classe suivi des parentes () et deux points :
# # la classe est un plan de construction pour créer des objets.
# # Un objet est une instance d'une classe.
# # Une classe peut contenir des attributs (variables) et des méthodes (fonctions).

# # Les attributs sont des variables qui décrivent l'objet et ses caractéristiques.

# par exemple : 
# une classe Voiture peut avoir des attributs comme la couleur, la marque et le modèle.
# une classe utilisateur peut avoir des attributs comme le nom, l'âge et l'adresse e-mail.
# une classe animal peut avoir des attributs comme le nom, la couleur et l'âge.

# ===============================================================================================================================

# ici nous allons creer une classe Animal qui represente un animal
class Animal():
    '''
    Classe qui représente un animal. 
    '''
    # pass : signifie que la classe est vide
    # pass est un mot clé qui permet de créer une classe vide
    
    '''
    # Attributs de la classe Animal
    # Un attribut est une variable qui appartient à la classe
    # On peut les définir dans le constructeur ou en dehors de celui-ci
    # Ici on les définit dans le constructeur
    '''
    
    # on peut définir des attributs de classe qui sont partagés par toutes les instances de la classe
    # name = "Animal"
    # age = 0
    # couleur = "Marron"
    
    
    
    
    # Constructeur de la classe Animal
    # Le constructeur est une méthode spéciale qui est appelée lors de la création d'un objet de la classe
    # le mot clé self fait référence à l'objet lui-même à l'instance de la classe
    # on peut ajouter des paramètres au constructeur pour initialiser les attributs de la classe
    def __init__(self, nom, couleur , age):
        '''
        # ici on parle d'une variable d'instance
        # qui est une variable qui appartient à l'objet instancié 
        # accessible par le mot clé self
        # chaque instance de la classe a sa propre variable ( nom, couleur, age)
        '''
        self.nom = nom
        self.couleur = couleur
        self.age = age
        
        
    def Communiquer(self):
         print(f"Je suis un animal je m'appelle {self.nom} et je suis de couleur {self.couleur} et j'ai {self.age} ans")
         
         
         
# ==============================================================================================================================


class Chien():
    '''
    classe qui représente un chien. 
    '''
    
    # Attributs de la classe Chien
    # Un attribut est une variable qui appartient à la classe
    # On peut les définir dans le constructeur ou en dehors de celui-ci
    
    name = "Chien"
    age = 0
    couleur = "Marron"
    
    # Constructeur de la classe Chien
    # Le constructeur est une méthode spéciale qui est appelée lors de la création d'un objet de la classe
    def __init__(self, nom, age, couleur):
        self.nom = nom
        self.age = age
        self.couleur = couleur
        
        
    # Méthode de la classe Chien
    # Une méthode est une fonction qui appartient à la classe
    
    def Communiquer(self):
        print(f"Je suis un chien je m'appelle {self.nom} et je suis de couleur {self.couleur} et j'ai {self.age} ans")
        
    def Manger(self):
        print(f"{self.nom} mange des croquettes")
        
    def Dormir(self):
        print(f"{self.nom} dort sur le canapé vive les poils")
        
# maintenant que nous avons nos classes, nous allons les utiliser pour créer des objets.