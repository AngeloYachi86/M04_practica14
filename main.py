import json

from Integrante_A.Coche import Coche
from Integrante_A.Archivo import Archivo
coches = [
    Coche("Ford", "Focus", 2019),
    Coche("Toyota", "Corolla", 2020),
    Coche("Volkswagen", "Golf", 2018),
    Coche("Renault", "Clio", 2021),
    Coche("Peugeot", "208", 2017)
]

archivos = [
    Archivo("documento1.txt", "10 KB", "2022-01-15"),
    Archivo("documento2.docx", "25 KB", "2022-02-03"),
    Archivo("foto1.jpg", "500 KB", "2022-01-02"),
    Archivo("presentacion.ppt", "1 MB", "2022-02-25"),
    Archivo("video1.mp4", "50 MB", "2022-01-10")
]

# Convertimos las listas en listas de diccionarios
coches_dict = [coche.to_dict() for coche in coches]
archivos_dict = [archivo.to_dict() for archivo in archivos]

# Creamos un objeto contenedor para guardar ambas listas
objeto_contenedor = {
    "coches": coches_dict,
    "archivos": archivos_dict
}

# Guardamos el objeto contenedor en un archivo .json
with open("json_API/a.json", "w") as file:
    json.dump(objeto_contenedor, file)
with open("json_API/a.json", "r") as file:
    print(json.load(file))