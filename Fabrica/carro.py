import fabrica

class Carro(fabrica.Fabrica):
    def __init__(self, llantas, color, precio, nombre_vehiculo):
        self.__nombre = nombre_vehiculo
        super().__init__(llantas, color, precio)

    def mostrar_datos(self):
        print(f"{self.__nombre}")
        return super().mostrar_datos()