from abc import ABC, abstractmethod
import random

class PokemonBase(ABC):
    def __init__(self):
        self.nombre = "Sin Pokémon"
        self.descripcion = "No descripción"
        self.ataque = 0
        self.defensa = 0
        self.vida = 0
        self.nivel = 1
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
        self.ataque = 30
        self.defensa = 30
        self.vida = 30

    def hablar(self):
        print(f"\n{self.nombre}!")

    def actualizar(self):
        self.ataque += 20
        self.defensa += 20
        self.vida += 20

    def detallesPokemon(self):
        print(f"\nDETALLES DEL POKEMON.\n"
              f"Nombre: {self.nombre}\n"
              f"Descripción: {self.descripcion}\n"
              f"Ataque: {self.ataque}\n"
              f"Defensa: {self.defensa}\n"
              f"Vida: {self.vida}\n"
              f"Nivel: {self.nivel}\n"
              f"Evolución: {self.evolucion}\n"
              f"Atrapado: {self.atrapado}\n")

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.vida += 10
        self.nivel += 10
        if self.nivel >= 100 and self.evolucion < 3:
            self.evolucion += 1
            self.nivel = 0
            if self.evolucion == 2:
                self.nombre = "Pikachu"
            elif self.evolucion == 3:
                self.nombre = "Raichu"
            print(f"\nEl Pokémon ha evolucionado\nAhora es: {self.nombre}")

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
        self.ataque += 15
        self.defensa += 10
        self.vida += 10


class PokemonFuego(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Fuego")
        self.ataque_especial = "Lanzallamas"

    def actualizar(self):
        self.ataque += 20
        self.defensa += 5
        self.vida += 10


class PokemonElectrico(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Eléctrico")
        self.ataque_especial = "Impactrueno"

    def actualizar(self):
        self.ataque += 18
        self.defensa += 8
        self.vida += 10


class PokemonHierba(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Hierba")
        self.ataque_especial = "Látigo Cepa"

    def actualizar(self):
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


def combate(mi_pokemon, enemigos, atrapados):
    enemigo = random.choice(enemigos)

    print(f"\nCombate iniciado contra {enemigo.nombre}")

    while mi_pokemon.vida > 0 and enemigo.vida > 0:
        print(f"\nTu Pokémon: {mi_pokemon.nombre} | ATK:{mi_pokemon.ataque} DEF:{mi_pokemon.defensa} VIDA:{mi_pokemon.vida}\n"
              f"Enemigo: {enemigo.nombre} | ATK:{enemigo.ataque} DEF:{enemigo.defensa} VIDA:{enemigo.vida}\n"
              f"\n1. Pasar turno\n2. Ataque normal\n3. Ataque especial\n4. Huir")

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
                  f"Vida reducida: {dano_vida}")

        elif opcion == "3":
            dano = 30
            enemigo.vida = max(0, enemigo.vida - dano)

            print(f"\n{mi_pokemon.nombre} usó {mi_pokemon.ataque_especial}\n"
                  f"Daño total: {dano}")

        elif opcion == "4":
            print(f"\n{mi_pokemon.nombre} huyó del combate")
            return

        if enemigo.vida <= 0:
            print(f"\n{enemigo.nombre} fue derrotado\n"
                  f"¿Desea capturar al pokemon {enemigo.nombre}?\n"
                  f"[1] Sí\n"
                  f"[2] No")

            decision = input("Elige: ")

            if decision == "2":
                print(f"\n{enemigo.nombre} se fue del combate")
                return

            elif decision == "1":
                print(f"\nCapturando...")

                if random.choice([True, False]):
                    enemigo.atrapado = True
                    atrapados.append(enemigo)
                    print(f"\n{enemigo.nombre} fue atrapado")
                else:
                    print(f"\nEl pokemon {enemigo.nombre} no pudo ser capturado y escapó")
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
            dano = 25
            mi_pokemon.vida = max(0, mi_pokemon.vida - dano)

            print(f"\n{enemigo.nombre} usó {enemigo.ataque_especial}\n"
                  f"Daño total: {dano}")

        elif accion == "huir":
            print(f"\n{enemigo.nombre} huyó del combate")
            return

        if mi_pokemon.vida <= 0:
            print(f"\n{mi_pokemon.nombre} ha sido derrotado")
            return


def verPokemonsAtrapados(lista, principal):
    print(f"\nPOKEMONES DISPONIBLES\n")
    principal.detallesPokemon()
    for p in lista:
        p.detallesPokemon()


def menu_entrenamiento(pokemon):
    while True:
        print(f"\nTIPOS DE ENTRENAMIENTO\n"
              f"[1] Entrenamiento Normal\n"
              f"[2] Entrenamiento Individual\n"
              f"[3] Entrenamiento Intensivo\n"
              f"[4] Entrenamiento Personalizado\n"
              f"[5] Volver")

        op = input("Elige: ")

        if op == "1":
            pokemon.entrenar()
        elif op == "2":
            print(f"\nELIGE EL STAT A INCREMENTAR.\n"
                  f"[1] Ataque\n"
                  f"[2] Defensa\n"
                  f"[3] Vida\n")
            sub = input("Elige: ")
            if sub == "1":
                pokemon.subirAtaque()
            elif sub == "2":
                pokemon.subirDefensa()
            elif sub == "3":
                pokemon.subirVida()
        elif op == "3":
            pokemon.actualizar()
        elif op == "4":
            pokemon.ataque = int(input("Ataque: "))
            pokemon.defensa = int(input("Defensa: "))
            pokemon.vida = int(input("Vida: "))
        elif op == "5":
            break

        print(f"{pokemon.detallesPokemon()}")


def crear_enemigo():
    print(f"\n[1] Agua\n"
          f"[2] Fuego\n"
          f"[3] Electrico\n"
          f"[4] Hierba\n")
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


print(f"\nBIENVENIDO A LA POKEDEX\n"
      f"\nElige tu Pokémon inicial\n"
      f"[1] Agua (Squirtle)\n"
      f"[2] Fuego (Charmander)\n"
      f"[3] Electrico (Pichu)\n"
      f"[4] Hierba (Bulbasaur)\n")
op = input("Opción: ")

if op == "1":
    pokemon_principal = PokemonAgua("Squirtle")
elif op == "2":
    pokemon_principal = PokemonFuego("Charmander")
elif op == "3":
    pokemon_principal = PokemonElectrico("Pichu")
else:
    pokemon_principal = PokemonHierba("Bulbasaur")

pokemon_principal.detallesPokemon()

enemigos = [
    PokemonFuego("Charmander"),
    PokemonAgua("Magikarp"),
    PokemonElectrico("Pichu"),
    PokemonHierba("Bulbasaur")
]

pokemones_atrapados = []

while True:
    print(f"\nSELECCIONE UNA OPCION A PROCEDER.\n"
          f"1. Detalles de mi Pokémon\n"
          f"2. Hablar Pokémon\n"
          f"3. Entrenamiento\n"
          f"4. Combatir\n"
          f"5. Ver Pokémon Atrapados\n"
          f"6. Crear Pokémon Enemigo\n"
          f"7. Salir\n")

    opcion = input("Elige: ")

    if opcion == "1":
        pokemon_principal.detallesPokemon()
    elif opcion == "2":
        pokemon_principal.hablar()
    elif opcion == "3":
        menu_entrenamiento(pokemon_principal)
    elif opcion == "4":
        combate(pokemon_principal, enemigos, pokemones_atrapados)
    elif opcion == "5":
        verPokemonsAtrapados(pokemones_atrapados, pokemon_principal)
    elif opcion == "6":
        enemigos.append(crear_enemigo())
    elif opcion == "7":
        break
