"""
Programación Orientada a Objetos
19-01-2023
Jeyfrey Calero"""


class Empleado:
    
    def __init__(self, nombre, apellido, salario):
    
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario


    def obtener_suma(self, cantidad):
        self.salario += cantidad

empleado = Empleado("Rubén ", "Gonzalez" , 1000000)
print(f'Salario antes de la suma: {empleado.salario}')

empleado.obtener_suma(100000)
print(f'Salario después de la suma: {empleado.salario}')

empleado.obtener_suma(250000)
print(f'Salario después de la suma: {empleado.salario}')