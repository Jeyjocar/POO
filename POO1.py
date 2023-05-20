"""
Programación Orientada a Objetos
19-01-2023
Jeyfrey Calero"""

class Persona:
    def __init__(self, nombre, edad): #el INIT hace referencia a las caracteristicas del objeto
        self.nombre = nombre
        self.edad = edad


persona1 = Persona("José")
edad_persona = Persona("45")

#nombre.nombre = 'Pedro'
print(persona1.nombre)