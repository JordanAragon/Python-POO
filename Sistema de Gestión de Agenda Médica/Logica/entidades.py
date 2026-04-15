class Medico:
    def __init__(self, nombre_medico, especialidad, id_registro_medico):
        self.nombre_medico = nombre_medico
        self.especialidad = especialidad
        self.id_registro_medico = id_registro_medico

class Cita:
    def __init__(self, fecha, hora, objeto_medico):
        self.fecha = fecha
        self.hora = hora
        self.medico = objeto_medico  

class Paciente:
    def __init__(self, nombre_paciente, id_paciente):
        self.nombre_paciente = nombre_paciente
        self.id_paciente = id_paciente
        self.lista_citas = []

    def agregar_cita(self, nueva_cita):
        if len(self.lista_citas) < 3:
            self.lista_citas.append(nueva_cita)
            print("Cita agendada con éxito para el paciente {self.nombre_paciente}.")
            return True
        else:
            print("Error: El paciente {self.nombre_paciente} ya tiene el máximo de 3 citas.")
            return False