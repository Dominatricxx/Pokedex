from abc import ABC, abstractmethod
import random
from datetime import datetime
import glob
import os
import sqlite3  # Base de datos integrada
import time

lineas_evolutivas = [
    ["Squirtle", "Wartortle", "Blastoise"],
    ["Charmander", "Charmeleon", "Charizard"],
    ["Pichu", "Pikachu", "Raichu"],
    ["Bulbasaur", "Ivysaur", "Venusaur"]
]

def puntosCarga():
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n\nGAME OVER\n")

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
        self.ataque = 0
        self.defensa = 0
        self.vida = 50
        self.nivel = 1
        self.evolucion = 1
        self.atrapado = True

    def limitar_stats(self):
        self.ataque = min(self.ataque, 1000)
        self.defensa = min(self.defensa, 1000)
        self.vida = min(self.vida, 1000)
        self.nivel = min(self.nivel, 100)

    def hablar(self):
        print(f"\n{self.nombre} dice: ¡¡{self.nombre}!!\n")

    def actualizar(self):
        self.limitar_stats()
        for linea in lineas_evolutivas:
            if self.nombre in linea:
                indice = linea.index(self.nombre)
                if self.nivel >= 100 and indice < len(linea) - 1:
                    self.nombre = linea[indice + 1]
                    self.evolucion += 1
                    self.nivel = 1
                    print(f"\n¡El Pokémon ha evolucionado! Ahora es: {self.nombre}\n")

                elif self.nivel == 100 and indice == len(linea) - 1:
                    print(f"\n¡{self.nombre} ha alcanzado su máximo nivel!\n")
                break

    def detallesPokemon(self):
        print(
            f"\n===== DETALLES DEL POKEMON =====\n"
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
            ataque_antes = self.ataque
            defensa_antes = self.defensa
            vida_antes = self.vida
            nivel_antes = self.nivel

            print(
                "\n===== ENTRENAMIENTO =====\n"
                "[1] Entrenamiento Normal\n"
                "[2] Entrenamiento Individual\n"
                "[3] Entrenamiento Intensivo\n"
                "[4] Entrenamiento Personalizado\n"
                "[5] Volver\n"
            )

            try:
                opcion = int(input("Elige: "))

            except ValueError:
                print("\n[ERROR]: El valor ingresado no es valido.")
                continue

            if opcion == 1:
                self.ataque += 10
                self.defensa += 10

                if self.nivel == 100:
                    self.nivel = self.nivel
                else:
                    self.nivel += 10

            elif opcion == 2:
                while True:
                    print(
                        "\n[1] Subir ataque\n"
                        "[2] Subir defensa\n"
                        "[3] Subir vida\n"
                    )

                    try:
                        eleccion = int(input("Elige: "))

                    except ValueError:
                        print("\n[ERROR]: El valor ingresado no es valido.")
                        continue

                    if eleccion == 1:
                        self.ataque += 10

                    elif eleccion == 2:
                        self.defensa += 10

                    elif eleccion == 3:
                        self.vida += 10
                    break


            elif opcion == 3:

                self.subirAtaque()
                self.subirDefensa()
                self.subirVida()


            elif opcion == 4:

                while True:
                    print(
                        "\n===== Elige un atributo =====\n"
                        "[1] Subir ataque\n"
                        "[2] Subir defensa\n"
                        "[3] Subir vida\n"
                        "[4] Subir nivel\n"
                        "[5] Volver\n"
                    )

                    
                    try:
                        eleccion = int(input("Elige: "))
                            
                    except ValueError:
                        print("\n[ERROR]: La opción ingresada no es valida.")

                    if eleccion == 1:
                        try:
                            self.ataque += int(input("\nIngresa el número de ataque [0/1000]: "))

                        except ValueError:
                            print("\n[ERROR]: El valor ingresado no es valido.")
                            continue

                        else:
                            print("\n[AVISO]: El ataque de tu pokemon sido incrementado exitosamente.")

                    elif eleccion == 2:
                        try:
                            self.defensa += int(input("\nIngresa el número de defensa [0/1000]: "))

                        except ValueError:
                            print("\n[ERROR]: El valor ingresado no es valido.")
                            continue

                        else:
                            print("\n[AVISO]: La defensa de tu pokemon sido incrementada exitosamente.")

                    elif eleccion == 3:
                        try:
                            self.vida += int(input("\nIngresa el número de vida [0/1000]: "))
                        
                        except ValueError:
                            print("\n[ERROR]: El valor ingresado no es valido.")
                            continue
                        
                        else:
                            print("\n[AVISO]: La vida de tu pokemon sido incrementada exitosamente.")

                    elif eleccion == 4:
                        try:
                            self.nivel += int(input("\nIngresa el nivel [1/100]: "))

                        except ValueError:
                            print("\n[ERROR]: El valor ingresado no es valido.")
                            continue

                        else:
                            print("\n[AVISO]: El nivel de tu pokemon a sido incrementado exitosamente.")

                    elif eleccion == 5:
                        break


            elif opcion == 5:
                break

            self.limitar_stats()
            self.actualizar()

            print("\n===== RESULTADOS DEL ENTRENAMIENTO =====")

            if self.ataque != ataque_antes and ataque_antes != 0:
                print(f"Ataque: {ataque_antes} → {self.ataque} (+{self.ataque - ataque_antes})")

            elif self.ataque != ataque_antes and ataque_antes == 0:
                print(f"Ataque: {ataque_antes} → {self.ataque} (+{self.ataque})")

            else:
                print(f"Ataque: {ataque_antes} → {self.ataque} (+0)")

            if self.defensa != defensa_antes and defensa_antes != 0:
                print(f"Defensa: {defensa_antes} → {self.defensa} (+{self.defensa - defensa_antes})")

            elif self.defensa != defensa_antes and defensa_antes == 0:
                print(f"Defensa: {defensa_antes} → {self.defensa} (+{self.defensa})")

            else:
                print(f"Defensa: {defensa_antes} → {self.defensa} (+0)")

            if self.vida != vida_antes and vida_antes != 0:
                print(f"Vida: {vida_antes} → {self.vida} (+{self.vida - vida_antes})")

            elif self.vida != vida_antes and vida_antes == 0:
                print(f"Vida: {vida_antes} → {self.vida} (+{self.vida})")

            else:
                print(f"Vida: {vida_antes} → {self.vida} (+0)")

            if self.nivel != nivel_antes and nivel_antes != 0:
                print(f"Nivel: {nivel_antes} → {self.nivel} (+{self.nivel - nivel_antes})")

            elif self.nivel != nivel_antes and nivel_antes == 0:
                print(f"Nivel: {nivel_antes} → {self.nivel} (+{self.nivel})")

            elif self.nivel == nivel_antes:
                print(f"Nivel: {nivel_antes} → {self.nivel} (+0)")

            else:
                print(f"Nivel: {nivel_antes} → {self.nivel} (+{self.nivel})")

            print("========================================\n")
            input("Presiona [ENTER] para regresar al menú de entrenamientos.")
            self.detallesPokemon()

    def subirAtaque(self):
        self.ataque += 20
        self.limitar_stats()

    def subirDefensa(self):
        self.defensa += 20
        self.limitar_stats()

    def subirVida(self):
        self.vida += 20
        self.limitar_stats()


class PokemonConEntrenamiento(Pokemon, Entrenamiento):
    pass


class PokemonAgua(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Agua")
        self.ataque_especial = "Hidrobomba"
        self.ataque = 20
        self.defensa = 30
        self.vida = 35

    def actualizar(self):
        super().actualizar()

        if self.nivel >= 100 and self.evolucion < 3:
            self.ataque += 15
            self.defensa += 10
            self.vida += 10

        super().actualizar()


class PokemonFuego(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Fuego")
        self.ataque_especial = "Lanzallamas"
        self.ataque = 45
        self.defensa = 60
        self.vida = 50

    def actualizar(self):
        if self.nivel >= 100 and self.evolucion < 3:
            self.ataque += 20
            self.defensa += 5
            self.vida += 10

        super().actualizar()


class PokemonElectrico(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Eléctrico")
        self.ataque_especial = "Impactrueno"
        self.ataque = 40
        self.defensa = 50
        self.vida = 70

    def actualizar(self):
        if self.nivel >= 100 and self.evolucion < 3:
            self.ataque += 18
            self.defensa += 8
            self.vida += 10

        super().actualizar()


class PokemonHierba(PokemonConEntrenamiento):
    def __init__(self, nombre):
        super().__init__(nombre, "Tipo Hierba")
        self.ataque_especial = "Látigo Cepa"
        self.ataque = 24
        self.defensa = 32
        self.vida = 44

    def actualizar(self):
        if self.nivel >= 100 and self.evolucion < 3:
            self.ataque += 10
            self.defensa += 15
            self.vida += 15

        super().actualizar()


def aplicar_danio(atacante, defensor):
    dano = atacante.ataque

    dano_defensa = min(defensor.defensa, dano)
    defensor.defensa -= dano_defensa

    dano_vida = dano - dano_defensa
    defensor.vida = max(0, defensor.vida - dano_vida)


def aplicar_danio_especial(atacante, defensor):
    dano = atacante.ataque * 2

    dano_defensa = min(defensor.defensa, dano)
    defensor.defensa -= dano_defensa

    dano_vida = dano - dano_defensa
    defensor.vida = max(0, defensor.vida - dano_vida)

def combate(mi_pokemon, enemigos, atrapados, nombre_usuario, rivales):
    
    tiempo_combate = datetime.now()
    nombre_archivo = f"Batalla_{tiempo_combate.strftime('%d-%m-%Y')}_{tiempo_combate.strftime('%H-%M-%S')}.txt"
    Fecha_combate = tiempo_combate.strftime("%d-%m-%Y %H:%M:%S")

    try:
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            usuario = f"\n{nombre_usuario}: ¡{mi_pokemon.nombre} yo te elijo!\n"
            print(usuario)
            archivo.write(usuario)

            enemigo = random.choice(enemigos)
            rival = random.choice(rivales)

            defensa_enemigo_antes = enemigo.defensa
            vida_enemigo_antes = enemigo.vida
            vida_antes = mi_pokemon.vida
            defensa_antes = mi_pokemon.defensa

            
            entrenador_enemigo = (
                "\n===== COMBATE POKEMON =====\n"
                f"Entrenador rival [{rival}]: ¡{enemigo.nombre}, adelante!\n"
                f"Combate iniciado contra {enemigo.nombre}\n"
            )

            print(entrenador_enemigo)
            archivo.write(entrenador_enemigo)

            contador_turnos = 0

            while mi_pokemon.vida > 0 and enemigo.vida > 0:
                defensa_enemigo_turno = enemigo.defensa
                vida_enemigo_turno = enemigo.vida
                defensa_mi_turno = mi_pokemon.defensa
                vida_mi_turno = mi_pokemon.vida

                contador_turnos += 1

                turno = (
                    f"\n===== TURNO {contador_turnos} =====\n"
                    f"Tu Pokémon: {mi_pokemon.nombre} | ATK:{mi_pokemon.ataque} DEF:{mi_pokemon.defensa} VIDA:{mi_pokemon.vida}\n"
                    f"Enemigo: {enemigo.nombre} | ATK:{enemigo.ataque} DEF:{enemigo.defensa} VIDA:{enemigo.vida}\n"
                )

                habilidades = (
                    "\n===== Habilidades =====\n"
                    "1. Pasar turno\n"
                    "2. Ataque normal\n"
                    "3. Ataque especial\n"
                    "4. Huir\n"
                    "=======================\n"
                )

                print(turno)
                print(habilidades)

                archivo.write(turno)
                archivo.write(habilidades)

                try:
                    opcion = int(input("Elige: "))
                    archivo.write(f"Elige: {opcion}\n")

                except ValueError:
                    print("\n[ERROR]: El valor ingresado no es valido.")
                    continue
                
                accion_valida = False

                if opcion == 1:
                    pasar_turno = f"\n{mi_pokemon.nombre} decidió pasar turno.\n"
                    print(pasar_turno)
                    archivo.write(pasar_turno)
                    accion_valida = True

                elif opcion == 2:

                    aplicar_danio(mi_pokemon, enemigo)

                    dano_defensa = defensa_enemigo_turno - enemigo.defensa
                    dano_vida = vida_enemigo_turno - enemigo.vida
                    dano_total = dano_defensa + dano_vida

                    ataque_normal = (
                        f"\n{mi_pokemon.nombre} usó ATAQUE NORMAL.\n"
                        f"Daño total: {dano_total}\n"
                        f"Defensa reducida: {dano_defensa}\n"
                        f"Vida reducida: {dano_vida}\n")
                    
                    print(ataque_normal)
                    archivo.write(ataque_normal)
                    accion_valida = True

                elif opcion == 3:
                    aplicar_danio_especial(mi_pokemon, enemigo)

                    dano_defensa = defensa_enemigo_turno - enemigo.defensa
                    dano_vida = vida_enemigo_turno - enemigo.vida
                    dano_total = dano_defensa + dano_vida

                    ataque_especial = (
                        f"\n{mi_pokemon.nombre} usó {mi_pokemon.ataque_especial}\n"
                        f"Daño total: {dano_total}\n"
                        f"Defensa reducida: {dano_defensa}\n"
                        f"Vida reducida: {dano_vida}\n"
                    )
                    
                    print(ataque_especial)
                    archivo.write(ataque_especial)
                    accion_valida = True

                elif opcion == 4:
                    huir_del_combate = (
                        f"\n{mi_pokemon.nombre} huyó del combate\n"
                        f"Fecha y hora del combate: {Fecha_combate}\n")
                    
                    print(huir_del_combate)
                    archivo.write(huir_del_combate)
                    accion_valida = True

                    enemigo.defensa = defensa_enemigo_antes
                    enemigo.vida = vida_enemigo_antes
                    mi_pokemon.defensa = defensa_antes
                    mi_pokemon.vida = vida_antes

                    input("Presiona [ENTER] para regresar al menú.")
                    return

                else:
                    print("\n[ERROR]: La opción elegida no es valida.")
                    continue

                if enemigo.vida <= 0:
                    enemigo_derrotado = (
                        f"\n{enemigo.nombre} fue derrotado.\n"
                        f"Fecha y hora del combate: {Fecha_combate}\n")
                    
                    print(enemigo_derrotado)
                    archivo.write(enemigo_derrotado)

                    enemigo.defensa = defensa_enemigo_antes
                    enemigo.vida = vida_enemigo_antes
                    mi_pokemon.defensa = defensa_antes
                    mi_pokemon.vida = vida_antes

                    if mi_pokemon.nivel == 100:
                        nivel_maximo = f"\n===== Tu pokemon ha alcanzado el nivel máximo =====\n"
                        print(nivel_maximo)
                        archivo.write(nivel_maximo)

                    else:
                        mi_pokemon.nivel += 2
                        nivel_aumentado = f"\n===== ¡Felicidades! tu pokemon ha subido al nivel {mi_pokemon.nivel} =====\n"
                        print(nivel_aumentado)
                        archivo.write(nivel_aumentado)

                    while True:
                        decision_texto = (f"\n¿Desea capturar al pokemon {enemigo.nombre}?\n"
                            f"[1] Sí\n"
                            f"[2] No\n")
                        
                        print(decision_texto)
                        archivo.write(decision_texto)

                        try:
                            decision = int(input("Elige: "))
                            archivo.write(f"Elige: {decision}\n")
                        
                        except ValueError:
                            print("\n[ERROR]: La elección elegida no es valida..\n")
                            continue

                        if decision == 2:
                            huir_del_combate = f"\n{enemigo.nombre} se fue del combate.\n"
                            
                            print(huir_del_combate)
                            archivo.write(huir_del_combate)

                            input("Presiona [ENTER] para regresar al menú.")
                            return

                        elif decision == 1:
                            capturar = f"\nCapturando...\n"
                            print(capturar)
                            archivo.write(capturar)

                            if random.choice([True, False]):
                                enemigo.atrapado = True
                                atrapados.append(enemigo)
                                felicitaciones = f"\n¡Felicidades! Haz logrado atrapar a {enemigo.nombre}.\n"
                                print(felicitaciones)
                                archivo.write(felicitaciones)

                                input("Presiona [ENTER] para regresar al menú.")
                            else:
                                hasta_la_proxima = f"\n{enemigo.nombre} no pudo ser capturado y escapó.\n"
                                print(hasta_la_proxima)
                                archivo.write(hasta_la_proxima)

                                input("Presiona [ENTER] para regresar al menú.")
                            return

                        elif decision != 2:
                            print("\n[ERROR]: La elección elegida no es valida.\n")
                            continue
                
                if accion_valida and enemigo.vida > 0:
                    accion = random.choice(["pasar", "normal", "especial", "huir"])

                    if accion == "pasar":
                        enemigo_paso_turno = f"\n{enemigo.nombre} decidió pasar turno.\n"
                        print(enemigo_paso_turno)
                        archivo.write(enemigo_paso_turno)

                    elif accion == "normal":
                        aplicar_danio(enemigo, mi_pokemon)

                        dano_defensa = defensa_mi_turno - mi_pokemon.defensa
                        dano_vida = vida_mi_turno - mi_pokemon.vida
                        dano_total = dano_defensa + dano_vida

                        enemigo_ataque_normal = (
                            f"\n{enemigo.nombre} usó ATAQUE NORMAL.\n"
                            f"Daño total: {dano_total}\n"
                            f"Defensa reducida: {dano_defensa}\n"
                            f"Vida reducida: {dano_vida}\n")
                        
                        print(enemigo_ataque_normal)
                        archivo.write(enemigo_ataque_normal)

                    elif accion == "especial":
                        aplicar_danio_especial(enemigo, mi_pokemon)

                        dano_defensa = defensa_mi_turno - mi_pokemon.defensa
                        dano_vida = vida_mi_turno - mi_pokemon.vida
                        dano_total = dano_defensa + dano_vida

                        enemigo_ataque_especial = (
                            f"\n{enemigo.nombre} usó {enemigo.ataque_especial}.\n"
                            f"Daño total: {dano_total}\n"
                            f"Defensa reducida: {dano_defensa}\n"
                            f"Vida reducida: {dano_vida}\n")
                        
                        print(enemigo_ataque_especial)
                        archivo.write(enemigo_ataque_especial)

                    elif accion == "huir":
                        enemigo_huyo_del_combate = f"\n{enemigo.nombre} huyó del combate\n"

                        print(enemigo_huyo_del_combate)
                        archivo.write(enemigo_huyo_del_combate)

                        enemigo.defensa = defensa_enemigo_antes
                        enemigo.vida = vida_enemigo_antes
                        mi_pokemon.defensa = defensa_antes
                        mi_pokemon.vida = vida_antes

                        input("Presiona [ENTER] para regresar al menú.")
                        return

                    if mi_pokemon.vida <= 0:
                        derrota = (
                            f"\n{mi_pokemon.nombre} ha sido derrotado.\n"
                            f"Fue necesario llevarlo al centro pokemon.\n"
                            "Después de recibir atención, ha vuelto a la normalidad y esta listo para regresar al campo.\n"
                            f"Fecha y hora del combate: {Fecha_combate}\n")
                        
                        print(derrota)
                        archivo.write(derrota)

                        enemigo.defensa = defensa_enemigo_antes
                        enemigo.vida = vida_enemigo_antes
                        mi_pokemon.defensa = defensa_antes
                        mi_pokemon.vida = vida_antes

                        input("Presiona [ENTER] para regresar al menú.")
                        return
    except IOError:
        print("\n[ERROR]: No se pudo escribir en el archivo de registro de batallas.")


def verPokemonsAtrapados(lista, principal):
    print("\nPOKEMONES DISPONIBLES\n")
    principal.detallesPokemon()

    for p in lista:
        p.detallesPokemon()


def crear_enemigo():
    while True:
        print(
            "\n===== Elige su tipo =====\n"
            "[1] Agua\n"
            "[2] Fuego\n"
            "[3] Electrico\n"
            "[4] Hierba\n"
        )

        try:
            tipo = int(input("Tipo: "))
            
        except ValueError:
            print("\n[ERROR]: El tipo elegido no es valido.\n")
            continue

        nombre = input("Nombre: ")

        if tipo == 1:
            p = PokemonAgua(nombre)
            break
        elif tipo == 2:
            p = PokemonFuego(nombre)
            break
        elif tipo == 3:
            p = PokemonElectrico(nombre)
            break
        elif tipo == 4:
            p = PokemonHierba(nombre)
            break
        else:
            print("\n[ERROR]: El tipo elegido no se encuentra disponible en está Pokedex.")
            continue
    
    while True:
        try:
            p.ataque = int(input("Ataque: "))
            break
        except ValueError:
            print("\n[ERROR]: No puedes ingresar un valor de ataque que no sea númerico y entero.\n")
            continue
    
    p.ataque = min(p.ataque, 1000)

    while True:
        try:
            p.defensa = int(input("Defensa: "))
            break
        except ValueError:
            print("\n[ERROR]: No puedes ingresar un valor de ataque que no sea númerico y entero.\n")
            continue

    p.defensa = min(p.defensa, 1000)

    while True:
        try:
            p.vida = int(input("Vida: "))
            break
        except ValueError:
            print("\n[ERROR]: No puedes ingresar un valor de ataque que no sea númerico y entero.\n")
            continue

    p.vida = min(p.vida, 1000)

    return p

def gestionar_batallas(ruta_carpeta="."):
    patron = os.path.join(ruta_carpeta, "Batalla_*.txt")
    
    try:
        archivos_batallas = glob.glob(patron)
    except IOError:
        print("\n[ERROR]: Ocurrió un error al acceder al directorio de archivos.\n")
        return

    if not archivos_batallas:
        print("\n[AVISO]: No se encontraron registros de batallas.\n")
        return
    
    print("\n======= REGISTRO DE BATALLAS =======")
    for indice, archivo in enumerate(archivos_batallas, start=1):
        nombre_archivo = os.path.basename(archivo)
        print(f"[{indice}. {nombre_archivo}]")
    
    try:
        seleccion = int(input("\nIngrese el número de la batalla que deseas abrir: "))

        if 1 <= seleccion <= len(archivos_batallas):
            archivo_elegido = archivos_batallas[seleccion - 1]

            print(f"\n===== Leyendo: {os.path.basename(archivo_elegido)} =====")
            try:
                with open(archivo_elegido, "r", encoding="utf-8") as fichero:
                    contenido = fichero.read()
                    print(contenido)
                print("-" * 30)
            except FileNotFoundError:
                print("\n[ERROR]: El archivo ya no existe en el sistema.")
            except IOError:
                print("\n[ERROR]: No se pudo leer el archivo seleccionado correctamente.")
        
        else:
            print("[AVISO]: El número ingresado está fuera de rango. Inténtalo de nuevo.")
    except ValueError:
        print("[ERROR]: El valor ingresado es inválido.")


# ==========================================================
# SISTEMA DE PERSISTENCIA MULTI-PARTIDA (SQLITE3)
# ==========================================================
def inicializar_base_datos():
    try:
        conexion = sqlite3.connect("pokedex.db")
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS partidas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            entrenador TEXT NOT NULL,
                            fecha_guardado TEXT NOT NULL)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon_actual (
                            partida_id INTEGER PRIMARY KEY,
                            nombre TEXT, tipo TEXT, nivel INTEGER, 
                            vida INTEGER, defensa INTEGER, ataque INTEGER, evolucion INTEGER, descripcion TEXT,
                            FOREIGN KEY(partida_id) REFERENCES partidas(id) ON DELETE CASCADE)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon_atrapados (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            partida_id INTEGER,
                            nombre TEXT, tipo TEXT, nivel INTEGER, vida INTEGER, defensa INTEGER, ataque INTEGER, evolucion INTEGER, descripcion TEXT,
                            FOREIGN KEY(partida_id) REFERENCES partidas(id) ON DELETE CASCADE)''')
        conexion.commit()
        conexion.close()
    except sqlite3.Error as e:
        print(f"\n[ERROR BASE DE DATOS]: {e}")

def obtener_partidas_guardadas():
    try:
        conexion = sqlite3.connect("pokedex.db")
        cursor = conexion.cursor()
        cursor.execute('''SELECT p.id, p.fecha_guardado, p.entrenador, pa.nombre 
                          FROM partidas p JOIN pokemon_actual pa ON p.id = pa.partida_id''')
        partidas = cursor.fetchall()
        conexion.close()
        return partidas
    except sqlite3.Error:
        return []

def guardar_partida_db(nombre_entrenador, pokemon_p, lista_atrapados, p_id=None):
    try:
        conexion = sqlite3.connect("pokedex.db")
        cursor = conexion.cursor()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Si p_id existe, actualizamos la partida actual. Si es None, creamos una nueva.
        if p_id:
            cursor.execute("UPDATE partidas SET fecha_guardado = ? WHERE id = ?", (fecha_actual, p_id))
            partida_id = p_id
        else:
            cursor.execute("INSERT INTO partidas (entrenador, fecha_guardado) VALUES (?, ?)", (nombre_entrenador, fecha_actual))
            partida_id = cursor.lastrowid
        
        tipo_str = "Agua"
        if isinstance(pokemon_p, PokemonFuego): tipo_str = "Fuego"
        elif isinstance(pokemon_p, PokemonElectrico): tipo_str = "Electrico"
        elif isinstance(pokemon_p, PokemonHierba): tipo_str = "Hierba"
        
        cursor.execute('''INSERT OR REPLACE INTO pokemon_actual (partida_id, nombre, tipo, nivel, vida, defensa, ataque, evolucion, descripcion) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (partida_id, pokemon_p.nombre, tipo_str, pokemon_p.nivel, pokemon_p.vida, pokemon_p.defensa, pokemon_p.ataque, pokemon_p.evolucion, pokemon_p.descripcion))
        
        cursor.execute("DELETE FROM pokemon_atrapados WHERE partida_id = ?", (partida_id,))
        for p in lista_atrapados:
            t_cap = "Agua"
            if isinstance(p, PokemonFuego): t_cap = "Fuego"
            elif isinstance(p, PokemonElectrico): t_cap = "Electrico"
            elif isinstance(p, PokemonHierba): t_cap = "Hierba"
            
            cursor.execute('''INSERT INTO pokemon_atrapados (partida_id, nombre, tipo, nivel, vida, defensa, ataque, evolucion, descripcion) 
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (partida_id, p.nombre, t_cap, p.nivel, p.vida, p.defensa, p.ataque, p.evolucion, p.descripcion))
        
        conexion.commit()
        conexion.close()
        return partida_id
    except sqlite3.Error as e:
        print(f"\n[ERROR AL GUARDAR]: {e}")
        return p_id

def cargar_instancia_pokemon(nombre, tipo, nivel, vida, defensa, ataque, evolucion, descripcion):
    if tipo == "Fuego": p = PokemonFuego(nombre)
    elif tipo == "Electrico": p = PokemonElectrico(nombre)
    elif tipo == "Hierba": p = PokemonHierba(nombre)
    else: p = PokemonAgua(nombre)
    
    p.nivel = nivel
    p.vida = vida
    p.defensa = defensa
    p.ataque = ataque
    p.evolucion = evolucion
    p.descripcion = descripcion
    return p

def cargar_partida_db(partida_id):
    try:
        conexion = sqlite3.connect("pokedex.db")
        cursor = conexion.cursor()
        
        cursor.execute("SELECT entrenador FROM partidas WHERE id = ?", (partida_id,))
        entrenador = cursor.fetchone()[0]
        
        cursor.execute("SELECT nombre, tipo, nivel, vida, defensa, ataque, evolucion, descripcion FROM pokemon_actual WHERE partida_id = ?", (partida_id,))
        pa = cursor.fetchone()
        poke_principal = cargar_instancia_pokemon(pa[0], pa[1], pa[2], pa[3], pa[4], pa[5], pa[6], pa[7])
        
        cursor.execute("SELECT nombre, tipo, nivel, vida, defensa, ataque, evolucion, descripcion FROM pokemon_atrapados WHERE partida_id = ?", (partida_id,))
        lista_rows = cursor.fetchall()
        atrapados = []
        for r in lista_rows:
            atrapados.append(cargar_instancia_pokemon(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))
            
        conexion.close()
        return entrenador, poke_principal, atrapados
    except sqlite3.Error as e:
        print(f"\n[ERROR AL CARGAR]: {e}")
        return None, None, []


# ==========================================================
# CONTROL DE EXCEPCIONES PREDEFINIDAS
# ==========================================================
def modulo_pruebas_errores():
    print(
        "\n--- PRUEBAS DE MANEJO DE ERRORES ---\n"
        "[1] Forzar ValueError (Entrada de tipo incorrecto)\n"
        "[2] Forzar IndexError (Acceso fuera de rango en listas)\n"
        "[3] Forzar ZeroDivisionError (División entre cero matemática)\n"
        "[4] Forzar FileNotFoundError (Lectura de archivo inexistente)\n"
    )
    try:
        prueba = int(input("Seleccione el error que desea probar: "))
        if prueba == 1:
            int("NoSoyUnNumero")
        elif prueba == 2:
            lista_vacia = ["Único Elemento"]
            _ = lista_vacia[5]
        elif prueba == 3:
            _ = 50 / 0
        elif prueba == 4:
            with open("archivo_que_no_existe_en_sistema.txt", "r") as f: pass
        else:
            print("\n[AVISO]: Opción de prueba no disponible.")
    except ValueError as e: print(f"\nExcepción Controlada: [ValueError] -> {e}")
    except IndexError as e: print(f"\nExcepción Controlada: [IndexError] -> {e}")
    except ZeroDivisionError as e: print(f"\nExcepción Controlada: [ZeroDivisionError] -> {e}")
    except FileNotFoundError as e: print(f"\nExcepción Controlada: [FileNotFoundError] -> {e}")
    input("\nPresiona [ENTER] para regresar al menú.")


# ==========================================================
# FLUJO INICIAL MEJORADO (CARGAR O CREAR PARTIDA DIRECTAMENTE)
# ==========================================================
inicializar_base_datos()

def inicializar_nuevo_perfil():
    global nombre_usuario, pokemon_principal, pokemones_atrapados, partida_actual_id
    nombre_usuario = input("\nPor favor, ingresa tu nombre de Entrenador: ")
    print(f"\nBienvenido {nombre_usuario}.\n"
          f"Actualmente no tienes ningún Pokémon en tu posesión.\n")
    input("Por favor procede con [ENTER] para seleccionar tu inicial.")
    
    while True:
        print(
            "\n===== Elige tu Pokémon inicial =====\n\n"
            "[1] Squirtle    |   (Agua)\n"
            "[2] Charmander  |   (Fuego)\n"
            "[3] Pichu       |   (Electrico)\n"
            "[4] Bulbasaur   |   (Hierba)\n"
        )
        try:
            op = int(input("Opción: "))
        except ValueError:
            print("\n[ERROR]: La opción elegida es invalida.")
            continue

        if op == 1: pokemon_principal = PokemonAgua("Squirtle"); break
        elif op == 2: pokemon_principal = PokemonFuego("Charmander"); break
        elif op == 3: pokemon_principal = PokemonElectrico("Pichu"); break
        elif op == 4: pokemon_principal = PokemonHierba("Bulbasaur"); break
        else:
            print("\n[ERROR]: El pokemon elegido no se encuentra disponible en está Pokedex.")
            continue
            
    pokemones_atrapados = []
    # Al ser nueva, pasamos p_id=None para que SQL cree un registro fresco y único
    partida_actual_id = None 
    print(f"\n[SISTEMA]: Perfil para '{nombre_usuario}' preparado. Recuerda usar la opción 9 para consolidarlo.")

print("\n===== BIENVENIDO ENTRENADOR =====\n")
partidas_guardadas = obtener_partidas_guardadas()

if not partidas_guardadas:
    print("No se encontraron partidas guardadas en el sistema.")
    print("Creando una nueva partida por defecto...")
    inicializar_nuevo_perfil()
else:
    print("--- PARTIDAS GUARDADAS DETECTADAS ---")
    print("[0] Crear una NUEVA partida desde cero")
    for idx, p in enumerate(partidas_guardadas, 1):
        print(f"[{idx}] Slot {idx}: [Guardado: {p[1]}] Entrenador: {p[2]} – {p[3]}")
    
    while True:
        try:
            sel = int(input("\nElige una ranura de guardado o selecciona 0 para una nueva aventura: "))
            if sel == 0:
                inicializar_nuevo_perfil()
                break
            elif 1 <= sel <= len(partidas_guardadas):
                partida_actual_id = partidas_guardadas[sel - 1][0]
                nombre_usuario, pokemon_principal, pokemones_atrapados = cargar_partida_db(partida_actual_id)
                print(f"\n¡Bienvenido de nuevo Entrenador {nombre_usuario}!")
                break
            else:
                print(f"[ERROR]: Opción fuera de rango.")
        except ValueError:
            print("[ERROR]: Debe ingresar un valor numérico.")

pokemon_principal.detallesPokemon()
input("Presiona [ENTER] para continuar al menú principal...")

enemigos = [
    PokemonFuego("Charmander"),
    PokemonAgua("Squirtle"),
    PokemonElectrico("Pichu"),
    PokemonHierba("Bulbasaur"),
]

while True:
    print(
        "\n===== SELECCIONE UNA OPCION =====\n"
        "1. Detalles de mi Pokémon\n"
        "2. Hablar Pokémon\n"
        "3. Entrenamiento\n"
        "4. Combatir\n"
        "5. Ver Pokémon Atrapados\n"
        "6. Crear Pokémon Enemigo\n"
        "7. Pruebas de Manejo de Errores\n"
        "8. Registros de Batallas\n"
        "9. Guardar Partida\n"
        "10. Salir\n"
    )

    try:
        opcion = int(input("Elige: "))
    except ValueError:
        print("\n[ERROR]: La opción ingresada es invalida. Por favor intenté de nuevo.")
        continue

    if opcion == 1:
        pokemon_principal.detallesPokemon()
        input("Presiona [ENTER] para regresar.")

    elif opcion == 2:
        pokemon_principal.hablar()
        input("Presiona [ENTER] para regresar.")

    elif opcion == 3:
        pokemon_principal.entrenar()

    elif opcion == 4:
        rivales = ["Gary Oak", "Paul"]
        combate(pokemon_principal, enemigos, pokemones_atrapados, nombre_usuario, rivales)

    elif opcion == 5:
        verPokemonsAtrapados(pokemones_atrapados, pokemon_principal)
        input("Presiona [ENTER] para regresar.")

    elif opcion == 6:
        enemigos.append(crear_enemigo())
        input("Presionar [ENTER] para regresar.")

    elif opcion == 7:
        modulo_pruebas_errores()

    elif opcion == 8:
        gestionar_batallas()
        input("Presionar [ENTER] para regresar.")

    elif opcion == 9:
        # Guarda directamente en su ranura correspondiente (sin menús extras para agilizar)
        partida_actual_id = guardar_partida_db(nombre_usuario, pokemon_principal, pokemones_atrapados, partida_actual_id)
        print(f"\n[AVISO]: ¡Progreso de '{nombre_usuario}' guardado exitosamente en la base de datos!")
        input("\nPresiona [ENTER] para continuar.")

    elif opcion == 10:
        print("\nCargando", end="")
        puntosCarga()
        break
