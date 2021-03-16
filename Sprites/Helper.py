import pygame, sys
#
# # setup pygame/window #
# mainClock = pygame.time.Clock()
# from pygame.locals import *
#
# pygame.init()
# pygame.display.set_caption('Physics Explanation')
# screen = pygame.display.set_mode((500, 500), 0, 32)
#
# player = pygame.Rect(100, 100, 40, 80)
#
# tiles = [pygame.Rect(200, 350, 50, 50), pygame.Rect(260, 320, 50, 50)]


def collision_test(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions


def move(rect, movement, tiles):  # movement = [5,2]
    tipo_coliciones = {'arriba': False, 'abajo': False, 'izquierda': False, 'derecha': False}
    rect.x += movement[0]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
            tipo_coliciones['derecha'] = True
        if movement[0] < 0:
            rect.left = tile.right
            tipo_coliciones['izquierda'] = True

    rect.y += movement[1]
    print(rect, movement)
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            print("A {}".format( rect))
            rect.bottom = tile.top + 3
            print("D {}".format(rect))
            tipo_coliciones['abajo'] = True
            movement[1] = 0
        elif movement[1] < 0:
            rect.top = tile.bottom
            movement[1] = 0
            tipo_coliciones['arriba'] = True


    return rect, movement, tipo_coliciones
#
#
# right = False
# left = False
# up = False
# down = False
#
# # loop #
# while True:
#
#     # clear display #
#     screen.fill((0, 0, 0))
#
#     movement = [0, 0]
#     if right == True:
#         movement[0] += 5
#     if left == True:
#         movement[0] -= 5
#     if up == True:
#         movement[1] -= 5
#     if down == True:
#         movement[1] += 5
#
#     player = move(player, movement, tiles)
#
#     pygame.draw.rect(screen, (255, 255, 255), player)
#
#     for tile in tiles:
#         pygame.draw.rect(screen, (255, 0, 0), tile)
#
#     # event handling #
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == KEYDOWN:
#             if event.key == K_RIGHT:
#                 right = True
#             if event.key == K_LEFT:
#                 left = True
#             if event.key == K_DOWN:
#                 down = True
#             if event.key == K_UP:
#                 up = True
#         if event.type == KEYUP:
#             if event.key == K_RIGHT:
#                 right = False
#             if event.key == K_LEFT:
#                 left = False
#             if event.key == K_DOWN:
#                 down = False
#             if event.key == K_UP:
#                 up = False
#
#     # update display #
#     pygame.display.update()
#     mainClock.tick(60)