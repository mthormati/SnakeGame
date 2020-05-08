import pyglet

class Board:
  def __init__(self):
    self.BOARD_SIZE = 20
    self.BLOCK_SIZE = 40

  def renderBoard(self):
    batch = pyglet.graphics.Batch()

    darkSquareColor = [12,16,21]
    lightSquareColor = [23,28,34]

    for i in range(self.BOARD_SIZE):
      for j in range(self.BOARD_SIZE):
        if (i + j) % 2 == 0:
          batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i',
            self.create_quad_vertex_list(i*self.BLOCK_SIZE,j*self.BLOCK_SIZE,self.BLOCK_SIZE,self.BLOCK_SIZE)), ('c3B',darkSquareColor*4))
        else:
          batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i',
            self.create_quad_vertex_list(i*self.BLOCK_SIZE,j*self.BLOCK_SIZE,self.BLOCK_SIZE,self.BLOCK_SIZE)), ('c3B',lightSquareColor*4))
    batch.draw()

  def create_quad_vertex_list(self, x, y, width, height):
    return x, y, x + width, y, x + width, y + height, x, y + height

if __name__ == "__main__":
  board = Board()
  pyglet.app.run()