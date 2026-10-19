'''
Bases interresantes
'''


'''
Binaire

0 1 = bit
'''


'''
Octale

1 2 3 4 5 6 7 = octet
8 9 10 11 12 13 14 15 = octet
'''


'''
Decimal

0 1 2 3 4 5 6 7 8 9 = decimal
'''


'''
Hexadecimal

1 2 3 4 5 6 7 8 9 A B C D E F = hexadecimale
'''

'''
ASCII

$ 0 1 @ é & 2 3 4 5 6 7 8 9 A B C D E F = ascii
'''

##################################################################################################################



### Bit (b)
#Le bit (binary digit) est l’unité de base en informatique. Il peut avoir deux valeurs : 
#0 ou 1.


### Octet (Byte – B)
#Un octet est un ensemble de 8 bits.
#Exemple : 01001100 est un octet.


### Kilo-octet (Ko ou KB)
#1 Ko = 1 024 octets = 8 192 bits


### Mégaoctet (Mo ou MB)
#1 Mo = 1 024 Ko = 1 048 576 octets


### Gigaoctet (Go ou GB)
#1 Go = 1 024 Mo = 1 073 741 824 octets


### Téraoctet (To ou TB)
#1 To = 1 024 Go = 1 099 511 627 776 octets


### Pétaoctet (Po ou PB)
#1 Po = 1 024 To = 1 125 899 906 842 624 octets




##################################################################################################################


### Deplacement de bits

#Le déplacement de bits est une opération qui consiste à déplacer les bits d’un nombre binaire vers la gauche ou vers la droite.

#Cette opération est très rapide et permet de multiplier ou diviser un nombre par une puissance de 2.
#Par exemple, si l’on déplace les bits d’un nombre binaire de 2 vers la gauche, on le multiplie par 2^2 = 4.
#Si l’on déplace les bits d’un nombre binaire de 2 vers la droite, on le divise par 2^2 = 4.

#Exemple : 00000001 (1)   << 2   =  00000100 (4)
#Exemple : 00000100 (4)   >> 2   =  00000001 (1)
#Exemple : 00000001 (1)   << 3   =  00001000 (8) 



##################################################################################################################

### Conversion binaire - décimal

#La conversion d’un nombre binaire en décimal se fait en multipliant chaque bit par 2^n, 
# où n est la position du bit dans le nombre binaire, en partant de la droite.
#La position du bit le plus à droite est 0, celle du bit suivant est 1, etc.
#On additionne ensuite les résultats pour obtenir le nombre décimal.

# on va effectuer la conversion d’un nombre binaire en décimal
# Ex : 741 en binaire = 1011101101 en décimal

# 741 - 512 = 229
# 229 - 128 = 101
# 101 - 64 = 37
# 37 - 32 = 5
# 5 - 4 = 1
# 1 - 1 = 0

# Dans le calcul ci-dessus nous avons utilisé la méthode de la soustraction pour convertir le nombre binaire en décimal.
# on demarre par le nombre binaire et on soustrait les puissances de 2 jusqu’à ce que le résultat soit égal à 0.
# On note les puissances de 2 que l’on a soustraites, ce qui nous donne le nombre binaire.


# 741 = 512 + 128 + 64 + 32 + 4 + 1
# 741 = 2^9 + 2^7 + 2^6 + 2^5 + 2^2 + 2^0


# [ 9,  | 8,   |7,   |6,   |5,   |4,   |3,   |2,   |1,   |0  ]
# [ 2^9,| 2^8, |2^7, |2^6, |2^5, |2^4, |2^3, |2^2, |2^1, |2^0]
# [ 512,| 256, |128, |64,  |32,  |16,  |8,   |4,   |2,   |1  ]
# [ 0,  | 1,   |0,   |1,   |1,   |0,   |1,   |0,   |1,   |0  ]

# Pourquoi connaitre ces informations ?
# Parce que c’est la base de l’informatique.

# ce qui permet de comprendre :
###  comment fonctionne un ordinateur et comment il traite les données.
###  comment fonctionne la mémoire d’un ordinateur et comment elle est organisée.
###  comment fonctionne un disque dur et comment il stocke les données.
###  comment fonctionne un réseau et comment les données sont transmises d’un ordinateur à un autre.


# la performance d’un ordinateur dépend de la vitesse à laquelle il peut traiter les données.
# La vitesse de traitement des données dépend de la vitesse à laquelle les données peuvent être lues et écrites sur le disque dur.
# La vitesse de lecture et d’écriture des données dépend de la vitesse à laquelle les données peuvent être transférées entre le disque dur et la mémoire de l’ordinateur.
# La vitesse de transfert des données dépend de la vitesse à laquelle les données peuvent être transférées entre le disque dur et le processeur de l’ordinateur.
# La vitesse de traitement des données dépend de la vitesse à laquelle le processeur peut traiter les données.


# donc certains conceptes comme 

# # le cache, la mémoire vive, la mémoire morte, le disque dur, le processeur et les bus sont utile à connaitre.

# le cache:
# # le cache est une mémoire très rapide qui est utilisée pour stocker les données et les programmes qui sont fréquemment utilisés.
# # le cache est une mémoire volatile, c’est-à-dire qu’elle perd son contenu lorsque l’ordinateur est éteint.

# la mémoire vive:
# # la mémoire vive est la mémoire de l’ordinateur qui est utilisée pour stocker les données et les programmes en cours d’exécution.
# # la mémoire vive est une mémoire volatile, c’est-à-dire qu’elle perd son contenu lorsque l’ordinateur est éteint.

# la mémoire morte:
# # la mémoire morte est la mémoire de l’ordinateur qui est utilisée pour stocker les données et les programmes qui ne changent pas.
# # la mémoire morte est une mémoire non volatile, c’est-à-dire qu’elle conserve son contenu lorsque l’ordinateur est éteint.
 
# le disque dur: 
# # le disque dur est un périphérique de stockage de données qui utilise des disques magnétiques pour stocker les données.
# # le disque dur est un périphérique de stockage non volatile, c’est-à-dire qu’il conserve son contenu lorsque l’ordinateur est éteint.

# le processeur: 
# # le processeur est le cerveau de l’ordinateur. Il est responsable du traitement des données et de l’exécution des programmes.
# # le processeur est un circuit intégré qui contient des millions de transistors qui effectuent des opérations logiques et arithmétiques sur les données.
# # le processeur est responsable de l’exécution des instructions du programme et de la gestion des données.

# les bus:
# # le bus de données est un ensemble de fils qui transportent les données entre le processeur, la mémoire et les périphériques de stockage.
# # le bus de données est responsable du transfert des données entre les différents composants de l’ordinateur.


