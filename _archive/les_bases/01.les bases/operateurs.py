# Ensuite on utilise les Operateurs mathématiques pour effectuer des calculs sur les variables

# On utilisera les operateurs suivants : +, -, *, /, //, %, ** 

# + : addition

# - : soustraction

# * : multiplication

# / : division

# // : division entière

# % : modulo (reste de la division)

# ** : puissance (exposant) 

a = 10

b = 5

print(a + b) # addition
print(a - b) # soustraction
print(a * b) # multiplication
print(a / b) # division
print(a // b) # division entière
print(a % b) # modulo
print(a ** b) # puissance

# ######################################################################################################################################

# On peut aussi utiliser les operateurs de comparaison : ==, !=, <, >, <=, >= 
# == : égal à
# != : différent de
# < : inférieur à
# > : supérieur à
# <= : inférieur ou égal à
# >= : supérieur ou égal à
# in : appartient à
# not in : n'appartient pas à
# is : est identique à
# is not : n'est pas identique à


print(a == b) # égal à
print(a != b) # différent de
print(a < b) # inférieur à
print(a > b) # supérieur à
print(a <= b) # inférieur ou égal à
print(a >= b) # supérieur ou égal à
print(a in b) # est contenu dans
print(a not in b) # n'est pas contenu dans
print(a is b) # est identique à
print(a is not b) # n'est pas identique à


######################################################################################################################################

# On peut aussi utiliser les operateurs logiques : and, or, not

value1 = 10
value2 = 12

# and : et
print(value1 > 5 and value2 < 15) # True

# or : ou
print(value1 > 5 or value2 < 10) # True

# not : non
print(not (value1 > 5 and value2 < 15)) # False 

######################################################################################################################################

# On peut aussi utiliser les operateurs d'affectation : =, +=, -=, *=, /=, //=, %=, **=  
a = 10
b = 5
c = None

# = : affectation
c = a + b # affectation de la valeur de a + b à c

# += : addition et affectation
c += a

# -= : soustraction et affectation
c -= a

# *= : multiplication et affectation
c *= a

# /= : division et affectation
c /= a

# //= : division entière et affectation
c //= a

# %= : modulo et affectation
c %= a

# **= : puissance et affectation
c **= a


######################################################################################################################################


