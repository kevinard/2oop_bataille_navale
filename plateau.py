class Plateau:
    def __init__(self, cases_horizontales, cases_verticales):
        self.__cases = [[0]*cases_horizontales for i in range(cases_verticales)]

    def get_cases(self):
        return self.__cases

    def get_case(self, i, j):
        return self.__cases[i][j]

    def set_cases(self, cases):
        self.__cases = cases

    def set_case(self, i, j, valeur):
        self.__cases[i][j] = valeur
