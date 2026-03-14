
from ursina import *

app = Ursina(fullscreen=False)

Entity(model='quad', scale=100, collider='box', color=color.black)

def make_pexel(x, y, coler, z=0):
    return Entity(model='quad', color=coler, scale=(0.1, 0.1, 0.1), position=(x, y, z))

def make_line(x1, x2, y1, y2, coler):
    t = 0
    while t <= 1:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        make_pexel(x, y, coler)
        t += 0.02

def make_circle(x, y, radius, coler):
    
    X = -radius
    #for X in range(-radius, radius, 0.1):
    #for X in range(-radius, radius + 1, 0.1):
    while X <= radius:
        #x**2 + y**2 == radius**2
        y = sqrt(radius**2 - X**2)
        ##y = -sqrt(radius**2 - x**2)
        make_pexel(X, y, coler)
        make_pexel(X, -y, coler)
        X += 0.01
        make_line(X, X, y, -y, coler)

    Y = -radius

    while Y <= radius:
        #x**2 + y**2 == radius**2
        x = sqrt(radius**2 - Y**2)
        ##y = -sqrt(radius**2 - x**2)
        make_pexel(x, Y, coler)
        make_pexel(-x, Y, coler)
        Y += 0.01
        make_line(x, -x, Y, Y, coler)



def make_rectangle(x, y, width, height, coler):
    for i in range(width + 1):
        make_pexel(x + i * 0.1, y, coler)

    for i in range(width + 1):
        make_pexel(x + i * 0.1, y + height * 0.1, coler)

    for i in range(height + 1):
        make_pexel(x, y + i * 0.1, coler)

    for i in range(height + 1):
        make_pexel(x + width * 0.1, y + i * 0.1, coler)

def update():
    if held_keys['left mouse']:
        if mouse.world_point:
            pos = mouse.world_point
            make_circle(pos.x, pos.y, 2, color.white)

app.run()