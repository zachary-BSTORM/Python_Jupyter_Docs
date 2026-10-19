"""Démo journée API — une API de gestion de produits avec FastAPI + templates Jinja2.

Lancement (depuis src/api) :  uvicorn app.main:app --reload
Documentation interactive :   http://127.0.0.1:8000/docs
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# ── L'application ────────────────────────────────────────────────────────────
# L'objet central : c'est à lui qu'on accroche toutes les routes.
app = FastAPI(title="API Boutique", description="Démo de formation — produits en JSON et en HTML")

# Les templates : des fichiers HTML « à trous » que Python remplit avec les données.
# Le chemin est calculé par rapport à CE fichier → marche quel que soit le dossier de lancement.
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


# ── Le modèle de données ─────────────────────────────────────────────────────
# Un modèle Pydantic ressemble à une dataclass, avec un bonus énorme pour une API :
# FastAPI s'en sert pour VALIDER automatiquement le JSON reçu (types, champs obligatoires)
# et pour documenter la route dans /docs.
class Produit(BaseModel):
    id: int
    nom: str
    prix: float
    stock: int = 0


# Notre « base de données » : un simple dictionnaire en mémoire.
# (En vraie application : PostgreSQL, SQLite... — hors sujet pour cette journée.)
produits: dict[int, Produit] = {
    1: Produit(id=1, nom="Clavier mécanique", prix=89.99, stock=12),
    2: Produit(id=2, nom="Souris ergonomique", prix=39.50, stock=30),
    3: Produit(id=3, nom="Écran 27 pouces", prix=219.00, stock=5),
}


# ═════════════════════════════════════════════════════════════════════════════
# PARTIE 1 — L'API JSON : ce que consomment les programmes
# ═════════════════════════════════════════════════════════════════════════════

@app.get("/api/produits")
def lister_produits() -> list[Produit]:
    """Retourne tous les produits. FastAPI convertit la liste en JSON tout seul."""
    return list(produits.values())


@app.get("/api/produits/{produit_id}")
def obtenir_produit(produit_id: int) -> Produit:
    """Retourne UN produit par son id.

    {produit_id} dans l'URL devient le paramètre produit_id de la fonction.
    Grâce au type `int`, FastAPI convertit et valide : /api/produits/abc → erreur 422 automatique.
    """
    if produit_id not in produits:
        # HTTP 404 = « ressource introuvable » — le code standard pour ce cas.
        raise HTTPException(status_code=404, detail=f"Produit {produit_id} introuvable")
    return produits[produit_id]


@app.post("/api/produits", status_code=201)
def creer_produit(nouveau: Produit) -> Produit:
    """Crée un produit à partir du JSON reçu dans le corps de la requête.

    Le paramètre étant typé `Produit`, FastAPI valide le JSON entrant :
    champ manquant ou mauvais type → erreur 422 claire, notre code n'est même pas appelé.
    HTTP 201 = « créé avec succès ».
    """
    if nouveau.id in produits:
        raise HTTPException(status_code=409, detail=f"L'id {nouveau.id} existe déjà")
    produits[nouveau.id] = nouveau
    return nouveau


@app.delete("/api/produits/{produit_id}", status_code=204)
def supprimer_produit(produit_id: int) -> None:
    """Supprime un produit. HTTP 204 = « fait, rien à renvoyer »."""
    if produit_id not in produits:
        raise HTTPException(status_code=404, detail=f"Produit {produit_id} introuvable")
    del produits[produit_id]


# ═════════════════════════════════════════════════════════════════════════════
# PARTIE 2 — Les pages HTML : les templates Jinja2
# ═════════════════════════════════════════════════════════════════════════════
# Même données, autre public : un humain avec un navigateur.
# On passe les données au template, qui remplit les trous {{ ... }} du HTML.

@app.get("/", response_class=HTMLResponse)
def page_accueil(request: Request):
    """La page d'accueil — le template reçoit les variables qu'il affichera."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"titre": "Bienvenue", "nb_produits": len(produits)},
    )


@app.get("/produits", response_class=HTMLResponse)
def page_produits(request: Request):
    """La liste des produits en HTML — le template boucle sur la liste avec {% for %}."""
    return templates.TemplateResponse(
        request=request,
        name="produits.html",
        context={"titre": "Nos produits", "produits": list(produits.values())},
    )
