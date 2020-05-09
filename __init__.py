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

  def game_loop(event):
    if snake.isAlive():
      snake.move()
    else:
      print("snake is dead")
    
  pyglet.clock.schedule_interval(game_loop, 0.5)

  pyglet.app.run()
