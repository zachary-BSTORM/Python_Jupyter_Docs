#===============================================================================================================================================
# imports
#===============================================================================================================================================

from elephant import Elephant
from soigneur import Soigneur
from enclos import Enclos


#===============================================================================================================================================
# programme principal
#===============================================================================================================================================

if __name__ == "__main__":
    
    # Création d'un soigneur
    print("Création d'un soigneur")
    john = Soigneur("Tarzan", "2000-01-01", ["elephant", "lion", "singe"])
    

    # Création d'un éléphant
    print("creation d'un éléphant")
    dumbo = Elephant(nom = "dumbo",soigneur = john)
    # dumbo.appetit = 50
    # dumbo.satisfaction = 80
    #dumbo.Manger()
    

    # Création d'un enclos
    print("Création d'un enclos")
    enclos1 = Enclos("Enclos 1", 5, 100)

    print("affichage des informations")
    print(f"dumbo - Éléphant: {dumbo.nom}, Appétit: {dumbo.appetit}, Satisfaction: {dumbo.satisfaction}, En vie: {dumbo.en_vie}, Soigneur: {dumbo.soigneur.nom}")
    print(f"John - soigneur: {john.nom}, Date de naissance: {john.date_naissance}, Expérience: {john.experience}")
    print(f"Enclos 1: {enclos1.nom}, Capacité max: {enclos1.capacite_max}, Taille: {enclos1.taille}")

    # affectation d'un soigneur à un éléphant
    print("Affectation d'un soigneur à un éléphant")
    dumbo.soigneur = john
    
    # ajout d'un éléphant à l'enclos
    print("Ajout d'un éléphant à l'enclos")
    enclos1.ajouter_animal(dumbo)
    
    # affichage des animaux dans l'enclos
    print("Affichage des animaux dans l'enclos")
    enclos1.afficher_animaux()
    