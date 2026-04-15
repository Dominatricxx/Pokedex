# Pokedex
INSTRUCCIONES GENERALES
Este examen tiene como objetivo que pongas en práctica los conceptos de Programación Orientada a Objetos en Python
mediante la creación de una Pokédex. La Pokédex te permitirá almacenar información y funcionalidades de diferentes
Pokémon, así como realizar acciones como entrenamiento, combate, evolución y atrapado de Pokémon. En este proyecto
deberás aplicar clases abstractas, métodos abstractos, herencia, herencia múltiple, polimorfismo, especialización, agregación,
objetos y menús interactivos por consola (todo lo visto en la unidad 2 y 3).

➢ Indicaciones generales
• Sigue cada paso cuidadosamente.
• Prueba cada parte del programa conforme avances.
• Usa input() para todas las interacciones con el usuario.
• El programa debe permanecer en ejecución hasta que el usuario elija salir.
• Las opciones del sistema deben seleccionarse mediante números.
• No debe haber comentarios en el código.
• Está permitido mejorar visualmente la salida del programa en consola.
PROYECTO: CREACIÓN DE UNA POKÉDEX
Contexto
Crearás una estructura de clases en Python que simule una Pokédex, es decir, un sistema donde podrás visualizar y gestionar
un Pokémon con sus habilidades. Deberás tener un Pokémon principal con el cual puedas:
• visualizar sus detalles
• entrenarlo
• evolucionarlo
• combatir
• atrapar Pokémon enemigos
• consultar Pokémon atrapados
1. CLASE BASE ABSTRACTA
Crea la clase principal abstracta PokemonBase: Clase que servirá como la clase principal para todos los Pokémon y tendrá
los siguientes atributos con valores predeterminados:
• nombre (str): valor predeterminado "Sin Pokémon"
• descripcion (str): valor predeterminado "No descripción"
• ataque (int): valor entre 1 y 1000, valor predeterminado 0
• defensa (int): valor entre 1 y 1000, valor predeterminado 0
• vida (int): valor entre 1 y 1000, valor predeterminado 0
• nivel (int): valor entre 1 y 100
• evolucion (int): valor inicial 1, límite 3
• atrapado (bool): valor predeterminado False
Nota: Asegúrate de que al llegar el atributo nivel a >=100, el Pokémon "evoluciona", lo que significa que el atributo evolución
aumenta en +1 (a la siguiente evolución y el nivel se reinicia de nuevo a 0).
Ejemplo de evolución: Siempre debe de iniciar el programa eligiendo a un Pokémon en su estado inicial (evolución = 1) y de
allí irá aumentando. Supongamos que el programador decide tener como Pokémon inicial al Pokémon llamado "Pichu" y su
atributo nivel llega a >=100, su atributo evolución aumenta en +1, éste pasa a evolucion = 2, convirtiéndose en "Pikachu". Si
el nivel vuelve a llegar a >=100, evolución pasa a ser evolucion = 3, evolucionando a "Raichu". Recordar que cuando el nivel
sea >= 100 el atributo nivel debe reiniciarse de nuevo a cero. Si el Pokémon solo tiene 2 evoluciones que su límite sea el
número de evolución y no pueda avanzar a más evoluciones.

Página 2
Cuando el Pokémon evolucione debe de aparecer en todo detalle bajo su nuevo nombre, lo demás se mantiene igual. Esto
quiere decir que en sus detalles como Pokémon tendrá el nombre nuevo de su evolución y cuando se elija la opción hablar
Pokémon deberá de hacer su sonido típico que usualmente es su nombre conforme a su evolución.
Métodos Abstractos en la Clase abstracta:
Debes declarar como abstractos los siguientes métodos:
• hablar()
• actualizar()
• detallesPokemon()
Ajuste adicional
También deberás agregar como método abstracto:
• 4. entrenar()
Nota: Usa el módulo ABC para declarar esta clase abstracta y los métodos abstractos.
2. MÉTODOS DE LA CLASE Pokemon QUE IMPLEMENTAN PokemonBase
Crea una clase concreta llamada Pokemon que herede de PokemonBase e implemente los métodos abstractos de ella:
Parte 1: Implementación de los métodos abstractos
• detallesPokemon(): Muestra en pantalla todos los detalles del Pokémon (nombre, descripción, ataque, defensa, vida,
nivel, evolución, y si ha sido atrapado).
• hablar(): Imprime el sonido típico del Pokémon (usualmente es su nombre).
• entrenar(): Aumenta el ataque, defensa, nivel y vida del Pokémon en +10. Si el nivel llega a >=100, imprime: "¡El
Pokémon ha evolucionado! Ahora es: [aquí el nombre nuevo de la evolución]" y reinicia el nivel de nuevo a 0,
incrementando obviamente la evolución en +1.
Parte 2: Métodos de mejora
Define métodos adicionales exclusivos en esta clase Pokemon (aumentos de atributos manera individual):
• subirAtaque(): Aumenta solamente el atributo ataque usando un boost_ataque de +20.
• subirDefensa(): Aumenta solamente el atributo defensa usando un boost_defensa de +20.
• subirVida(): Aumenta solamente el atributo vida usando un boost_vida de +20.
• Ejemplo:
atributo ataque = 20
ataque = ataque + boost_ataque, ahora su ataque debería de aumentar +20 de lo que ya tenía anteriormente,
haciendo el ataque que suba hasta +40
Cada uno debe aumentar únicamente un atributo usando boosts individuales:
• boost_ataque = +20
• boost_defensa = +20
• boost_vida = +20
Nota: Aunque estos métodos estarán implementados en la clase Pokemon, su existencia también estará formalmente exigida
por la clase abstracta Entrenamiento. Por eso, cuando se construya PokemonConEntrenamiento, estos métodos
servirán para cumplir con la lógica de la herencia múltiple.

Página 3

Parte 3: Método de actualización completa
Incluye en la clase Pokemon el método: actualizar()
Debe actualizar al mismo tiempo: ataque, defensa y vida; sumando:
• boost_ataque
• boost_defensa
• boost_vida
A diferencia de los métodos individuales, aquí se actualizan todos a la vez.
3. CREAR SUBCLASES DE Pokémon CON ESPECIALIZACION
Crea cuatro subclases de Pokémon para representar las categorías de los Pokémon. Cada subclase deberá tener un atributo
especial y su propio método actualizar() que hereda de la clase base.
• Categorías de Pokémon:
1. PokemonAgua
2. PokemonFuego
3. PokemonEléctrico
4. PokemonHierba

Estas subclases deberán heredar de PokemonConEntrenamiento. Porque el Pokémon jugable debe combinar:
• la lógica general de Pokémon
• la interfaz de entrenamiento de Entrenamiento
• y la especialización de su tipo
De esta manera, el diseño completo queda así:
3.1. Atributo especial
Cada subclase deberá tener el atributo: ataque_especial, para que los pokemones creados en su correspondiente subclase puedan
tener cada quien su ataque especial; por ejemplo:
• Agua → "Hidrobomba"
• Fuego → "Lanzallamas"
• Eléctrico → "Impactrueno"
• Hierba → "Látigo Cepa"
3.2. Método actualizar() en subclases
Cada subclase debe sobrescribir el método actualizar() para modificar atributos de acuerdo a su tipo. Esto significa que el
método actualizar() no debe comportarse exactamente igual en todos los Pokémon, sino que debe depender de la categoría.
4. HERENCIA MÚLTIPLE CON Entrenamiento
Define una clase abstracta adicional llamada Entrenamiento, que tendrá métodos abstractos para incrementar habilidades.
Esta clase servirá para representar formalmente que un Pokémon puede realizar mejoras individuales..
• Métodos abstractos en Entrenamiento:
o subirAtaque()
o subirDefensa()
o subirVida()

Luego, define una clase PokemonConEntrenamiento que herede tanto de Pokemon como de Entrenamiento, e implemente
estos métodos.

Página 4

4.1 Clase PokemonConEntrenamiento
Define una clase llamada PokemonConEntrenamiento que herede de:
• Pokemon
• Entrenamiento
Función de esta clase
Su propósito es combinar:
• el comportamiento general de un Pokémon
• con la obligación formal de implementar el sistema de entrenamiento individual
4.2 Implementación correcta
Como la clase Pokemon ya contiene la lógica funcional de:
• subirAtaque()
• subirDefensa()
• subirVida()
la clase PokemonConEntrenamiento puede:
• heredar esa implementación
• y quedar como la clase intermedia que conecta ambos modelos mediante herencia múltiple
Nota: No se trata de repetir código innecesariamente, sino de mostrar correctamente el uso de herencia múltiple en un
sistema donde una clase aporta comportamiento general y la otra aporta un contrato abstracto especializado
5. SIMULACIÓN DE COMBATE Y ATRAPADO
Ahora que tienes tu Pokémon y sus habilidades, crea las siguientes funcionalidades en tu programa:
5.1. Crear Pokémon enemigos
Debes crear: 4 Pokémon enemigos ya instanciados, 2 con atributos altos y 2 con atributos bajos.
Además, debe existir una opción para crear un Pokémon enemigo personalizado.
Al entrar a combate, el programa deberá elegir aleatoriamente a uno de los Pokémon enemigos disponibles.
Puedes usar random o una lista y selección aleatoria para pelear con un Pokémon enemigo.
5.2. Combate
Regla principal
El ataque de un Pokémon se resta primero contra la defensa del oponente. Cuando la defensa llegue a 0, el daño restante
deberá pasar a restarse a la vida. Es importante recalcar que no debe haber valores negativos.
Si el daño excede la defensa: la defensa se queda en 0 y el sobrante se descuenta de la vida
Ejemplo
Si mi Pokémon tiene:
• ataque = 20
• defensa = 50
• vida = 100

Página 5

y el enemigo tiene:
• ataque = 60
• defensa = 100
• vida = 150
si el enemigo me ataca:
• 60 se resta a mi defensa 50
• mi defensa queda en 0
• sobran 10
• esos 10 pasan a la vida
• mi vida queda en 90
Opciones del combate
Dentro del combate deben existir las siguientes opciones: 1.Pasar turno, 2.Ataque normal, 3.Ataque especial y 4.Huir
Turnos
• El usuario elegirá su acción mediante el menú
• El enemigo deberá escoger aleatoriamente entre: ataque normal, ataque especial y pasar turno
Visualización durante el combate
Al entrar al combate deben mostrarse los stats de: mi Pokémon y el Pokémon enemigo Después de cada turno deben mostrarse
para ambos: nombre, ataque, defensa y vida para revisar correctamente los cálculos del combate.
Ataque especial
El ataque especial deberá estar asociado al atributo ataque_especial de cada subclase.
Cuando un enemigo pierde
Si la vida del Pokémon enemigo llega a 0 podrás atraparlo y el atributo atrapado se convierte en True.
Opcional: Puedes usar random() para decidir si: se dejó atrapar o si escapó.
Pokémon atrapados
Todo Pokémon atrapado debe aparecer en la opción: Ver Pokémon Atrapados. Es opcional decidir si ese Pokémon atrapado
podrá o no ser usado luego como Pokémon jugable.
5.3. Método verPokemonsAtrapados()
Debes incluir un método llamado verPokemonsAtrapados() que muestre: la lista de Pokémon atrapados junto con sus detalles.
Ubícalo en la clase que consideres necesaria para su correcto funcionamiento.
6. INTERACCIONES CON EL USUARIO
Haz que el programa sea interactivo para que el usuario pueda seleccionar diferentes opciones y realizar acciones con el
Pokémon. Usa input() para guiar al usuario durante la ejecución de todo el programa y asegúrate de que el programa se
mantenga en ejecución hasta que el usuario decida finalizar (que sea elegir las opciones mediante números).
Todo el programa debe de ser mediante input() para la selección de opciones.

Página 6

Requerimientos de la Interfaz de Usuario y funcionalidades:
• Al iniciar, la Pokédex (terminal) debe:
o Dar la bienvenida al usuario y pedirle su nombre.
o Informarle que no tiene Pokémon aún, que es necesario escoger 1 de los 4 Pokémon a elegir, es decir:
Darle la opción de elegir un Pokémon entre las subclases que creaste (Agua, Fuego, Eléctrico, Hierba).

• Luego de elegir el Pokémon, se deben mostrar todos sus detalles en pantalla.
• Después permitir al usuario poder elegir alguna opción del menú principal, como entrenarlo o realizar acciones
adicionales.
• Todo lo referente a entrenamiento debe de estar en una opción del programa llamada Entrenar Pokémon.
Ejemplo: Si el usuario elige la opción Entrenar Pokémon, deben de estar las siguientes 4 opciones:
1. Entrenamiento Normal: únicamente actualiza ataque, defensa y nivel (al mismo tiempo).
2. Entrenamiento Individual: únicamente actualiza de manera individual ataque o defensa o vida.
3. Entrenamiento Intensivo: únicamente actualiza ataque, defensa y vida (al mismo tiempo utilizando boost).
4. Entrenamiento Personalizado: actualiza manualmente todos los valores del Pokémon (ingresarle valores).
• Al elegir cualquiera de las 4 opciones anteriores nos debe de mostrar sus atributos rápidamente para saber cuánto
aumentaron nuestros stats y regresarnos al menú de los entrenamientos (no al menú inicial), esto es por si queremos
seguir entrenando más.
• Permite en una opción crear un Pokémon enemigo para poder ingresar sus valores y que esté ingresado en la lista
para poder combatir contra él (si es elegido de manera aleatoria).
Nota: Todas las interacciones deben realizarse mediante input() y permitir al usuario elegir qué hacer con el Pokémon en cada
momento, no se te olvide siempre usar adecuadamente las opciones de cancelar y/o salir en cada menú del programa.
7. EVALUACIÓN Y CRITERIOS
El examen se evaluará en base a los siguientes criterios:
• ¿Cumple todos los requerimientos técnicos del exámen?
• ¿Todo el programa se ejecuta correctamente en consola y hace lo que se supone que debe de hacer?
• ¿Se observa herencia, polimorfismo, encapsulamiento, sobrecarga , métodos abstractos, sobreescritura, etc?
• Participación equitativa entre los integrantes del equipo (programadores).
• Cada alumno responderá preguntas individuales al final (Preguntas hechas por el maestro).
Recordatorios Finales
• Asegúrate de que el programa es interactivo y permite múltiples interacciones hasta que el usuario quiera
terminar/cerrar el programa.
• Prueba cada método y cada interacción para verificar que todo funcione correctamente.
• No es necesario que les guste Pokémon, solo investiguen los nombres, evoluciones, cuantas de ellas tiene, el sonido
que emite, ponerle un ataque normal y un ataque especial.
• NO COMENTARIOS EN CODIGO (esto es para poder realizar las preguntas en el código el día del exámen).
• Está permitido personalizar de manera visual o gráfica el programa, como poner barras de ataque, iconos, figura del
Pokémon hecha con caracteres, poner color, hacer mejoras en la visualización de los detalles del Pokémon, etc.
• Usa estructuras condicionales ciclos para controlar las acciones o fragmentos del programa.
• Visualización del menú principal en terminal:

1. Detalles de mi Pokémon
2. Hablar Pokémon
3. Entrenamiento (aquí irán los 4 entrenamientos diferentes)
4. Combatir
5. Ver Pokémon Atrapados
6. Crear Pokémon Enemigo
7. Salir
