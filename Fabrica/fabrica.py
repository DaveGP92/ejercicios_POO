import moto
class Fabrica():
    def __init__(self, llantas, color, precio):
        self.__llantas = llantas
        self.__color = color
        self.__precio = precio
    
    def mostrar_datos(self):
        print(f"""
            Cantidad de llantas: {self.__llantas}
            Color: {self.__color}
            Precio: {self.__precio}""")
        

