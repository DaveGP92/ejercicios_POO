
class Jugador:
    def __init__(self, nombre):
        
        self.nombre = nombre
        self.hp = 4000
        self.n_cartas = 20

    def get_info(self):

        print(f"Nombre: {self.nombre}\nCartas restantes: {self.n_cartas}\nPuntos de vida: {self.hp}")