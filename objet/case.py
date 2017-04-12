from objet.banc_poisson import BancPoisson
from objet.plancton import Plancton


class Case(object):
    def __init__(self, temperature, profondeur, liste_banc, liste_plancton, capacite_max_plancton, capacite_max_poisson):
        self._temperature = temperature
        self._profondeur = profondeur
        self._liste_banc = liste_banc
        self._liste_plancton = liste_plancton
        self._capacite_max_plancton = capacite_max_plancton
        self._capacite_max_poisson = capacite_max_poisson

    def pecher(self):
        for banc in self.liste_banc:
            banc.reduire_population()

    def iterer_case(self):
        for plancton in self.liste_plancton:
            plancton.se_developper(self.temperature, self._capacite_max_plancton)
        for banc in self.liste_banc:
            banc.se_developper(self.liste_plancton, self._capacite_max_poisson)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, val):
        self._temperature = val

    @property
    def profondeur(self):
        return self._profondeur

    @profondeur.setter
    def profondeur(self, val):
        self._profondeur = val

    @property
    def liste_banc(self):
        return self._liste_banc

    @liste_banc.setter
    def liste_banc(self, val):
        self._liste_banc = val

    @property
    def liste_plancton(self):
        return self._liste_plancton

    @liste_plancton.setter
    def liste_plancton(self, val):
        self._liste_plancton = val

    @property
    def capacite_max_plancton(self):
        return self._capacite_max_plancton

    @capacite_max_plancton.setter
    def capacite_max_plancton(self, val):
        self._capacite_max_plancton = val

    @property
    def capacite_max_poisson(self):
        return self._capacite_max_poisson

    @capacite_max_poisson.setter
    def capacite_max_poisson(self, val):
        self._capacite_max_poisson = val