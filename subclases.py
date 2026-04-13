from pokemonconentrenamiento import PokemonConEntrenamiento


class PokemonAgua(PokemonConEntrenamiento):
  def __init__(self):
     self.ataque_especial = "Hidrobomba"

  def actualizar(self):
    print(" a ")
    
class PokemonFuego(PokemonConEntrenamiento):
  def __init__(self):
    self.ataque_especial = "Lanzallamas"

  def actualizar(self):
    print(" a ")
    
class PokemonElectrico(PokemonConEntrenamiento):
  def __init__(self):
    self.ataque_especial = "Impactrueno"

  def actualizar(self):
    print(" a ")
    
class PokemonHierba(PokemonConEntrenamiento):
  def __init__(self):
    self.ataque_especial = "Látigo Cepa"

  def actualizar(self):
    print(" a ")
  
