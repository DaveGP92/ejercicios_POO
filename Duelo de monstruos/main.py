import jugador, jugador_1, jugador_2,monstruo, monstruo_agua, monstruo_aire, monstruo_fuego

nombre = input("Escribe el nombre del jugador 1:\n")
jugador_1 = jugador_1.Jugador1(nombre)

jugador_1.get_info()

nombre = input("Escribe el nombre del jugador 2:\n")

jugador_2 = jugador_2.Jugador2(nombre)

jugador_2.get_info()

print(f"Cada jugador comienza con un total de 40 cartas y un total de 4000 puntos de vida.\n")

accion = jugador_1.sel_accion()()
print(accion)


