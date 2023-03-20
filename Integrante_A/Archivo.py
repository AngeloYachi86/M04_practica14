class Archivo:
    def __init__(self, nombre, tamaño, fecha_modificacion):
        self.nombre = nombre
        self.tamaño = tamaño
        self.fecha_modificacion = fecha_modificacion

    #getters
    def getNombre(self):
        return self.nombre

    def getTamaño(self):
        return self.tamaño

    def getFecha_modificacion(self):
        return self.fecha_modificacion

    #setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setTamaño(self, tamaño):
        self.tamaño = tamaño

    def setFecha_modificacion(self, fecha_modificacion):
        self.fecha_modificacion = fecha_modificacion


    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tamaño": self.tamaño,
            "fecha_modificacion": self.fecha_modificacion
        }