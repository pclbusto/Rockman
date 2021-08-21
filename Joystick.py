import pygame
from Sprites import Sprite_Image_Loader, Rockman
from Stage.Stage_Loader import Stage_Loader

pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([48*14, 48*14])
mainClock = pygame.time.Clock()

# Run until the user asks to quit
running = True

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick = joysticks[0]
print(joystick.get_name())

# print(joystick.get_button())

#
# #tiles_manager = Tiles_Manager()
# stage_loader = Stage_Loader()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    buttons = joystick.get_numbuttons()
    print(joystick.get_button(0))
    # for i in range(buttons):
    #     button = joystick.get_button(i)
    #     print(button)
    pygame.display.flip()
    mainClock.tick(60)



pygame.quit()