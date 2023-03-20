import json

class Cat:
    def __init__(self, nombre, raza, edad, color):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_raza(self):
        return self.raza

    def establecer_raza(self, raza):
        self.raza = raza

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_color(self):
        return self.color

    def establecer_color(self, color):
        self.color = color

    def informacion(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}, Color: {self.color}")

    def to_dict(self):
        return {"nombre": self.nombre, "raza": self.raza, "edad": self.edad, "color": self.color}
