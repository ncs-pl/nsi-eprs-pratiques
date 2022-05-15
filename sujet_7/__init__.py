# Ex. 1
def conv_bin(n):
    # Pour convertir un nombre décimal en binaire, il suffit d'effectuer la division euclidienne de
    # ce nombre par 2 pour obtenir son quotient (q) et un reste (r).
    # Il suffit ensuite de répéter cette division de q par 2 jusqu'à obtenir q = 0.
    # La représentation binaire sera l'ensemble des restes de bas en haut.
    # Exemple :
    # Écrire 274 en binaire :
    #   274 = 137 * 2 + 0
    #   137 = 68 * 2 + 1
    #   68 = 44 * 2 + 0
    #   44 = 22 * 2 + 0
    #   22 = 11 * 2 + 0
    #   11 = 5 * 2 + 1
    #   5 = 2 * 2 + 1
    #   2 = 1 * 2 + 0
    #   1 = 0 * 2 + 1       <- FIN car q = 0
    #
    # D'où 274 s'écrit 101100010 en binaire.

    restes = []

    while n > 0:  #
        # on ajoute le reste de la division euclidienne de n par 2, aussi appelé modulo
        restes.append(n % 2)
        # On divise n par 2 (division euclidienne)
        n //= 2

    restes.reverse()  # inverse l'ordre des éléments de la liste, nous donnant l'écriture en base 2

    return restes, len(restes)


assert conv_bin(9) == ([1, 0, 0, 1], 4)


# Ex. 2
def tri_bulles(t):
    n = len(t)
    # On veut obtenir les entiers naturels allant de 0 à la taille de t, dans le sens inverse.
    # On doit donc inverser les membres et préciser un pas de -1
    for i in range(n - 1, 0, -1):
        for j in range(i):
            # On inverse j et j+1 si et seulement si j > j + 1
            if t[j] > t[j + 1]:
                temp = t[j]
                t[j] = t[j + 1]
                t[j + 1] = temp
    return t


assert tri_bulles([99, 45, 1, 6, 26]) == [1, 6, 26, 45, 99]
