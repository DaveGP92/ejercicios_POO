
class Monstruo:
    def __init__(self, nombre, tipo, p_ataque):

        self.__nombre = nombre
        self.__tipo = tipo
        self.__ataque = p_ataque
    
    def get_info(self):

        print(f"Nombre: {self.nombre}\nTipo: {self.tipo}\nAtaque: {self.ataque}")
    
    def atacar(self):
        print(f"{self.nombre} ha atacado")
        