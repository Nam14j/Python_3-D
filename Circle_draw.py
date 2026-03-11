
from ursina import *

app = Ursina(fullscreen=True)

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
    for s in range(0, 360, 1):
        rad = math.radians(s)
        x_pos = x + radius * math.cos(rad)
        y_pos = y + radius * math.sin(rad)
        make_pexel(x_pos, y_pos, coler)
        
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
            make_circle(pos.x, pos.y, 4, color.white)

app.run()