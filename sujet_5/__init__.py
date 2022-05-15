# Ex. 1
def RechercheMinMax(tab):
    if len(tab) == 0:
        return {
            "min": None,
            "max": None,
        }

    # on initialise le résultat à l'aide de la première valeure du tableau
    minmax = {
        "min": tab[0],
        "max": tab[0]
    }

    # On parcours chaque nombre du tableau
    for n in tab:
        # si le nombre est plus grand que notre max,
        # alors ce nombre est le nouveau maximum
        if n > minmax["max"]:
            minmax["max"] = n
            continue

        # si le nombre est plus petit que notre min,
        # alors ce nombre est notre minimum
        if n < minmax["min"]:
            minmax["min"] = n

    return minmax


assert RechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert RechercheMinMax([]) == {'min': None, 'max': None}

# Ex. 2
class Carte:
    """Initialise Couleur (entre 1 a 4), et Valeur (entre 1 a 13)"""
    def __init__(self, c, v):
        # Vérifie que les paramètres sont valides
        assert 1 <= c <= 4, "Couleur doit être compris entre 1 et 4 !"
        assert 1 <= c <= 13, "Valeur doit être compris entre 1 et 13 !"

        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        # Pour chacune des cartes possibles (As, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valet, Dame, Roi),
        # ajouter chaque variante (As, Pique, Carreau, Trefle) dans le paquet
        self.contenu = [ Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(1, 14)]

    """Renvoie la Carte qui se trouve a  la position donnee"""
    def getCarteAt(self, pos):
        # Vérifie que la position soit valide
        assert len(self.contenu) > 0, "Le paquet est vide!"
        assert 0 <= pos <= 52, "La position n'existe pas!"

        if 0 <= pos < 52:
            return self.contenu[pos]


unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(20)
assert uneCarte.getNom() + " de " + uneCarte.getCouleur() == "8 de coeur"