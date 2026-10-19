# =================================================================================================
#Imports
# =================================================================================================

# =================================================================================================
#Variables
# =================================================================================================
nb1 = 0
operator = ""
nb2 = 0
result = 0
again = True


# =================================================================================================
#Functions
# =================================================================================================
def get_number():
    """
    loop until a number is entered
    :return: number
    """
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def get_operator():
    is_correct = False
    
    while is_correct == False:
        operator = input("Entrez un opérateur (+, -, *, /) : ")
        if operator not in ["+", "-", "*", "/"]:
            print("L'opérateur doit être +, -, * ou /.")
        else:
            is_correct = True
    return operator
            
            
# =================================================================================================
#Program
# =================================================================================================     
## Version simple 

while again:
    
    nb1 = get_number()
    operator = get_operator()
    nb2 = get_number()

    if operator == "+":
        result = nb1 + nb2
        
    elif operator == "-":
        result = nb1 - nb2
        
    elif operator == "*":
        result = nb1 * nb2
        
    elif operator == "/":
        if nb2 == 0:
            print("Erreur : Division par zéro.")
            continue
        
        result = nb1 / nb2
        
    print(f"Le résultat de {nb1} {operator} {nb2} est : {result}")

    input_user = input("Voulez-vous faire un autre calcul ? (o/n) : ")
    if input_user == "n":
        again = False
        
# =================================================================================================
        
## Version avec gestion des erreurs

while again:
    nb1 = get_number()
    operator = get_operator()
    nb2 = get_number()

    if operator == "+":
        result = nb1 + nb2
    elif operator == "-":
        result = nb1 - nb2
    elif operator == "*":
        result = nb1 * nb2
    elif operator == "%":
        result = nb1 % nb2
    elif operator == "/":
        if nb2 != 0:
            result = nb1 / nb2
        else:
            print("Division by zero is not allowed.")
            continue
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        continue

    print(f"The result of {nb1} {operator} {nb2} is: {result}")

    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower() == "yes"

