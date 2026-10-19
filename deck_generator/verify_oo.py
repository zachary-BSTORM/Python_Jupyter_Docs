# -*- coding: utf-8 -*-
"""Vérifie par exécution les extraits de code du deck OO enrichi."""
import io
from contextlib import redirect_stdout

OK = 0
KO = []

def verifie(nom, code, attendu=None, erreur=None):
    global OK
    tampon = io.StringIO()
    exc = None
    try:
        with redirect_stdout(tampon):
            exec(code, {})
    except Exception as e:
        exc = type(e).__name__
    sortie = tampon.getvalue().strip()
    ok = (exc == erreur) if erreur else (exc is None and (attendu is None or sortie == attendu))
    if ok:
        OK += 1
    else:
        KO.append(f"{nom}: sortie={sortie!r} exc={exc}")

# S14 self
verifie("self", '''
class Voiture:
    def klaxonner(self):
        print("Tut tut !")

v = Voiture()
v.klaxonner()
Voiture.klaxonner(v)
''', "Tut tut !\nTut tut !")

# S15 __init__
verifie("init", '''
class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

v1 = Voiture("Renault", 2019)
v2 = Voiture("Kia", 2024)
print(v1.marque, v2.marque)
''', "Renault Kia")

# S16 classe vs instance
verifie("classe-vs-instance", '''
class Voiture:
    nb_roues = 4
    def __init__(self, marque):
        self.marque = marque

v1 = Voiture("Renault")
v2 = Voiture("Kia")
print(v1.nb_roues, v2.nb_roues)
print(v1.marque, v2.marque)
''', "4 4\nRenault Kia")

# S17 masquage
verifie("masquage", '''
class Compteur:
    total = 0

c = Compteur()
c.total = 10
print(Compteur.total)
print(c.total)
''', "0\n10")

# S23 property Car
verifie("property", '''
class Car:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        if value <= 0:
            raise ValueError(f"Puissance invalide : {value}")
        self.__hp = value

c = Car("Clio", 90)
print(c.hp)
''', "90")

# S24 refus silencieux -> AttributeError plus tard
verifie("setter-silencieux", '''
class Car:
    def __init__(self, hp):
        self.hp = hp
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        if value > 0:
            self.__hp = value

c = Car(-5)
print(c.hp)
''', erreur="AttributeError")

# S24 bon setter
verifie("setter-valueerror", '''
class Car:
    def __init__(self, hp):
        self.hp = hp
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        if value <= 0:
            raise ValueError("Puissance invalide")
        self.__hp = value

try:
    Car(-5)
except ValueError as e:
    print(e)
''', "Puissance invalide")

# S29 str vs repr
verifie("str-repr", '''
class Voiture:
    def __init__(self, marque):
        self.marque = marque
    def __str__(self):
        return f"Voiture {self.marque}"
    def __repr__(self):
        return f"Voiture(marque={self.marque!r})"

v = Voiture("Kia")
print(v)
print([v, v])
''', "Voiture Kia\n[Voiture(marque='Kia'), Voiture(marque='Kia')]")

# S31 eq
verifie("eq", '''
class Voiture:
    def __init__(self, plaque):
        self.plaque = plaque

v1 = Voiture("1-ABC-123")
v2 = Voiture("1-ABC-123")
print(v1 == v2)

class Voiture2:
    def __init__(self, plaque):
        self.plaque = plaque
    def __eq__(self, other):
        return self.plaque == other.plaque

print(Voiture2("1-ABC-123") == Voiture2("1-ABC-123"))
''', "False\nTrue")

# S32 eq + hash
verifie("eq-hash", '''
class Voiture:
    def __init__(self, plaque):
        self.plaque = plaque
    def __eq__(self, other):
        return self.plaque == other.plaque
    def __hash__(self):
        return hash(self.plaque)

parc = {Voiture("1-ABC-123"), Voiture("1-ABC-123")}
print(len(parc))
''', "1")

# S33 dataclass
verifie("dataclass", '''
from dataclasses import dataclass

@dataclass
class Voiture:
    marque: str
    annee: int
    prix: float = 0.0

v = Voiture("Kia", 2024, 15900.0)
print(v)
print(v == Voiture("Kia", 2024, 15900.0))
''', "Voiture(marque='Kia', annee=2024, prix=15900.0)\nTrue")

# S36 super
verifie("super", '''
class Voiture:
    def __init__(self, marque):
        self.marque = marque

class VoitureElectrique(Voiture):
    def __init__(self, marque, autonomie):
        super().__init__(marque)
        self.autonomie = autonomie

ve = VoitureElectrique("Tesla", 500)
print(ve.marque, ve.autonomie)
''', "Tesla 500")

# S37 redefinition + super dans la methode
verifie("redef", '''
class Voiture:
    def demarrer(self):
        return "Vroum"

class VoitureElectrique(Voiture):
    def demarrer(self):
        return "..." + " (silence electrique)"

print(Voiture().demarrer())
print(VoitureElectrique().demarrer())
''', "Vroum\n... (silence electrique)")

# S39 polymorphisme + isinstance
verifie("isinstance", '''
class Voiture:
    pass
class VoitureElectrique(Voiture):
    pass

ve = VoitureElectrique()
print(isinstance(ve, VoitureElectrique), isinstance(ve, Voiture))
print(issubclass(VoitureElectrique, Voiture))
''', "True True\nTrue")

# S42 FlyingCar corrige
verifie("flyingcar", '''
class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year

class Plane:
    def __init__(self, id, year, nb_motor):
        self.id = id
        self.year = year
        self.nb_motor = nb_motor

class FlyingCar(Car, Plane):
    def __init__(self, name, year, id, nb_motor):
        Car.__init__(self, name, year)
        Plane.__init__(self, id, year, nb_motor)

fc = FlyingCar("drone", 2026, "zx47", 2)
print(fc.name, fc.year, fc.id, fc.nb_motor)
''', "drone 2026 zx47 2")

# S43 ordre des parents
verifie("mro", '''
class Car:
    def description(self):
        return "je roule"

class Plane:
    def description(self):
        return "je vole"

class FlyingCar(Car, Plane):
    pass

print(FlyingCar().description())
print([c.__name__ for c in FlyingCar.__mro__])
''', "je roule\n['FlyingCar', 'Car', 'Plane', 'object']")

# S44 composition
verifie("composition", '''
class Moteur:
    def __init__(self, chevaux):
        self.chevaux = chevaux

class Voiture:
    def __init__(self, marque, chevaux):
        self.marque = marque
        self.moteur = Moteur(chevaux)

print(Voiture("Kia", 136).moteur.chevaux)
''', "136")

# S45 exception perso
verifie("exception-perso", '''
class SoldeInsuffisantError(Exception):
    pass

def retirer(solde, montant):
    if montant > solde:
        raise SoldeInsuffisantError(f"Retrait {montant} refuse : solde {solde}")
    return solde - montant

try:
    retirer(50, 200)
except SoldeInsuffisantError as e:
    print(e)
''', "Retrait 200 refuse : solde 50")

# S47 ABC
verifie("abc", '''
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self): ...

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote
    def aire(self):
        return self.cote ** 2

print(Carre(3).aire())
try:
    Forme()
except TypeError:
    print("abstraite : non instanciable")
''', "9\nabstraite : non instanciable")

# S51 compteur statique
verifie("compteur", '''
class Voiture:
    nb_creees = 0
    def __init__(self, marque):
        self.marque = marque
        Voiture.nb_creees += 1

Voiture("Renault"); Voiture("Kia"); Voiture("Tesla")
print(Voiture.nb_creees)
''', "3")

# S52 staticmethod
verifie("staticmethod", '''
class Conversion:
    @staticmethod
    def km_en_miles(km):
        return round(km * 0.621371, 1)

print(Conversion.km_en_miles(100))
''', "62.1")

# S53 classmethod
verifie("classmethod", '''
class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee
    @classmethod
    def depuis_dict(cls, d):
        return cls(d["marque"], d["annee"])

v = Voiture.depuis_dict({"marque": "Kia", "annee": 2024})
print(v.marque, v.annee)
''', "Kia 2024")

# S56 duck typing
verifie("duck", '''
class Canard:
    def crier(self):
        return "Coin coin"

class Robot:
    def crier(self):
        return "Bip bip"

for truc in [Canard(), Robot()]:
    print(truc.crier())
''', "Coin coin\nBip bip")

# S58 Protocol
verifie("protocol", '''
from typing import Protocol

class PeutCrier(Protocol):
    def crier(self) -> str: ...

class Canard:
    def crier(self):
        return "Coin coin"

def faire_crier(truc: PeutCrier):
    print(truc.crier())

faire_crier(Canard())
''', "Coin coin")

# Intro __main__ — exécuté ici comme un module IMPORTÉ (__name__ != "__main__")
# → le bloc ne doit RIEN afficher : c'est exactement le comportement enseigné.
verifie("main-guard", '''
def aide():
    print("Je suis l'outil")

if __name__ == "__main__":
    aide()
''', "")

# NOUVELLES SLIDES (ajouts 2026-10-13)

# Pas de surcharge de methodes
verifie("surcharge", '''
class Voiture:
    def rouler(self):
        return "je roule"
    def rouler(self, km):               # écrase la 1re en silence !
        return f"je roule {km} km"

# Voiture().rouler()        # TypeError — il ne reste QUE la version à km
print(Voiture().rouler(10)) # je roule 10 km

class Voiture2:
    def rouler(self, km=None):          # LA solution : paramètre optionnel
        return "je roule" if km is None else f"je roule {km} km"

print(Voiture2().rouler(), "|", Voiture2().rouler(5))
''', "je roule 10 km\nje roule | je roule 5 km")

verifie("surcharge-typeerror", '''
class Voiture:
    def rouler(self):
        return "je roule"
    def rouler(self, km):
        return f"je roule {km} km"

Voiture().rouler()
''', erreur="TypeError")

# Conteneurs __len__ / __getitem__ / __contains__
verifie("conteneur", '''
class Garage:
    def __init__(self, *voitures):
        self.voitures = list(voitures)
    def __len__(self):                 # len(g)
        return len(self.voitures)
    def __getitem__(self, i):          # g[i]  — et l'itération offerte !
        return self.voitures[i]
    def __contains__(self, v):         # "..." in g
        return v in self.voitures

g = Garage("Clio", "Kia", "Tesla")
print(len(g), g[0], "Kia" in g)
for v in g:
    print(v, end=" ")
''', "3 Clio True\nClio Kia Tesla")

# Surcharge arithmetique __add__
verifie("add-duree", '''
class Duree:
    def __init__(self, h, m):
        self.h, self.m = h, m
    def __add__(self, other):              # self + other
        total = (self.h + other.h) * 60 + self.m + other.m
        return Duree(total // 60, total % 60)
    def __repr__(self):
        return f"{self.h}h{self.m:02d}"

print(Duree(1, 40) + Duree(2, 35))
''', "4h15")

# Attributs dynamiques
verifie("getattr", '''
class Voiture:
    def __init__(self, marque):
        self.marque = marque

v = Voiture("Kia")
print(hasattr(v, "marque"))
print(getattr(v, "marque"))
print(getattr(v, "prix", 0))

setattr(v, "annee", 2024)
print(v.annee)

champ = "marque"
print(getattr(v, champ))
''', "True\nKia\n0\n2024\nKia")

# __slots__
verifie("slots", '''
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(3, 4)
print(p.x, p.y)
''', "3 4")

verifie("slots-erreur", '''
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y

p = Point(3, 4)
p.z = 5
''', erreur="AttributeError")

# __call__
verifie("call", '''
class Compteur:
    def __init__(self):
        self.n = 0
    def __call__(self):
        self.n += 1
        return self.n

c = Compteur()
print(c(), c(), c())
''', "1 2 3")

# Objet <-> JSON
verifie("json-pont", '''
import json

class Voiture:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee
    @classmethod
    def depuis_dict(cls, d):
        return cls(**d)

v = Voiture("Kia", 2024)
texte = json.dumps(v.__dict__)
print(texte)
v2 = Voiture.depuis_dict(json.loads(texte))
print(v2.marque, v2.annee)
''', '{"marque": "Kia", "annee": 2024}\nKia 2024')

# Enum : definition
verifie("enum-def", '''
from enum import Enum

class Statut(Enum):
    EN_ATTENTE = 1
    VALIDEE = 2
    ANNULEE = 3

print(Statut.VALIDEE)
print(Statut.VALIDEE.name)
print(Statut.VALIDEE.value)
print(Statut(3))
''', "Statut.VALIDEE\nVALIDEE\n2\nStatut.ANNULEE")

# Enum : usage
verifie("enum-usage", '''
from enum import Enum, auto

class Direction(Enum):
    NORD = auto()
    SUD = auto()
    EST = auto()
    OUEST = auto()

d = Direction.NORD
if d is Direction.NORD:
    print("cap au nord")

for d in Direction:
    print(d.name, end=" ")
''', "cap au nord\nNORD SUD EST OUEST")

# Mixin
verifie("mixin", '''
class ComparableParPrix:
    def moins_cher_que(self, other):
        return self.prix < other.prix

class Voiture(ComparableParPrix):
    def __init__(self, marque, prix):
        self.marque, self.prix = marque, prix

class Maison(ComparableParPrix):
    def __init__(self, ville, prix):
        self.ville, self.prix = ville, prix

print(Voiture("Kia", 15900).moins_cher_que(Maison("Mons", 250000)))
''', "True")

print(f"{OK} extraits OK, {len(KO)} echecs")
for k in KO:
    print("ECHEC", k)
