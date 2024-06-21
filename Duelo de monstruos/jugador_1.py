import jugador

class Jugador1(jugador.Jugador):

   def __init__(self, nombre):
      
      self.equipo = 'A'
      super().__init__(nombre)
   
   def get_info(self):
      super().get_info()
      print(f"Equipo: {self.equipo}")



