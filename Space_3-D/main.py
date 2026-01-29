from ursina import *

app = Ursina()

Sun = Entity(model='sphere', texture='sunmap.jpg', color=color.yellow, scale=3, position=(0,0,0), wireframe=False, wireframe_color=color.white)

earth_pivot = Entity(position=Sun.position)
mars_pivot = Entity(position=Sun.position)
jupiter_pivot = Entity(position=Sun.position)
uranus_pivot = Entity(position=Sun.position)
saturn_pivot = Entity(position=Sun.position)
mercury_pivot = Entity(position=Sun.position)
venus_pivot = Entity(position=Sun.position)

Earth = Entity(parent=earth_pivot, model='sphere', 
               color=color.white, 
               scale=1.5,
               texture='Earth_Texture.png', 
               position=(3,0,0), 
               wireframe=False)

Mars = Entity(parent=mars_pivot,
              model='sphere',
              color=color.white,
              texture='Mars_Texture.png', 
              scale=1.2,
              position=(4,0,0),
              wireframe=False)

Jupiter = Entity(parent=jupiter_pivot,
                model='sphere', 
                color=color.white,
                texture='Jupiter_Texture.png',
                scale=2.5,
                position=(7,0,0),
                wireframe=False)

Urannus = Entity(parent=uranus_pivot,
                model='sphere',
                color=color.white,
                texture='Uranus_Texture.png',
                scale=2,
                position=(9,0,0),
                wireframe=False)

Saturn = Entity(parent=saturn_pivot,
                model='sphere',
                color=color.white,
                texture='Saturn_Texture.png',
                scale=2.2,
                position=(11,0,0),
                wireframe=False)

Mercury = Entity(parent=mercury_pivot,
                model='sphere',
                color=color.white,
                texture='Mercury_Texture.png',
                scale=0.8,
                position=(2,0,0),
                wireframe=False)

Venus = Entity(parent=venus_pivot,
               model='sphere',
               color=color.white,
               texture='Venus_Texture.png',
               scale=1.5,
               position=(2.5,-1.5,-1.5),
               wireframe=False)

rotation_speed = 50

def update():
    Earth.rotation_y += rotation_speed * time.dt
    Mars.rotation_y += (rotation_speed - 10) * time.dt
    Jupiter.rotation_y += (rotation_speed - 20) * time.dt
    Urannus.rotation_y += (rotation_speed - 15) * time.dt
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
