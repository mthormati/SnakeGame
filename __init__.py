import pyglet

from constants import *
from food import Food
from location import Location
from render import *
from score import Score

if __name__ == "__main__":
  window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT+SCORE_HEIGHT, resizable=False, caption='Snake')
  pyglet.gl.glClearColor(0.5, 0.6, 0.7, 1.0)
  snake = Snake(Location(SNAKE_START_X, SNAKE_START_Y), LEFT, SNAKE_START_SIZE)
  food = Food(snake.getSnakeList())
  score = Score()
  paused = False
  
  @window.event
  def on_draw():
    window.clear()
    renderHeader(score, 'Press <space> to pause/unpause\nPress <enter> to restart')
    renderBoard(food, snake)

  @window.event
  def on_key_press(symbol, modifiers):
    global paused, snake, food, score
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
    elif symbol == pyglet.window.key.SPACE:
      paused = not paused
    elif symbol == pyglet.window.key.ENTER:
      snake = Snake(Location(SNAKE_START_X, SNAKE_START_Y), LEFT, SNAKE_START_SIZE)
      food = Food(snake.getSnakeList())
      score.resetScore()

  def game_loop(event):
    if not paused:
      if snake.isAlive():
        snake.move()
        snake.setMoveBudget(1)
        if snake.canEatFood(food):
          snake.grow()
          food.placeFood(snake.getSnakeList())
          score.incrementScore()
      else:
        score.compareAndSetHighScore()
    
  pyglet.clock.schedule_interval(game_loop, 0.15)

  pyglet.app.run()
