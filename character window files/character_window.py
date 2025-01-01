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


def level_calculating():
    # берет уровни прогресса персонажа
    with open("progress.txt", mode="r") as progress_file:
        specifications = [int(specification.split(":")[1])
                          for specification in
                          progress_file.read().split("\n")]

    level_specifications = [specification if specification > 1 else 0
                            for specification in specifications]

    total_level = 1 + sum(level_specifications)

    return total_level, specifications


def display_character(character_view_coordinates):
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


def display_character_progress(general_lvl_coordinates, other_lvl_coordinates):
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
    display_character(character_view_coordinates)
    all_sprites.draw(window)

    # вывод уровней персонажа
    display_character_progress(general_lvl_coordinates, other_lvl_coordinates)

    # обновление окна
    pygame.display.flip()

    # запуск окна
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
