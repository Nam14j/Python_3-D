from math import sqrt
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing with Pixels")

def make_pexel(x, y, coler, z=0):
    pygame.draw.rect(screen, coler, (int(x * 10), int(y * 10), 10, 10))

def make_line(x1, x2, y1, y2, coler):
    t = 0
    while t <= 1:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        make_pexel(x, y, coler)
        t += 0.01

def make_circle(x, y, radius, coler):
    X = -radius
    while X <= radius:
        Y = sqrt(radius**2 - X**2)
        make_pexel(x + X, y + Y, coler)
        make_pexel(x + X, y - Y, coler)
        make_line(x + X, x + X, y + Y, y - Y, coler)
        X += 0.1

    Y = -radius
    while Y <= radius:
        X = sqrt(radius**2 - Y**2)
        make_pexel(x + X, y + Y, coler)
        make_pexel(x - X, y + Y, coler)
        make_line(x + X, x - X, y + Y, y + Y, coler)
        Y += 0.1

def make_rectangle(x, y, width, height, coler):
    width = int(width)
    height = int(height)

    for i in range(width + 1):
        make_pexel(x + i, y, coler)
        make_pexel(x + i, y + height, coler)

    for i in range(height + 1):
        make_pexel(x, y + i, coler)
        make_pexel(x + width, y + i, coler)

def make_triangle_and_rectangle_around(x1, y1, x2, y2, x3, y3, coler):
    make_line(x1, x2, y1, y2, coler)
    make_line(x2, x3, y2, y3, coler)
    make_line(x3, x1, y3, y1, coler)
    min_x = min(x1, x2, x3)
    max_x = max(x1, x2, x3)
    min_y = min(y1, y2, y3)
    max_y = max(y1, y2, y3)
    make_rectangle(min_x, min_y, max_x - min_x, max_y - min_y, (0, 0, 255))

def update():
    screen.fill((0, 0, 0))
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        x = pos[0] / 10
        y = pos[1] / 10
        make_triangle_and_rectangle_around(x, y, x + 20, y, x + 5, y + 10, (255, 0, 0))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update()

pygame.quit()