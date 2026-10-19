from encapsulation import Rectangle


# # Création d'un objet de la classe Rectangle

if __name__ == "__main__":
    
    # Création d'un objet de la classe Rectangle
    rectangle = Rectangle(5, 10)
    
    # Affichage de la largeur et de la hauteur
    # avec les méthodes get_hauteur et get_largeur
    print(rectangle.get_hauteur())
    print(rectangle.get_largeur())

    # Affichage de la surface du rectangle
    print(rectangle.Surface())
    
    # Modification de la largeur et de la hauteur avec les méthodes set_hauteur et set_largeur
    rectangle.set_hauteur(20)
    rectangle.set_largeur(15)
    

    # Affichage de la nouvelle largeur et de la hauteur
    # avec les méthodes get_hauteur et get_largeur
    print(rectangle.get_hauteur())
    print(rectangle.get_largeur())
    
    # Affichage de la nouvelle surface du rectangle avec la méthode Surface
    print(rectangle.Surface())
    
    # Affichage de l'objet rectangle avec la méthode __str__
    print(rectangle)
