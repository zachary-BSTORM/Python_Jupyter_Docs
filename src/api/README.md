# Journée API — une API simple avec FastAPI et des templates

Démo pour la journée « API » : une petite application de gestion de produits qui montre
les deux visages d'une application web Python :

1. **L'API JSON** (`/api/...`) — ce que consomment les autres programmes (front-end, mobile, scripts).
2. **Les pages HTML** (`/` et `/produits`) — générées avec des **templates Jinja2**
   (des fichiers HTML à trous que Python remplit avec les données).

## Installation

```bash
pip install fastapi uvicorn jinja2
```

(ou `pip install -r requirements.txt` depuis ce dossier)

## Lancement

Depuis ce dossier (`src/api`) :

```bash
uvicorn app.main:app --reload
```

- `app.main:app` = « dans le fichier `app/main.py`, l'objet qui s'appelle `app` »
- `--reload` = redémarre tout seul à chaque modification du code (pratique en développement)

Puis ouvrir :

| URL | Ce qu'on voit |
|---|---|
| http://127.0.0.1:8000/ | la page d'accueil (template HTML) |
| http://127.0.0.1:8000/produits | la liste des produits (template HTML) |
| http://127.0.0.1:8000/api/produits | la même liste, en JSON |
| http://127.0.0.1:8000/api/produits/1 | un seul produit, en JSON |
| http://127.0.0.1:8000/docs | ⭐ la documentation interactive générée automatiquement |

## Le `/docs` — l'argument massue de FastAPI

FastAPI lit les types de tes fonctions et génère **tout seul** une page de documentation
interactive (Swagger UI) où l'on peut tester chaque route depuis le navigateur.
C'est le premier réflexe à montrer en formation.

## Structure

```
src/api/
├── README.md            ← ce fichier
├── requirements.txt
└── app/
    ├── main.py          ← les routes (les « portes d'entrée » de l'application)
    └── templates/       ← les fichiers HTML à trous (Jinja2)
        ├── base.html    ← squelette commun (menu, style) dont héritent les autres pages
        ├── index.html   ← page d'accueil
        └── produits.html← liste des produits
```
