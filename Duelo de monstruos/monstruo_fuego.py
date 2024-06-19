import monstruo

class MonstruoFuego(monstruo.Monstruo):

    def __init__(self, nombre, tipo, ataque):
        super().__init__(nombre, tipo, ataque)
    

monstruo_1_fuego = MonstruoFuego("Dragón fuego", "Fuego", 1200)

monstruo_1_fuego.get_info()
monstruo_1_fuego.atacar()