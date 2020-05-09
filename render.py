import pyglet

from constants import *
from food import Food
from snake import Snake
from location import Location
from score import Score

def renderBoard(food: Food, snake: Snake):
  batch = pyglet.graphics.Batch()

  darkSquareColor = [12, 16, 21]
  lightSquareColor = [48, 59, 71]
  foodColor = [189, 30, 46]
  snakeColor = [35, 158, 235] if snake.isAlive() else [151, 50, 168]

  for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
      vertexList = ('v2i', createQuadVertexList(i*BLOCK_SIZE,j*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))
      if snake.isSnakeBlock(Location(i, j)):
        batch.add(4, pyglet.gl.GL_QUADS, None, vertexList, ('c3B',snakeColor*4))
      elif i == food.getX() and j == food.getY():
        batch.add(4, pyglet.gl.GL_QUADS, None, vertexList, ('c3B',foodColor*4))
      elif (i + j) % 2 == 0:
        batch.add(4, pyglet.gl.GL_QUADS, None, vertexList, ('c3B',darkSquareColor*4))
      else:
        batch.add(4, pyglet.gl.GL_QUADS, None, vertexList, ('c3B',lightSquareColor*4))
  batch.draw()

def renderScore(score: Score):
  label = pyglet.text.Label('Score: ' + str(score.getScore()),
                          font_name='Times New Roman',
                          font_size=28,
                          x=10, y=WINDOW_HEIGHT + SCORE_HEIGHT//2,
                          anchor_y='center')
  label.draw()

def createQuadVertexList(x: int, y: int, width: int, height: int):
  return x, y, x + width, y, x + width, y + height, x, y + height