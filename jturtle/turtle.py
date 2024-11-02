# jturtle - Simple Turtle Library to be used
# in Jupyter Notebooks
# (c) 2018-24 Dmitri Soshnikov, http://twitter.com/shwars

import matplotlib.pyplot as plt
import math

class Turtle:

    def init(self):
        self.x = 0
        self.y = 0
        self.direction = 90
        self.down = True
        self.linewidth = 1
        self.color = 'black'
        self.pointstyle = '.'
        self.commands = []

    def __init__(self):
        self.autoinit = True
        self.reset_commands = True
        self.show_axes = False
        self.keep_aspect = True
        self.init()

    def backward(self,x):
        self.forward(-x)

    def forward(self, x):
        px, py = self.x, self.y
        self.x = self.x + x * math.cos(math.radians(self.direction))
        self.y = self.y + x * math.sin(math.radians(self.direction))
        if self.down:
            #l = plt.Line2D((px, self.x), (py, self.y), lw=self.linewidth)
            #plt.gca().add_line(l)
            self.commands.append(('L',px,self.x,py,self.y,self.linewidth,self.color))

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

    def expand_dim(self,args,prop=0.1):
        (xmi,xma),(ymi,yma) = args
        dx = (xma-xmi)*prop
        dy = (yma-ymi)*prop
        return ((xmi-dx,xma+dx),(ymi-dy,yma+dy))

    def get_dim(self):
        xmin = min([min(x[1],x[3]) for x in self.commands])
        xmax = max([max(x[1],x[3]) for x in self.commands])
        ymin = min([min(x[2],x[4]) for x in self.commands])
        ymax = max([max(x[2],x[4]) for x in self.commands])
        if self.keep_aspect:
            return self.expand_dim(((min(xmin,ymin),max(xmax,ymax)),(min(xmin,ymin),max(xmax,ymax))))
        else:
            return self.expand_dim(((xmin,xmax),(ymin,ymax)))

    def draw(self,renderer=None,commands=None):
        if renderer is None:
            renderer = plt.gca()
        if commands is None:
            commands = self.commands
        for t in commands:
            if t[0]=='L':
                l = plt.Line2D(t[1:3], t[3:5], lw=t[5], color=t[6])
            elif t[0]=='P':
                l = plt.Line2D(t[1:3], t[3:5], lw=t[5], color=t[6], marker=t[7])
            else:
                raise Exception("Unknown figure type: {}".format(t[0]))
            renderer.add_line(l)

    def explain(self):
        for t in self.commands:
            print("{}: ({},{}) -> ({},{})".format(t[0],t[1],t[2],t[3],t[4]))

    def show(self):
        plt.axis('scaled')
        plt.axis('off')
        xdim,ydim = self.get_dim()
        plt.gca().set_xlim(xdim)
        plt.gca().set_ylim(ydim)
        self.draw()
        plt.show()
        if self.reset_commands:
            self.commands = []
        if self.autoinit:
            self.init()

    def show_steps(self):
        n=len(self.commands)
        xdim,ydim = self.get_dim()
        fig,ax = plt.subplots(1,n)
        for i in range(n):
            ax[i].set_xlim(xdim)
            ax[i].set_ylim(ydim)
            ax[i].axis('off')
            ax[i].axis('scaled')
            self.draw(renderer=ax[i],commands=self.commands[0:i+1])
        if self.reset_commands:
            self.commands = []
        if self.autoinit:
            self.init()

    def done(self,step_by_step=False):
        if step_by_step:
            self.show_steps()
        else:
            self.show()

    def line(self,a,b):
        self.commands.append(('L',a[0],b[0],a[1],b[1],self.linewidth,self.color))

    def point(self,p,pointstyle=None):
        self.commands.append(('P',p[0],p[0],p[1],p[1],self.linewidth,self.color,self.pointstyle if pointstyle is None else pointstyle))

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

def line(a,b):
    ensureTurtle().line(a,b)

def point(p,pointstyle=None):
    ensureTurtle().point(p,pointstyle)

def explain():
    ensureTurtle().explain()
