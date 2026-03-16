from math import sqrt
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing with Pixels")

def make_pexel(x, y, coler, z=0):
    pygame.draw.rect(screen, coler, (x * 10, y * 10, 10, 10))

def make_line(x1, x2, y1, y2, coler):
    t = 0
    while t <= 1:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        make_pexel(x, y, coler)
        t += 0.02

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
    for i in range(width + 1):
        make_pexel(x + i * 0.1, y, coler)
    for i in range(width + 1):
        make_pexel(x + i * 0.1, y + height * 0.1, coler)
    for i in range(height + 1):
        make_pexel(x, y + i * 0.1, coler)
    for i in range(height + 1):
        make_pexel(x + width * 0.1, y + i * 0.1, coler)

def update():
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        make_circle(pos[0] / 10, pos[1] / 10, 7, (255, 255, 255))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update()

pygame.quit()