
class Jugador:
    def __init__(self, nombre):
        
        self.__nombre = nombre
        self.__hp = 4000
        self.__n_cartas = 20

    def get_info(self):

        print(f"\nNombre: {self.__nombre}\nCartas restantes: {self.__n_cartas}\nPuntos de vida: {self.__hp}")
    
    def atacar(self):
        pass

        