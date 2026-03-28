import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Single Line Editor")
font = pygame.font.Font(None, 32)

letters = []

running = True

while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            letters.append(event.unicode)
    
    text_string = "".join(letters)
    text_surface = font.render(text_string, True, (0, 0, 0))
    screen.blit(text_surface, (20, 300))
    
    pygame.display.flip()

pygame.quit()