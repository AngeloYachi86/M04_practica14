class Coche:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def obtener_marca(self):
        return self.marca

    def establecer_marca(self, marca):
        self.marca = marca

    def obtener_modelo(self):
        return self.modelo

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def obtener_year(self):
        return self.año

    def establecer_year(self, año):
        self.año = año

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: {self.precio}")

    def to_dict(self):
        return {"marca": self.marca, "modelo": self.modelo, "year": self.año, "precio": self.precio}




