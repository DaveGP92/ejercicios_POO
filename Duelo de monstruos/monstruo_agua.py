import monstruo

class MonstruoAgua(monstruo.Monstruo):

    def __init__(self, nombre, tipo, p_ataque):
        super().__init__(nombre, tipo, p_ataque)

monstruo_1_agua = MonstruoAgua("Dragón agua", "Agua", 1450)

monstruo_2_agua = MonstruoAgua("Serpiente", "Agua", 1300)
