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
        self.nivel = 0

    def hablar(self):
        print(f"¡{self.nombre}!")

    def actualizar(self):
        if self.nivel >= 100 and self.evolucion < 3:
            self.evolucion += 1
            self.nivel = 0

            if self.evolucion == 2:
                self.nombre = "Pikachu"
            
            elif self.evolucion == 3:
                self.nombre = "Raichu"
            print(f" ¡El Pokémon ha evolucionado! Ahora es: {self.nombre}")

    def detallesPokemon(self):
        print(f" Nombre: {self.nombre}")
        print(f" Descripción: {self.descripcion}")
        print(f" Ataque: {self.ataque}")
        print(f" Defensa: {self.defensa}")
        print(f" Vida: {self.vida}")
        print(f" Nivel: {self.nivel}")
        print(f" Evolución: {self.evolucion}")
        print(f" Atrapado: {self.atrapado}")
    
    def entrenar(self):
        while True:
            print(" ===== Elige un entrenamiento =====")
            print(" [1] Entrenamiento Normal")
            print(" [2] Entrenamiento Individual")
            print(" [3] Entrenamiento Intensivo")
            print(" [4] Entrenamiento Personalizado")
            print(" [5] Regresar al menú.")
            opcion = int(input(" -> "))
            print(" ===================================\n")

            if opcion == 1:
                print(" ===== Registro de stats =====")
                print(f" Ataque: {self.ataque}")
                print(f" Defensa: {self.defensa}")
                print(f" Vida: {self.vida}")
                print(f" Nivel: [{self.nivel}/100]")
                print(" ==============================\n")

                self.ataque += 10
                self.defensa += 10
                self.nivel += 10
                print(f" ===== Tu pokemon a incrementado su [Ataque {self.ataque}+], [Defensa {self.defensa}+], y [Nivel {self.nivel}/100] =====\n")
            
            elif opcion == 2:
                print(" ===== Elige un atributo =====")
                print(" [1] Subir ataque")
                print(" [2] Subir defensa")
                print(" [3] Subir vida")
                eleccion_atributo = int(input(" -> "))
                print(" ==============================")

                print(" ===== Registro de stats =====")
                print(f" Ataque: {self.ataque}")
                print(f" Defensa: {self.defensa}")
                print(f" Vida: {self.vida}")
                print(f" Nivel: [{self.nivel}/100]")
                print(" ==============================\n")

                if eleccion_atributo == 1:
                    self.ataque += 10
                    print(f" ===== Tu pokemon a incrementado su ataque a [{self.ataque}] =====\n")
                
                elif eleccion_atributo == 2:
                    self.defensa += 10
                    print(f" ===== Tu pokémon a incrementado su defensa a [{self.defensa}] =====\n")

                elif eleccion_atributo == 3:
                    self.vida += 10
                    print(f" ===== Tu pokémon a incrementado su vida a [{self.vida}] =====\n")

            elif opcion == 3:
                print(" ===== Registro de stats =====")
                print(f" Ataque: {self.ataque}")
                print(f" Defensa: {self.defensa}")
                print(f" Vida: {self.vida}")
                print(f" Nivel: [{self.nivel}/100]")
                print(" ==============================\n")

                self.subirAtaque()
                self.subirDefensa()
                self.subirVida()
                print(f" ===== Tu pokemon a incrementado su [Ataque {self.ataque}+], [Defensa {self.defensa}+], y [Vida {self.vida}+] =====\n")

            elif opcion == 4:
                while True:
                    print(" ====== Elige un atributo ======")
                    print(" [1] Subir ataque")
                    print(" [2] Subir defensa")
                    print(" [3] Subir vida")
                    print(" [4] Subir nivel")
                    print(" [5] Regresar al menú.")
                    eleccion_atributo = int(input(" -> "))
                    print(" ================================\n")

                    if eleccion_atributo == 1:
                        ataque_personalizado = int(input(" Ingresa su ataque [1/1000]: "))
                        self.ataque += ataque_personalizado
                        print(f" ===== ¡Felicidades! Ahora tu pokémon cuenta con un ataque de [{self.ataque}] =====\n")

                        input(" Presiona [Enter] para regresar al menú de elección de atributos.")
                    
                    elif eleccion_atributo == 2:
                        defensa_personalizada = int(input(" Ingresa su defensa [1/1000]: "))
                        self.defensa += defensa_personalizada
                        print(f" ===== ¡Felicidades! Ahora tu pokémon cuenta con una defensa de [{self.defensa}] =====\n")

                        input(" Presiona [Enter] para regresar al menú de elección de atributos.")
                    
                    elif eleccion_atributo == 3:
                        vida_personalizada = int(input(" Ingresa su vida [1/1000]: "))
                        self.vida += vida_personalizada
                        print(f" ===== ¡Felicidades! Ahora tu pokémon cuenta con una vida de [{self.vida}] =====\n")

                        input(" Presiona [Enter] para regresar al menú de elección de atributos.")
                    
                    elif eleccion_atributo == 4:
                        nivel_personalizado = int(input(" Ingresa su nivel [1/100]: "))
                        self.nivel += nivel_personalizado
                        print(f" ===== ¡Felicidades! Ahora tu pokémon cuenta con un nivel de [{self.nivel}] =====\n")

                        input(" Presiona [Enter] para regresar al menú de elección de atributos.")
                    
                    elif eleccion_atributo == 5:
                        print(" Regresando al menu...\n")
                        break

            elif opcion == 5:
                print(" Regresando al menu principal...\n")
                break
    
    def subirAtaque(self):
        boost_ataque = 20
        self.ataque += boost_ataque

    def subirDefensa(self):
        boost_defensa = 20
        self.defensa += boost_defensa
    
    def subirVida(self):
        boost_vida = 20
        self.vida += boost_vida

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

class PokemonConEntrenamiento(Pokemon, Entrenamiento):
    def hablar(self):
        return Pokemon.hablar()

    def actualizar(self):
        return Pokemon.actualizar()

    def detallesPokemon(self):
        return Pokemon.detallesPokemon()
    
    def entrenar(self):
        return Pokemon.entrenar()

    def subirAtaque(self):
        return Pokemon.subirAtaque()

    def subirDefensa(self):
        return Pokemon.subirDefensa()

    def subirVida(self):
        return Pokemon.subirVida()

class PokemonAgua(PokemonConEntrenamiento, Pokemon):
    def __init__(self):
        self.ataque_especial = "Hidrobomba"
    
    def actualizar(self):
        return PokemonConEntrenamiento.actualizar()

class PokemonFuego(Pokemon):
    def __init__(self):
        self.ataque_especial = "Lanzallamas"
    
    def actualizar(self):
        return PokemonConEntrenamiento.actualizar()
    
class PokemonElectrico(Pokemon):
    def __init__(self):
        self.ataque_especial = "Impactrueno"
    
    def actualizar(self):
        return PokemonConEntrenamiento.actualizar()

class PokemonHierba(Pokemon):
    def __init__(self):
        self.ataque_especial = "Látigo Cepa"
    
    def actualizar(self):
        return PokemonConEntrenamiento.actualizar()

lista_pokemon_enemigos = []

pokemon_enemigo1 = PokemonAgua("...")
lista_pokemon_enemigos.append(pokemon_enemigo1)

pokemon_enemigo2 = PokemonHierba("...")
lista_pokemon_enemigos.append(pokemon_enemigo2)

pokemon_enemigo3 = PokemonFuego("...")
lista_pokemon_enemigos.append(pokemon_enemigo3)

pokemon_enemigo4 = PokemonElectrico("...")
lista_pokemon_enemigos.append(pokemon_enemigo4)

def PokemonEnemigoPersonalizado():
    print(" ===== Elige su tipo =====")
    print(" [1] Agua")
    print(" [2] Fuego")
    print(" [3] Electrico")
    print(" [4] Hierba")
    eleccion_tipo = int(input(" -> "))
    print(" =========================\n")

    if eleccion_tipo == 1:
        pokemon_enemigo = PokemonAgua("...")
        lista_pokemon_enemigos.append(pokemon_enemigo)
    
    elif eleccion_tipo == 2:
        pokemon_enemigo = PokemonFuego("...")
        lista_pokemon_enemigos.append(pokemon_enemigo)
    
    elif eleccion_tipo == 3:
        pokemon_enemigo = PokemonElectrico("...")
        lista_pokemon_enemigos.append(pokemon_enemigo)
    
    elif eleccion_tipo == 4:
        pokemon_enemigo = PokemonHierba("...")
        lista_pokemon_enemigos.append(pokemon_enemigo)

