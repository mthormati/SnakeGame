import pyglet

class Board:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food

    def renderBorad(self):
        batch = pyglet.graphics.Batch()
        #Fill batch with colored squares
        dark = [125,135,150]
        light = [232,235,239]
        hoverColor = [255,245,157]
        x = y = 0
        for i in range(8):
            for j in range(8):
            #Create quad with one of three colors and add quad to batch
            if (j,i) == mousePos:
                batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i',create_quad_vertex_list(x,y,100,100)), ('c3B',hoverColor*4))
            elif (i + j) % 2 == 0:
                batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i',create_quad_vertex_list(x,y,100,100)), ('c3B',dark*4))
            else:
                batch.add(4, pyglet.gl.GL_QUADS, None, ('v2i',create_quad_vertex_list(x,y,100,100)), ('c3B',light*4))
            x += 100
            x = 0
            y += 100
        return batch