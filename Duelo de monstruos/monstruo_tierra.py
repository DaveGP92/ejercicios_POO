import monstruo

class MonstruoTierra(monstruo.Monstruo):

    def __init__(self, nombre, tipo, p_ataque):
        super().__init__(nombre, tipo, p_ataque)

monstruo_1_tierra = MonstruoTierra("Dragón tierra", "Tierra", 1150)

monstruo_2_tierra = MonstruoTierra("Topo", "Tierra", 1480)

