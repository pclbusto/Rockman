import pygame
import json
from Sprites.Sprite_Image_Loader import Sprite_Sheet

class Tiles_Manager():
    def __init__(self):
        self.tiles = {}
        self.size = 3
        imagen_tiles = open('Imagen/Tiles.png')
        file_imagen_json = open('Docs/Tiles.json')
        data_image_json = json.load(file_imagen_json)
        #print(data_image_json)
        self.sprite_sheet = Sprite_Sheet()
        lista_tiles = []
        for k, v in data_image_json.items():
            size_tile = [val*self.size for val in v['size_tile']]

            for rectangulo in v['tiles']:
                rect = [x * self.size for x in rectangulo]
                size_x = (rect[2] - rect[0] + self.size)
                size_y = (rect[3] - rect[1] + self.size)
                if size_tile[0] != size_x:
                    print("ERROR en tamaño de tile_x tamaño esperado{} tamaño calculado{}".format(size_tile[0], size_x))
                if size_tile[1] != size_y:
                    print("ERROR en tamaño de tile_y tamaño esperado{} tamaño calculado{}".format(size_tile[1], size_y))
                lista_tiles.append(self.sprite_sheet.image_tiles.subsurface((rect[0], rect[1],
                                                                           size_x,
                                                                           size_y)))
            self.tiles[k] = {'size_tile': size_tile, 'tiles': lista_tiles}

class Stage_Loader():
    def __init__(self):

        self.size = (48, 48)
        # self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #             [1, 1, 1, 1, 1, 1, 1, 1, 28, 29, 1, 1, 1, 1],
        #             [1, 1, 1, 1, 1, 1, 1, 1, 34, 35, 1, 1, 1, 1],
        #             [2, 2, 2, 2, 2, 5, 2, 2, 2, 2, 5, 2, 1, 1],
        #             [13, 13, 13, 13, 13, 5, 13, 13, 1, 1, 5, 1, 1, 1],
        #             [14, 14, 14, 19, 19, 5, 18, 19, 1, 1, 28, 29, 1, 1],
        #             [20, 20, 20, 19, 19, 5, 19, 19, 1, 1, 34, 35, 1, 1],
        #             [18, 19, 22, 19, 19, 5, 19, 19, 28, 29, 28, 29, 1, 1],
        #             [19, 19, 19, 19, 19, 5, 19, 18, 34, 35, 34, 35, 1, 1],
        #             [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
        #             [3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 1, 1],
        #             [3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 1, 1]
        #             ]
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]
                    ]
        self.tiles_rect = []
        self.map_image_generator()

    def map_image_generator(self):
        tiles_manager = Tiles_Manager()

        surface = pygame.Surface((tiles_manager.tiles['cutman']['size_tile'][0]*self.size[0], tiles_manager.tiles['cutman']['size_tile'][1]*self.size[1]), pygame.SRCALPHA)

        for x, fila in enumerate(self.map):
            for y, columna in enumerate(fila):
                surf_aux = tiles_manager.tiles['cutman']['tiles'][columna]
                surface.blit(surf_aux, (self.size[0]*y, self.size[1]*x))
                if columna not in [1, 13, 14, 18, 19, 20]:
                    self.tiles_rect.append(pygame.Rect(self.size[0]*y, self.size[1]*x, self.size[0], self.size[1]))

        self.image_map = surface



