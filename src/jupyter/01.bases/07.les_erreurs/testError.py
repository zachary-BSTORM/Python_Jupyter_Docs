from errors import AgeInvalideError, NomVideError

def set_age(age):
    if age < 0:
        raise AgeInvalideError("L'âge ne peut pas être négatif")
    if age > 150:
        raise AgeInvalideError("L'âge semble irréaliste")
    return age

def set_nom(nom):
    if nom == "":
        raise NomVideError("Le nom ne peut pas être vide")
    return nom

# --- Test 1 : âge négatif ---
print("--- Test 1 ---")
try:
    set_age(-5)
except AgeInvalideError as e:
    print(f"Erreur : {e}")

# --- Test 2 : nom vide ---
print("--- Test 2 ---")
try:
    set_nom("")
except NomVideError as e:
    print(f"Erreur : {e}")

# --- Test 3 : tout va bien ---
print("--- Test 3 ---")
try:
    age = set_age(25)
    nom = set_nom("Alice")
    print(f"{nom} a {age} ans")
except AgeInvalideError as e:
    print(f"Erreur : {e}")
except NomVideError as e:
    print(f"Erreur : {e}")

# --- Test 4 : erreur inattendue (Exception générale) ---
print("--- Test 4 ---")
try:
    set_age("abc")
except AgeInvalideError as e:
    print(f"Erreur : {e}")
except NomVideError as e:
    print(f"Erreur : {e}")
except Exception as e:
    print(f"Erreur inattendue : {e}")