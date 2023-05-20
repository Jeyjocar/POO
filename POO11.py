"""
02-02-2023
POO8
Jeyfrey Calero"""

"""Este código seria el principal que hereda de POO10 las características de la clase Mi ingrediente"""

from Recetario import Mi_ingrediente


def main():
    receta = Mi_ingrediente("Arroz", 2, "Libras")
    receta.cantidad = 15
   

if __name__ == "__main__":
    main()
    