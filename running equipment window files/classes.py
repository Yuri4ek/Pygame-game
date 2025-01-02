import pygame
import os
from functions import load_image


class Character(pygame.sprite.Sprite):
    '''
        Бегущий персонаж
    '''

    def __init__(self, all_sprites, character_spawn_coordinates):
        super().__init__()

        # координаты
        self.character_spawn_coordinates = character_spawn_coordinates
        self.x1, self.y1, self.x2, self.y2 = character_spawn_coordinates

        # добавление персонажа
        self.sprite = self.initialization()
        all_sprites.add(self.sprite)

    def initialization(self):
        sprite = pygame.sprite.Sprite()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = ('..', 'assets', 'images', 'character',
                     'Running_El_Primo.png')
        sprite.image = load_image(current_dir, file_path,
                                  self.character_spawn_coordinates)

        sprite.rect = sprite.image.get_rect()
        sprite.rect.x, sprite.rect.y = self.x1, self.y1

        return sprite
