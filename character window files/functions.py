import os
import pygame


def load_image(current_dir, file_path, character_view_coordinates):
    x1, y1, x2, y2 = character_view_coordinates

    fullname = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return None

    # создаем и возвращаем картинку
    image = pygame.image.load(fullname)

    image = image.convert()
    colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey)

    return pygame.transform.scale(image, (x2 - x1, y2 - y1))