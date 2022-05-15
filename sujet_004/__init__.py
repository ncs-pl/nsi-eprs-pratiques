# Ex. 1
def recherche(tab):
    couples = []

    # Pour chaque nombre du tableau, par rapport à sa position,
    # si ce nombre + 1 correspond à son voisin,
    # alors ils sont consécutifs.
    for index_nbr in range(len(tab) - 1):
        if tab[index_nbr] + 1 == tab[index_nbr + 1]:
            couples.append((tab[index_nbr], tab[index_nbr + 1]))

    return couples


assert recherche([1, 4, 3, 5]) == []
assert recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]


# Ex. 2
def propager(m, i, j, val):
    if m[i][j] == 0:
        return

    m[i][j] = val

    # l'élément en haut fait partie de la composante
    if (i - 1) >= 0 and m[i - 1][j] == 1:
        propager(m, i - 1, j, val)

    # l'élément en bas fait partie de la composante
    if (i + 1) < len(m) and m[i + 1][j] == 1:
        propager(m, i + 1, j, val)

    # l'élément à gauche fait partie de la composante
    if (j - 1) >= 0 and m[i][j - 1] == 1:
        propager(m, i, j - 1, val)

    # l'élément à droite fait partie de la composante
    if (j + 1) < len(m) and m[i][j + 1] == 1:
        propager(m, i, j + 1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
propager(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]