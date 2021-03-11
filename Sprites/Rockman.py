import pygame
from Sprites.Sprite_Image_Loader import *
import json

class Rockman(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
        self.size = 3
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = Sprite_Sheet()
        f = open('Docs/megaman_sprite.json')
        data = json.load(f)
        self.sprites_dic = {}

        self.load_states(data)
        self.estado = 'running'

        self.index_picture = 0
        self.image = self.sprites_dic[self.estado]['lista_sprites'][self.sprites_dic[self.estado]['lista_secuencia'][0]]
        self.rect = self.image.get_rect()

    def load_states(self, data):
        lista = []
        for k, v in data.items():
            self.load_state(k, data[k])

    def load_state(self, key, data):
        lista = []
        print(data)
        for rectangulo in data['rectangulos']:
            rect = [x * self.size for x in rectangulo]
            lista.append(self.sprite_sheet.image.subsurface((rect[0], rect[1],
                                                                      rect[2] - rect[0],
                                                                      rect[3] - rect[1])))
        # contruccion de secuencia de animacion
        secuencia = []
        for tupla in data['secuencia_animacion']:
            lista_aux= [int(tupla[1])] * int(tupla[0])
            secuencia += lista_aux
        cantiad_imagen = len(secuencia)
        self.sprites_dic[key] = {'lista_sprites' : lista, 'lista_secuencia' : secuencia, 'cantiad_imagen' : cantiad_imagen}




    def load_idle(self, data):
        self.idle_list = []
        for rectangulo in data['idle']['rectangulos']:
            rect = [x * self.size for x in rectangulo]
            self.idle_list.append(self.sprite_sheet.image.subsurface((rect[0], rect[1],
                                                                      rect[2] - rect[0],
                                                                      rect[3] - rect[1])))
        self.estado = 'idle'
        # contruccion de secuencia de animacion
        self.secuencia_idle = []
        for tupla in data['idle']['secuencia_animacion']:
            print(tupla)
            lista = [int(tupla[1])] * int(tupla[0])
            self.secuencia_idle += lista
        self.cantiad_imagen_idle = len(self.secuencia_idle)

    def load_running(self, data):
        self.running_list = []
        for rectangulo in data['running']['rectangulos']:
            rect = [x * self.size for x in rectangulo]
            self.running_list.append(self.sprite_sheet.image.subsurface((rect[0], rect[1],
                                                                      rect[2] - rect[0],
                                                                      rect[3] - rect[1])))
        self.estado = 'running'
        # contruccion de secuencia de animacion
        self.secuencia_running = []
        for tupla in data['running']['secuencia_animacion']:
            lista = [int(tupla[1])] * int(tupla[0])
            self.secuencia_running += lista
        self.cantiad_imagen_running = len(self.secuencia_running)

    def change_state(self, new_state):
        self.estado = new_state
        self.index_picture = 0

    def update(self):
            self.image = self.sprites_dic[self.estado]['lista_sprites'][self.sprites_dic[self.estado]['lista_secuencia'][self.index_picture]]
            self.index_picture += 1
            self.index_picture %= self.sprites_dic[self.estado]['cantiad_imagen']
            self.rect = self.image.get_rect()






