# pour pouvoir utiliser nos classes, nous allons les importer dans notre fichier de test
# et les instancier pour créer des objets

# ici nous importons la classe Animal
from les_class import Animal

# ici nous importons la classe Chien
from les_class import Chien

# ici nous precisons que le code qui suit ne sera executé que si le fichier est executé directement
# et non pas s'il est importé en tant que module dans un autre fichier
if __name__ == "__main__":


# Instanciation de la classe Animal
# On crée un objet de la classe Animal
# On peut passer des arguments au constructeur de la classe
# On peut aussi ne pas passer d'arguments au constructeur de la classe, mais il faut alors définir des valeurs par défaut pour les arguments du constructeur

    rex = Animal("rex", "roux", 5)
    
    
    # On peut accéder aux attributs de l'objet en utilisant le point
    rex.nom = "rex"
    rex.couleur = "roux"
    rex.age = 5

    # On peut utiliser les methodes de l'objet a partir du moment ou nous avons une instance de la classe
    # On peut appeler la méthode Communiquer de l'objet rex qui est une instance de la classe Animal
    rex.Communiquer();
    
    