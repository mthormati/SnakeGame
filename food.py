import pyglet
import random

from constants import *
from location import Location

class Food:
  def __init__(self):
    self.location = self.getRandomLocation()

  def getX(self):
    return self.location.getX()

  def getY(self):
    return self.location.getY()

  def getRandomLocation(self):
    return Location(random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
