"""
Programación Orientada a Objetos
19-01-2023
Jeyfrey Calero"""

class electronic():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False  #para poder cambiar a TRUE estos estados se deben crear MÉTODOS por cada uno
        self.actualizado = False
        self.apagado = False

    def encender(self):
        self.encendido = True

    def actualizar(self):
        self.actualizar = True
    
    def apagado(self):
        self.apagado = True
    

    def estado(self):
        print("Marca: ", self.marca, "\n Modelo: ", self.modelo, "\n On: ", self.encendido, "\n Update: ", self.actualizado, 
        "\n Off: ", self.apagado)

class Nevera(electronic):
    def refrigerar(self, congelar):
        self.congelar = congelar
        if (self.congelar):
            return "la nevera se encuentra congelando"
        else:
            "La nevera no está funcionando bien"



class Microondas(electronic):
    cocinar = ""

    def cocinando(self):
        self.cocinar = "Estoy cocinando fideos"

    def estado(self):
        print("Marca: ", self.marca, "\n Modelo: ", self.modelo, "\n On: ", self.encendido, "\n Update: ", self.actualizado, 
        "\n Off: ", self.apagado, "\n", self.cocinar)

Frezer1 = Nevera("Samsung", "Inverter")
Frezer1.actualizar()
Frezer1.estado()
print(Frezer1.refrigerar(False))


micro = Microondas("Samsung", "Rectangular")
micro.cocinando()
micro.estado()

    





