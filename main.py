import pygame
from Sprites import Sprite_Image_Loader, Rockman
pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
mainClock = pygame.time.Clock()

# Run until the user asks to quit
running = True


Rockman = Rockman.Rockman()

while running:
    mx, my = pygame.mouse.get_pos()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the background with white
    screen.fill((0, 0, 0))
    Rockman.update()
    screen.blit(Rockman.image, (0, 0))
    pygame.display.flip()
    mainClock.tick(60)


# Done! Time to quit.

pygame.quit()