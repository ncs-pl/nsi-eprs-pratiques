# Ex. 1
def recherche(elt, tab):
    # Pour chaque élément de tab, selon sa position
    for i in range(len(tab)):
        # si l'élément à la position i est celui recherché,
        # alors il suffit de retourner sa position
        if tab[i] == elt:
            return i

    return -1  # si le code arrive ici, c'est que l'élément elt n'était pas dans tab


assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3


# Ex.2
def insere(a, tab):
    l = list(tab)  # l contient les mêmes éléments que tab
    l.append(a)
    i = len(tab) - 1  # on va itérer sur chaque élément pour les trier par ordre croissant
    while a < tab[i] and i >= 0:  # tant que `a` est strictement inférieur à l'élément le précédent
        l[i + 1] = l[i]  # on inverse `a` et son prédécesseur
        l[i] = a
        i = i - 1  # on décrémente i
    return l


assert insere(3, [1, 2, 4, 5]) == [1, 2, 3, 4, 5]
assert insere(10, [1, 2, 7, 12, 14, 25]) == [1, 2, 7, 10, 12, 14, 25]
assert insere(1, [2, 3, 4]) == [1, 2, 3, 4]
