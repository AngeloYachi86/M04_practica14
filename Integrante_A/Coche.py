class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    # getters
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getAño(self):
        return self.año

    # setters
    def setMarca(self, marca):
        self.marca = marca

    def setAño(self, año):
        self.año = año

    def setModelo(self, modelo):
        self.modelo = modelo

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "año": self.año
        }



