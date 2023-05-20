"""
02-02-2023
POO8
Jeyfrey Calero"""


class Calzado():
    def __init__(self):
        self._marca = ""
        self._talla = None

        @property
        def marca(self):
            return self._marca

        @marca.setter
        def marca(self, valor):
            self._marca = valor
        
        @marca.deleter
        def marca(self):
            del self._marca

        @property
        def talla(self):
            return self._talla

        @talla.setter
        def talla(self, valor):
            self._talla = valor
        
        @talla.deleter
        def talla(self):
            del self._talla


        def __str__(self):
            return f'''marca: {self.marca},
talla: {self.talla}'''