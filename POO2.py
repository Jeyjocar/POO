"""
Programación Orientada a Objetos
19-01-2023
Jeyfrey Calero"""


class Dog:
    def __init__(self, nombre, edad, color, toys):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.toys = toys

    def sentado(self, nombre):
            print(f'{self.nombre} esta sentado o se va a sentar?')

    def ladrar(self, ladrando):
        print(f'{self.nombre} esta ladrando')
        if ladrando == True:
            print("está ladrando")
        else:
            print("No está ladrando")





mi_dog = Dog("Jango", 4,"Chocolate", "Huesos")
print(f'Mi perro se llama: {mi_dog.nombre}, tiene una edad de {mi_dog.edad} años, es de color {mi_dog.color}, y le encanta jugar con {mi_dog.toys}')
mi_dog.sentado = True



