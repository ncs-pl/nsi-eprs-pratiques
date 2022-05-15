# Ex. 1
def delta(tab):
    result = []

    for i in range(len(tab)):
        # le premier élément de tab ne peut pas subir de calcul
        if i == 0:
            result.append(tab[i])
        # Calculer la différence entre l'élément actuel et son antécédant
        else:
            result.append(tab[i] - tab[i - 1])

    return result


assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]


# Ex. 2
class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return str(self.valeur)

    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ""
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit) + ')'

    return s


e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None),
                                                 '+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+',
                                                                                         Noeud(None, 1, None)))
assert expression_infixe(e) == "((3*(8+7))-(2+1))"
