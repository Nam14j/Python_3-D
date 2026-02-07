from ursina import *

app = Ursina()

Sky(texture='Texturelabs_Sky_173XL.jpg')

Sun = Entity(model='sphere', texture='sunmap.jpg', rotation=(7.25,0,0), color=color.yellow, scale=3, position=(0,0,0), wireframe=False, wireframe_color=color.white)

earth_pivot = Entity(position=Sun.position)
mars_pivot = Entity(position=Sun.position)
jupiter_pivot = Entity(position=Sun.position)
uranus_pivot = Entity(position=Sun.position)
saturn_pivot = Entity(position=Sun.position)
mercury_pivot = Entity(position=Sun.position)
venus_pivot = Entity(position=Sun.position)

earth_tilt = Entity(parent=earth_pivot, rotation=(23.44,0,0))
mars_tilt = Entity(parent=mars_pivot, rotation=(25.19,0,0))
jupiter_tilt = Entity(parent=jupiter_pivot, rotation=(3.13,0,0))
uranus_tilt = Entity(parent=uranus_pivot, rotation=(97.77,0,0))
saturn_tilt = Entity(parent=saturn_pivot, rotation=(26.73,0,0))
mercury_tilt = Entity(parent=mercury_pivot, rotation=(0.03,0,0))
venus_tilt = Entity(parent=venus_pivot, rotation=(177,0,0))

SCALE = 6 

Mercury = Entity(parent=mercury_tilt, model='sphere',
    texture='Mercury_Texture.png', scale=0.8,
    position=(0.39 * SCALE, 0, 0))

Venus = Entity(parent=venus_tilt, model='sphere',
    texture='Venus_Texture.png', scale=1.5,
    position=(0.72 * SCALE, 0, 0))

Earth = Entity(parent=earth_tilt, model='sphere',
    texture='Earth_Texture.png', scale=1.5,
    position=(1.00 * SCALE, 0, 0))

Moon = Entity(parent=Earth, model='sphere',
    texture='Moon_Texture.png', scale=0.4,
    position=(0.2 * SCALE, 0, 0))

Mars = Entity(parent=mars_tilt, model='sphere',
    texture='Mars_Texture.png', scale=1.2,
    position=(1.52 * SCALE, 0, 0))

Jupiter = Entity(parent=jupiter_tilt, model='sphere',
    texture='Jupiter_Texture.png', scale=2.5,
    position=(5.20 * SCALE, 0, 0))

Saturn = Entity(parent=saturn_tilt, model='sphere',
    texture='Saturn_Texture.png', scale=2.2,
    position=(9.58 * SCALE, 0, 0))

Uranus = Entity(parent=uranus_tilt, model='sphere',
    texture='Uranus_Texture.png', scale=2,
    position=(19.22 * SCALE, 0, 0))


rotation_speed = 50

def update():
    Earth.rotation_y += rotation_speed * time.dt
    Mars.rotation_y += (rotation_speed - 10) * time.dt
    Jupiter.rotation_y += (rotation_speed - 20) * time.dt
    Uranus.rotation_y += (rotation_speed - 15) * time.dt
    Saturn.rotation_y += (rotation_speed - 18) * time.dt
    Mercury.rotation_y += (rotation_speed + 5) * time.dt
    Venus.rotation_y += (rotation_speed - 8) * time.dt

    earth_pivot.rotation_y += 20 * time.dt
    mars_pivot.rotation_y += 16 * time.dt
    jupiter_pivot.rotation_y += 10 * time.dt
    uranus_pivot.rotation_y += 7 * time.dt
    saturn_pivot.rotation_y += 6 * time.dt
    mercury_pivot.rotation_y += 30 * time.dt
    venus_pivot.rotation_y += 24 * time.dt

EditorCamera()
app.run()
