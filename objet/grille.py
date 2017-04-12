import numpy as np
from map import Diamantcarre
from case import Case
class Grille(object):
    def __init__(self,cote):
        self._cote = cote
        self._taille = 2**cote +1
        self._contenu = np.zeros(self._taille, self._taille)

    def iterer_grille(self):
        for i in range(self._taille):
            for j in range(self._taille):
                self._contenu[i,j].iterer_case

    def initialiser_grille(self):
        profondeur = Diamantcarre(self._cote, 0.5, [10,200])
        temperature = Diamantcarre(self._cote, 0.5, [10,25])
        for i in range(self._taille):
            for j in range(self._taille):
                self._contenu[i,j] = Case(temperature[i,j], profondeur[i,j],[],[],0,0)
    @cote.setter
    def cote(self, val):
        self._cote = val

    @property
    def cote(self):
        return self._cote

    @property
    def contenu(self):
        return self._contenu

    @contenu.setter
    def contenu(self, val):
        self._contenu = val