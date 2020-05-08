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