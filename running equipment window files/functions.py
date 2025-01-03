import os
import pygame


def get_progress():
    '''
        Возвращает прогресс персонажа
    '''

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = ['..', 'character window files', 'progress.txt']
    progress_file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(progress_file_name):
        return None

    # берет уровни прогресса персонажа
    with open(progress_file_name, mode="r") as progress_file:
        specifications = [specification.split(":")[1]
                          for specification in
                          progress_file.read().split("\n")]

    return specifications


def write_progress(specifications,
                   arm_flag=False, press_flag=False, legs_flag=False):
    '''
        Записывает новые значения в progress.txt
    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = ['..', 'character window files', 'progress.txt']
    progress_file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(progress_file_name):
        return None

    # прогресс персонажа
    specifications[0] = str(int(specifications[0]) + 1) \
        if arm_flag and int(specifications[0]) < 3 else specifications[0]

    specifications[1] = str(int(specifications[1]) + 1) \
        if press_flag and int(specifications[1]) < 3 else specifications[1]

    specifications[2] = str(int(specifications[2]) + 1) \
        if legs_flag and int(specifications[2]) < 3 else specifications[2]

    progress_text = f"arm:{specifications[0]}\n" \
                    f"press:{specifications[1]}\n" \
                    f"legs:{specifications[2]}"

    # записывает прогресс
    with open(progress_file_name, mode="w") as progress_file:
        progress_file.write(progress_text)


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
