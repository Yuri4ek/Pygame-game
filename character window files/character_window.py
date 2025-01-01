import pygame
from functions import load_image
import os
import subprocess


def get_coordinates():
    # взятие данных обьектов
    with open("objects coordinates.txt", mode="r") as file:
        data = [l.split(";") for l in file.read().split("\n")]

    # размер окна
    size = width, height = list(map(int, data[0][2].split(",")))

    # координаты обьектов окна
    character_view_coordinates = list(map(int, data[1][1].split(",")))
    general_lvl_coordinates = list(map(int, data[2][1].split(",")))
    other_lvl_coordinates = list(map(int, data[3][1].split(",")))

    return (size, character_view_coordinates,
            general_lvl_coordinates, other_lvl_coordinates)


def make_character(character_view_coordinates):
    x1, y1, x2, y2 = character_view_coordinates

    sprite = pygame.sprite.Sprite()

    # обновление картинки персонажа
    subprocess.run(["python", "make total character.py"])

    # загрузка картинки персонажа
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = 'total_character.png'
    sprite.image = load_image(file_path, character_view_coordinates)

    # помещение персонажа в прямоугольник
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x, sprite.rect.y = x1, y1

    all_sprites.add(sprite)


size, character_view_coordinates, \
    general_lvl_coordinates, other_lvl_coordinates = get_coordinates()

if __name__ == '__main__':
    # инициализация окна
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Pump It Up💪💪💪")

    # добавление фона
    background_image = pygame.image.load('window.png')
    window.blit(background_image, (0, 0))

    # вывод персонажа
    all_sprites = pygame.sprite.Group()
    make_character(character_view_coordinates)
    all_sprites.draw(window)

    # обновление окна
    pygame.display.flip()

    # запуск окна
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
