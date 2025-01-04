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
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_name = 'Running_El_Primo.png'
        self.make_image(self.image_name)

        # местоположение
        self.make_rect()

    def update(self, window_size, fps, track_speed, character_run):
        # меняем изображение
        self.image_name = 'Running_El_Primo2.png' \
            if self.image_name == 'Running_El_Primo.png' and character_run \
            else 'Running_El_Primo.png'
        self.make_image(self.image_name)

        # движение
        self.move(window_size, fps, track_speed, character_run)

    def make_image(self, image_name):
        file_path = ('..', 'assets', 'images', 'character', image_name)
        image = load_image(self.current_dir, file_path)
        self.image = pygame.transform.scale(image, self.size)

    def make_rect(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.x1
        self.rect.y = self.y1

    def move(self, window_size, fps, track_speed, character_run):
        x2 = self.rect.x + self.widht

        if x2 <= window_size[0]:
            # движение из-за беговой дорожки
            self.rect = self.rect.move(track_speed // fps, 0)
        if character_run and self.rect.x >= self.x1:
            # движение персонажа
            self.rect = self.rect.move(-(self.speed // fps), 0)
