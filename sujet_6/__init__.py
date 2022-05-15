# Ex. 1
def maxi(tab):
    # on initialise le résultat
    m = (tab[0], 0)

    # Pour chaque nombre du tableau, à l'aide de sa position,
    # si ce nombre est plus grand que notre maximum trouvé,
    # alors ce nombre est le nouveau maximum.
    for i in range(len(tab)):
        # En ne vérifiant que si le nombre est strictement supérieur,
        # nous gardons déjà la première apparation de ce nombre.
        if tab[i] > m[0]:
            m = (tab[i], i)

    return m


assert maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)


# Ex. 2
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    # Tant que nous avons rien trouvé et pas fini de lire la séquence
    while i < n and trouve == False:
        j = 0
        while j < g and gene[j] == seq_adn[i + j]:
            # Tant que le caractère j du gène est présent dans la séquence
            j = j + 1
        if j == g:
            trouve = True

        i = i + 1
    return trouve


assert recherche("AATC", "GTACAAATCTTGCC")
assert not recherche("AGTC", "GTACAAATCTTGCC")
