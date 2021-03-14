import pygame

class Sprite_Sheet():

    def __init__(self):
        size = 3
        self.image_spritesheet_megaman = pygame.image.load("Imagen//NES - Mega Man - Mega Man.png").convert_alpha()
        self.image_spritesheet_megaman.set_colorkey((128, 0, 128))
        self.image_spritesheet_megaman = pygame.transform.scale(self.image_spritesheet_megaman, (self.image_spritesheet_megaman.get_width()*size, self.image_spritesheet_megaman.get_height()*size))
        self.image_tiles = pygame.image.load("Imagen//Tiles.png").convert_alpha()
        self.image_tiles = pygame.transform.scale(self.image_tiles, (self.image_tiles.get_width()*size, self.image_tiles.get_height()*size))


