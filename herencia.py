# clase padre(SUPERCLASE)
class Personaje:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def presentarse(self):
       print(f"¡Hola Soy! {self.nombre} y mi poder es {self.poder}")

# clase derivada de la superclase(subclase)
class Superheroe(Personaje):
    def __init__(self, nombre, poder, ciudad):
        super().__init__(nombre, poder) # Utilizaremos SUPER para pasarle la informacion a la superclase
        self.ciudad = ciudad

    def salvar_la_ciudad(self):
        print(f"{self.nombre} esta salvando {self.ciudad} usando su poder {self.poder}")
# clase derivada de la superclase(subclase)
class Villano(Personaje):
    def __init__(self, nombre, poder, archienemigo):
        super().__init__(nombre, poder)
        self.archienemigo = archienemigo

    def plan_maligno(self):
        print(f"¡CUIDADO! {self.nombre} esta planeando un plan malvado en contra de {self.archienemigo} usando su poder {self.poder}")

heroe = Superheroe("Captain Codigo", "Supermegafactorizacion", "Python City")
villano = Villano("Pugman", "Crear errores en tus aplicaciones favoritas", "Captain Codigo")

# heroe.presentarse()
# villano.presentarse()

heroe.salvar_la_ciudad()
villano.plan_maligno()


