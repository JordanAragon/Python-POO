class Mascota:
    def __init__(self, nombre, edad_cronologica):
        self.nombre = nombre
        self.edad_cronologica = edad_cronologica


class Gato(Mascota):
    def calcular_edad_humana(self):
        super().__init__(self.nombre, self.edad_cronologica)
        if self.edad_cronologica == 1:
            return 15
        elif self.edad_cronologica == 2:
            return 24
        elif self.edad_cronologica > 2:
            return 24 + (self.edad_cronologica - 2) * 4
        else:
            return 0


class Perro(Mascota):
    def __init__(self, nombre, edad_cronologica, tamaño):
        super().__init__(nombre, edad_cronologica)
        self.tamaño = tamaño

    def calcular_edad_humana(self):
        if self.tamaño == "pequeño":
            return self.edad_cronologica * 5
        elif self.tamaño == "mediano":
            return self.edad_cronologica * 6
        elif self.tamaño == "grande":
            return self.edad_cronologica * 7
        else:
            return 0

        