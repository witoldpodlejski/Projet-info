class Plancton(object):
    def __init__(self, espece, temperature_preferencielle, population, taux_croissance):
        self._espece = espece
        self._temperature_preferencielle = temperature_preferencielle
        self._population = population
        self._taux_croissance = taux_croissance


    def se_developper(self, temperature, capacite_max_plancton):
        diff_temp=abs((self.temperature_preferencielle - temperature)/5)
        if diff_temp < 1 :
            self.population = int(self.population + self.population * (1 - diff_temp) * self.taux_croissance * (1-self.population/capacite_max_plancton))
        else:
            self.population = int(self.population + self.population * (1 - diff_temp))


    def reduire_population(self, val):
        self.population(self.population - val)

    @property
    def temperature_preferencielle(self):
        return self._temperature_preferencielle

    @property
    def taux_croissance(self):
        return self._taux_croissance

    @temperature_preferencielle.setter
    def temperature_preferencielle(self, val):
        self._temperature_preferencielle = val

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, val):
        self._population = val

