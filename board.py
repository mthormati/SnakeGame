import pyglet

from constants import *
from food import Food

class Board:
  def __init__(self, food: Food):
    self.food = food

  def renderBoard(self):
    batch = pyglet.graphics.Batch()

    darkSquareColor = [12,16,21]
    lightSquareColor = [23,28,34]
    foodColor = [189,30,46]

    for i in range(BOARD_SIZE):
      for j in range(BOARD_SIZE):
        if i == self.food.getX() and j == self.food.getY():
          batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i',
            self.create_quad_vertex_list(i*BLOCK_SIZE,j*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)), ('c3B',foodColor*4))
        elif (i + j) % 2 == 0:
          batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i',
            self.create_quad_vertex_list(i*BLOCK_SIZE,j*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)), ('c3B',darkSquareColor*4))
        else:
          batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i',
            self.create_quad_vertex_list(i*BLOCK_SIZE,j*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)), ('c3B',lightSquareColor*4))
    batch.draw()

  def create_quad_vertex_list(self, x, y, width, height):
    return x, y, x + width, y, x + width, y + height, x, y + height

if __name__ == "__main__":
  board = Board()
  pyglet.app.run()