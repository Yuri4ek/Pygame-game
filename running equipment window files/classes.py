import pygame
import os
from functions import load_image


class RunningCharacter(pygame.sprite.Sprite):
    def __init__(self, group, character_spawn_coordinates):
        super().__init__(group)

        # характеристики
        self.speed = 100
        self.x1, self.y1, self.x2, self.y2 = character_spawn_coordinates
        self.size = self.widht, self.height = (self.x2 - self.x1,
                                               self.y2 - self.y1)

        # изображение
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = ('..', 'assets', 'images', 'character',
                     'Running_El_Primo.png')
        image = load_image(current_dir, file_path)
        self.image = pygame.transform.scale(image, self.size)

        # местоположение
        self.rect = self.image.get_rect()
        self.rect.x = self.x1
        self.rect.y = self.y1

    def update(self, window_size, fps, track_speed, character_run):
        x2 = self.rect.x + self.widht

        if x2 <= window_size[0]:
            # движение из-за беговой дорожки
            self.rect = self.rect.move(track_speed // fps, 0)
        if character_run and self.rect.x >= self.x1:
            # движение персонажа
            self.rect = self.rect.move(-(self.speed // fps), 0)
