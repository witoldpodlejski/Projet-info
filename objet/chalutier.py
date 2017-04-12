class Chalutier(object):
    def __init__(self ,position):
        self._position = position
        self._capacite = 1000
        self._stock = 0
    def pecher(self):
        return self._position.pecher()
    def vider_cale(self):
        self._stock = 0
    def se_deplacer(self, position):
        self._position = position
    def augmenter_stock(self, val):
        self._stock += val
        if self._stock > self._capacite :
            self._stock = self._capacite
            print('Chalutier rempli !')
