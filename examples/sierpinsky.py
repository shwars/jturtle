import sys
sys.path.append('d:\\work\\jturtle')

import jturtle as turtle
import random


vertices = [(0,0),(100,0),(50,100)]
x,y = 50,50


for _ in range(10000):
    vx,vy = random.choice(vertices)
    x = (x+vx)/2
    y = (y+vy)/2
    turtle.point((x,y),pointstyle=',')
turtle.done()


