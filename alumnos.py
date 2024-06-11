#Crear tres alumnos desde la misma clase y matricularlos a diferentes materias.

#Creamos la clase
class Estudiante:
    #creamos el constructor de la clase
    def __init__(self, nombre, apellidos, semestre):
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.sem = semestre
        self.materias = []
    #creamos métodos de la clase
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} {self.apellidos} y estoy en {self.sem} grado. Y matriculé {self.materias}")
    
    def matricular_asignatura(self):
        
        decision = input(f"Hola, {self.nombre}¿Desea matricular alguna asignatura? (S) sí o (N) no.\n").lower()
        if decision == 's':
            asignatura = input(f"¿Qué asignatura quieres matricular, {self.nombre}?\n")
            self.materias.append(asignatura)
        
            respuesta = input("¿Quieres matricular otra asignatura? (S) sí o (N) no\n").lower()
            while respuesta == 's':
                nueva_asignatura = input("Escribe otra asignatura.\n")
                self.materias.append(nueva_asignatura)
                respuesta = input("¿Quieres matricular otra asignatura? (S) sí o (N) no\n").lower()
                                
        else:
            print(f"Tiene matriculadas {self.materias}")
            print("Vuelve cuando quieras matricular algo.")
        
        return self.materias

    def cancelar_asignatura(self):
        print(f"Actualmente tienes matriculadas {self.materias}")
        decision = input("¿Desea cancelar alguna asignatura? (S) sí o (N) no\n").lower()
        if decision == 's':
            mat_cancelada = input("¿Qué asignatura quieres cancelar?\n")
            self.materias.remove(mat_cancelada)
            print(f"Cancelaste {mat_cancelada}, tienes matriculada {self.materias}")
        
            respuesta = input("¿Quieres cancelar otra asignatura? (S) sí o (N) no\n").lower()
        
            while respuesta == 's':
                asig_cancelada = input("Escribe otra asignatura.\n")
                self.materias.remove(asig_cancelada)
                print(f"Cancelaste {asig_cancelada}")
                respuesta = input("¿Quieres cancelar otra asignatura? (S) sí o (N) no\n").lower()
            
            
            print(f"Tienes matriculadas {self.materias}")
                
        else:
            print(f"Tienes matriculadas {self.materias}")

        
        

#Instanciamos la clase Estudiante

estudiante_01 = Estudiante("Juan Carlos", "Restrepo Jiménez", 6)

estudiante_02 = Estudiante("María", "Vélez Ramos", 7)

estudiante_03 = Estudiante("Jhon Everth", 'Sánchez Pérez', 7)


#Cada estudiante tiene tres métodos: presentarse(), matricular_asignatura(), cancelar_asignatura()

