"""
02-02-2023
POO8
Jeyfrey Calero"""


from POO8 import Calzado  #importamos del archivo o código POO8 la clase CALZADO

def main():
    calzado1 = Calzado()
    calzado1.marca = "Nike"
    calzado1.talla = 41

    #print(f'Me fui a una tienda de calzado y me compré unos zapatos {calzado1.marca}, de talla {calzado1.talla}')
    print(calzado1)

if __name__=="__main__":  #esta función está la función, codigo o el mensaje que queremos mostrar al inicio al usuario
    main() 