import pyglet

from board import *
from constants import *
from food import Food
from location import Location

if __name__ == "__main__":
  window = pyglet.window.Window(width=WINDOW_HEIGHT, height=WINDOW_WIDTH, resizable=False, caption='Snake')
  snake = Snake(Location(SNAKE_START_X, SNAKE_START_Y), LEFT, SNAKE_START_SIZE)
  food = Food(snake.getSnakeList())
  
  @window.event
  def on_draw():
    window.clear()
    renderBoard(food, snake)

  @window.event
  def on_key_press(symbol, modifiers):
    currDirection = snake.getDirection()
    moveBudget = snake.getMoveBudget()
    if symbol == pyglet.window.key.LEFT and currDirection != RIGHT and moveBudget > 0:
      snake.setDirection(LEFT)
      snake.setMoveBudget(0)
    elif symbol == pyglet.window.key.UP and currDirection != DOWN and moveBudget > 0:
      snake.setDirection(UP)
      snake.setMoveBudget(0)
    elif symbol == pyglet.window.key.RIGHT and currDirection != LEFT and moveBudget > 0:
      snake.setDirection(RIGHT)
      snake.setMoveBudget(0)
    elif symbol == pyglet.window.key.DOWN and currDirection != UP and moveBudget > 0:
      snake.setDirection(DOWN)
      snake.setMoveBudget(0)

  def game_loop(event):
    if snake.isAlive():
      snake.move()
      snake.setMoveBudget(1)
      if snake.canEatFood(food):
        food.placeFood(snake.getSnakeList())
    else:
      print("snake is dead")
    
  pyglet.clock.schedule_interval(game_loop, 0.20)

  pyglet.app.run()
