import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Single Line Editor")

font = pygame.font.Font(None, 32)
white = (255, 255, 255)
black = (0, 0, 0)

letters = []
cursor_pos = 0
clock = pygame.time.Clock()

running = True

def draw_keyboard_cursor():
    text_before = "".join(letters[:cursor_pos])
    cursor_x = 20 + font.size(text_before)[0]
    cursor_y = 300
    pygame.draw.line(screen, black, (cursor_x, cursor_y), (cursor_x, cursor_y + font.get_height()), 2)

while running:
    clock.tick(60)
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if cursor_pos > 0:
                    letters.pop(cursor_pos - 1)
                    cursor_pos -= 1

            elif event.key == pygame.K_LEFT:
                if cursor_pos > 0:
                    cursor_pos -= 1

            elif event.key == pygame.K_RIGHT:
                if cursor_pos < len(letters):
                    cursor_pos += 1

            elif event.unicode and event.unicode.isprintable():
                letters.insert(cursor_pos, event.unicode)
                cursor_pos += 1

    text_string = "".join(letters)
    text_surface = font.render(text_string, True, black)
    screen.blit(text_surface, (20, 300))

    draw_keyboard_cursor()

    pygame.display.flip()

pygame.quit()