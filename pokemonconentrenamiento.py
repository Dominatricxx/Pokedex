from entrenamiento import Entrenamiento
from pokemon import Pokemon

class PokemonConEntrenamiento(Entrenamiento, Pokemon):
  def subirAtaque():
    if grado == "Basico":
      ataque += 5
    elif grado == "Legendario":
      ataque += 15
      
  def subirDefensa():
    if grado == "Basico":
      defensa += 5
    elif grado == "Legendario":
      defensa += 15

  def subirVida():
    if grado == "Basico":
      vida += 5
    elif grado == "Legendario":
      vida += 15


      
