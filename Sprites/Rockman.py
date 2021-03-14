import pygame
from Sprites.Sprite_Image_Loader import *
import json
from Sprites.Helper import *

class Rockman(pygame.sprite.Sprite):
    SENTIDO_IZQUIERDO = 'izquierdo'
    SENTIDO_DERECHO = 'derecho'
    ESTADO_IDLE = 'idle'
    ESTADO_RUNNING = 'running'
    ESTADO_INCH = 'inch'
    ESTADO_JUMPING = 'jumping'

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
        self.size = 3
        self.VELOCIDAD_MAXIMA = 1.375 * self.size
        self.ACELERACION_Y = -4.87 * self.size
        self.ACELERACION_X = 0.125 * self.size
        self.GRAVITY = 0.25 * self.size
        self.ACELERACION_SALTO = 4.87
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = Sprite_Sheet()
        f = open('Docs/megaman_sprite.json')
        data = json.load(f)
        self.sprites_dic = {}
        self.load_states(data)
        self.estado = self.ESTADO_IDLE
        self.index_picture = 0
        self.sentido = self.SENTIDO_DERECHO
        self.image = self.sprites_dic[self.estado][self.sentido][self.sprites_dic[self.estado]['lista_secuencia'][0]]
        self.rect = self.image.get_rect()
        self.pos = (0, 0)
        self.frames_salto = 0
        self.velocidad_x = 0
        self.velocidad_y = 0

    def load_states(self, data):
        lista = []
        for k, v in data.items():
            self.load_state(k, data[k])

    def load_state(self, key, data):
        lista_izquierda = []
        lista_derecha = []
        for rectangulo in data['rectangulos']:
            rect = [x * self.size for x in rectangulo]
            lista_izquierda.append(self.sprite_sheet.image_spritesheet_megaman.subsurface((rect[0], rect[1],
                                                                      rect[2] - rect[0]+1,
                                                                      rect[3] - rect[1]+1)).convert())
        for imagen in lista_izquierda:
            lista_derecha.append(pygame.transform.flip(imagen, True, False))
        # contruccion de secuencia de animacion
        secuencia = []
        for tupla in data['secuencia_animacion']:
            lista_aux = [int(tupla[1])] * int(tupla[0])
            secuencia += lista_aux
        cantiad_imagen = len(secuencia)
        reflejar = data['reflejar'] == 1
        self.sprites_dic[key] = {self.SENTIDO_IZQUIERDO: lista_izquierda, self.SENTIDO_DERECHO: lista_derecha, 'lista_secuencia': secuencia, 'cantiad_imagen' : cantiad_imagen, 'reflejar':reflejar}

    def change_state(self, new_state):
        self.estado = new_state
        self.index_picture = 0

    def move(self, tiles):
        print("entrada {}".format(self.rect))
        list_teclas = pygame.key.get_pressed()
        self.velocidad_y += self.GRAVITY
        if list_teclas[pygame.K_LEFT] == 0 and list_teclas[pygame.K_RIGHT] == 0:
            if self.estado == self.ESTADO_RUNNING:
                self.change_state(self.ESTADO_IDLE)
                self.velocidad_x = 0

        if list_teclas[pygame.K_LEFT]:
            if self.velocidad_x > -self.VELOCIDAD_MAXIMA:
                self.velocidad_x -= self.ACELERACION_X
            # continua hacia el mismo sentido
            if self.sentido == Rockman.SENTIDO_IZQUIERDO:
                if self.estado == self.ESTADO_IDLE:
                    self.change_state(self.ESTADO_INCH)
                if self.estado == self.ESTADO_INCH:
                    self.change_state(self.ESTADO_RUNNING)
            if self.sentido != Rockman.SENTIDO_IZQUIERDO:
                self.sentido = Rockman.SENTIDO_IZQUIERDO
                self.change_state(self.ESTADO_IDLE)
        if list_teclas[pygame.K_RIGHT]:
            if self.velocidad_x < self.VELOCIDAD_MAXIMA:
                self.velocidad_x += self.ACELERACION_X

            # continua hacia el mismo sentido
            if self.sentido == Rockman.SENTIDO_DERECHO:
                if self.estado == self.ESTADO_IDLE:
                    self.change_state(self.ESTADO_INCH)
                if self.estado == self.ESTADO_INCH:
                    self.change_state(self.ESTADO_RUNNING)
            if self.sentido != Rockman.SENTIDO_DERECHO:
                self.sentido = Rockman.SENTIDO_DERECHO
                self.change_state(self.ESTADO_IDLE)
        if list_teclas[pygame.K_a]:
            #saltamos
            print("pulsada a")
            if self.estado in[self.ESTADO_RUNNING, self.ESTADO_IDLE]:
                print("SALTANDO")
                self.change_state(self.ESTADO_JUMPING)
                self.velocidad_y = self.ACELERACION_Y
                self.frames_salto = 0
            elif self.estado == self.ESTADO_JUMPING:
                print("restamos")
                self.frames_salto += 1

        print(self.velocidad_y)
        rect, velocidad = move(self.rect, [self.velocidad_x, self.velocidad_y], tiles)
        self.velocidad_x = velocidad[0]
        self.velocidad_y = velocidad[1]
        self.set_pos((rect.x, rect.y))
        self.update_image()
        print("salida {}".format(self.rect))



    def set_pos(self, pos_nueva):
        self.pos = pos_nueva
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


    def update_image(self):
        self.image = self.sprites_dic[self.estado][self.sentido][self.sprites_dic[self.estado]['lista_secuencia'][self.index_picture]]
        self.index_picture += 1
        self.index_picture %= self.sprites_dic[self.estado]['cantiad_imagen']
        self.rect = self.image.get_rect().copy()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]








