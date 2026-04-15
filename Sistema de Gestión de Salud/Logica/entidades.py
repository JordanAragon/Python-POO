class paciente:
    def __init__(self, nombre, apellido, edad, peso, altura):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    
    def obtener_estado(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"
        
class gestion_paciente:
    def __init__(self):
        self.lista_pacientes = []

    def agregar_paciente(self, paciente):
        self.lista_pacientes.append(paciente)

    def buscar_paciente(self, apellidos):
        for paciente in self.lista_pacientes:
            if paciente.apellido == apellidos:
                return paciente
        return None
    
    def actualizar_datos(self, apellidos, nuevo_peso, nueva_altura):
        paciente = self.buscar_paciente(apellidos)
        if paciente:
            paciente.peso = nuevo_peso
            paciente.altura = nueva_altura
            return True
        return False