import pygame

class Sprite_Sheet():

    def __init__(self):
        size = 3
        self.image = pygame.image.load("Imagen//NES - Mega Man - Mega Man.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*size, self.image.get_height()*size))

        self.image.set_colorkey((128, 0, 128))
