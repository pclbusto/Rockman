import pygame
from Sprites import Sprite_Image_Loader, Rockman
from Stage.Stage_Loader import Stage_Loader

pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([48*14, 48*14])
mainClock = pygame.time.Clock()

# Run until the user asks to quit
running = True


rect = pygame.Rect(10,10,100,100)
print(rect)
rect.y += 1
print(rect)
rect.y -= 1
print(rect)
rockman = Rockman.Rockman()
#tiles_manager = Tiles_Manager()
stage_loader = Stage_Loader()
while running:
    mx, my = pygame.mouse.get_pos()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
         #   rockman.update_state(event)

    rockman.move(stage_loader.tiles_rect)
    # Fill the background with white
    screen.fill((0, 0, 0))

    #print(tiles_manager.tiles['cutman']['tiles'])

    #for index, tile in enumerate(tiles_manager.tiles['cutman']['tiles']):
    screen.blit(stage_loader.image_map, (0, 0))

#    pygame.draw.rect(screen, (255, 0, 0), rockman.rect)
    screen.blit(rockman.image, rockman.pos)

    #screen.blit(rockman.image, rockman.pos)
    pygame.display.flip()
    mainClock.tick(60)


# Done! Time to quit.

pygame.quit()