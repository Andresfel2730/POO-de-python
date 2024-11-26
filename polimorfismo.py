#SUPERCLASE
class Instrumento():
    def __init__(self, nombre):
        self.nombre = nombre
    def tocar(self):
        print("Hacer un sonido generico")

class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("La guitarra")

    # vamos a sobreescribir el metodo con un comportamiento propio de esta clase(OVERRIDE)
    def tocar(self):
        print(f"\033[91m{self.nombre} Esta haciendo el mejor solo de su vida usando bendings y ligados")

class Bateria(Instrumento):
    def __init__(self):
        super().__init__("La bateria")

    # vamos a sobreescribir el metodo con un comportamiento propio de esta clase(OVERRIDE)
    def tocar(self):
        print(f"\033[92m{self.nombre} Esta llevando un buen ritmo en 4 cuartos")

class Piano(Instrumento):
    def __init__(self):
        super().__init__("El piano")

    # vamos a sobreescribir el metodo con un comportamiento propio de esta clase(OVERRIDE)
    def tocar(self):
        print(f"\033[93m{self.nombre} Nos esta deleitando con un gran blues clasico")

guitarra = Guitarra()
bateria = Bateria()
piano = Piano()

# POLIMORFISMO: Es la capacidad de un metodo de hacer distintas cosas dependiendo de la clase origen
guitarra.tocar()
bateria.tocar()
piano.tocar()