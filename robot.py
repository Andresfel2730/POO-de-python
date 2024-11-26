# CLASE: es una plantilla que define caracteristicas y comportamientos de un objeto
class Robot:
    #constructor: es un metodo especial que se ejecuta al crear una instancia y permite inicializar los atributos
    # self: se refiere a la instancia especifica
    def __init__(self, nombre, tipo):
        #atributos y caracteristicas
        self.nombre = nombre
        self.tipo = tipo

    # METODO: Es una funcion que define el comportamiento o accion de un objeto
    def saludar(self):
        print(f"¡Hola! soy {self.nombre} y soy un robot en una muestras de Robots y hablo gracias a una IA")
    def hacer_truco(self):
        if self.tipo == "Humanoide":
            print(f"Soy {self.nombre} y estoy haciendo el paso del Robot")
        else:
            print(f"Soy {self.nombre} de tipo {self.tipo} por favor darme instrucciones")        

    
    # Instancia: que es un objeto especifico creado a partir de la plantilla llamada CLASE
robotin = Robot("Robotin", "Humanoide")
tostadora = Robot("Tosty", "Electrodomestico")

# robotin.saludar()
# tostadora.saludar()
# robotin.hacer_truco()
tostadora.hacer_truco()