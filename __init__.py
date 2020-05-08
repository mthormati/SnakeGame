import pyglet
from board import Board

if __name__ == "__main__":
  window = pyglet.window.Window(width=800, height=800, resizable=False, caption='Snake')
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
