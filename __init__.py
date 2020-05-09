import pyglet

from board import *
from constants import *
from food import Food
from location import Location

if __name__ == "__main__":
  window = pyglet.window.Window(width=WINDOW_HEIGHT, height=WINDOW_WIDTH, resizable=False, caption='Snake')
  food = Food()
  snake = Snake(Location(SNAKE_START_X, SNAKE_START_Y), LEFT, SNAKE_START_SIZE)
  
  @window.event
  def on_draw():
    print("drawing")
    window.clear()
    renderBoard(food, snake)

  def game_loop(event):
    snake.move()
    
  pyglet.clock.schedule_interval(game_loop, 1)

  pyglet.app.run()



# snake = Snake(10,10)
# food = Food()
# food.putInRandomPosition()
# while snake.isAlive():
#     check for key input in background
#     snake.updatePosition()
#     board.renderBoard()
#     timeout(small duraction)
