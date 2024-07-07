# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.

# Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.

import moto, carro

moto_1 = moto.Moto(2, nombre_vehiculo="moto_1", color="negro", precio=125000)
moto_1.mostrar_datos()
carro_1 = carro.Carro(4, "rojo", 256000, "carro_1")
carro_1.mostrar_datos()