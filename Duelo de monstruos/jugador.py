
class Jugador:
    def __init__(self, nombre):
        
        self.__nombre = nombre
        self.__hp = 4000
        self.__n_cartas = 20

    def get_info(self):

        print(f"\nNombre: {self.__nombre}\nCartas restantes: {self.__n_cartas}\nPuntos de vida: {self.__hp}")

    
    def sel_accion(self):

        decision = input(f"¿Qué desea hacer el jugador {self.__nombre}: atacar (a) o pasar el turno (p)?:\n").lower()

        def atacar():
            return f"{self.__nombre} ha atacado."
        
        def pasar_turno():
            return f"{self.__nombre} pasa el turno."
        
        if decision == "a":
            return atacar
        
        elif decision == "p":
            return pasar_turno
        
    
        
        