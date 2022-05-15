# Ex. 1
def moyenne(tab):
    notes = 0
    coefs = 0

    # Pour chaque couple (note, coef) du tableau
    for t in tab:
        # on ajoute la note multipliée par son coef aux notes existantes
        notes += t[0] * t[1]
        # on ajoute le coef aux coefs existants
        coefs += t[1]

    return notes / coefs


assert moyenne([(15, 2), (9, 1), (12, 3)]) == 12.5


# Ex. 2
def pascal(n):
    C = [[1]]
    for k in range(1, n): # on souhaite n lignes
        Ck = [1] # chaque ligne du triangle de Pascal commence par un 1
        for i in range(1, k):
            # les antécédants sont à la ligne précédente (k-1)
            # et l'un est sur la même colone (i) et l'autre sur la
            # colone d'avant (i-1)
            Ck.append(C[k-1][i - 1] + C[k-1][i])
        Ck.append(1) # chaque ligne du triangle de Pascal se termine par un 1
        C.append(Ck)
    return C


assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10,
                                                                             10, 5, 1]]
