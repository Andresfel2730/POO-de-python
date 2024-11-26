# CLASE ABSTRACTA: La plantilla o modelo de las clases que la heredan

from abc import ABC, abstractmethod
class Animal(ABC):
    # atributo estatico (atributo de clase): va a estar disponible independiente de las instancias
    cant_de_animales = 0

    def __init__(self,nombre):
        self.nombre = nombre
        Animal.cant_de_animales += 1

    # un metodo abstracto de esta forma obliga a la clases derivadas a implementar este comportamiento
    @abstractmethod
    def hacer_sonido(self):
        pass

    # Metodo de clase: es un metodo que se puede ejecutar desde la clase misma
    # cls: se refiere a la clase [Al ser un atributo estatico le pertenece a la clase y no a la instancia]
    @classmethod
    def obtenerCantidadAnimales(cls):
        print(f"la cantidad actual de animales es: {cls.cant_de_animales}") 

# CLASE DERIVADA PERRO
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace: 'Guau Guau'")
    def mover_cola(self):
        print(f"{self.nombre} esta moviendo la cola de felicidad")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace: 'Miau Miau'")
    def ronronear(self):
        print(f"{self.nombre} ronronea de felicidad")

perrito = Perro("Manchita")
gatito = Gato("peluza")

perrito.hacer_sonido()
gatito.hacer_sonido()

perrito.mover_cola()
gatito.ronronear()

Animal.obtenerCantidadAnimales()