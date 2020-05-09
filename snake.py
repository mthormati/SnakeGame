from constants import *

from location import Location

class Snake:
  def __init__(self, location: Location, direction: int, size: int):
    self.HEAD = 0
    self.TAIL = size - 1
    self.direction = direction
    self.snakeList = [location]
    for i in range(1, size):
      self.snakeList.append(Location(location.getX() + i, location.getY()))

  def isSnakeBlock(self, location: Location):
    for i in range(self.TAIL + 1):
      if location.isEqual(self.snakeList[i]):
        return True
    return False

  def move(self):
    for i in range(self.TAIL, self.HEAD, - 1):
      self.snakeList[i] = self.snakeList[i - 1]
    headX = self.snakeList[self.HEAD].getX()
    headY = self.snakeList[self.HEAD].getY()
    if self.direction == LEFT:
      self.snakeList[self.HEAD] = Location(headX - 1, headY)
    elif self.direction == UP:
      self.snakeList[self.HEAD] = Location(headX, headY + 1)
    elif self.direction == RIGHT:
      self.snakeList[self.HEAD] = Location(headX + 1, headY)
    else:
      self.snakeList[self.HEAD] = Location(headX, headY - 1)
