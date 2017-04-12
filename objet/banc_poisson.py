class BancPoisson(object):
    def __init__(self, population, espece):
        self._espece = espece
        self._population = population

    @property
    def espece(self):
        return self._espece

    @property
    def population(self):
        return self._population

    def reduire_population(self):
        self._population = int(self._population * 0.75)

    def se_developper(self, liste_plancton, capacite_max_banc):
        nb_proie = 0
        for i in liste_plancton:
            for j in self.espece.liste_proie:
                if i.nom == j:
                    nb_proie += i.population

        reste_proie = nb_proie - self.population * 100
        if reste_proie > 0:
            self._population = int(self.population + self.population * self._espece._taux_croissance * (1 - self.population / capacite_max_banc))
            return reste_proie / nb_proie
        else:
            self._population = int((self.population + reste_proie / 10) * (1 + self._espece._taux_croissance * (1 - self.population / capacite_max_banc)))
            return 0.9

    def se_deplacer(self, liste_case):
        nb_proie =0
        for i in liste_case[0]._liste_pancton:
            for j in self.espece.liste_proie:
                if i.nom == j:
                    nb_proie += i.population
        coeff = nb_proie / (abs((liste_case[0].temperature - self.espece.temperature_preferencielle)/3) + 1)
        preference = [0, coeff]

        for i in range(1, len(liste_case)):
            for j in liste_case[i]._liste_pancton:
                for k in self.espece.liste_proie:
                    if j.nom == k:
                        nb_proie += j.population
            coeff = nb_proie / abs(liste_case[i].temperature - self.espece.temperature_preferencielle)
            if coeff > preference[1]:
                preference = [i, coeff]
                # elif coeff == preference[0,1] :
                preference.append([i, coeff])
        return liste_case[preference[0]]
