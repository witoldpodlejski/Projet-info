
class EspecePoisson(object):
    def __init__(self,liste_proie,nom,taille, temperature_preferencielle, taux_croissance):
        self._liste_proie = liste_proie
        self._nom = nom
        self._taille = taille
        self._temperature_preferencielle = temperature_preferencielle
        self._taux_croissance = taux_croissance

    @property
    def liste_proie(self):
        return self._liste_proie
    @property
    def nom(self):
        return self._nom
    @property
    def taille(self):
        return self._taille
    @property
    def temperature_preferencielle(self):
        return self._temperature_preferencielle


