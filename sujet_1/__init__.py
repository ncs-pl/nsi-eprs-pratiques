# Ex. 1
def recherche(cherche, mot):
    occurrence = 0

    # Pour chaque lettre dans mot,
    # si la lettre correspond à celle recherchée (cherche),
    # alors on augmente occurrence de 1
    for lettre in mot:
        if lettre == cherche:
            occurrence += 1

    return occurrence


assert recherche('e', "sciences") == 2
assert recherche('i', "mississippi") == 4
assert recherche('a', "mississippi") == 0

# Ex. 2
Pieces = [100, 50, 20, 10, 5, 2, 1]


def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution  # s'il n'y a plus rien à rendre, on return la solution
    p = Pieces[i]
    # si la plus grande pièce est inférieure ou égale à la somme à rendre,
    # alors nous pouvons ajouter cette pièce à la solution
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else:
        # dans le cas où notre plus grande pièce est strictement supérieure à la somme
        # à rendre, alors il faut essayer avec la prochaine plus grande pièce possible
        return rendu_glouton(arendre, solution, i + 1)


assert rendu_glouton(68, [], 0) == [50, 10, 5, 2, 1]
assert rendu_glouton(291, [], 0) == [100, 100, 50, 20, 20, 1]
