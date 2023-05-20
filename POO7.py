"""
02-02-2023
POO7
Jeyfrey Calero"""

class Estudiante:
    def __init__(self):
        self._nombre = ""
        self._edad = None #NONE indica que va a estar vacío y que luego se le asigna el valor
        
    @property #@ property indica que vamos a acceder a ellos
    def nombre(self):
        return self._nombre     # con el guión bajo se encapsula un método (solo se puede acceder dentro misma clase)
    @nombre.setter
    def nombre(self, Valor):   #Setter devolver Getter = extraer 
        self._nombre = Valor
    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def edad(self):
        return self._edad     # con el guión bajo se encapsula un método (solo se puede acceder dentro misma clase)
    @edad.setter
    def edad(self, Valor):   #Setter devolver Getter = extraer 
        self._edad = Valor
    @edad.deleter
    def edad(self):
        del self._edad

def main():
    estudiante1 = Estudiante()
    estudiante2 = Estudiante()
    estudiante1.nombre = "Eleazar Pérez"
    estudiante1.edad = 17
    estudiante2.nombre = "Maritza Solano"
    estudiante2.edad = 15



    print("Datos del primer estudiante: ")
    print(f'Nombre: {estudiante1.nombre}')
    print(f'Edad: {estudiante1.edad}')
    print("Datos para el segundo estudiante")
    print(f'Nombre: {estudiante2.nombre}')
    print(f'Edad: {estudiante2.edad}')


if __name__ == '__main__':  #Función por defecto de PYTHON que valida la función
    main()


