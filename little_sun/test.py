from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        """Este método debe ser implementado por todas las clases hijas"""
        pass

    @abstractmethod
    def moverse(self):
        """Este método debe ser implementado por todas las clases hijas"""
        pass

    def presentarse(self):
        """Este método es común para todas las clases hijas"""
        return f"Soy {self.nombre}"


# Clase hija que implementa la clase abstracta
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

    def moverse(self):
        return "Corriendo en cuatro patas"


# Clase hija que implementa la clase abstracta
class Pajaro(Animal):
    def hacer_sonido(self):
        return "¡Pío!"

    def moverse(self):
        return "Volando por el aire"


# Ejemplo de uso
def main():
    # No se puede instanciar la clase abstracta
    # animal = Animal("Generic")  # Esto causaría un error

    perro = Perro("Max")
    pajaro = Pajaro("Piolin")

    print(perro.presentarse())  # Soy Max
    print(perro.hacer_sonido())  # ¡Guau!
    print(perro.moverse())  # Corriendo en cuatro patas

    print(pajaro.presentarse())  # Soy Piolin
    print(pajaro.hacer_sonido())  # ¡Pío!
    print(pajaro.moverse())  # Volando por el aire


if __name__ == "__main__":
    main()
