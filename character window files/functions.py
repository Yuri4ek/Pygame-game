import os
import pygame


def load_image(file_path, character_view_coordinates):
    x1, y1, x2, y2 = character_view_coordinates

    # если файл не существует, то выходим
    if not os.path.isfile(file_path):
        return None

    # создаем и возвращаем картинку
    image = pygame.image.load(file_path)

    image = image.convert()
    colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey)

    return pygame.transform.scale(image, (x2 - x1, y2 - y1))
