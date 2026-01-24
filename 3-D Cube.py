from ursina import *

app = Ursina()

cube = Entity(
    model='cube',
    color=color.green,
    scale=2,
    wireframe=True,
    wireframe_color=color.black
)

rotation_speed = 100

def update():
    if held_keys['right arrow']:
        cube.rotation_y -= rotation_speed * time.dt
    if held_keys['left arrow']:
        cube.rotation_y += rotation_speed * time.dt
    if held_keys['up arrow']:
        cube.rotation_x += rotation_speed * time.dt
    if held_keys['down arrow']:
        cube.rotation_x -= rotation_speed * time.dt

EditorCamera()
app.run()
