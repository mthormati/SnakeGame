class Location:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
  
  def getX(self):
    return self.x
  
  def getY(self):
    return self.y

  def getLocation(self):
    return self.x, self.y

  def isEqual(self, loc: 'Location'):
    if self.x == loc.x and self.y == loc.y:
      return True
    return False
  
  def setLocation(self, x: int, y: int):
    self.x = x
    self.y = y