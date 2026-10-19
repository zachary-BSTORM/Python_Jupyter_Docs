"""
'r'	Lecture seule	Fichier doit exister, sinon erreur.
'w'	Écriture seule (écrasement)	Crée un nouveau fichier ou écrase le fichier existant.
'x'	Création	Crée un nouveau fichier, erreur si le fichier existe déjà.
'a'	Ajout (append)	Crée un nouveau fichier si inexistant, sinon écrit à la fin.
'b'	Mode binaire	À combiner avec un autre mode : 'rb', 'wb', etc.
't'	Mode texte (défaut)	À combiner : 'rt', 'wt', etc.
'+'	Lecture et écriture	À combiner : 'r+', 'w+', 'a+' (voir détails ci-dessous).
"""

# Lecture
with open("mon_fichier.txt", "r") as f:
    contenu = f.read()

# Écriture
with open("mon_fichier.txt", "w") as f:
    f.write("Bonjour")

# Lecture/écriture sans écrasement
with open("mon_fichier.txt", "r+") as f:
    contenu = f.read()
    f.write("Suite")