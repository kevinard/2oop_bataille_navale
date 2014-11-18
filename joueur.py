class Joueur:
    def __init__(self, nom, numero):
        self.__nom = nom
        self.__numero = numero

    def get_nom(self):
        return self.__nom

    def get_numero(self):
        return self.__numero

    def set_nom(self, nom):
        self.__nom = nom

    def set_numero(self, numero):
        self.__numero = numero

    def jouer(self):
        pass
