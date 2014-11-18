class Bateau:
    def __init__(self, nom, nb_cases, position):
        self.__nom = nom
        self.__nb_cases = nb_cases
        self.__position = position

    def get_nom(self):
        return self.__nom

    def get_nb_cases(self):
        return self.__nb_cases

    def get_position(self):
        return self.__position

    def set_nom(self, nom):
        self.__nom = nom

    def set_nb_cases(self, nb_cases):
        self.__nb_cases = nb_cases

    def set_nom(self, position):
        self.__position = position
