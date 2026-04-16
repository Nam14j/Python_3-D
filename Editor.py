import pygame

pygame.init()
pygame.key.set_repeat(400, 40)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Single Line Editor")

font = pygame.font.Font(None, 32)
white = (255, 255, 255)
black = (0, 0, 0)

letters = []
cursor_pos = 0
clock = pygame.time.Clock()

running = True

# This function draws the cursor, also in text_before = "".join(letters[:cursor_pos]), : makes it start from 1 and noot 0.
def draw_cursor():
    text_before = "".join(letters[:cursor_pos])
    cursor_x = 20 + font.size(text_before)[0]
    cursor_y = 300
    pygame.draw.line(screen, black, (cursor_x, cursor_y), (cursor_x, cursor_y + font.get_height()), 2)

# This function finds out the cursor position based on the mouse clicked position. also char is charecter, so char_width is the width of the charecter.
# Also 0 from char_width = font.size(letters[i])[0] is the width of the charecrer.
def get_cursor_from_mouse(mouse_x):
    x = 20

    for i in range(len(letters)):
        char_width = font.size(letters[i])[0]

        hitbox = pygame.Rect(x - char_width // 2, 280, char_width, 60)

        if hitbox.collidepoint(mouse_x, 300):
            return i

        x += char_width

    return len(letters)


while running:
    clock.tick(60)
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #This part checks if the user clicked in the text box, and if the mouse cursor is in the text box then it updates the cursor pos.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            text_box = pygame.Rect(20, 280, 760, 60)

            if text_box.collidepoint(mouse_x, mouse_y):
                cursor_pos = get_cursor_from_mouse(mouse_x)

        elif event.type == pygame.KEYDOWN:
            # This parts deleats
            if event.key == pygame.K_BACKSPACE:
                if cursor_pos > 0:
                    letters.pop(cursor_pos - 1)
                    cursor_pos -= 1

            # Moves the cursor left
            elif event.key == pygame.K_LEFT:
                if cursor_pos > 0:
                    cursor_pos -= 1
            # Moves the cursor right
            elif event.key == pygame.K_RIGHT:
                if cursor_pos < len(letters):
                    cursor_pos += 1

            # This part adds the cursor position to the list of letters when the user types a character.
            # Also checks of the charecter is pritible.
            elif event.unicode and event.unicode.isprintable():
                letters.insert(cursor_pos, event.unicode)
                cursor_pos += 1
    #This parts renders the array of letters on screen.
    text_string = "".join(letters)
    text_surface = font.render(text_string, True, black)
    screen.blit(text_surface, (20, 300))

    draw_cursor()

    pygame.display.flip()

pygame.quit()