import monstruo

class MonstruoAgua(monstruo.Monstruo):

    def __init__(self, nombre, tipo, p_ataque):
        super().__init__(nombre, tipo, p_ataque)

monstruo_1_agua = MonstruoAgua("Dragón agua", "Agua", 1450)

monstruo_1_agua.get_info()
monstruo_1_agua.atacar()