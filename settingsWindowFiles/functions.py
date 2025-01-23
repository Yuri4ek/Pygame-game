import pygame
import os


def get_path(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(current_dir, *file_path)

    # если файл не существует, то выходим
    if not os.path.isfile(file_name):
        return None

    return file_name


def get_coordinates():
    # взятие данных обьектов
    with open(get_path(["..", "settingsWindowFiles",
                        "objects coordinates.txt"]), mode="r") as file:
        data = [l.split(";") for l in file.read().split("\n")]

    # размер окна
    size = width, height = list(map(int, data[0][2].split(",")))

    # координаты обьектов окна
    first_backgroud_coordinates = list(map(int, data[1][1].split(",")))
    second_backgroud_coordinates = list(map(int, data[2][1].split(",")))

    return (size, first_backgroud_coordinates, second_backgroud_coordinates)


def check_touch(mouse_coordinates, object_coordinates):
    x1, y1, x2, y2 = object_coordinates
    return x1 <= mouse_coordinates[0] <= x2 and \
        y1 <= mouse_coordinates[1] <= y2


def run_window(window_style, size, first_backgroud_coordinates,
               second_backgroud_coordinates):
    window = pygame.display.set_mode(size, pygame.RESIZABLE)

    # добавление фона
    background_path = ["..", "assets", "images", "backgrounds",
                       f"settings_{window_style}.png"]
    background_image = pygame.image.load(get_path(background_path))
    window.blit(background_image, (0, 0))
    pygame.display.flip()

    # запуск окна
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_coordinates = event.pos

                if check_touch(mouse_coordinates, first_backgroud_coordinates):
                    window_style = "forest"
                elif check_touch(mouse_coordinates,
                                 second_backgroud_coordinates):
                    window_style = "gym"

                # изменение фона
                background_path = ["..", "assets", "images", "backgrounds",
                                   f"settings_{window_style}.png"]
                background_image = pygame.image.load(
                    get_path(background_path))
                window.blit(background_image, (0, 0))
                pygame.display.flip()

    return window_style
