# jturtle - Simple Turtle Library to be used
# in Jupyter Notebooks and elsewhere
# (c) 2018 Dmitri Soshnikov, http://twitter.com/shwars

import matplotlib.pyplot as plt
import math

class Turtle:

    def init(self):
        self.x = 0
        self.y = 0
        self.direction = 90
        self.down = True
        self.linewidth = 1

    def __init__(self):
        self.autoinit = True
        self.init()

    def forward(self, x):
        px, py = self.x, self.y
        self.x = self.x + x * math.cos(math.radians(self.direction))
        self.y = self.y + x * math.sin(math.radians(self.direction))
        if self.down:
            l = plt.Line2D((px, self.x), (py, self.y), lw=self.linewidth)
            plt.gca().add_line(l)

    def right(self, x):
        self.direction -= x

    def left(self, x):
        self.direction += x

    def penup(self):
        self.down = False

    def pendown(self):
        self.down = True

    def set_line_width(self,line_width):
        self.linewidth = line_width

    def show(self):
        plt.axis('scaled')
        plt.show()
        if self.autoinit:
            self.init()

defTurtle = None

def ensureTurtle():
    global defTurtle
    if defTurtle is None:
        defTurtle = Turtle()
    return defTurtle

def forward(x):
    ensureTurtle().forward(x)

def left(x):
    ensureTurtle().left(x)

def right(x):
    ensureTurtle().right(x)

def show():
    ensureTurtle().show()

def penup():
    ensureTurtle().penup()

def pendown():
    ensureTurtle().pendown()

def init():
    ensureTurtle().init()