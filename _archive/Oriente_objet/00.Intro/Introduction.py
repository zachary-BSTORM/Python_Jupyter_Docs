# l'orienté objet 
# est un paradigme de programmation qui utilise des objets pour représenter des données et des comportements.
# Il permet de structurer le code de manière modulaire et réutilisable.

# Comparaison avec la programmation procédurale :
# Dans la programmation procédurale, le code est organisé en fonctions et procédures,
# tandis que dans l'orienté objet, le code est organisé autour d'objets qui encapsulent à la fois des données et des méthodes.
# Cela permet de mieux modéliser le monde réel et de créer des programmes plus complexes et flexibles.

# ===================================================================================================================================

# Les concepts clés de l'orienté objet incluent :
# 1. Classes : Modèles pour créer des objets. Elles définissent les attributs et les méthodes d'un objet.
# 2. Objets : Instances de classes. Ils contiennent des données et peuvent exécuter des méthodes.
# 3. Héritage : Mécanisme permettant de créer une nouvelle classe à partir d'une classe existante, en héritant de ses attributs et méthodes.
# 4. Polymorphisme : Capacité à traiter des objets de différentes classes de manière uniforme, en utilisant une interface commune.
# 5. Encapsulation : Protection des données d'un objet en restreignant l'accès direct à ses attributs et en fournissant des méthodes pour interagir avec eux.
# 6. Abstraction : Simplification de la complexité en cachant les détails d'implémentation et en ne montrant que les fonctionnalités essentielles.

# ====================================================================================================================================
# Concretement, 
# l'orienté objet permet de créer des programmes plus organisés et faciles à maintenir 
# en regroupant les données et les comportements associés dans des objets.

# par exemple une voiture peut être représentée par une classe "Voiture" qui a des attributs comme "marque", "modèle" et "année",
# et des méthodes comme "démarrer" et "accélérer".

# En utilisant l'orienté objet, on peut créer plusieurs objets "Voiture" avec des valeurs différentes pour les attributs,
# tout en partageant les mêmes méthodes.

# chaque voiture est unique mais elles partagent toutes les mêmes comportements basés sur la classe( le model ) "Voiture".

# =====================================================================================================================================

# En résumé, l'orienté objet est un paradigme de programmation 
# qui facilite la création de programmes modulaires, réutilisables et faciles à maintenir.
# Il repose sur des concepts tels que :  les classes, les objets, l'héritage, le polymorphisme, l'encapsulation et l'abstraction.

# ======================================================================================================================================

# Vu que nous allons structurer notre code en classes et objets,
# nous allons structurer notre code egalement.

# Il est possible de creer un dossier Models qui contiendra tous les models de notre application.
# et dans ce dossiers chaque classe sera dans un fichier a part.
# Par exemple, si nous avons une classe "Voiture", nous allons creer un fichier "Voiture.py" dans le dossier Models.
# dans le cas ou nous aurions plusieurs classes liées au meme model il peut etre judicieux de les mettre dans un dossier également.

# si nous avions besoin d'un model "Utilisateur" nous pourrions avoir besoin d'une classe 
# pour ajouter un utilisateur ( sans identifiant dans le cas ou il serait généré automatiquement )
# pour que l'utilisateur puisse modifier ses données ( sans identifiant également et sans mot de passe ni role(admin - user))
# pour que l'utilisateur se connecte (ou nous n'aurions besoin que de son identifiant et mot de passe )

# donc bien structurer notre code en dossiers et sous dossiers et fichiers est important.

# =========================================================================================================================

 # A partir du moment ou nous avons des elements dans plusieurs endroits de notre programme,
 # nous allons devoir les importer dans les fichiers ou nous en avons besoin.
 # Pour ceci il y a une logique d'importation à comprendre.
 
    # En python, nous avons plusieurs types d'importation :
    # 1. Importer un module entier :
    #    import module_name 
    
    #    Exemple : import math
    #    Cela importe le module math entier et vous pouvez accéder à ses fonctions en utilisant le préfixe math.
    
    #    Exemple : math.sqrt(16)  # Renvoie 4.0
    # 2. Importer une fonction spécifique d'un module :
    #    from module_name import function_name
    #    Exemple : from math import sqrt
    #    Cela importe uniquement la fonction sqrt du module math, vous pouvez l'utiliser directement sans le préfixe math.
    #    Exemple : sqrt(16)  # Renvoie 4.0
    
    # 3. Importer plusieurs fonctions d'un module :
    #    from module_name import function1, function2
    #    Exemple : from math import sqrt, pow
    #    Cela importe les fonctions sqrt et pow du module math.
    #    Exemple : sqrt(16)  # Renvoie 4.0
    #    Exemple : pow(2, 3)  # Renvoie 8.0
    
    # 4. Importer un module avec un alias :
    #    import module_name as alias_name
    #    Exemple : import numpy as np
    #    Cela importe le module numpy et lui donne l'alias np, vous pouvez l'utiliser avec l'alias.
    #    Exemple : np.array([1, 2, 3])  # Crée un tableau numpy
    
    # 5. Importer tout le contenu d'un module (non recommandé) :
    #    from module_name import *
    #    Exemple : from math import *
    #    Cela importe toutes les fonctions et variables du module math, mais cela peut causer des conflits de noms.
    #    Exemple : sqrt(16)  # Renvoie 4.0
    #    Exemple : pi  # Renvoie 3.141592653589793
    #    Exemple : cos(0)  # Renvoie 1.0
    
# donc pour importer un element 

# from Models.Voiture import Voiture

# ou

# import Models.Voiture as V

# ou encore

# from Models import Voiture as V 

# Pour eviter d'executer le code de la classe lors de l'importation,
# nous allons utiliser la condition suivante :
# if __name__ == "__main__":
#     # Code à exécuter uniquement si le fichier est exécuté directement
#     # Cela n'est pas exécuté lors de l'importation du module


# if __name__ == "__main__": signifie que le code à l'intérieur de ce bloc ne sera exécuté que si le fichier est exécuté directement,
# et non pas s'il est importé en tant que module dans un autre fichier.
# Cela permet de séparer le code qui doit être exécuté lors de l'importation 
# du code qui doit être exécuté lors de l'exécution directe du fichier.

# sinon le code sera executé lors de l'importation du module dans un autre fichier.

# =========================================================================================================================

# Bonnes pratiques :

# 1. Utiliser des noms de fichiers et de classes significatifs.

# 2. eviter les noms de fichiers trop longs ou trop courts et preferer des noms explicites.

# 3. Utiliser des noms de classes en PascalCase (ex : MaClasse) et des noms de fichiers en snake_case (ex : ma_classe.py).

# 4. Un seul concept par classe : chaque classe doit avoir une seule responsabilité.

# 5. Documenter le code : ajouter des commentaires et des docstrings pour expliquer le fonctionnement de chaque classe et méthode.

