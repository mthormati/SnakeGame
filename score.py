
class Score:
  def __init__(self):
    self.score = 0
    self.highScore = 0
  
  def getScore(self):
    return self.score
  
  def getHighScore(self):
    return self.highScore

  def incrementScore(self):
    self.score += 1

  def resetScore(self):
    self.score = 0
  
  def compareAndSetHighScore(self):
    if self.score > self.highScore:
      self.highScore = self.score