import os
import pygame
import subprocess


def load_image(file_path, character_view_coordinates):
    '''
        Создание pygame картинки
    '''

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
    character_view_coordinates = list(map(int, data[1][1].split(",")))
    general_lvl_coordinates = list(map(int, data[2][1].split(",")))
    other_lvl_coordinates = list(map(int, data[3][1].split(",")))

    return (size, character_view_coordinates,
            general_lvl_coordinates, other_lvl_coordinates)


def level_calculating():
    '''
        Возвращает уровни прокачки персонажа
    '''

    # берет уровни прогресса персонажа
    with open("progress.txt", mode="r") as progress_file:
        specifications = [int(specification.split(":")[1])
                          for specification in
                          progress_file.read().split("\n")]

    level_specifications = [specification if specification > 1 else 0
                            for specification in specifications]

    total_level = 1 + sum(level_specifications)

    return total_level, specifications


def display_character(all_sprites, character_view_coordinates):
    '''
        Отображение персонажа
    '''

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


def display_character_progress(window,
                               general_lvl_coordinates, other_lvl_coordinates):
    '''
        Отображение прогресса (уровней персонажа)
    '''

    total_level, specifications = level_calculating()
    arm, press, legs = specifications

    if general_lvl_coordinates:
        x1, y1, x2, y2 = general_lvl_coordinates

        # создание данных для отображения главного уровня персонажа
        text_size = y2 - y1
        font = pygame.font.Font(None, text_size)
        color = pygame.Color(255, 255, 255)

        # вывод уровня персонажа
        text = font.render(f"Уровень: {total_level}", True, color)
        window.blit(text, (x1, y1))

    if other_lvl_coordinates:
        x1, y1, x2, y2 = other_lvl_coordinates

        # создание данных для отображения уровней персонажа
        text_size = (y2 - y1) // 4
        font = pygame.font.Font(None, text_size)
        color = pygame.Color(255, 255, 255)

        texts = [f"Прокачка",
                 f"рук – {arm}",
                 f"пресса – {press}",
                 f"ног – {legs}"]

        # вывод уровней персонажа
        for i in range(len(texts)):
            text = font.render(texts[i], True, color)
            window.blit(text, (x1, y1 + i * text_size))
