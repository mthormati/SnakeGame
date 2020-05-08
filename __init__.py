import pyglet
from board import Board
from constants import *

if __name__ == "__main__":
  window = pyglet.window.Window(width=WINDOW_HEIGHT, height=WINDOW_WIDTH, resizable=False, caption='Snake')
  board = Board()
  
  @window.event
  def on_draw():
    window.clear()
    board.renderBoard()

  pyglet.app.run()



# snake = Snake(10,10)
# food = Food()
# food.putInRandomPosition()
# while snake.isAlive():
#     check for key input in background
#     snake.updatePosition()
#     board.renderBoard()
#     timeout(small duraction)
