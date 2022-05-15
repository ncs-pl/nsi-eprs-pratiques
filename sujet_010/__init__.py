# Ex. 1
def occurrence_lettres(phrase):
    occurrences = {}

    # Pour chaque lettre dans la phrase
    for lettre in phrase:
        # si la lettre existe dans notre dictionnaire, alors on incrémente de 1 son occurrence
        if lettre in occurrences:
            occurrences[lettre] += 1
        # sinon on ajoute la lettre dans le dictionnaire
        else:
            occurrences[lettre] = 1

    return occurrences


assert occurrence_lettres("Hello world !") == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}


# Ex. 2
def fusion(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    l12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    # Cette boucle fusionne les i-premiers éléments des deux listes (même nombre d'éléments).
    # On doit juste être sûr que les indices (i1 et i2) ne dépassent pas les longueurs des listes.
    # Les autres boucles "while" fusionnent les autres éléments des listes (dans le cas où une liste est plus grande
    # que l'autre).
    while i1 < n1 and i2 < n2:
        if l1[i1] < l2[i2]:
            l12[i] = l1[i1]  # si l'élément i1 est plus petit que i2, alors il est inséré en premier
            i1 = i1 + 1  # et on incrémente i1 pour passer au prochain élément de la liste 1
        else:
            l12[i] = l2[i2]
            i2 = i2 + 1  # même fonctionnement qu'au-dessus, mais dans le cas où i2 est plus petit qu'i1
        i += 1
    while i1 < n1:
        l12[i] = l1[i1]  # dans le cas où l1 est plus grande que l2, on ajoute les éléments restant de l1
        i1 = i1 + 1
        i = i + 1  # on incrémente le compteur global
    while i2 < n2:
        l12[i] = l2[i2]  # dans le cas où l2 est plus grande que l1, on ajoute les éléments restant de l2
        i2 = i2 + 1
        i = i + 1  # on incrémente le compteur global
    return l12


assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]
