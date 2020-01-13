# jturtle - Simple Turtle Library to be used
# in Jupyter Notebooks
# (c) 2018-20 Dmitri Soshnikov, http://twitter.com/shwars

import matplotlib.pyplot as plt
import math

class Turtle:

    def init(self):
        self.x = 0
        self.y = 0
        self.direction = 90
        self.down = True
        self.linewidth = 1
        self.commands = []

    def __init__(self):
        self.autoinit = True
        self.init()

    def backward(self,x):
        self.forward(-x)

    def forward(self, x):
        px, py = self.x, self.y
        self.x = self.x + x * math.cos(math.radians(self.direction))
        self.y = self.y + x * math.sin(math.radians(self.direction))
        if self.down:
            l = plt.Line2D((px, self.x), (py, self.y), lw=self.linewidth)
            plt.gca().add_line(l)
            self.commands.append((px,self.x,py,self.y,self.linewidth))

    def right(self, x):
        self.direction -= x

    def left(self, x):
        self.direction += x

    def penup(self):
        self.down = False

    def pendown(self):
        self.down = True

    def pensize(self,line_width=None):
        if line_width is not None:
            self.linewidth = line_width
        return self.linewidth

    def show(self):
        if self.show_axes:
            plt.axis('scaled')
        else:
            plt.axis('off')
        plt.show()
        if self.autoinit:
            self.init()

    def show_steps(self):
        n=len(self.commands)
        fig,ax = plt.subplots(1,n)
        for i,t in enumerate(self.commands):
            l = plt.Line2D(t[0:2], t[2:4], t[4])
            ax[i].add_line(l)
        if self.show_axes:
            plt.axis('scaled')
        else:
            plt.axis('off')
        plt.show()

    def done(self,step_by_step=False):
        if step_by_step:
            self.show_steps()
        else:
            self.show()

defTurtle = None

def ensureTurtle():
    global defTurtle
    if defTurtle is None:
        defTurtle = Turtle()
    return defTurtle

def forward(x):
    ensureTurtle().forward(x)

def backward(x):
    ensureTurtle().backward(x)

def left(x):
    ensureTurtle().left(x)

def right(x):
    ensureTurtle().right(x)

def show():
    ensureTurtle().show()

def done(step_by_step=False):
    ensureTurtle().done(step_by_step)

def penup():
    ensureTurtle().penup()

def pendown():
    ensureTurtle().pendown()

def pensize(width=None):
    return ensureTurtle().pensize(width)

def init():
    ensureTurtle().init()
