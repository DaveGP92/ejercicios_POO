import monstruo

class MonstruoAire(monstruo.Monstruo):

    def __init__(self, nombre, tipo, p_ataque):
        super().__init__(nombre, tipo, p_ataque)

monstruo_1_aire = MonstruoAire("Dragón aire", "aire", 1250)

monstruo_1_aire.get_info()
monstruo_1_aire.atacar()