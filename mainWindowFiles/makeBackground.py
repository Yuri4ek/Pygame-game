import os
import pygame
from mainWindowFiles.functions import get_coordinates


def get_path(name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = ['..', 'assets', 'images', 'backgrounds', name]
    file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(file_name):
        return None

    return file_name


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        return None
    image = pygame.image.load(fullname)
    return image


# это доработать и на другие фото
def draw_text(screen):
    x1, y1, x2, y2 = 0, 0, 0, 0

    # создание данных для отображения главного уровня персонажа
    text_size = y2 - y1
    font = pygame.font.Font(None, text_size)
    color = pygame.Color(255, 255, 255)

    # вывод уровня персонажа
    text = font.render("Уровень", True, color)
    screen.blit(text, (x1, y1))


def run(image_name):
    size, start_game_btn, settings_btn = get_coordinates()

    screen = pygame.display.set_mode(size)

    background_image = pygame.image.load(get_path(image_name))
    screen.blit(background_image, (0, 0))

    pygame.image.save(screen, 'surface.png')


run('gym.png')
