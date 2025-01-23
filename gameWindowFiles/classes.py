import pygame
import os


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, group, character_spawn_coordinates):
        super().__init__(group)

        # характеристики
        self.speed = 30
        self.x1, self.y1, self.x2, self.y2 = character_spawn_coordinates
        self.size = self.widht, self.height = (self.x2 - self.x1,
                                               self.y2 - self.y1)

        # изображение
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_name = 'mini_El_Primo.png'
        self.make_image(self.image_name)

        # местоположение
        self.rect = self.image.get_rect()
        self.rect.x = self.x1
        self.rect.y = self.y1

    def make_image(self, image_name):
        file_path = ('..', 'assets', 'images', 'character', image_name)
        image = load_image(self.current_dir, file_path)
        self.image = pygame.transform.scale(image, self.size)

    def update(self, step_x, step_y):
        self.rect = self.rect.move(self.speed * step_x, self.speed * step_y)


def load_image(current_dir, file_path):
    '''
        Создание pygame картинки
    '''

    fullname = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return None

    # создаем и возвращаем картинку
    image = pygame.image.load(fullname)

    image = image.convert()
    colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey)

    return image
