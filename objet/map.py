import numpy as np
import random


class Diamantcarre(object):
    def __init__(self, taille, rugosite, seed):
        self._taille = (2 ** taille) + 1
        self._max = self._taille - 1
        self._rugosite = rugosite
        self._grille = np.zeros([self._taille, self._taille])
        self._grille[0][0] = random.uniform(seed[0], seed[1])
        self._grille[0][-1] = random.uniform(seed[0], seed[1])
        self._grille[-1][0] = random.uniform(seed[0], seed[1])
        self._grille[-1][-1] = random.uniform(seed[0], seed[1])
        self.divide(self._max)

    def set(self, x, y, val):
        self._grille[x, y] = val;

    def get(self, x, y):
        if (x < 0 or x > self._max or y < 0 or y > self._max):
            return 0
        else :
            return self._grille[x, y]

    def divide(self, espace):
        espace = int(espace)
        x = espace / 2
        y = espace / 2
        demi = int(espace / 2)
        scale = self._rugosite * espace

        if (demi < 1):
            return
        print(demi)

        # carre
        for y in range(demi, self._max, espace):
            for x in range(demi, self._max, espace):
                amplitude = random.uniform(0, 1) * scale * 2 - scale
                self.carre(x, y, demi, amplitude)

        # diamant
        for y in range(0, self._max + 1, demi):
            for x in range((y + demi) % espace, self._max + 1, espace):
                amplitude = random.uniform(0, 1) * scale * 2 - scale
                self.diamant(x, y, demi, amplitude)

        self.divide(espace / 2)

    def carre(self, x, y, distance, amplitude):

        haut_gauche = self.get(x - distance, y - distance)
        haut_droit = self.get(x + distance, y - distance)
        bas_gauche = self.get(x + distance, y + distance)
        bas_droit = self.get(x - distance, y + distance)

        moyenne = ((haut_gauche + haut_droit + bas_gauche + bas_droit) / 4)
        self.set(x, y, moyenne + amplitude)

    def diamant(self, x, y, distance, amplitude):

        haut = self.get(x, y - distance)
        droit = self.get(x + distance, y)
        bas = self.get(x, y + distance)
        gauche = self.get(x - distance, y)

        moyenne = ((haut + droit + bas + gauche) / 4)
        self.set(x, y, moyenne + amplitude)

    def get__grille(self):
        return self._grille


a = diamantcarre(3, 0.5, [0, 5])
print(a.get__grille())
