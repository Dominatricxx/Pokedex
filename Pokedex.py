from abc import ABC, abstractmethod

class PokemonBase(ABC):
    def __init__(self):
        self.nombre = "Sin Pokémon"
        self.descripcion = "No descripción"
        self.ataque = 0
        self.defensa = 0
        self.vida = 0
        self.nivel = 0
        self.evolucion = 1
        self.atrapado = False

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def actualizar(self):
        pass

    @abstractmethod
    def detallesPokemon(self):
        pass

    @abstractmethod
    def entrenar(self):
        pass


class Pokemon(PokemonBase):
    def __init__(self, nombre, descripcion):
        super().__init__()
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = 50
        self.defensa = 50
        self.vida = 50
        self.nivel = 1

    def hablar(self):
        print(self.nombre + "!!!")

    def actualizar(self):
        if self.nivel >= 100 and self.evolucion < 3:
            self.evolucion += 1
            self.nivel = 0
            if self.evolucion == 2:
                self.nombre = "Pikachu"
            elif self.evolucion == 3:
                self.nombre = "Raichu"
            print("¡El Pokémon ha evolucionado! Ahora es:", self.nombre)

    def detallesPokemon(self):
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Ataque:", self.ataque)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)
        print("Nivel:", self.nivel)
        print("Evolución:", self.evolucion)
        print("Atrapado:", self.atrapado)

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.vida += 10
        self.nivel += 10
        self.actualizar()

    def subirAtaque(self):
        self.ataque += 20

    def subirDefensa(self):
        self.defensa += 20

    def subirVida(self):
        self.vida += 20


pokemon_principal = Pokemon("Pichu", "Un Pokémon eléctrico pequeño")
pokemones_atrapados = []

while True:
    print("\n--- POKEDEX ---")
    print("1. Ver detalles")
    print("2. Hablar")
    print("3. Entrenar")
    print("4. Subir ataque")
    print("5. Subir defensa")
    print("6. Subir vida")
    print("7. Atrapar Pokémon")
    print("8. Ver Pokémon atrapados")
    print("9. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        pokemon_principal.detallesPokemon()

    elif opcion == "2":
        pokemon_principal.hablar()

    elif opcion == "3":
        pokemon_principal.entrenar()

    elif opcion == "4":
        pokemon_principal.subirAtaque()

    elif opcion == "5":
        pokemon_principal.subirDefensa()

    elif opcion == "6":
        pokemon_principal.subirVida()

    elif opcion == "7":
        nombre = input("Nombre del Pokémon a atrapar: ")
        nuevo = Pokemon(nombre, "Pokémon atrapado")
        nuevo.atrapado = True
        pokemones_atrapados.append(nuevo)
        print("Pokémon atrapado!")

    elif opcion == "8":
        for p in pokemones_atrapados:
            print("-", p.nombre)

    elif opcion == "9":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")