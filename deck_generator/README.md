# Générateur du deck « Python - Base (enrichi) »

Régénère `../Python - Base (enrichi).pptx` (73 slides, style bstorm Training).

## Utilisation

```
pip install python-pptx
python deck_content.py
```

- **`deck_content.py`** — tout le contenu des slides (textes, code, tableaux). C'est ici qu'on modifie le cours.
- **`deck_lib.py`** — le moteur de mise en page (couleurs, polices, boîtes de code avec coloration syntaxique, tableaux, puces, logo/numéro de page).
- **`assets/`** — logos bstorm et page « Qui sommes-nous ? » extraits du PDF officiel.

## Le style reproduit

| Élément | Valeur |
|---|---|
| Format | 720 × 405 pt (16:9, comme les exports Google Slides bstorm) |
| Vert bstorm | `#23AC67` (titres de slides, numéros de page) |
| Violet bstorm | `#3B2C87` (titres de sections, badge BONUS) |
| Police des titres | **Zen Maru Gothic** — https://fonts.google.com/specimen/Zen+Maru+Gothic |
| Police du corps | **Barlow** — https://fonts.google.com/specimen/Barlow |
| Code | Consolas, boîte blanche à bordure grise, mots-clés bleus / strings teal / commentaires gris |

⚠ Les deux polices Google Fonts ne sont pas installées par défaut sous Windows :
télécharger chaque famille, sélectionner les `.ttf` → clic droit → **Installer**.
Sans elles, PowerPoint substitue une police proche (le deck reste lisible).

## Syntaxe du contenu (`deck_content.py`)

Chaque slide de contenu est un appel `C(titre, *blocs)` :

- `("txt", [("p", "paragraphe"), ("b0", "puce"), ("b1", "sous-puce")])` — `**gras**` et `` `code` `` supportés
- `("code", "...code python...")` — colorisé automatiquement (module `tokenize`)
- `("table", ["En-tête", ...], [[...lignes...]], [largeurs pt], {"mono_cols": (0,)})`
- `("gap", 8)` — espace vertical
- `bonus=True` — ajoute le badge 🎓 BONUS
