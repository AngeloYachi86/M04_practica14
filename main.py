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





import Cat
import Coche

# Crear una lista con 5 instancias de Cat.
gatos = [
    Cat("Pelusa", "Persa", 2, "Negro"),
    Cat("frank", "Siames", 4, "Marrón"),
    Cat("Garfield", "Mestizo", 1, "Naranja"),
    Cat("Luna", "Sphynx", 3, "Gris"),
    Cat("pedro", "Siames", 5, "Blanco y Marrón")
]

# Crear una lista con 5 instancias de Coche.
coches = [
    Coche("Toyota", "Corolla", 2020, 15000),
    Coche("Honda", "Civic", 2019, 12000),
    Coche("Ford", "Mustang", 2021, 35000),
    Coche("Chevrolet", "Camaro", 2020, 40000),
    Coche("Nissan", "Altima", 2018, 9000)
]

# Convertir las dos listas en listas de diccionarios utilizando el método to_dict().
gatos_dict = [gato.to_dict() for gato in gatos]
coches_dict = [coche.to_dict() for coche in coches]

