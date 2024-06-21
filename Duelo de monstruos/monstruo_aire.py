import monstruo

class MonstruoAire(monstruo.Monstruo):

    def __init__(self, nombre, tipo, p_ataque):
        super().__init__(nombre, tipo, p_ataque)

monstruo_1_aire = MonstruoAire("Dragón aire", "aire", 1250)

monstruo_2_aire = MonstruoAire("Águila", "aire", 1525)
