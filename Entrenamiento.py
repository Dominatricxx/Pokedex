from abc import ABC, abstractmethod

class Entrenamiento(ABC):
  @abstractmethod
  def subirAtaque():
    print(" Ataque ")

  @abstractmethod
  def subirDefensa():
    print(" Defensa ")

  @abstractmethod
  def subirVida():
    print(" Vida ")
