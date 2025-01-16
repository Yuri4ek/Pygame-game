import pygame
import os
from functions import load_image


class PullingCharacter(pygame.sprite.Sprite):
    def __init__(self, group, character_coordinates):
        super().__init__(group)

        # характеристики
        self.x1, self.y1, self.x2, self.y2 = character_coordinates
        self.size = self.widht, self.height = (self.x2 - self.x1,
                                               self.y2 - self.y1)

        # изображение
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_name = 'Pulling_El_Primo.png'
        self.make_image(self.image_name)

        # местоположение
        self.make_rect()

    def update(self, count):
        # меняем изображение (имитируем подтягивание)
        self.image_name = 'Pulling_El_Primo3.png' if count == 3 else \
            'Pulling_El_Primo2.png' if count == 2 else 'Pulling_El_Primo.png'
        self.make_image(self.image_name)

    def make_image(self, image_name):
        file_path = ('..', 'assets', 'images', 'character', 'pull_up',
                     image_name)
        image = load_image(self.current_dir, file_path)
        self.image = pygame.transform.scale(image, self.size)

    def make_rect(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.x1
        self.rect.y = self.y1
