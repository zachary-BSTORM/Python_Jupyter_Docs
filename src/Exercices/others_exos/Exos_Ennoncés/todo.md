# Exercice : Système de gestion de tâches (Todo App)

## Contexte

Vous devez créer un programme Python permettant de gérer une liste de tâches.

L’objectif est de simuler le fonctionnement d’une application réelle avec des fonctionnalités complètes : ajout, modification, suppression, filtrage et pagination.

---

## Structure des données

Les tâches seront stockées dans une liste de dictionnaires.

Exemple :

tasks = [
{
"id": 1,
"title": "Coder le projet",
"status": "todo",
"priority": 3,
"tags": ["dev", "urgent"]
}
]

---

## Contraintes générales

* Chaque tâche doit avoir un id unique
* Le status doit être : "todo", "in_progress" ou "done"
* La priorité doit être un entier entre 1 et 5
* Les tags sont une liste de chaînes de caractères
* Le programme doit être structuré avec des fonctions
* Le code doit être lisible et organisé

---

## Fonctionnalités à implémenter

### 1. Ajouter une tâche

Créer une fonction permettant d’ajouter une tâche à la liste.

add_task(tasks, title, priority, tags)

* Générer automatiquement un id unique
* Ajouter la tâche avec le status par défaut "todo"

---

### 2. Afficher les tâches

Créer une fonction pour afficher les tâches avec filtres et pagination.

list_tasks(tasks, params)

params est un dictionnaire optionnel pouvant contenir :

* "status" : filtre par statut
* "priority_min" : priorité minimum
* "tag" : filtre par tag
* "page" : numéro de page (10 éléments par page)

Exemples :

list_tasks(tasks, {"status": "todo"})
list_tasks(tasks, {"priority_min": 3, "page": 2})
list_tasks(tasks, {"tag": "dev"})

Affichage attendu :

id - titre - status - priorité - tags

---

### 3. Modifier une tâche

Créer une fonction pour modifier une tâche existante.

update_task(tasks, task_id, new_data)

new_data est un dictionnaire pouvant contenir :

* "title"
* "status"
* "priority"
* "tags"

---

### 4. Supprimer une tâche

Créer une fonction pour supprimer une tâche.

delete_task(tasks, task_id)

---

### 5. Marquer une tâche comme terminée

Créer une fonction :

mark_done(tasks, task_id)

Elle doit changer le status en "done"

---

## Gestion des erreurs

Le programme doit gérer correctement :

* tâche introuvable
* paramètres invalides
* filtres sans résultat

Afficher des messages clairs.

---

## Sauvegarde et chargement des données (Bonus)

Il est possible de sauvegarder les tâches dans un fichier JSON afin de conserver les données après l’arrêt du programme.

### 1. Sauvegarder les tâches

Créer une fonction :

save_tasks(tasks, filename)

Cette fonction doit :

* convertir la liste de tâches en JSON
* écrire les données dans un fichier

---

### 2. Charger les tâches

Créer une fonction :

load_tasks(filename)

Cette fonction doit :

* lire un fichier JSON
* convertir les données en liste Python
* retourner la liste des tâches

Si le fichier n’existe pas, retourner une liste vide.

---

### 3. Utilisation du module json

Importer le module :

import json

Fonctions utiles :

* json.dump(data, file, indent=4)
* json.load(file)

---

### 4. Exemple de structure JSON

Le fichier JSON doit contenir une liste de tâches :

[
{
"id": 1,
"title": "Coder le projet",
"status": "todo",
"priority": 3,
"tags": ["dev", "urgent"]
}
]

---

### 5. Intégration dans le programme

* Charger les tâches au démarrage
* Sauvegarder les tâches après chaque modification

---

### 6. Gestion des erreurs

* vérifier si le fichier existe
* gérer les erreurs de lecture
* éviter de faire planter le programme

---

## Bonus (facultatif)

* Trier les tâches par priorité ou titre
* Sauvegarder les tâches dans un fichier JSON
* Charger les tâches au démarrage
* Créer un menu interactif en console

---

## Conseils

* Commencer par add_task et list_tasks
* Tester chaque fonction séparément
* Ajouter les filtres progressivement
* Ne pas tout faire d’un coup
