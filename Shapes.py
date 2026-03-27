from math import sqrt
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing with Pixels")

def make_pixel(x, y, color):
    pygame.draw.rect(screen, color, (int(x * 10), int(y * 10), 10, 10))

def make_line(x1, x2, y1, y2, color):
    t = 0
    while t <= 1:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        make_pixel(x, y, color)
        t += 0.01

def make_circle(x, y, radius, color):
    X = -radius
    while X <= radius:
        Y = sqrt(radius**2 - X**2)
        make_pixel(x + X, y + Y, color)
        make_pixel(x + X, y - Y, color)
        make_line(x + X, x + X, y + Y, y - Y, color)
        X += 0.1

    Y = -radius
    while Y <= radius:
        X = sqrt(radius**2 - Y**2)
        make_pixel(x + X, y + Y, color)
        make_pixel(x - X, y + Y, color)
        make_line(x + X, x - X, y + Y, y + Y, color)
        Y += 0.1

def make_rectangle(x, y, width, height, color):
    width = int(width)
    height = int(height)

    for i in range(width + 1):
        make_pixel(x + i, y, color)
        make_pixel(x + i, y + height, color)

    for i in range(height + 1):
        make_pixel(x, y + i, color)
        make_pixel(x + width, y + i, color)

def near(mx, my, x, y, d):
    return mx - d <= x <= mx + d and my - d <= y <= my + d

def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    make_line(x1, x2, y1, y2, color)
    make_line(x2, x3, y2, y3, color)
    make_line(x3, x1, y3, y1, color)

    min_x = min(x1, x2, x3)
    max_x = max(x1, x2, x3)
    min_y = min(y1, y2, y3)
    max_y = max(y1, y2, y3)

    make_rectangle(min_x, min_y, max_x - min_x, max_y - min_y, (0, 0, 255))

    pygame.draw.circle(screen, (255, 255, 0), (int(x1 * 10) + 5, int(y1 * 10) + 5), 5)
    pygame.draw.circle(screen, (255, 255, 0), (int(x2 * 10) + 5, int(y2 * 10) + 5), 5)
    pygame.draw.circle(screen, (0, 255, 0), (int(x3 * 10) + 5, int(y3 * 10) + 5), 5)

x1, y1 = 10, 10
x2, y2 = 30, 30
x3, y3 = 15, 20

drag = None

running = True
while running:
    mx, my = pygame.mouse.get_pos()
    mx /= 10
    my /= 10

    mouse_down = pygame.mouse.get_pressed()[0]

    if mouse_down:
        if drag is None:
            if near(mx, my, x1, y1, 1):
                drag = 1
            elif near(mx, my, x2, y2, 1):
                drag = 2
            elif near(mx, my, x3, y3, 1):
                drag = 3

        if drag == 1:
            x1, y1 = mx, my
        elif drag == 2:
            x2, y2 = mx, my
        elif drag == 3:
            x3, y3 = mx, my
    else:
        drag = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_triangle(x1, y1, x2, y2, x3, y3, (255, 0, 0))
    pygame.display.flip()

pygame.quit()