import jugador

class Jugador2(jugador.Jugador):

    def __init__(self, nombre):

        self.equipo = 'B'
        super().__init__(nombre)
    
    def get_info(self):
        super().get_info()
        print(f"Equipo: {self.equipo}")


jugador_2 = Jugador2("Goku")

jugador_2.get_info()
