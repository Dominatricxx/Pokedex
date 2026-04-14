import os
import time
from abc import ABC, abstractmethod
import random

def puntosCarga():
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n\nGAME OVER\n")

def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

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


class Entrenamiento(ABC):
    @abstractmethod
    def subirAtaque(self):
        pass

    @abstractmethod
    def subirDefensa(self):
        pass

    @abstractmethod
    def subirVida(self):
        pass


class Pokemon(PokemonBase):
    def __init__(self, nombre, descripcion):
        super().__init__()
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = 50
        self.defensa = 50
        self.vida = 50
        self.nivel = 0
        self.evolucion = 1
        self.atrapado = True

    def hablar(self):
        print(f"\n¡{self.nombre}!")

    def actualizar(self):
        if self.nivel >= 100 and self.evolucion < 3:
            self.evolucion += 1
            self.nivel = 0

            if self.evolucion == 2:
                self.nombre = "Pikachu"
            elif self.evolucion == 3:
                self.nombre = "Raichu"

            print(f"\n¡El Pokémon ha evolucionado! Ahora es: {self.nombre}\n")

        elif self.nivel == 100 and self.evolucion == 3:
            print(f"\n¡{self.nombre} ha alcanzado su máximo nivel!\n")

    def detallesPokemon(self):
        print(
            f"===== DETALLES DEL POKEMON =====\n"
            f"Nombre: {self.nombre}\n"
            f"Descripción: {self.descripcion}\n"
            f"Ataque: {self.ataque}\n"
            f"Defensa: {self.defensa}\n"
            f"Vida: {self.vida}\n"
            f"Nivel: [{self.nivel}/100]\n"
            f"Evolución: {self.evolucion}\n"
            f"Atrapado: {self.atrapado}\n"
            f"================================\n"
        )

    def entrenar(self):
        while True:
            limpiarPantalla()
            ataque_antes = self.ataque
            defensa_antes = self.defensa
            vida_antes = self.vida
            nivel_antes = self.nivel

            print(
                "===== ENTRENAMIENTO =====\n"
                "[1] Entrenamiento Normal\n"
                "[2] Entrenamiento Individual\n"
                "[3] Entrenamiento Intensivo\n"
                "[4] Entrenamiento Personalizado\n"
                "[5] Volver\n"
            )

            opcion = input("Elige: ")

            if opcion == "1":
                self.ataque += 10
                self.defensa += 10
                self.nivel += 10

            elif opcion == "2":
                print(
                    "\n[1] Subir ataque\n"
                    "[2] Subir defensa\n"
                    "[3] Subir vida\n"
                )

                eleccion = input("Elige: ")

                if eleccion == "1":
                    self.ataque += 10

                elif eleccion == "2":
                    self.defensa += 10

                elif eleccion == "3":
                    self.vida += 10


            elif opcion == "3":

                self.subirAtaque()
                self.subirDefensa()
                self.subirVida()


            elif opcion == "4":

                while True:
                    limpiarPantalla()
                    print(
                        "===== Elige un atributo =====\n"
                        "[1] Subir ataque\n"
                        "[2] Subir defensa\n"
                        "[3] Subir vida\n"
                        "[4] Subir nivel\n"
                        "[5] Volver\n"
                    )

                    eleccion = input("Elige: ")

                    if eleccion == "1":
                        self.ataque += int(input("Cantidad: "))

                    elif eleccion == "2":
                        self.defensa += int(input("Cantidad: "))

                    elif eleccion == "3":
                        self.vida += int(input("Cantidad: "))

                    elif eleccion == "4":
                        self.nivel += int(input("Cantidad: "))

                    elif eleccion == "5":
                        break


            elif opcion == "5":
                print()
                break

            self.actualizar()

            print("===== RESULTADOS DEL ENTRENAMIENTO =====")

            if self.ataque != ataque_antes and ataque_antes != 0:
                print(f"Ataque: {ataque_antes} → {self.ataque} (+{self.ataque - ataque_antes})")
            
            elif self.ataque != ataque_antes and ataque_antes == 0:
                print(f"Ataque: {ataque_antes} → {self.ataque} (+{self.ataque})")

            if self.defensa != defensa_antes and defensa_antes != 0:
                print(f"Defensa: {defensa_antes} → {self.defensa} (+{self.defensa - defensa_antes})")
            
            elif self.defensa != defensa_antes and defensa_antes == 0:
                print(f"Defensa: {defensa_antes} → {self.defensa} (+{self.defensa})")

            if self.vida != vida_antes and vida_antes != 0:
                print(f"Vida: {vida_antes} → {self.vida} (+{self.vida - vida_antes})")
            
            elif self.vida != vida_antes and vida_antes == 0:
                print(f"Vida: {vida_antes} → {self.vida} (+{self.vida})")

            if self.nivel != nivel_antes and nivel_antes != 0:
                print(f"Nivel: {nivel_antes} → {self.nivel} (+{self.nivel - nivel_antes})")

            elif self.nivel != nivel_antes and nivel_antes == 0:
                print(f"Nivel: {nivel_antes} → {self.nivel} (+{self.nivel})")
            
            else:
                print(f"Nivel: {nivel_antes} → {self.nivel} (+{self.nivel})")
            
            print("========================================\n")

            input("Presiona [Enter] para regresar al menú de entrenamientos.")


    def subirAtaque(self):
        self.ataque += 20

    def subirDefensa(self):
        self.defensa += 20

    def subirVida(self):
        self.vida += 20


class PokemonConEntrenamiento(Pokemon, Entrenamiento):
    pass


class PokemonAgua(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Agua")
        self.ataque_especial = "Hidrobomba"

    def actualizar(self):
        super().actualizar()
        self.ataque += 15
        self.defensa += 10
        self.vida += 10


class PokemonFuego(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Fuego")
        self.ataque_especial = "Lanzallamas"

    def actualizar(self):
        super().actualizar()
        self.ataque += 20
        self.defensa += 5
        self.vida += 10


class PokemonElectrico(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Eléctrico")
        self.ataque_especial = "Impactrueno"

    def actualizar(self):
        super().actualizar()
        self.ataque += 18
        self.defensa += 8
        self.vida += 10


class PokemonHierba(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Hierba")
        self.ataque_especial = "Látigo Cepa"

    def actualizar(self):
        super().actualizar()
        self.ataque += 10
        self.defensa += 15
        self.vida += 15


def aplicar_danio(atacante, defensor):
    dano = atacante.ataque

    if defensor.defensa >= dano:
        defensor.defensa -= dano
    else:
        restante = dano - defensor.defensa
        defensor.defensa = 0
        defensor.vida = max(0, defensor.vida - restante)

def aplicar_danio_especial(atacante, defensor):
    dano = atacante.ataque * 2

    if defensor.defensa >= dano:
        defensor.defensa -= dano
    else:
        restante = dano - defensor.defensa
        defensor.defensa = 0
        defensor.vida = max(0, defensor.vida - restante)


def combate(mi_pokemon, enemigos, atrapados):
    enemigo = random.choice(enemigos)

    print(f"\nCombate iniciado contra {enemigo.nombre}")

    while mi_pokemon.vida > 0 and enemigo.vida > 0:
        print(
            f"\nTu Pokémon: {mi_pokemon.nombre} | ATK:{mi_pokemon.ataque} DEF:{mi_pokemon.defensa} VIDA:{mi_pokemon.vida}\n"
            f"Enemigo: {enemigo.nombre} | ATK:{enemigo.ataque} DEF:{enemigo.defensa} VIDA:{enemigo.vida}\n"

            "\n===== Habilidades =====\n"
            "1. Pasar turno\n"
            "2. Ataque normal\n"
            "3. Ataque especial\n"
            "4. Huir\n"
            "=======================\n"
        )

        opcion = input("Elige: ")

        if opcion == "1":
            print(f"\n{mi_pokemon.nombre} decidió pasar turno")

        elif opcion == "2":
            defensa_antes = enemigo.defensa
            vida_antes = enemigo.vida

            aplicar_danio(mi_pokemon, enemigo)

            dano_defensa = max(0, defensa_antes - enemigo.defensa)
            dano_vida = max(0, vida_antes - enemigo.vida)
            dano_total = dano_defensa + dano_vida

            print(f"\n{mi_pokemon.nombre} usó ATAQUE NORMAL\n"
                  f"Daño total: {dano_total}\n"
                  f"Defensa reducida: {dano_defensa}\n"
                  f"Vida reducida: {dano_vida}\n")

        elif opcion == "3":
            defensa_enemigo_antes = enemigo.defensa
            vida_enemigo_antes = enemigo.vida

            aplicar_danio_especial(mi_pokemon, enemigo)

            dano_enemigo_defensa = max(0, defensa_enemigo_antes - enemigo.defensa)
            dano_enemigo_vida = max(0, vida_enemigo_antes - enemigo.vida)
            dano_enemigo_total = dano_enemigo_defensa + dano_enemigo_vida

            print(f"\n{mi_pokemon.nombre} usó {mi_pokemon.ataque_especial}\n"
                  f"Daño total: {dano_enemigo_total}\n"
                  f"Defensa reducida: {dano_enemigo_defensa}\n"
                  f"Vida reducida: {dano_enemigo_vida}")
                

        elif opcion == "4":
            print(f"\n{mi_pokemon.nombre} huyó del combate")
            return

        if enemigo.vida <= 0:
            print(f"\n{enemigo.nombre} fue derrotado\n"
                  f"¿Desea capturar al pokemon {enemigo.nombre}?\n"
                  f"[1] Sí\n"
                  f"[2] No\n")

            decision = input("Elige: ")

            if decision == "2":
                print(f"\n{enemigo.nombre} se fue del combate")
                return

            elif decision == "1":
                print(f"\nCapturando...")

                if random.choice([True, False]):
                    enemigo.atrapado = True
                    atrapados.append(enemigo)
                    print(f"\n{enemigo.nombre} fue atrapado.\n")

                    input(" Presiona [ENTER] para regresar al menú.")
                else:
                    print(f"\nEl pokemon {enemigo.nombre} no pudo ser capturado y escapó.\n")

                    input("Presiona [ENTER] para regresar al menú.")
                return

        accion = random.choice(["pasar", "normal", "especial", "huir"])

        if accion == "pasar":
            print(f"\n{enemigo.nombre} decidió pasar turno")

        elif accion == "normal":
            defensa_antes = mi_pokemon.defensa
            vida_antes = mi_pokemon.vida

            aplicar_danio(enemigo, mi_pokemon)

            dano_defensa = max(0, defensa_antes - mi_pokemon.defensa)
            dano_vida = max(0, vida_antes - mi_pokemon.vida)
            dano_total = dano_defensa + dano_vida

            print(f"\n{enemigo.nombre} usó ATAQUE NORMAL\n"
                  f"Daño total: {dano_total}\n"
                  f"Defensa reducida: {dano_defensa}\n"
                  f"Vida reducida: {dano_vida}")

        elif accion == "especial":
            defensa_antes = mi_pokemon.defensa
            vida_antes = mi_pokemon.vida

            aplicar_danio_especial(enemigo, mi_pokemon)

            dano_defensa = max(0, defensa_antes - mi_pokemon.defensa)
            dano_vida = max(0, vida_antes - mi_pokemon.vida)
            dano_total = dano_defensa + dano_vida

            print(f"\n{enemigo.nombre} usó {enemigo.ataque_especial}\n"
                  f"Daño total: {dano_total}\n"
                  f"Defensa reducida: {dano_defensa}\n"
                  f"Vida reducida: {dano_vida}")

        elif accion == "huir":
            print(f"\n{enemigo.nombre} huyó del combate\n")
            return

        if mi_pokemon.vida <= 0:
            print(f"\n{mi_pokemon.nombre} ha sido derrotado\n")

            input(" Presiona [ENTER] para regresar al menú.")
            return


def verPokemonsAtrapados(lista, principal):
    print("\nPOKEMONES DISPONIBLES\n")
    principal.detallesPokemon()

    for p in lista:
        p.detallesPokemon()


def crear_enemigo():
    print(
        "===== Elige su tipo =====\n"
        "[1] Agua\n"
        "[2] Fuego\n"
        "[3] Electrico\n"
        "[4] Hierba\n"
    )

    tipo = input("Tipo: ")
    nombre = input("Nombre: ")

    if tipo == "1":
        p = PokemonAgua(nombre)
    elif tipo == "2":
        p = PokemonFuego(nombre)
    elif tipo == "3":
        p = PokemonElectrico(nombre)
    else:
        p = PokemonHierba(nombre)

    p.ataque = int(input("Ataque: "))
    p.defensa = int(input("Defensa: "))
    p.vida = int(input("Vida: "))

    return p


print(
    "\n¡BIENVENIDO A LA POKEDEX!\n"
    "\n===== Elige tu Pokémon inicial =====\n"
    "[1] Squirtle    |   (Agua)\n"
    "[2] Charmander  |   (Fuego)\n"
    "[3] Pichu       |   (Electrico)\n"
    "[4] Bulbasaur   |   (Hierba)\n"
)

op = input("Opción: ")
print()


if op == "1":
    pokemon_principal = PokemonAgua("Squirtle")
elif op == "2":
    pokemon_principal = PokemonFuego("Charmander")
elif op == "3":
    pokemon_principal = PokemonElectrico("Pichu")
else:
    pokemon_principal = PokemonHierba("Bulbasaur")

enemigos = [
    PokemonFuego("Charmander"),
    PokemonAgua("Magikarp"),
    PokemonElectrico("Pichu"),
    PokemonHierba("Bulbasaur"),
]

pokemones_atrapados = []

while True:
    limpiarPantalla()
    print(
        "===== SELECCIONE UNA OPCION =====\n"
        "1. Detalles de mi Pokémon\n"
        "2. Hablar Pokémon\n"
        "3. Entrenamiento\n"
        "4. Combatir\n"
        "5. Ver Pokémon Atrapados\n"
        "6. Crear Pokémon Enemigo\n"
        "7. Salir\n"
    )
    opcion = input("Elige: ")

    if opcion == "1":
        limpiarPantalla()
        pokemon_principal.detallesPokemon()

        input("Presiona [ENTER] para regresar.")

    elif opcion == "2":
        pokemon_principal.hablar()

        input("Presiona [ENTER] para regresar.")

    elif opcion == "3":
        limpiarPantalla()
        pokemon_principal.entrenar()

    elif opcion == "4":
        limpiarPantalla()
        combate(pokemon_principal, enemigos, pokemones_atrapados)

    elif opcion == "5":
        verPokemonsAtrapados(pokemones_atrapados, pokemon_principal)

    elif opcion == "6":
        enemigos.append(crear_enemigo())

    elif opcion == "7":
        print("\nCargando", end="")
        puntosCarga()
        break
