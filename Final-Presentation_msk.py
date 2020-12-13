# Mathew Kelne
# Final Presentation
# Intro to Computer Science


from turtle import *
from random import random
from freegames import line
#from turtle import line

def draw():
    "Draw maze."
    color('black')
    width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                Screen(x, y, x + 40, y + 40)
            else:
                Screen(x, y + 40, x + 40, y)

    update()

def tap(x, y):
    "Draw line and dot for screen tap."
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()

    width(2)
    color('purple')
    goto(x, y)
    dot(4)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()