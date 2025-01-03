import os
import pygame


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


def get_coordinates():
    '''
        Возвращает координаты окна и его обьектов
    '''

    # взятие данных обьектов
    with open("objects coordinates.txt", mode="r") as file:
        data = [l.split(";") for l in file.read().split("\n")]

    # размер окна
    size = width, height = list(map(int, data[0][2].split(",")))

    # координаты обьектов окна
    character_spawn_coordinates = list(map(int, data[1][1].split(",")))
    left_block_coordinates = list(map(int, data[2][1].split(",")))
    down_block_coordinates = list(map(int, data[3][1].split(",")))

    return (size, character_spawn_coordinates,
            left_block_coordinates, down_block_coordinates)
