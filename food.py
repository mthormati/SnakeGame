import pyglet
import random

from constants import *
from location import Location
from typing import List

class Food:
  def __init__(self, excludedBlocks: List[Location]):
    self.location = self.getRandomLocation(excludedBlocks)

  def getX(self):
    return self.location.getX()

  def getY(self):
    return self.location.getY()

  def getLocation(self):
    return self.location
  
  def inExcludedBlock(self, loc: Location, excludedBlocks: List[Location]):
    for block in excludedBlocks:
      if loc.isEqual(block):
        return True
    return False

  def getRandomLocation(self, excludedBlocks: List[Location]):
    loc = Location(random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
    while self.inExcludedBlock(loc, excludedBlocks):
      loc = Location(random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1))
    return loc
