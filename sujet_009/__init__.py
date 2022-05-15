# Ex. 1
def calcul(n):
    # on initialise le résultat, sachant que le premier élément, c'est-à-dire U0, est toujours le nombre donné
    valeurs_u = [n]

    while n > 1:  # tant que 'n' est supérieur à 2, la suite est utilisée
        # Un nombre est pair si et seulement s'il est congru à 0 modulo 2, c'est-à-dire que le reste de la division
        # euclidienne de ce nombre par 2 est nul.
        if n % 2 == 0:
            # 'n' étant pair ici, une division euclidienne ou non est supposé retourner un entier naturel.
            # Cependant, une simple division en Python (a/b) retourne un entier irrationnel, pas naturel
            n //= 2
        # sinon, il est impair
        else:
            n = 3 * n + 1

        # on ajoute 'n' aux valeurs après le calcul de la suite
        valeurs_u.append(n)

    return valeurs_u


assert calcul(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

# Ex. 2
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
        "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
        "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    code_c = ""
    code_a = 0  # on initialise le code additionné à 0
    for c in mot:
        code_c = code_c + str(dico[c])  # on ajoute la valeur numérique de la lettre dans le code concaténé (string)
        code_a = code_a + dico[c]  # on additionne la valeur numérique de la lettre au code additionné
    code_c = int(code_c)
    # code_c est divisible par code_a si et seulement si le reste de la division euclidienne de code_c par code_a
    # vaut 0, c'est-à-dire que code_c est congru à 0 modulo code_a
    if code_c % code_a == 0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]


assert est_parfait("PAUL") == [50, 1612112, False]
assert est_parfait("ALAIN") == [37, 1121914, True]
